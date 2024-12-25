# time to travel ----> ----> is 130 sec   
 
import time
import multiprocessing

def travel1(Brr):

    for i in range(49999950):
        print("Task1 : ",Brr[i])

def travel2(Brr):

    for i in range (49999950,len(Brr)):
        print("Task2 : ",Brr[i])


def main():
    Arr = list()
    
    for i in range (100,100000000):
        Arr.append(i)
    


    starttime = time.time()
    t1 = multiprocessing.Process(target=travel1, args=(Arr,))
    t2 = multiprocessing.Process(target=travel2, args=(Arr,))

    t1.start()
  
    t2.start()
   
    t1.join()
  
    t2.join()

    endtime = time.time()
    print(endtime-starttime)


if __name__ == "__main__":
    main()