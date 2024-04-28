from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os
from tkinter import simpledialog

file = None

def new():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
def newwindow():
    # Create a new window for the Notepad
    new_window = Toplevel(root)
    new_window.title("Untitled - Notepad")

    # Text area
    new_text_area = Text(new_window, wrap="word")
    new_text_area.pack(fill="both", expand=True)

    # Scrollbar
    new_scrollbar = Scrollbar(new_window)
    new_scrollbar.pack(side="right", fill="y")
    new_scrollbar.config(command=new_text_area.yview)
    new_text_area.config(yscrollcommand=new_scrollbar.set)

    # Menu
    new_menu = Menu(new_window)
    new_window.config(menu=new_menu)

    # File menu
    new_file_menu = Menu(new_menu, tearoff=0)
    new_file_menu.add_command(label="New", command=new, accelerator="Ctrl+N")
    new_file_menu.add_command(label="Newwindow", command=newwindow, accelerator="Ctrl+shift+N")
    new_file_menu.add_command(label="Open", command=open1, accelerator="Ctrl+O")
    new_file_menu.add_command(label="Save", command=save, accelerator="Ctrl+S")
    new_file_menu.add_command(label="Save As", command=saveas, accelerator="Ctrl+Shift+S")
    new_file_menu.add_separator()
    new_file_menu.add_command(label="Exit", command=new_window.destroy, accelerator="Alt+F4")
    new_menu.add_cascade(label="File", menu=new_file_menu)

    # Edit menu
    new_edit_menu = Menu(new_menu, tearoff=0)
    new_edit_menu.add_command(label="Undo", command=undo, accelerator="Ctrl+Z")
    new_edit_menu.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
    new_edit_menu.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
    new_edit_menu.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
    new_edit_menu.add_command(label="Delete", command=delete, accelerator="Del")
    new_edit_menu.add_separator()
    new_edit_menu.add_command(label="Select All", command=selectall, accelerator="Ctrl+A")
    new_menu.add_cascade(label="Edit", menu=new_edit_menu)

    # Format menu
    new_format_menu = Menu(new_menu, tearoff=0)
    new_format_menu.add_command(label="Word Wrap", command=ww)
    new_format_menu.add_command(label="Font", command=font)
    new_menu.add_cascade(label="Format", menu=new_format_menu)

    # View menu
    new_view_menu = Menu(new_menu, tearoff=0)
    new_zoom_menu = Menu(new_view_menu, tearoff=0)
    new_zoom_menu.add_command(label="Zoom In", command=zoomin, accelerator="Ctrl++")
    new_zoom_menu.add_command(label="Zoom Out", command=zoomout, accelerator="Ctrl+-")
    new_zoom_menu.add_command(label="Restore Default Zoom", command=rdzoom, accelerator="Ctrl+0")
    new_view_menu.add_cascade(label="Zoom", menu=new_zoom_menu)
    new_view_menu.add_command(label="Status Bar", command=statusbar)
    new_menu.add_cascade(label="View", menu=new_view_menu)

    # Help menu
    new_help_menu = Menu(new_menu, tearoff=0)
    new_help_menu.add_command(label="View Help", command=viewhelp)
    new_help_menu.add_command(label="Send Feedback", command=sendfb)
    new_help_menu.add_separator()
    new_help_menu.add_command(label="About Notepad", command=about)
    new_menu.add_cascade(label="Help", menu=new_help_menu)

    # Set initial window size
    new_window.geometry('500x400')

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
        saveas()  # Call saveas function if file is None
    else:
        try:
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file:\n{e}")


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

    # Paper Frame
    paper_frame = ttk.LabelFrame(page_setup_window, text="Paper")
    paper_frame.grid(column=0, row=0, padx=10, pady=5)

    ttk.Label(paper_frame, text="Size:").grid(column=0, row=0)
    size_combobox = ttk.Combobox(paper_frame, values=('A3', 'A4', 'A5', 'B4 (JIS)', 'B5 (JIS)', 'Executive', 'Legal', 'Letter', 'Statement', 'Tobloid'))
    size_combobox.current(0)  # set the selected item
    size_combobox.grid(column=1, row=0)

    ttk.Label(paper_frame, text="Source:").grid(column=0, row=1)
    source_combobox = ttk.Combobox(paper_frame, values=('Default Tray', 'Manual Feed'))
    source_combobox.grid(column=1, row=1)

    # Orientation Frame
    orientation_frame = ttk.LabelFrame(page_setup_window, text="Orientation")
    orientation_frame.grid(column=0, row=1, padx=10, pady=5)

    orientation = tk.StringVar()
    portrait_radio_btn = ttk.Radiobutton(orientation_frame, text='Portrait', value='Portrait', variable=orientation)
    portrait_radio_btn.grid(column=0, row=0)
    landscape_radio_btn = ttk.Radiobutton(orientation_frame, text='Landscape', value='Landscape', variable=orientation)
    landscape_radio_btn.grid(column=1, row=0)

    # Margins Frame
    margins_frame = ttk.LabelFrame(page_setup_window, text="Margins (millimeters)")
    margins_frame.grid(column=0, row=2, padx=10, pady=5)

    ttk.Label(margins_frame, text="Left:").grid(column=0, row=0)
    left_margin_entry = ttk.Entry(margins_frame)
    left_margin_entry.grid(column=1, row=0)

    ttk.Label(margins_frame, text="Right:").grid(column=2, row=0)
    right_margin_entry = ttk.Entry(margins_frame)
    right_margin_entry.grid(column=3, row=0)

    ttk.Label(margins_frame, text="Top:").grid(column=0, row=1)
    top_margin_entry = ttk.Entry(margins_frame)
    top_margin_entry.grid(column=1, row=1)

    ttk.Label(margins_frame, text="Bottom:").grid(column=2, row=1)
    bottom_margin_entry = ttk.Entry(margins_frame)
    bottom_margin_entry.grid(column=3, row=1)

    # Preview Frame
    preview_frame = ttk.LabelFrame(page_setup_window, text="Preview")
    preview_frame.grid(column=1, row=0, rowspan=3, padx=10, pady=5, sticky='nswe')

    # Placeholder for preview content
    preview_content = tk.Canvas(preview_frame, bg='white', width=200, height=100)
    preview_content.pack(expand=True, fill='both')

    def apply_page_setup():
        # Retrieve selected settings
        selected_size = size_combobox.get()
        selected_source = source_combobox.get()
        selected_orientation = orientation.get()
        selected_left_margin = left_margin_entry.get()
        selected_right_margin = right_margin_entry.get()
        selected_top_margin = top_margin_entry.get()
        selected_bottom_margin = bottom_margin_entry.get()

        # Implement logic to apply page setup settings here
        # For demonstration, let's just display the selected settings
        message = f"Size: {selected_size}\n"
        message += f"Source: {selected_source}\n"
        message += f"Orientation: {selected_orientation}\n"
        message += f"Left Margin: {selected_left_margin}\n"
        message += f"Right Margin: {selected_right_margin}\n"
        message += f"Top Margin: {selected_top_margin}\n"
        message += f"Bottom Margin: {selected_bottom_margin}\n"
        messagebox.showinfo("Page Setup", message)

    # Create a button to apply page setup settings
    apply_button = ttk.Button(page_setup_window, text="Apply", command=apply_page_setup)
    apply_button.grid(row=4, column=0, padx=5, pady=5)

    # Create a button to cancel page setup settings
    cancel_button = ttk.Button(page_setup_window, text="Cancel", command=page_setup_window.destroy)
    cancel_button.grid(row=4, column=1, padx=5, pady=5)

    # Update the preview when settings change
    def update_preview(*args):
        # Clear the current preview
        preview_content.delete("all")

        # Get the selected paper size
        paper_size = size_combobox.get()

        # Define the dimensions of the paper based on size (in millimeters)
        if paper_size == 'A3':
            paper_width = 297
            paper_height = 420
        elif paper_size == 'A4':
            paper_width = 210
            paper_height = 297
        elif paper_size == 'A5':
            paper_width = 148
            paper_height = 210
        elif paper_size == 'B4 (JIS)':
            paper_width = 257
            paper_height = 364
        elif paper_size == 'B5 (JIS)':
            paper_width = 182
            paper_height = 257
        elif paper_size == 'Executive':
            paper_width = 184
            paper_height = 267
        elif paper_size == 'Legal':
            paper_width = 216
            paper_height = 356
        elif paper_size == 'Letter':
            paper_width = 216
            paper_height = 279
        elif paper_size == 'Statement':
            paper_width = 140
            paper_height = 216
        elif paper_size == 'Tobloid':
            paper_width = 279
            paper_height = 432

        # Get the selected orientation
        selected_orientation = orientation.get()

        # Calculate the width and height based on orientation
        if selected_orientation == 'Portrait':
            width = paper_width
            height = paper_height
        else:  # Landscape
            width = paper_height
            height = paper_width

        # Get the margins (default to 0 if not specified)
        left_margin = int(left_margin_entry.get() or 0)
        right_margin = int(right_margin_entry.get() or 0)
        top_margin = int(top_margin_entry.get() or 0)
        bottom_margin = int(bottom_margin_entry.get() or 0)

        # Draw the paper rectangle with margins
        x0 = left_margin
        y0 = top_margin
        x1 = width - right_margin
        y1 = height - bottom_margin
        preview_content.create_rectangle(x0, y0, x1, y1, outline="black", fill="gray")

    # Bind the update_preview function to changes in the settings
    size_combobox.bind('<<ComboboxSelected>>', update_preview)
    orientation.trace_add('write', update_preview)
    left_margin_entry.bind('<KeyRelease>', update_preview)
    right_margin_entry.bind('<KeyRelease>', update_preview)
    top_margin_entry.bind('<KeyRelease>', update_preview)
    bottom_margin_entry.bind('<KeyRelease>', update_preview)


def undo():
    TextArea.edit_undo()
def cut():
    TextArea.event_generate("<Control-x>")

def copy():
    TextArea.event_generate("<Control-c>")

def paste():
    TextArea.event_generate("<Control-v>")

def delete():
    TextArea.delete(SEL_FIRST, SEL_LAST)


def search_google(selected_text):
    import webbrowser
    search_query = 'https://www.google.com/search?q=' + '+'.join(selected_text.split())
    webbrowser.open_new_tab(search_query)


def find_text():
    # Create a dialog box for finding text
    find_dialog = tk.Toplevel(root)
    find_dialog.title("Find")
    
    # Label and Entry for entering text to find
    ttk.Label(find_dialog, text="Find what:").grid(row=0, column=0, padx=5, pady=5)
    find_entry = ttk.Entry(find_dialog, width=30)
    find_entry.grid(row=0, column=1, padx=5, pady=5)
    
    # Function to find text within the TextArea
    def find():
        # Get the text to find
        text_to_find = find_entry.get()
        if text_to_find:
            # Search for the text within the TextArea
            start_index = "1.0"
            while True:
                start_index = TextArea.search(text_to_find, start_index, stopindex="end", nocase=1)
                if not start_index:
                    messagebox.showinfo("Find", "No more matches found")
                    break
                end_index = f"{start_index}+{len(text_to_find)}c"
                TextArea.tag_add(SEL, start_index, end_index)
                TextArea.mark_set(INSERT, end_index)
                TextArea.see(INSERT)
                start_index = end_index
    
    # Button to initiate the search
    find_button = ttk.Button(find_dialog, text="Find", command=find)
    find_button.grid(row=0, column=2, padx=5, pady=5)


def find_next():
    global last_search
    # Get the search string from the user
    search_str = simpledialog.askstring("Find Next", "Find what:", initialvalue=last_search)
    
    if search_str:
        # Search for the text from the current cursor position onwards
        start_pos = TextArea.search(search_str, INSERT, stopindex=END)
        if start_pos:
            end_pos = f"{start_pos}+{len(search_str)}c"
            # Highlight the found text
            TextArea.tag_remove(SEL, "1.0", END)
            TextArea.tag_add(SEL, start_pos, end_pos)
            TextArea.mark_set(INSERT, end_pos)
            TextArea.see(INSERT)
            last_search = search_str
        else:
            messagebox.showinfo("Notepad", f"Cannot find '{search_str}'")


def find_previous():
    # Get the search string from a dialog box
    search_string = simpledialog.askstring("Find Previous", "Enter text to find:")
    
    # If the search string is not empty
    if search_string:
        # Get the current text content
        content = TextArea.get("1.0", "end-1c")
        
        # Find the position of the last occurrence of the search string before the current cursor position
        start_position = content.rfind(search_string, 0, TextArea.index("insert"))
        
        # If a match is found
        if start_position != -1:
            # Calculate end position
            end_position = f"{start_position}+{len(search_string)}c"
            # Highlight the found text
            TextArea.tag_remove("found", "1.0", "end")
            TextArea.tag_add("found", f"{start_position}", end_position)
            TextArea.tag_config("found", background="yellow")
            # Set cursor to the start of the found text
            TextArea.mark_set("insert", start_position)
            TextArea.see("insert")
        else:
            messagebox.showinfo("Find Previous", f"No occurrences of '{search_string}' found before the cursor position.")

def replace():
    # Function to handle the replace operation
    
    # Create a dialog box for input
    replace_dialog = tk.Toplevel(root)
    replace_dialog.title("Replace")
    
    # Labels and entry fields for "Find what" and "Replace with"
    ttk.Label(replace_dialog, text="Find what:").grid(row=0, column=0, padx=5, pady=5)
    find_entry = ttk.Entry(replace_dialog)
    find_entry.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(replace_dialog, text="Replace with:").grid(row=1, column=0, padx=5, pady=5)
    replace_entry = ttk.Entry(replace_dialog)
    replace_entry.grid(row=1, column=1, padx=5, pady=5)
    
    # Function to perform the replace operation
    def perform_replace():
        find_text = find_entry.get()
        replace_text = replace_entry.get()
        
        if find_text:
            # Replace all occurrences of find_text with replace_text
            content = TextArea.get(1.0, "end")
            updated_content = content.replace(find_text, replace_text)
            TextArea.delete(1.0, "end")
            TextArea.insert("end", updated_content)
        
        # Close the replace dialog
        replace_dialog.destroy()
    
    # Button to perform the replace operation
    ttk.Button(replace_dialog, text="Replace", command=perform_replace).grid(row=2, column=0, columnspan=2, padx=5, pady=5)


def goto():
    # Create a new window for "Go To" dialog
    goto_window = Toplevel(root)
    goto_window.title("Go To Line")

    # Label and Entry for entering line number
    ttk.Label(goto_window, text="Line Number:").grid(row=0, column=0, padx=5, pady=5)
    line_number_entry = ttk.Entry(goto_window)
    line_number_entry.grid(row=0, column=1, padx=5, pady=5)

    # Function to navigate to the specified line
    def goto_line():
        try:
            # Get the line number entered by the user
            line_number = int(line_number_entry.get())
            # Ensure line number is within the range of available lines
            if 1 <= line_number <= int(TextArea.index('end').split('.')[0]):
                # Move cursor to the specified line
                TextArea.mark_set("insert", f"{line_number}.0")
                TextArea.see("insert")
            else:
                messagebox.showerror("Error", "Invalid line number")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid line number")

    # Button to confirm and navigate to the specified line
    ttk.Button(goto_window, text="Go To", command=goto_line).grid(row=1, column=0, columnspan=2, padx=5, pady=5)


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
    import webbrowser
    webbrowser.open("https://www.bing.com/search?q=get+help+with+notepad+in+windows&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA")


def sendfb():
    def submit_feedback():
        feedback = feedback_entry.get()
        messagebox.showinfo("Feedback", f"Thank you for your feedback:\n{feedback}")

    # Create the main window
    root = tk.Tk()
    root.title("Feedback Form")

    # Create a label and entry field for feedback
    feedback_label = tk.Label(root, text="Please provide your feedback:")
    feedback_label.pack()
    feedback_entry = tk.Entry(root, width=50)
    feedback_entry.pack()

    # Create a button to submit feedback
    submit_button = tk.Button(root, text="Submit", command=submit_feedback)
    submit_button.pack()

def about():
    messagebox.showinfo("Notepad - Made by Rahul", "This notepad is made in python and this is a clone of Microsoft Notepad.")
# notepad
root = Tk()
root.geometry('500x400')
root.title("Untitled - Notepad")
root.minsize('240','240')
root.maxsize('720', '620')
root.wm_iconbitmap("1.ico")
mymenu = Menu(root)
# creating filemenu
filemenu = Menu(mymenu,tearoff=0)
filemenu.add_command(label="New", command=new, accelerator="Ctrl+N")
filemenu.add_command(label="New Window", command=newwindow, accelerator="Ctrl+Shift+N")
filemenu.add_command(label="Open", command=open1, accelerator="Ctrl+O")
filemenu.add_command(label="Save", command=save, accelerator="Ctrl+S")
filemenu.add_command(label="Save As", command=saveas, accelerator="Ctrl+Shift+S")
filemenu.add_separator()
filemenu.add_command(label="Page Setup", command=pagesetup)
filemenu.add_command(label="Print", command=print, accelerator="Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)
root.config(menu=mymenu)
mymenu.add_cascade(label="File", menu=filemenu)

# creating Edit Menu
editmenu = Menu(mymenu,tearoff=0)
editmenu.add_command(label="Undo", command=undo, accelerator="Ctrl+Z")
editmenu.add_separator()
editmenu.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
editmenu.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
editmenu.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
editmenu.add_command(label="Delete", command=delete, accelerator="Del")
editmenu.add_separator()
editmenu.add_command(label="Search with Google...", command=search_google, accelerator="Ctrl+E")
editmenu.add_command(label="Find", command=find_text, accelerator="Ctrl+F")
editmenu.add_command(label="Find Next", command=find_next, accelerator="F3")
editmenu.add_command(label="Find Previous", command=find_previous, accelerator="Shift+F3")
editmenu.add_command(label="Replace", command=replace, accelerator="Ctrl+H")
editmenu.add_command(label="Go To", command=goto, accelerator="Ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select All", command=selectall, accelerator="Ctrl+A")
editmenu.add_command(label="Time/Date", command=td, accelerator="F5")
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