from tkinter import *

window=Tk() #empty window

def kg_to_g():
    grams=float(e1_value.get())*1000
    t1.insert(END,grams)
    pounds=float(e1_value.get())*2.20462
    t2.insert(END,pounds)
    oz=float(e1_value.get())*35.274
    t3.insert(END,oz)

kg=Label(window,text='Kg')
kg.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text='Convert kilograms',command=kg_to_g)
b1.grid(row=0,column=2)

t1=Text(window,height=1,width=35)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=35)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=35)
t3.grid(row=1,column=2)

window.mainloop()
