
import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.title("Insert Data")

connection = mysql.connector.connect(host='localhost', user='root', password='project101',
                                     port='3306', database='db1')
c = connection.cursor()

bkg = "#636e72"


frame = tk.Frame(root, bg=bkg)

label_first_name = tk.Label(frame, text="First Name: ", font=('verdana',12), bg=bkg)
entry_first_name = tk.Entry(frame, font=('verdana',12))

label_last_name = tk.Label(frame, text="Last Name: ", font=('verdana',12), bg=bkg)
entry_last_name = tk.Entry(frame, font=('verdana',12))

label_email = tk.Label(frame, text="Email: ", font=('verdana',12), bg=bkg)
entry_email = tk.Entry(frame, font=('verdana',12))

label_Number = tk.Label(frame, text="Number: ", font=('verdana',12), bg=bkg)
entry_Number = tk.Entry(frame, font=('verdana',12))

label_Department = tk.Label(frame, text="Department: ", font=('verdana',12), bg=bkg)
entry_Department = tk.Entry(frame, font=('verdana',12))

def insertData():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    Number = entry_Number.get()
    Department = entry_Department.get()

    insert_query = 'INSERT INTO `teachers`(`first_name`, `last_name`, `email`, `Number`, Department) VALUES (%s,%s,%s,%s,%s)'
    vals = (first_name,last_name,email,Number,Department)
    c.execute(insert_query,vals)
    connection.commit()


button_insert = tk.Button(frame, text="Insert", font=('verdana',14), bg='orange',
                          command = insertData)

label_first_name.grid(row=0, column=0)
entry_first_name.grid(row=0, column=1, pady=10, padx=10)

label_last_name.grid(row=1, column=0)
entry_last_name.grid(row=1, column=1, pady=10, padx=10)

label_email.grid(row=2, column=0, sticky='e')
entry_email.grid(row=2, column=1, pady=10, padx=10)

label_Number.grid(row=3, column=0, sticky='e')
entry_Number.grid(row=3, column=1, pady=10, padx=10)

label_Department.grid(row=4, column=0, sticky='e')
entry_Department.grid(row=4, column=1, pady=10, padx=10)

button_insert.grid(row=5,column=0, columnspan=2, pady=10, padx=10, sticky='nsew')

frame.grid(row=0, column=0)


root.mainloop()