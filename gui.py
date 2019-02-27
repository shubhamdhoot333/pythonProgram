import tkinter
root = tkinter.Tk()
a=1
for r in range(4):
   for c in range(3):
            if r==3 and c==0:
                    tkinter.Button(root, text='ok', borderwidth=1, height=3, width=5).grid(row=r, column=c)
            elif r==3 and c==2:
                     tkinter.Button(root, text='cancel', borderwidth=1, height=3, width=5).grid(row=r, column=c)
            elif r==3 and c==1:
                   tkinter.Button(root, text=0, borderwidth=1, height=3, width=5).grid(row=r, column=c)
            else:
               tkinter.Button(root, text=a,borderwidth=1,height=3, width=5).grid(row=r, column=c)
            a+=1
root.mainloop()