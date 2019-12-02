import tkinter as tk
import RPi.GPIO as GPIO
import psutil

# Pin Setup:
GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme.
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.IN)


generatorVoltage = 20.34
x = "Generator voltage:"
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 600, height = 600)
canvas1.pack()

#PV panels
def PVC ():  
    label1 = tk.Label(root, text= '  PV Panels Connected  ', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(100, 150, window=label1)
    GPIO.output(26, True)

button1 = tk.Button(text='Connect PV Panels',command=PVC, bg='blue',fg='white')
canvas1.create_window(100, 50, window=button1)

def PVD ():  
    label2 = tk.Label(root, text= 'PV Panels Disconnected', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(100, 150, window=label2)
    GPIO.output(26, False)

button2 = tk.Button(text='Disconnect PV Panels',command=PVD, bg='red',fg='white')
canvas1.create_window(100, 100, window=button2)

#Generator
def GeneratorC ():  
    label3 = tk.Label(root, text= '  Generator Connected  ', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(350, 150, window=label3)

button3 = tk.Button(text='Connect Generator',command=GeneratorC, bg='blue',fg='white')
canvas1.create_window(350, 50, window=button3)

def GeneratorD ():  
    label4 = tk.Label(root, text= 'Generator Disconnected', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(350, 150, window=label4)

button4 = tk.Button(text='Disconnect Generator',command=GeneratorD, bg='red',fg='white')
canvas1.create_window(350, 100, window=button4)

def voltage ():  
    label5 = tk.Label(root, text= 'Generator Disconnected', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(350, 250, window=label5)
    root.after(1200, voltage)
    
def voltage1 ():  
    label6 = tk.Label(root, text= '    Generators Voltage', fg='blue', font=('helvetica', 12, 'bold'), bg='grey')
    canvas1.create_window(350, 170, window=label6)
    label7 = tk.Label(root, text=generatorVoltage, fg='blue', font=('helvetica', 12, 'bold'), bg='grey')
    canvas1.create_window(350, 200, window=label7)
    label8 = tk.Label(root, text= 'V    ', fg='blue', font=('helvetica', 12, 'bold'), bg='grey')
    canvas1.create_window(385,200, window=label8)
    root.after(2000, voltage1)

root.after(1200, voltage)
root.after(2000, voltage1)
root.wm_title("Microgrid GUI")
root.mainloop()


