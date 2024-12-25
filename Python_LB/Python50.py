# time to travel <--- ---> <--- ---> is 178 sec   
 
import time
import multiprocessing



def travel1(Brr):

    for i in range(24999975,100,-1):
        print("Task1 : ",Brr[i])

def travel2(Brr):

    for i in range (24999975,49999950):
        print("Task2 : ",Brr[i])

def travel3(Brr):

    for i in range((49999951+24999975),24999976,-1):
        print("Task3 : ",Brr[i])

def travel4(Brr):

    for i in range (49999951+24999975,(49999951+24999975+24999975)):
        print("Task4 : ",Brr[i])


def main():
    Arr = list()
    
    for i in range (100,100000000):
        Arr.append(i)
    


    starttime = time.time()
    t1 = multiprocessing.Process(target=travel1, args=(Arr,))
    t2 = multiprocessing.Process(target=travel2, args=(Arr,))
    t3 = multiprocessing.Process(target=travel3, args=(Arr,))
    t4 = multiprocessing.Process(target=travel4, args=(Arr,))

    t1.start()
  
    t2.start()

    t3.start()
  
    t4.start()
   
    t1.join()
  
    t2.join()
   
    t3.join()
  
    t4.join()

    endtime = time.time()
    print(endtime-starttime)


if __name__ == "__main__":
    main()