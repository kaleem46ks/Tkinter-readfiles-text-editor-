import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('LOOP')

labels = ['What is your name : ','What is your age: ','Your gender: ', 'Country: ', 'State: ','City: ', 'Address']
# Labels
for i in range(len(labels)):
    current_label = 'Label'+ str(i)
    current_label = ttk.Label(win, text= labels[i])
    current_label.grid(row=i,column=0, sticky=tk.W, padx=2, pady=2)

# entrybox
# name_var = tk.StringVar()
user_info = {
    'Name': tk.StringVar(),
    'Age': tk.StringVar(),
    'Gender': tk.StringVar(),
    'Country': tk.StringVar(),
    'State': tk.StringVar(),
    'City': tk.StringVar(),
    'Address': tk.StringVar()
}

counter = 0
for i in user_info:
    current_entry = 'Entry'+ str(i)
    current_entry = ttk.Entry(win, width=16, textvariable= user_info[i])
    current_entry.grid(row=counter,column=1,padx=2, pady= 2)
    counter += 1

def submit():
    print(user_info['Name'].get())
    print(user_info['Age'].get())
    print(user_info['Gender'].get())
    print(user_info['Country'].get())
    print(user_info['State'].get())
    print(user_info.get('City').get())

submit_btn = ttk.Button(win, text='Submit', command= submit)
submit_btn.grid(row=7,columnspan=2)

win.mainloop()
