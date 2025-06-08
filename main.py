import tkinter as tk
import numpy as np

window = tk.Tk()
window.geometry("800x800")
window.title("Statistics with num py")


list = []


def button():
    global list
    a = Entery1.get()
    a = int(a)
    list.append(a)
    label2.configure(text = f"list : {list}")

def calculate():
    global list
    array1 = np.array(list)
    sum = np.sum(array1)
    max = np.max(array1)
    mean = np.mean(array1)
    average = np.average(array1)
    standart_diviation = np.std(array1)
    label1.configure(text = f"""sum : {sum},
     max : {max},
     mean : {mean},
     average : {average},
     standard divation : {standart_diviation}""")

def clear():
    global list
    list.clear()
    label1.configure(text = "")
    label2.configure(text = "")


Entery1 = tk.Entry(font = ("Comic Sans MS", 20))
Entery1.place(relx = 0.3, rely = 0.3, anchor = "center")

button1 = tk.Button(text = "Add to list", font = ("Comic Sans MS", 20), command = button)
button1.place(relx = 0.3, rely = 0.4, anchor = "center")

button2 = tk.Button(text = "Calculate", font = ("Comic Sans MS", 20), command = calculate)
button2.place(relx = 0.5, rely = 0.4, anchor = "center")

label1 = tk.Label(text = "", font  = ("Comic Sans MS", 20))
label1.place(relx = 0.8, rely = 0.3, anchor = "center")

label2 = tk.Label(text = "", font  = ("Comic Sans MS", 20))
label2.place(relx = 0.8, rely = 0.2, anchor = "center")

button3 = tk.Button(text = "Clear", font = ("Comic Sans MS", 20), command = clear)
button3.place(relx = 0.4, rely = 0.5, anchor = "center")


window.mainloop()




