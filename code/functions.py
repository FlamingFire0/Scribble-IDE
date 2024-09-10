import tkinter as tk
from tkinter import filedialog, END, X, Y, LEFT, RIGHT, BOTTOM, Menu, TOP, BOTH
import ttkbootstrap as ttk
import yaml

with open("window.yaml", "r") as f:
    root_info = dict(yaml.safe_load(f))

font_size = 16
zoom_scale = 0
opened = ""
brackets = dict(root_info.get("bracket_close", {"(":")", "{":"}", "<":">", "[":"]", "'":"'", '"':'"'}))

#region other 
def set_font_size(size):
    global font_size
    font_size = int(size)

def root(workspace):
    return workspace.master.master

def zoom(extra):
    global zoom_scale
    zoom_scale += extra
    font.configure(size=font_size+zoom_scale)


def nothing(*args, **kwargs):
    pass


def lorem_ipsum(workspace):
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Imperdiet sed euismod nisi porta lorem. Elementum tempus egestas sed sed risus. Gravida cum sociis natoque penatibus et. Blandit cursus risus at ultrices. Elit ut aliquam purus sit amet luctus venenatis lectus magna. Vitae nunc sed velit dignissim sodales. Dignissim sodales ut eu sem integer vitae. Porttitor lacus luctus accumsan tortor. Lorem ipsum dolor sit amet.".replace(
        ". ", ".\n\n")
    new_file(workspace)
    workspace.insert(END, lorem)

#endregion

#region edit 
def open_file(workspace):
    global opened

    new_file(workspace)

    data = filedialog.askopenfile()

    workspace.delete("0.0", END)
    workspace.insert("insert", data.read())
    opened = data.name

def new_file(workspace, close=False):
    global opened
    if opened:
        with open(opened) as f:
            if f.read().strip() != workspace.get("0.0", END).strip():
                response = tk.messagebox.askyesnocancel(
                    "Save changes?", "Same changes have been made to the opened file. \nIf you click No, changes will be deleted!", default="yes", parent=root(workspace))

                if response is None:
                    # User clicked "Cancel"
                    return
                elif response:
                    # User clicked "Yes,"
                    save_file()
    else:
        if workspace.get("0.0", END).strip() != "":
            response = tk.messagebox.askyesnocancel(
                "Save changes?", "Same changes have been made to the opened file. \nIf you click No, changes will be deleted!", default="yes", parent=root(workspace))

            if response is None:
                # User clicked "Cancel"
                return
            elif response:
                # User clicked "Yes,"
                save_file()
    opened = ""
    workspace.delete("0.0", END)
    if close:
        root(workspace).destroy()


def save_file(workspace):
    global opened
    if opened:
        with open(opened, "w") as f:
            f.write(workspace.get("0.0", END).strip())
    else:
        save_file_as()


def save_file_as(workspace):
    global opened

    with filedialog.asksaveasfile(mode='w', filetypes=[
        ('All Files', '*.*'),
        ('Python Files', '*.py'),
        ('Text Documents', '*.txt')
    ], defaultextension=".txt") as f:
        f.write(str(workspace.get("0.0", END)))

#endregion

#region undo/redo 
undo_memory = ["" for i in range(10)]
redo_memory = []

def undo(workspace):
    global undo_memory, redo_memory

    redo_memory.append(workspace.get("0.0", END))

    workspace.delete("0.0", END)
    workspace.insert("insert", undo_memory.pop().strip())


def redo(workspace):
    global redo_memory, undo_memory

    undo_memory.append(workspace.get("0.0", END))

    workspace.delete("0.0", END)
    workspace.insert("insert", redo_memory.pop().strip())
#endregion

#region bracket mod 
#def insert_closing_bracket(workspace, symbol):
#    delay = 1
#
#    def func():
#        # positions = [int(pos) for pos in workspace.index(INSERT).split(".")]
#        workspace.insert("insert", symbol)
#        workspace.mark_set("insert", "insert-1c")
#
#    workspace.after(delay, func)
#    # workspace.insert(f"{positions[0]}.{positions[1]+1}", symbol)


def remove_closing_brackets(workspace):
    for symbol in brackets.items():
        if workspace.get("insert-1c") == symbol[0]:
            if workspace.get("insert") == symbol[1]:
                workspace.delete("insert")
                break


def insert_closing_brackets(workspace):
    def func():
        for symbol in brackets.items():
            #print(workspace.get("insert-1c"),workspace.get("insert"),workspace.get("insert+1c"))
            if workspace.get("insert-1c") == symbol[0]:
                    #workspace.delete("insert")
                    workspace.insert("insert", symbol[1])
                    workspace.mark_set("insert", "insert-1c")
                    break
                
    workspace.after(1, func)


#endregion

#

