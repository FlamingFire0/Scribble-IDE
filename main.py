#region imports 
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, END, X,Y,LEFT,RIGHT,BOTTOM, Menu, TOP,BOTH
import ttkbootstrap as ttk
from tkinter.simpledialog import askstring
import random
from screeninfo import get_monitors
from tkinter import font
from code import *


#endregion
#region start/important 

root = ttk.Window(themename=root_info.get("theme", "fermion"))

set_font_size(root_info.get('font_size', '16'))
font = font.Font(family=root_info.get('font', 'JetBrains Mono'), 
                 size=font_size+zoom_scale)

#center
dimensions = [int(i) for i in root_info.get("geometry", "800x800").split("x")]
for m in get_monitors():
    if m.is_primary:
        root.geometry(f"+{int(m.width/2-dimensions[0]/2)}+{int(m.height/2-dimensions[1]/2)-100}")
        break

#generic
root.title(root_info.get("title", "[NAME NOT FOUND]"))
root.geometry(root_info.get("geometry", "800x800"))
#image and x button
root.wm_iconphoto(False, ImageTk.PhotoImage(Image.open(root_info.get("icon", "icon.ico"))))
root.protocol('WM_DELETE_WINDOW', lambda: new_file(workspace, True))

    
#endregion
#region input 
input_frame = ttk.Frame(root)


scrollbar = ttk.Scrollbar(input_frame)


workspace = tk.Text(input_frame, tabs=4, relief="flat", yscrollcommand=scrollbar.set,
                    font=font, wrap=tk.WORD)
scrollbar.config(command=workspace.yview)

tk.Label(root, text="Text").pack(side=BOTTOM)

keyBindsBasic(workspace)
#endregion
#region extra keybinds 


def place_color_marker(x=None):
    workspace.insert(END, " ")
    color = askstring('Color selector', 'Enter a text color:').strip().lower()
    name = f'color-{random.random()}'
    workspace.tag_add(name, INSERT, END)
    workspace.tag_config(name, foreground=color)



workspace.bind(sequence="<Control-KeyPress-q>", func=place_color_marker)


def new_line_downwards(x=None):
    if int(workspace.index(END).split(".")[0])-int(workspace.index(INSERT).split(".")[0]) == 1:
        workspace.insert(END, "\n")

workspace.bind(sequence="<Down>", func=new_line_downwards)


def open_unicode_enter(x=None):
    print(unicode(askstring('unicode picker', 'Enter a unicode id:', ).strip().upper(), "utf-8"))



workspace.bind(sequence="<Control-KeyPress-u>", func=open_unicode_enter)
#endregion
#region menu 

menubar = ttk.Frame(root)

def create_menubutton(text, tearoff=0):
    menubutton = tk.Menubutton(
        menubar, text=text, underline=-1, relief=tk.RAISED)
    menubutton.menu = Menu(menubutton, tearoff=tearoff)
    menubutton["menu"] = menubutton.menu
    return menubutton


file_menu_button = create_menubutton("📄 File")
edit_menu_button = create_menubutton("⚒️ Edit")
help_menu_button = create_menubutton("❓ Help")


file_menu_button.menu.add_command(label="New", command=lambda: new_file(workspace))
file_menu_button.menu.add_command(label="Open", command=lambda: open_file(workspace))
file_menu_button.menu.add_command(label="Save", command=lambda: save_file(workspace))
file_menu_button.menu.add_command(label="Save as...", command=lambda: save_file_as(workspace))
file_menu_button.menu.add_separator()
file_menu_button.menu.add_command(label="Exit", command=lambda: new_file(workspace, True))


edit_menu_button.menu.add_command(label="Undo", command=lambda: undo(workspace))
edit_menu_button.menu.add_command(label="Redo", command=lambda: redo(workspace))
edit_menu_button.menu.add_separator()
edit_menu_button.menu.add_command(label="Lorem Ipsum", command=lambda: lorem_ipsum(workspace))
#edit_menu_button.menu.add_command(label="Cut", command=nothing)
#edit_menu_button.menu.add_command(label="Copy", command=nothing)
#edit_menu_button.menu.add_command(label="Paste", command=nothing)
#edit_menu_button.menu.add_command(label="Delete", command=nothing)
#edit_menu_button.menu.add_command(label="Select All", command=nothing)

help_menu_button.menu.add_command(
    label="Version: "+root_info.get("version", "[VERSION NOT FOUND]"), command=nothing)


#endregion
#region pack 

file_menu_button.pack(side=LEFT)
edit_menu_button.pack(side=LEFT)
help_menu_button.pack(side=LEFT)

menubar.pack(side=TOP, anchor=tk.NW)


statusbar = ttk.Label(root,text="")

scrollbar.pack(side=RIGHT, fill=Y)
workspace.pack(side=LEFT, fill=tk.BOTH, expand=True)
input_frame.pack(side=TOP, fill=tk.BOTH, expand=True)
#statusbar.pack(side=BOTTOM, fill=X, expand=True)
 
#ttk.Button(root, text="⨉").pack(side=RIGHT, anchor=tk.NE)
#endregion 
root.mainloop()