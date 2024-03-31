import tkinter as tk
import tkinter.messagebox

def calc():
       try:
              n1=int(e1.get())
              n2=int(e2.get())
              opr=e3.get()
              if opr=='+':
                     r=n1+n2
              elif opr=='-':
                     r=n1-n2
              elif opr=='*':
                     r=n1*n2
              elif opr=='/':
                     if n2==0:
                            raise ZeroDivisionError
                     else:
                            r=n1/n2
              l1.config(text="result:"+str(r))
       except:
              l1.config(text="inv input")
       
rt=tk.Tk()
rt.title("calculater")
rt.geometry('300x100')

l1=tk.Label(rt,text='Result:')
l1.grid(row=1,column=0,columnspan=4)

e1=tk.Entry(rt,width=10)
e1.grid(row=0,column=0)
e3=tk.Entry(rt,width=5)
e3.grid(row=0,column=1)
e2=tk.Entry(rt,width=10)
e2.grid(row=0,column=2)

b1=tk.Button(rt,text='calculator',command=calc)
b1.grid(row=0,column=3)

rt.mainloop()
