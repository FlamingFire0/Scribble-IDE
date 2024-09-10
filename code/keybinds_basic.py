import tkinter as tk
from .functions import *



def keyBindsBasic(workspace):

    workspace.bind(sequence="<Control-KeyPress-z>", func=lambda x: undo(workspace))
    workspace.bind(sequence="<Control-KeyPress-y>", func=lambda x: redo(workspace))
    workspace.bind(sequence="<Control-KeyPress-o>", func=lambda x: open_file(workspace))
    workspace.bind(sequence="<Control-KeyPress-s>", func=lambda x: save_file(workspace))
    workspace.bind(sequence="<Control-Shift-KeyPress-s>", func=lambda x: save_file_as(workspace))
    workspace.bind(sequence="<space>", func=lambda x: undo_memory.append(workspace.get("0.0", END))) #memory checkpoint
    #workspace.bind(sequence="<KeyPress>", func=lambda x: )

    #def close_bracket(workspace, *symbols):
    #    for symbol in symbols:
    #        opening = symbol[0].replace("<", "KeyPress-<>")
    #        closing = symbol[1]
    #        
    #        workspace.bind(sequence=opening, func=lambda x: insert_closing_bracket(workspace, closing))
    #    

    #workspace.bind(sequence="{", func=lambda x: insert_closing_bracket(workspace, "}"))
    #workspace.bind(sequence="(", func=lambda x: insert_closing_bracket(workspace, ")"))
    #workspace.bind(sequence="[", func=lambda x: insert_closing_bracket(workspace, "]"))
    #workspace.bind(sequence="'", func=lambda x: insert_closing_bracket(workspace, "'"))
    #workspace.bind(sequence='"', func=lambda x: insert_closing_bracket(workspace, '"'))
    workspace.bind(sequence="<KeyPress>" , func=lambda x: insert_closing_brackets(workspace))
    workspace.bind(sequence="<BackSpace>", func=lambda x: remove_closing_brackets(workspace))
    
    #workspace.bind(sequence="<Control-KeyPress-equal>", func=lambda x: zoom(workspace, font,  5))
    #workspace.bind(sequence="<Control-KeyPress-minus>", func=lambda x: zoom(workspace, font, -5))