############################################
# Name      : Aryan Karande
# Date      : 14th Aug
# Version   : 3 
# 
# Description : Updated the get_data() to 
#               infer video in batches  
############################################

import os,json
import numpy as np
from PIL import Image
import torch
import torch.nn as nn
import torchvision
from torch.utils.data import DataLoader
from tqdm import tqdm
import datetime as datetime
import evaluate
from datasets import load_dataset,load_metric
from transformers import VideoMAEImageProcessor, VideoMAEForVideoClassification
from torchvision import datasets, transforms
from torchvision.transforms import (
    Compose,
    Lambda,
    Normalize,
    RandomCrop,
    RandomHorizontalFlip,
    Resize,
)
import cv2
import evaluate
from facenet_pytorch import MTCNN
from scipy.spatial import distance
#from face_detector import YoloDetector
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

#fd_model = YoloDetector(target_size=720, device="cuda:0", min_face=90)
fd_model = MTCNN(keep_all=True,device=device)
model_ckpt = "/data/data/weights/video-mae-ft/checkpoint-1171-240715-ft/checkpoint-63600" #"checkpoint-93170-240706-ft-val/checkpoint-170920"
batch_size = 1 # batch size for dataloader, one file at a time
num_inp_per_batch = 32 # batch size for inference

file_list_csv = 'infer_files.csv'

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

label2id = {'fake':'0','real':'1'}
id2label = {'0':'fake','1':'real'}
print(f"Unique classes: {list(label2id.keys())}.")

image_processor = VideoMAEImageProcessor.from_pretrained(model_ckpt)
model = VideoMAEForVideoClassification.from_pretrained(
    model_ckpt,
    label2id=label2id,
    id2label=id2label,
    ignore_mismatched_sizes=True,  # provide this in case you're planning to fine-tune an already fine-tuned checkpoint
)
if model.to(device):
    print("Model Running !!!!!!")
    
if model.eval():
    print("Model eval Running !!!!")

with open(file_list_csv,"r") as f:
    n_test = len(f.readlines())-1

dataset = load_dataset(
  'csv',
  data_files={'files': file_list_csv},
  delimiter=',',
  #column_names=['file', 'path'],
  column_names=['file', 'path'],
  skiprows=0
  #streaming=True  #need IterableDataset if this is used.  explore later
)
test_loader = DataLoader(dataset["files"], batch_size=1, shuffle=False,drop_last=False)

mean = image_processor.image_mean
std = image_processor.image_std
if "shortest_edge" in image_processor.size:
    height = width = image_processor.size["shortest_edge"]
else:
    height = image_processor.size["height"]
    width = image_processor.size["width"]
resize_to = (height, width)
test_transform=Compose(
   [
      #UniformTemporalSubsample(num_frames_to_sample),
      Lambda(lambda x: x / 255.0),
      Normalize(mean, std),
      #Resize(resize_to),
   ]
)

def infer(inp):
    print("Inside Infer")
    # Concatenate the list of video tensors along the first dimension (batch dimension)
    inp_video = torch.cat(inp, dim=0)
    inp_video = inp_video.to(device).transpose(1, 2)  # Adjust dimensions as required by the model
    print(f"Size of the input given to model : {inp_video.size}")
    print(f"Shape of the input given to model : {inp_video.shape}")
    out = model(inp_video)
    predictions_probs = torch.exp(
        torch.nn.functional.log_softmax(
            out.logits.cpu(), dim=1)).detach().numpy()
    predictions = torch.argmax(torch.tensor(predictions_probs), dim=1)
    return predictions, predictions_probs

"""
def infer(inp):
    inp_video = torch.cat(inp['video'],dim=0)
    inp_video = inp_video.to(device).transpose(1,2)
    out = model(inp_video)
    predictions_probs = torch.exp(
        torch.nn.functional.log_softmax(
        out.logits.cpu(),dim=1)).detach().numpy()
    predictions = torch.argmax(torch.tensor(predictions_probs),dim=1)
    #print(inp['video_name'],inp['clip_index'],predictions)
    return predictions,predictions_probs
""" 


def detect_faces(rgb_stack):
    def _get_matching_id(box):
        found = False
        for key in assorted_boxes:
            latest = assorted_boxes[key][-1]
            d = distance.euclidean(latest,box)
            thresh = min(latest[2]-latest[0], latest[3]-latest[1])
            if d < thresh:
                return True,key
        new_key = sorted(assorted_boxes.keys())[-1] + 1
        return False,new_key

    num_frames = len(rgb_stack)
    #boxes,_ = fd_model.predict(rgb_stack)
    boxes,_ = fd_model.detect(rgb_stack)
    np.save('boxes.npy',np.array(boxes))

    assorted_boxes = {}
    def _get_distances(box,bid,distances):
        for key in assorted_boxes:
            latest = assorted_boxes[key][-1]
            d = distance.euclidean(latest,box)
            # <TODO> try different values instead of 0.3 if it fails
            thresh = min(latest[2]-latest[0], latest[3]-latest[1])*0.3
            if d < thresh:
                distances.append([d,bid,key])
        return distances
    for frame_boxes in boxes: # loop over frame for boxes
        distances = []
        if not frame_boxes is None:
            for bid,box in enumerate(frame_boxes): # loop over box in every frame
                distances = _get_distances(box,bid,distances)
            distances = np.array(distances)
            added_bids = []
            while distances.shape[0] > 0:
                y = np.argsort(distances[:,0],kind='mergesort')
                distances = distances[y]
                assorted_boxes[int(distances[0][2])].append(frame_boxes[int(distances[0][1])])
                # remove the box and assorted_key from the np array
                # distances: [euc distance, box id , key id]
                _box = distances[0][1]
                _key = distances[0][2]
                y = np.where((distances[:,1] == _box) | (distances[:,2] == _key))
                distances = np.delete(distances,y,axis=0)
                added_bids.append(int(_box))
            for bid,box in enumerate(frame_boxes):
                if not bid in added_bids:
                    new_key = len(assorted_boxes.keys()) + 1
                    assorted_boxes[new_key] = [box]

    # each key in assorted_boxes now has cropped faces of single person
    stacked_faces = {}
    for key in assorted_boxes:
        # Is this face seen in at least 70% of the frames?
        if len(assorted_boxes[key]) >= int(len(boxes) * 0.7):
            # Initialize bounding box coordinates for union
            ws, hs = float('inf'), float('inf')  # Min values for width and height
            we, he = 0, 0  # Max values for width and height
            
            # Calculate the union of bounding boxes
            for box in assorted_boxes[key]:
                ws = min(ws, int(box[0]))  # Update min x (start width)
                we = max(we, int(box[2]))  # Update max x (end width)
                hs = min(hs, int(box[1]))  # Update min y (start height)
                he = max(he, int(box[3]))  # Update max y (end height)

            # Convert the rgb_stack into a tensor
            frames = torch.tensor(np.array(rgb_stack))
            
            # Crop the frames using the union bounding box
            current = frames[:, hs:he, ws:we, :]

            # Resize and store the cropped faces for this person
            test_frames = []
            for i in range(num_frames):
                img = Image.fromarray(current[i, :, :, :].numpy())
                img = img.resize((224, 224), Image.Resampling.LANCZOS)
                test_frames.append(img)
            
            # Store the cropped frames and union bounding box in stacked_faces
            stacked_faces[key] = {}
            stacked_faces[key]['frames'] = test_frames
            stacked_faces[key]['bbox'] = [ws, we, hs, he]

    return stacked_faces

def get_data(batch, outname):
    predictions_json = []
    ppdir = "./post_processed"
    os.makedirs(ppdir, exist_ok=True)
    
    batch_videos = []
    chunks = []
    predictions_probs = None

    for i in range(len(batch['file'])):
        fname = batch['file'][i]
        fpath = batch['path'][i]
        cap = cv2.VideoCapture(f"{fpath}")
        fps = cap.get(cv2.CAP_PROP_FPS)
        rgb_stack = []
        timestamps = []
        num_frames = 16
        count = 0
        
        while cap.isOpened():
            frame_exists, rgb = cap.read()
            if frame_exists:
                rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
                rgb_stack.append(rgb)
                timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC))
                
                if len(rgb_stack) == num_frames:
                    stacked_faces = detect_faces(rgb_stack)
                    
                    chunk_data = {
                        "chunk_index": count,
                        "start_time": "{:.2f}".format(timestamps[0] / 1000),
                        "end_time": "{:.2f}".format(timestamps[-1] / 1000),
                        "faces": []
                    }

                    for key, face_data in stacked_faces.items():
                        face_stack = face_data['frames']
                        bbox = face_data['bbox']
                        
                        current = np.stack([np.array(x) for x in face_stack], axis=0).astype(np.float32)
                        if current.shape[1] == 3:
                            current = current.transpose(0, 2, 3, 1)
                        chunk_video_path = os.path.join(ppdir, f"{outname}_face{key}_{count}.mp4")
                        torchvision.io.write_video(chunk_video_path, torch.tensor(current), fps=30)
                        
                        current = torch.tensor(current).permute(0,3,1,2)
                        imgs_tensor = test_transform(current)
                        imgs_tensor = imgs_tensor.permute(1,0,2,3)

                        batch_videos.append({
                            'video': imgs_tensor.unsqueeze(0),
                            'video_name': chunk_video_path,
                            'clip_start_time': timestamps[0] / 1000,
                            'clip_end_time': timestamps[-1] / 1000,
                            'bbox': bbox
                        })

                        face_data = {
                            "video_path": chunk_video_path,
                            "fake_probability": None,
                            "location": [bbox]
                        }
                        chunk_data["faces"].append(face_data)

                    if chunk_data["faces"]:
                        chunks.append(chunk_data)

                    rgb_stack = []
                    timestamps = []
                    count += 1
                
                #print(f"Length of video key in dict : {len(batch_videos)}")
                
                """
                if len(batch_videos) == 32:
                    print(f"Batch Processing in *** infer 1 *** {batch_videos}")
                    predictions, predictions_probs = infer([video['video'] for video in batch_videos])
                    print(f"Result from Model : {predictions_probs}")
                    for i, video in enumerate(batch_videos):
                        for chunk in chunks:
                            for face_data in chunk["faces"]:
                                if video['video_name'] == face_data['video_path']:
                                    face_data["fake_probability"] = float(predictions_probs[i][0])
                    batch_videos = []
                """ 
                    
                if len(batch_videos) >= 32:
                    print(f"Batch Processing in *** infer 1 *** {len(batch_videos)}")
                    predictions, predictions_probs = infer([video['video'] for video in batch_videos[:len(batch_videos)]])
                    print(f"Results from *** infer 1 *** {predictions_probs}")
                    # Process the first 32 videos
                    for i, video in enumerate(batch_videos[:32]):
                        for chunk in chunks:
                            for face_data in chunk["faces"]:
                                if video['video_name'] == face_data['video_path']:
                                    face_data["fake_probability"] = float(predictions_probs[i][0])
                    # Remove processed videos
                    batch_videos = batch_videos[len(batch_videos):]


            
            else:
                cap.release()
                break

        if batch_videos:
            print(f"Length of video key in dict in *** infer 2 ***: {len([video['video'] for video in batch_videos])}")
            print(f"Batching Processing in  *** infer 2 *** {len(batch_videos)}")
            predictions, predictions_probs = infer([video['video'] for video in batch_videos])
            print(f"Results from *** infer 2 *** {predictions_probs}")
            print(f"Result from Model : {predictions_probs}")
            for i, video in enumerate(batch_videos):
                for chunk in chunks:
                    for face_data in chunk["faces"]:
                        if video['video_name'] == face_data['video_path']:
                            face_data["fake_probability"] = float(predictions_probs[i][0])
            batch_videos = []

    return {"data": {"chunks": chunks}}

# Final loop to process data
results_dir = 'results'
os.makedirs(results_dir, exist_ok=True)
fileno = 0
with tqdm(total=n_test, desc='test file', unit='files', miniters=1) as pbar:
    for batch in test_loader:
        print(f"Processing file {fileno}: {batch['file'][0]}")
        fileno += 1
        vname = batch['file'][0]
        outname = os.path.splitext(vname)[0]
        preds = get_data(batch, outname)
        result_fname = os.path.join(results_dir, f"{outname}.json")
        print(f"Writing results to {result_fname}")
        with open(result_fname, 'w') as f:
            f.write(json.dumps(preds, indent=2))
