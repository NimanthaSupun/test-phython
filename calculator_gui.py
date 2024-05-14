import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
import math

root = tk.Tk()

width,height = 500,600

display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

top = int(display_height/2 - height / 2)
letf = int(display_width/2 - width/2)

root.geometry(f"{width}x{height}+{letf}+{top}")

# white ('#D4D4D2')
# black('#1C1C1C')
# ash('#505050')
# orange('#FF9500')

# calculator_gui.py


root.title('Calculator')

root.configure(background='#1C1C1C')



def button_press(num):
   
   global equal_text 
   equal_text = equal_text + str(num)
   label_text.set(equal_text)


def equals():

    global equal_text

    try:

        total = str(eval(equal_text))
        label_text.set(total)
        equal_text = total

    except ZeroDivisionError:

        label_text.set('ZERO Division Error')
        equal_text = ""

    except SyntaxError:

        label_text.set('Syntas Error')
        equal_text = ""        


def clear():
    
    global equal_text
    label_text.set("")
    equal_text = ""

# backsspace button.

def CC():
     
     global equal_text
     equal_text = equal_text[:-1] 
     label_text.set(equal_text)

# power button.

def PO():

    global equal_text
    
    try:

        num = float(equal_text)
        total = str(num ** 2)
        label_text.set(total)
        equal_text = total

    except ValueError:
        label_text.set('Invalid Input')
        equal_text = ""

# square root button

def Square():
    
    global equal_text

    try:
        num = float(equal_text)
        total = str(math.sqrt(num))
        label_text.set(total)
        equal_text = total

    except ValueError:

        label_text.set('Invalid Input')
        equal_text = ""


equal_text = ""

label_text = tk.StringVar()


label = tk.Label(root,background='White',width=26,height=3,
                 font=('consolas',20),bg='#f7ffd6',textvariable=label_text)


label.pack(pady=3)

frame = tk.Frame(root)
frame.pack()



buttonAc = tk.Button(frame,text='AC',
                    width=8,height=3,
                    font=20,
                    command=clear,
                    activebackground='#000',
                    activeforeground='white',
                    bg='#D4D4D2',
                    fg='#1C1C1C')
buttonAc.grid(column=0,row=0)


buttonPower = tk.Button(frame,text='x²',
                    width=8,height=3,
                    font=20,
                    command = PO,
                    activebackground='#000',
                    activeforeground='white',
                    bg='#D4D4D2',
                    fg='#1C1C1C')
buttonPower.grid(column=1,row=0)


buttonSquare = tk.Button(frame,text='\u221A',
                    width=8,height=3,
                    font=20,
                    command = Square,
                    activebackground='#000',
                    activeforeground='white',
                    bg='#D4D4D2',
                    fg='#1C1C1C')
buttonSquare.grid(column=2,row=0)


buttonplus = tk.Button(frame,text='+',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press('+'),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#FF9500',
                    fg='white')
buttonplus.grid(column=3,row=0)


buttonminus = tk.Button(frame,text='-',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press('-'),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#FF9500',
                    fg='white')
buttonminus.grid(column=3,row=1)


buttonmulti = tk.Button(frame,text='X',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press('*'),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#FF9500',
                    fg='white')
buttonmulti.grid(column=3,row=2)



buttondivi = tk.Button(frame,text='/',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press('/'),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#FF9500',
                    fg='white')
buttondivi.grid(column=3,row=3)




buttonequal = tk.Button(frame,text='=',
                    width=8,height=3,
                    font=20,
                    command= equals,
                    activebackground='#000',
                    activeforeground='white',
                    bg='#FF9500',
                    fg='white')
buttonequal.grid(column=3,row=4)




button7 = tk.Button(frame,text='7',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press(7),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')
button7.grid(column=0,row=1)


button8 = tk.Button(frame,text='8',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press(8),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')
button8.grid(column=1,row=1)


button9 = tk.Button(frame,text='9',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press(9),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')
button9.grid(column=2,row=1)


button4 = tk.Button(frame,text='4',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press(4),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')
button4.grid(column=0,row=2)


button5 = tk.Button(frame,text='5',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press(5),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')
button5.grid(column=1,row=2)


button6 = tk.Button(frame,text='6',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press(6),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')
button6.grid(column=2,row=2)



button1 = tk.Button(frame,text='1',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press(1),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')
button1.grid(column=0,row=3)


button2 = tk.Button(frame,text='2',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press(2),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')
button2.grid(column=1,row=3)


button3 = tk.Button(frame,text='3',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press(3),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')
button3.grid(column=2,row=3)


button0 = tk.Button(frame,text='0',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press(0),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')
button0.grid(column=0,row=4)


buttonBack = tk.Button(frame,text='BACK',
                    width=8,height=3,
                    font=20,
                    command=lambda:CC(),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='#1C1C1C')
buttonBack.grid(column=1,row=4)


buttondecimal = tk.Button(frame,text='.',
                    width=8,height=3,
                    font=20,
                    command=lambda:button_press('.'),
                    activebackground='#000',
                    activeforeground='white',
                    bg='#a5a2a1',
                    fg='white')

buttondecimal.grid(column=2,row=4)


root.mainloop()