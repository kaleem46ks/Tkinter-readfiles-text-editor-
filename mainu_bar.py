import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Mainu Bar Tutorial')

def func():
    print('Func called')
# Menu

# ----------------------simple menubar --------------------------
# menubar= tk.Menu(win)
# menubar.add_command(label='Save', command=func)
# menubar.add_command(label='Save As', command=func)
# menubar.add_command(label='Copy', command=func)
# menubar.add_command(label='Paste', command=func)

main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New Text File',command=func)
file_menu.add_command(label='New Window',command=func)
file_menu.add_separator()       #-------> line between menu
file_menu.add_command(label='Open File',command=func)

# Edit menu
edit_menu = tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label='Undo',command=func)
edit_menu.add_command(label='Redo',command=func)
edit_menu.add_separator() 
edit_menu.add_command(label='Cut',command=func)


main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit', menu= edit_menu)

win.configure(menu=main_menu)

win.mainloop()