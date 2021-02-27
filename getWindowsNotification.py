import time 
from plyer import notification 

def GiveMeNotification(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "D:\Python Amazing Projects\img\Hopstarter-Book-Address-Book-Mac.ico",
        timeout = 15
    )
if __name__=="__main__":
    listOfGreeting=["Hey Deepak","What's up Deepak","Hello Deepak","Hoo Deepak"]
    listOfWork=["You Have to learn Data Structure and Algorithm","Hey Do u want to watch some comedy video, May be Khan sir's Video","Hey you forgot to implement some problem statement ","!!Hey you have to take some food !!"]
    i=0
    while True:
        if(i==len(listOfWork)):
            i=0
        GiveMeNotification(listOfGreeting[i],listOfWork[i])
        i+=1
        time.sleep(1800)   # Will iterate after every 30 min  (30*60=1800 second)
  

