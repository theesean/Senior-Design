import tkinter as tk
import RPi.GPIO as GPIO
import psutil
from PIL import Image, ImageTk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk





root= tk.Tk()


canvas1 = tk.Canvas(root, width = 1600, height = 830)
canvas1.pack()

#########################################################

label9 = tk.Label(root, text= '  PV Panels  ', fg='blue', font=('helvetica', 36, 'bold'), bg='white', bd = 9)#title for PV panels
canvas1.create_window(300, 70, window=label9)

label12 = tk.Label(root, text= 'Voltage: ', fg='blue', font=('helvetica', 18, 'bold'),  bd = 9)
canvas1.create_window(257, 220, window=label12)

label14 = tk.Label(root, text= 'V', fg='blue', font=('helvetica', 18, 'bold'),  bd = 9)
canvas1.create_window(380, 220, window=label14)

########################################################

label13 = tk.Label(root, text= '  Generator  ', fg='blue', font=('helvetica', 36, 'bold'), bg='white', bd = 9)#title for Generator
canvas1.create_window(800, 70, window=label13)

label15 = tk.Label(root, text= 'Voltage: ', fg='blue', font=('helvetica', 18, 'bold'),  bd = 9)
canvas1.create_window(757, 220, window=label15)

label16 = tk.Label(root, text= 'V', fg='blue', font=('helvetica', 18, 'bold'),  bd = 9)
canvas1.create_window(880, 220, window=label16)


#PV panel
def PVC ():  
    label1 = tk.Label(root, text= '  Connected  ', fg='green', font=('helvetica', 18, 'bold'))
    canvas1.create_window(300, 150, window=label1)

button1 = tk.Button(text='Connect PV Panels', font=("Purisa", 25), command=PVC, bg='green',fg='white', bd = 9)
canvas1.create_window(300, 575, window=button1)

def PVD ():  
    label2 = tk.Label(root, text= 'Disconnected', fg='red', font=('helvetica', 18, 'bold'))
    canvas1.create_window(300, 150, window=label2)

button2 = tk.Button(text='Disconnect PV Panels', font=("Purisa", 25), command=PVD, bg='red',fg='white', bd = 9)
canvas1.create_window(300, 700, window=button2) 

#Generator
def GeneratorC ():  
    label3 = tk.Label(root, text= '  Connected  ', fg='green', font=('helvetica', 18, 'bold'))
    canvas1.create_window(800, 150, window=label3)

button3 = tk.Button(text='Connect Generator', font=("Purisa", 25), command=GeneratorC, bg='green',fg='white', bd = 9)
canvas1.create_window(800, 575, window=button3)

def GeneratorD ():  
    label4 = tk.Label(root, text= 'Disconnected', fg='red', font=('helvetica', 18, 'bold'))
    canvas1.create_window(800, 150, window=label4)

button4 = tk.Button(text='Disconnect Generator', font=("Purisa", 25), command=GeneratorD, bg='red',fg='white', bd = 9)
canvas1.create_window(800, 700, window=button4)

def voltage1 ():
    t = 120.2
    #label6 = tk.Label(root, text= '    Generator\'s Voltage', fg='blue', font=('helvetica', 12, 'bold'), bg='grey')
    #canvas1.create_window(800, 190, window=label6)
    label7 = tk.Label(root, text=t, fg='blue', font=('helvetica', 18, 'bold'))
    canvas1.create_window(840, 220, window=label7)
    #label8 = tk.Label(root, text= 'V', fg='blue', font=('helvetica', 12, 'bold'), bg='grey')
    #canvas1.create_window(800,220, window=label8)
    root.after(100, voltage1)
    
def voltage2 ():
    k = 120.3
    #label10 = tk.Label(root, text= '    Generator\'s Voltage', fg='blue', font=('helvetica', 12, 'bold'), bg='grey')
    #canvas1.create_window(300, 190, window=label10)
    label11 = tk.Label(root, text=k, fg='blue', font=('helvetica', 18, 'bold'))
    canvas1.create_window(340, 220, window=label11)
    #label12 = tk.Label(root, text= 'V', fg='blue', font=('helvetica', 12, 'bold'), bg='grey')
    #canvas1.create_window(300, 220, window=label12)
    root.after(100, voltage2)
    

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

root.after(500, voltage1)
root.after(500, voltage2)
root.wm_title("Microgrid GUI")
root.geometry("1600x1200")
root.mainloop()