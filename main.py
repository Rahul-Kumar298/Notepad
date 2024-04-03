from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os

def new():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def newwindow():
    new_window = Toplevel(root)
    new_window.title("New Window")
def open1():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt",
                                       filetypes=[("All Files", "*.*"),
                                                  ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())

def save():
    global file
    if file is None:
        saveas()
    else:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))

def saveas():
    global file
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))
def pagesetup():
     # Create a new window for page setup
    page_setup_window = Toplevel(root)
    page_setup_window.title("Page Setup")

    # Define and add widgets for page setup
    label = ttk.Label(page_setup_window, text="Page Layout:")
    label.grid(row=0, column=0, padx=10, pady=5)

    layout_var = StringVar()
    layout_combo = ttk.Combobox(page_setup_window, textvariable=layout_var, values=["Portrait", "Landscape"])
    layout_combo.current(0)
    layout_combo.grid(row=0, column=1, padx=10, pady=5)

    label_size = ttk.Label(page_setup_window, text="Page Size:")
    label_size.grid(row=1, column=0, padx=10, pady=5)

    size_var =StringVar()
    size_combo = ttk.Combobox(page_setup_window, textvariable=size_var, values=["A4", "Letter", "Legal"])
    size_combo.current(0)
    size_combo.grid(row=1, column=1, padx=10, pady=5)

    # Add a preview section
    preview_frame = ttk.LabelFrame(page_setup_window, text="Preview", height=200, width=300)
    preview_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    # Create a button to apply page setup settings
    apply_button = ttk.Button(page_setup_window, text="Apply", command=apply_page_setup)
    apply_button.grid(row=3, column=0, padx=5, pady=5)

    # Create a button to cancel page setup settings
    cancel_button = ttk.Button(page_setup_window, text="Cancel", command=page_setup_window.destroy)
    cancel_button.grid(row=3, column=1, padx=5, pady=5)

def apply_page_setup():
    # Apply page setup settings
    # Implement the logic to apply page setup settings here
    messagebox.showinfo("Page Setup", "Page setup settings applied.")

def undo():
    pass
def cut():
    TextArea.event_generate("<Control-x>")

def copy():
    TextArea.event_generate("<Control-c>")

def paste():
    TextArea.event_generate("<Control-v>")

def delete():
    TextArea.delete(SEL_FIRST, SEL_LAST)
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
    TextArea.tag_add(SEL, "1.0", END)
    TextArea.mark_set(INSERT, "1.0")
    TextArea.see(INSERT)
    return 'break'
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

# notepad
root = Tk()
root.geometry('250x300')
root.title("NotePad")
root.minsize('240','240')
root.maxsize('720', '620')
root.wm_iconbitmap("1.ico")
mymenu = Menu(root)
# creating filemenu
filemenu = Menu(mymenu,tearoff=0)
filemenu.add_command(label="New", command=new, accelerator="Ctrl+N")
filemenu.add_command(label="New Window", command=newwindow)
filemenu.add_command(label="Open", command=open1)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As", command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Page Setup", command=pagesetup)
filemenu.add_command(label="Print", command=print)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
root.config(menu=mymenu)
mymenu.add_cascade(label="file", menu=filemenu)

# creating Edit Menu
editmenu = Menu(mymenu,tearoff=0)
editmenu.add_command(label="Undo", command=undo)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
editmenu.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
editmenu.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
editmenu.add_command(label="Delete", command=delete)
editmenu.add_separator()
editmenu.add_command(label="Search with Bing...", command=swb)
editmenu.add_command(label="Find", command=find)
editmenu.add_command(label="Find Next", command=fnext)
editmenu.add_command(label="Find Previous", command=fprev)
editmenu.add_command(label="Replace", command=replace)
editmenu.add_command(label="Go To", command=goto)
editmenu.add_separator()
editmenu.add_command(label="Select All", command=selectall, accelerator="Ctrl+A")
editmenu.add_command(label="Time/Date", command=td)
root.config(menu=mymenu)
mymenu.add_cascade(label="Edit", menu=editmenu)

# creating Format Menu
formatmenu = Menu(mymenu,tearoff=0)
formatmenu.add_command(label="Word Wrap", command=ww)
formatmenu.add_command(label="Font", command=font)
root.config(menu=mymenu)
mymenu.add_cascade(label="Format", menu=formatmenu)

# creting view menu
viewmenu = Menu(mymenu,tearoff=0)
# creating zoom menu
zoommenu = Menu(viewmenu,tearoff=0)
zoommenu.add_command(label="Zoom In", command=zoomin)
zoommenu.add_command(label="Zoom Out", command=zoomout)
zoommenu.add_command(label="Restore Default Zoom", command=rdzoom)
root.config(menu=mymenu)
viewmenu.add_cascade(label="Zoom",menu=zoommenu)
viewmenu.add_command(label="Status Bar", command=statusbar)
root.config(menu=mymenu)
mymenu.add_cascade(label="View", menu=viewmenu)

# creating Help Menu
helpmenu = Menu(mymenu,tearoff=0)
helpmenu.add_command(label="View Help", command=viewhelp)
helpmenu.add_command(label="Send Feedback", command=sendfb)
helpmenu.add_separator()
helpmenu.add_command(label="About NotePad" , command=about)
root.config(menu=mymenu)
mymenu.add_cascade(label="Help", menu=helpmenu)

scrollbar = Scrollbar(root )
scrollbar.pack(side=RIGHT, fill=Y)
TextArea = Text(root, yscrollcommand=scrollbar.set)
TextArea.pack(fill=BOTH, expand=True)
scrollbar.config(command=TextArea.yview)
root.mainloop()