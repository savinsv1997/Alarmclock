#  Alaram clock
import time
import datetime
from tkinter import *
import winsound
#create a while loop
import sec




def alaram(set_alaram_timer):

    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%y")
        print("The set date is : ",date)
        print(now)
        if now == set_alaram_timer:
            print("Time to wake up")
            winsound.Beep()
            break
def actual_time():
    set_alaram_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alaram(set_alaram_timer)
# Creating GUI using tkinter
clock = Tk()
clock.title("Dataflair alaram clock")
clock.geometry("40*20")
time_formate = Label(clock, text = "Enter the time in 24 hours formate!", fg="red",bg = "black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()
#Execution of the window.

print("savin is good")


print("12345555")
print("asdfgfds")
print("savin")
print("good")



