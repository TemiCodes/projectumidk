from tkinter import *
from tkinter import ttk
op=Tk()
op.title("DRAWING SHAPES")
op.geometry("1001x700")
op.configure(bg="pink")
convas=Canvas(width="950", height="500", borderwidth=2)
convas.pack()
lbl=Label(op,text="choose color:")
lbl.place(relx=0.8,rely=0.9,anchor=CENTER)
fillcolor=["red","blue","yellow","green","cyan"]
drop_down=ttk.Combobox(op,state="readonly",values=fillcolor, width=10)
drop_down.place(relx=0.95,rely=0.9,anchor=CENTER)
labelx=Label(op,text="startx:")
values=["10","50","100","200","300","400","500","600","800","900"]
startx=ttk.Combobox(op,state="readonly",values=values,width=10)
labelx.place(relx=0.8,rely=0.8,anchor=CENTER)
startx.place(relx=0.9,rely=0.8,anchor=CENTER)
labely=Label(op,text="starty:")
starty=ttk.Combobox(op,state="readonly",values=values,width=10)
labely.place(relx=0.6,rely=0.8,anchor=CENTER)
starty.place(relx=0.7,rely=0.8,anchor=CENTER)
labelxend=Label(op,text="endx:")
endx=ttk.Combobox(op,state="readonly",values=values,width=10)
labelxend.place(relx=0.4,rely=0.8,anchor=CENTER)
endx.place(relx=0.5,rely=0.8,anchor=CENTER)
labelyend=Label(op,text="endy:")
endy=ttk.Combobox(op,state="readonly",values=values,width=10)
labelyend.place(relx=0.2,rely=0.8,anchor=CENTER)
endy.place(relx=0.3,rely=0.8,anchor=CENTER)
op.mainloop()
#open with python please