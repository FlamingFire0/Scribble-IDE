import tkinter as tk


root = tk.Tk()

main = tk.Text(root)

main.bind(sequence="<KeyPress>", func=print)


main.pack()


root.mainloop()