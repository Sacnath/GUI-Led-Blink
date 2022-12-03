from tkinter import *
import time
import serial
from PIL import Image,ImageTk


arduino = serial.Serial('COM6',9600)

def start_motor():
    arduino.write(b'H')
    #print('sent 1')



def stop_motor():
    arduino.write(b'L')
    #print('sent 0')
    

windows = Tk()
windows.title('My Project')
windows.geometry('500x200')
windows.configure(bg='white')

height = 100
width = 100

border = 3

start = Image.open('start2.jpg').resize((width,height))
start_img = ImageTk.PhotoImage(start)

stop = Image.open('stop21.png').resize((width,height))
stop_img = ImageTk.PhotoImage(stop)

start_button = Button(windows,text='start',command = start_motor,image =start_img,bd = border)
start_button.place(x=20,y=30,width=width,height=height)

stop_button = Button(windows,text='stop',command = stop_motor,image = stop_img,bd = border )
stop_button.place(x=350,y=30,width=width,height=height)

windows.mainloop()
