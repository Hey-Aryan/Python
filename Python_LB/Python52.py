# time to travel ---> ---> ---> ---> is 60 sec   
 
import time
import threading
import os



def travel1(Brr):

    for i in range(100,24999975):
        print("Task1 : ",Brr[i])

def travel2(Brr):

    for i in range (24999976,49999950):
        print("Task2 : ",Brr[i])

def travel3(Brr):

    for i in range(49999951,74999926):
        print("Task3 : ",Brr[i])

def travel4(Brr):

    for i in range (74999927,99999900):
        print("Task4 : ",Brr[i])


def main():
    Arr = list()
    
    for i in range (100,100000000):
        Arr.append(i)
    


    starttime = time.time()
    print("PID of parent process is : ",os.getpid())
    print("Thread ID of main thread is : ",threading.current_thread())
    t1 = threading.Thread(target=travel1, args=(Arr,))
    t2 = threading.Thread(target=travel2, args=(Arr,))
    t3 = threading.Thread(target=travel3, args=(Arr,))
    t4 = threading.Thread(target=travel4, args=(Arr,))

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