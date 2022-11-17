import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Label Frame')

label_frame = ttk.LabelFrame(win,text='Enter your details below ')
label_frame.grid(row=0,column=0, padx=40)

labels = ['What is your name : ','What is your age: ','Your gender: ', 'Country: ', 'State: ','City: ', 'Address']
# Labels
for i in range(len(labels)):
    current_label = 'Label'+ str(i)
    current_label = ttk.Label(label_frame, text= labels[i])
    current_label.grid(row=i,column=0, sticky=tk.W)

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
    current_entry = ttk.Entry(label_frame, width=16, textvariable= user_info[i])
    current_entry.grid(row=counter,column=1)
    counter += 1

def submit():
    print(user_info['Name'].get())
    print(user_info['Age'].get())
    print(user_info['Gender'].get())
    print(user_info['Country'].get())
    print(user_info['State'].get())
    print(user_info.get('City').get())

submit_btn = ttk.Button(win, text='Submit', command= submit)
submit_btn.grid(row=1,columnspan=2)

for child in label_frame.winfo_children():
    child.grid_configure(padx=4,pady=4)

win.mainloop()