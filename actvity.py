import time
seconds=input("enter the time in seconds: ")
def countdown_timer(seconds):
   while seconds>0:
        mins=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{mins}:{secs}'
        print(timer,end='\r')
        time.sleep(1)
        seconds=seconds-1
   print("TIME IS UP ")    
countdown_timer(int(seconds))    

