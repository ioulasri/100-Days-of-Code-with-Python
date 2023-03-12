from tkinter import *
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='Reply', message='The result is %s!' % name)


top = Tk()
top.title('Number converter')
top.iconbitmap('py-blue-trans-out.ico')
Label(top, text="Enter your decimal number:").pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
Label(top, text="Enter the second number:").pack(side=TOP)
rnt = Entry(top)
rnt.pack(side=TOP)
btn = Button(top, text="+", command=(lambda: reply(int(ent.get()) + int(rnt.get()))))
btn.pack(side=LEFT)
btn = Button(top, text="-", command=(lambda: reply(int(ent.get()) - int(rnt.get()))))
btn.pack(side=LEFT)
btn = Button(top, text="*", command=(lambda: reply(int(ent.get()) * int(rnt.get()))))
btn.pack(side=LEFT)
btn = Button(top, text="/", command=(lambda: reply(int(ent.get()) / int(rnt.get()))))
btn.pack(side=LEFT)
top.mainloop()
