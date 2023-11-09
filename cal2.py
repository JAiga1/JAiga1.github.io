from tkinter import *
win=Tk()
win.title('calcutor')
win.configure(background='gray12')
e=Entry(win,width=40,borderwidth=10,fg='snow',bg='gray12')
e.pack()
e.grid(row=0,column=0,columnspan=5,ipadx=20)


def backspace():
    en=e.get()
    L=len(en)
    e.delete(L-1)


def insert(nu):
    current=e.get()
    if current=='0':
        e.delete(0,END)
    else:    
        e.delete(0,END)
        cur1=str(current)+str(nu)
        e.insert(0,cur1)

    

def equal():
    j=e.get()
    tot=str(eval(j))
    e.delete(0,END)
    e.insert(0,tot)

def clear():
    e.delete(0,END)       


but1=Button(win,text='1',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert(1))
but1.grid(row=1,column=0)

but2=Button(win,text='2',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert(2))
but2.grid(row=1,column=1)

but3=Button(win,text='3',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert(3))
but3.grid(row=1,column=2)

but4=Button(win,text='4',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert(4))
but4.grid(row=2,column=0)

but5=Button(win,text='5',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert(5))
but5.grid(row=2,column=1)

but6=Button(win,text='6',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert(6))
but6.grid(row=2,column=2)

but7=Button(win,text='7',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert(7))
but7.grid(row=3,column=0)

but8=Button(win,text='8',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert(8))
but8.grid(row=3,column=1)

but9=Button(win,text='9',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert(9))
but9.grid(row=3,column=2)

but_clear=Button(win,text='clear',pady=20,padx=80,fg='snow', bg='gray12',command=clear)
but_clear.grid(row=5,column=1,columnspan=2)

but0=Button(win,text='0',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert(0))
but0.grid(row=4,column=0)

but_equal=Button(win,text='=',pady=20,padx=40,fg='snow', bg='gray12',command=equal)
but_equal.grid(row=6,column=1)

but_add=Button(win,text='+',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert('+'))
but_add.grid(row=4,column=1)

but_sub=Button(win,text='-',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert('-'))
but_sub.grid(row=4,column=2)

but_mul=Button(win,text='X',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert('*'))
but_mul.grid(row=5,column=0)

but_di=Button(win,text='/',pady=20,padx=40,fg='snow', bg='gray12',command=lambda:insert('/'))
but_di.grid(row=6,column=0)

but_bs=Button(win,text='BS',pady=20,padx=40,fg='snow', bg='gray12',command=backspace)
but_bs.grid(row=6,column=2)




win.mainloop()