from tkinter import *
# notepad
root = Tk()
root.geometry('250x300')
root.title("NotePad")
root.minsize('240','240')
root.maxsize('720', '620')
def new():
    pass
def newwindow():
    pass
def open1():
    pass
def save():
    pass
def saveas():
    pass
def pagesetup():
    pass
def undo():
    pass
def cut():
    pass
def copy():
    pass
def paste():
    pass
def delete():
    pass
def swb():
    pass
def find():
    pass
def fnext():
    pass
def fprev():
    pass
def replace():
    pass
def goto():
    pass
def selectall():
    pass
def td():
    pass
def ww():
    pass
def font():
    pass
def zoomin():
    pass
def zoomout():
    pass
def rdzoom():
    pass
def statusbar():
    pass
def viewhelp():
    pass
def sendfb():
    pass
def about():
    pass
mymenu = Menu(root)
m1 = Menu(mymenu,tearoff=0)
m1.add_command(label="New", command=new)
m1.add_command(label="New Window", command=newwindow)
m1.add_command(label="Open", command=open1)
m1.add_command(label="Save", command=save)
m1.add_command(label="Save As", command=saveas)
m1.add_separator()
m1.add_command(label="Page Setup", command=pagesetup)
m1.add_command(label="Print", command=print)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
root.config(menu=mymenu)
mymenu.add_cascade(label="file", menu=m1)


m2 = Menu(mymenu,tearoff=0)
m2.add_command(label="Undo", command=undo)
m2.add_separator()
m2.add_command(label="Cut", command=cut)
m2.add_command(label="Copy", command=copy)
m2.add_command(label="Paste", command=paste)
m2.add_command(label="Delete", command=delete)
m2.add_separator()
m2.add_command(label="Search with Bing...", command=swb)
m2.add_command(label="Find", command=find)
m2.add_command(label="Find Next", command=fnext)
m2.add_command(label="Find Previous", command=fprev)
m2.add_command(label="Replace", command=replace)
m2.add_command(label="Go To", command=goto)

m2.add_separator()
m2.add_command(label="Select All", command=selectall)
m2.add_command(label="Time/Date", command=td)
root.config(menu=mymenu)
mymenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mymenu,tearoff=0)
m3.add_command(label="Word Wrap", command=ww)
m3.add_command(label="Font", command=font)
root.config(menu=mymenu)
mymenu.add_cascade(label="Format", menu=m3)

m4 = Menu(mymenu,tearoff=0)

m5 = Menu(m4,tearoff=0)
m5.add_command(label="Zoom In", command=zoomin)
m5.add_command(label="Zoom Out", command=zoomout)
m5.add_command(label="Restore Default Zoom", command=rdzoom)
root.config(menu=mymenu)
m4.add_cascade(label="Zoom",menu=m5)

m4.add_command(label="Status Bar", command=statusbar)
root.config(menu=mymenu)
mymenu.add_cascade(label="View", menu=m4)

m6 = Menu(mymenu,tearoff=0)
m6.add_command(label="View Help", command=viewhelp)
m6.add_command(label="Send Feedback", command=sendfb)
m6.add_separator()
m6.add_command(label="About NotePad" , command=about)
root.config(menu=mymenu)
mymenu.add_cascade(label="Help", menu=m6)

scrollbar = Scrollbar(root )
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)

scrollbar.config(command=text.yview)



root.mainloop()