import tkinter as tk
import RPi.GPIO as GPIO
import psutil
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk




# Pin Setup:
GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme.
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(4, GPIO.IN)


root= tk.Tk()


canvas1 = tk.Canvas(root, width = 1600, height = 830)
canvas1.pack()


#PV panels
def PVC ():  
    label1 = tk.Label(root, text= '  PV Panels Connected  ', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(100, 150, window=label1)
    GPIO.output(26, True)

button1 = tk.Button(text='Connect PV Panels', font=("Purisa", 25), command=PVC, bg='blue',fg='white', bd = 9)
canvas1.create_window(250, 50, window=button1)

def PVD ():  
    label2 = tk.Label(root, text= 'PV Panels Disconnected', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(100, 150, window=label2)
    GPIO.output(26, False)

button2 = tk.Button(text='Disconnect PV Panels', font=("Purisa", 25), command=PVD, bg='red',fg='white', bd = 9)
canvas1.create_window(250, 200, window=button2) 

#Generator
def GeneratorC ():  
    label3 = tk.Label(root, text= '  Generator Connected  ', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(350, 150, window=label3)

button3 = tk.Button(text='Connect Generator', font=("Purisa", 25), command=GeneratorC, bg='red',fg='white', bd = 9)
canvas1.create_window(700, 50, window=button3)

def GeneratorD ():  
    label4 = tk.Label(root, text= 'Generator Disconnected', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(350, 150, window=label4)

button4 = tk.Button(text='Disconnect Generator', font=("Purisa", 25), command=GeneratorD, bg='red',fg='white', bd = 9)
canvas1.create_window(700, 200, window=button4)

def voltage1 ():
    t = GPIO.input(4)
    label6 = tk.Label(root, text= '    Generator\'s Voltage', fg='blue', font=('helvetica', 12, 'bold'), bg='grey')
    canvas1.create_window(1150, 190, window=label6)
    label7 = tk.Label(root, text=t*5, fg='blue', font=('helvetica', 12, 'bold'), bg='grey')
    canvas1.create_window(1150, 220, window=label7)
    label8 = tk.Label(root, text= 'V', fg='blue', font=('helvetica', 12, 'bold'), bg='grey')
    canvas1.create_window(1163,220, window=label8)
    root.after(1000, voltage1)

#Display SDSU Logo
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("SDLogo3c2.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=1600-284, y=0)
        

app = Window(root)

root.after(1000, voltage1)
root.wm_title("Microgrid GUI")
root.geometry("1600x1200")
root.mainloop()