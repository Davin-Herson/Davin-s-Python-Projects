import tkinter as tk

def add():
    getText = int(box.get()) + int(box2.get())
    testlabel.config(text= "Result: " + str(getText))
def sub():
    getText = int(box.get()) - int(box2.get())
    testlabel.config(text= "Result: " + str(getText))
def multiply():
    getText = int(box.get()) * int(box2.get())
    testlabel.config(text= "Result: " + str(getText))
def divide():
    getText = int(box.get()) / int(box2.get())
    testlabel.config(text= "Result: " + str(getText))


window = tk.Tk()
window.title("Calculator")
window.geometry("500x300")
window.config(bg="white")

kalimat1 = tk.Label(window, text="Calculator", bg="white", fg="black", font="Consolas")
kalimat1.grid(column=4, row=0)

# C# string, int, bool, double, float

box = tk.Entry(window)
box.grid(column=4, row=1, sticky="ns")

box2 = tk.Entry(window)
box2.grid(column=4, row=2, sticky="ns")


label1 = tk.Label(window, text="number 1", bg="white", fg="black") 
label1.grid(column=1, row=1)

label2 = tk.Label(window, text="number 2", bg="white", fg="black") 
label2.grid(column=1, row=2)


button1 = tk.Button(window, text="add (+)", bg="green", fg="black", width=15, command=add)
button1.grid(column=4, row=4)

button2 = tk.Button(window, text="subtract (-)", bg="green", fg="black", width=15, command=sub)
button2.grid(column=4, row=5)

button3 = tk.Button(window, text="multiple (x)", bg="green", fg="black", width=15, command=multiply)
button3.grid(column=4, row=6)

button4 = tk.Button(window, text="divide (÷)", bg="green", fg="black", width=15, command=divide)
button4.grid(column=4, row=7)


testlabel = tk.Label(window, text="Place a number in the input.", bg="white", fg="black") 
testlabel.grid(column=0, row=10)

window.mainloop()
