from distutils.cmd import Command
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
root.title = ("Key System")
root.geometry('1030x380')
my_tree = ttk.Treeview(root)
store_name = "Store Name" 


def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def insert(id, name, price, quantity):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS inventory(itemID TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")
    cursor.execute("INSERT INTO inventory VALUES('"+str(id)+"', '"+str(name)+"', '"+str(price)+"', '"+str(quantity)+"')")
    conn.commit()
    
    
def delete(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS inventory(itemID TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")
    cursor.execute("DELETE FROM inventory WHERE itemID='"+str(data)+"'")
    conn.commit()
    
    
    
def update(id, name, price, quantity, idName):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS inventory(itemID TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")
    cursor.execute("UPDATE inventory SET itemId='"+str(id)+"', itemName='"+str(name)+"', itemPrice='"+str(price)+"', itemQuantity='"+str(quantity)+"' WHERE itemId='"+str(idName)+"'")
    conn.commit()
    
    
def read():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS inventory(itemID TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")
    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    return results

def insert_data():
    item_id = str(entry_id.get())
    item_name = str(entry_name.get())
    item_price = str(entry_price.get())
    item_quantity = str(entry_quantity.get())
    if item_id == "" or item_id == " ":
        print("Error inserting data")
    if item_name == "" or item_name == " ":
        print("Error inserting data")
    if item_price == "" or item_price == " ":
        print("Error inserting data")
    if item_quantity == "" or item_quantity == " ":
        print("Error inserting data")
    else:
        insert(str(item_id), str(item_name), str(item_price), str(item_quantity))
        
    for data in my_tree.get_children():
        my_tree.delete(data)
    
    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid='0', text = "", values=(result), tag="orow")
    
    my_tree.tag_configure('orow', background="#EEEEEE", font=('Arial bold', 15))
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)
    
    
    
def delete_data():
    selected_item = my_tree.selection()[0]
    delete_data = str(my_tree.item(selected_item)['values'][0])
    delete(delete_data)
    
    for data in my_tree.get_children():
        my_tree.delete(data)
    
    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid='0', text = "", values=(result), tag="orow")
    
    my_tree.tag_configure('orow', background="#EEEEEE", font=('Arial bold', 15))
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)
    
    
def update_data():
    selected_item = my_tree.selection()[0]
    update_name = str(my_tree.item(selected_item)['values'][0])
    update(entry_id.get(), entry_name.get(), entry_price.get(), entry_quantity.get(), update_name)
    
    for data in my_tree.get_children():
        my_tree.delete(data)
    
    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid='0', text = "", values=(result), tag="orow")
    
    my_tree.tag_configure('orow', background="#EEEEEE", font=('Arial bold', 15))
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)
    
    
    
    
title_label = Label(root, text=store_name, font=('Arial bold', 30), bd=2)
title_label.grid(row=0, column=0, columnspan=8, padx=20, pady=20)

id_label = Label(root, text="ID", font=('Arial Bold', 15))
name_label = Label(root, text="Name", font=('Arial Bold', 15))
price_label = Label(root, text="Price", font=('Arial Bold', 15))
quantity_label = Label(root, text="Quantity", font=('Arial Bold', 15))
id_label.grid(row=1, column= 0, padx=10, pady=10)
name_label.grid(row=2, column= 0, padx=10, pady=10)
price_label.grid(row=3, column= 0, padx=10, pady=10)
quantity_label.grid(row=4, column= 0, padx=10, pady=10)

entry_id = Entry(root, width=25, bd=5, font=('Arial Bold', 15))
entry_name = Entry(root, width=25, bd=5, font=('Arial Bold', 15))
entry_price = Entry(root, width=25, bd=5, font=('Arial Bold', 15))
entry_quantity = Entry(root, width=25, bd=5, font=('Arial Bold', 15))
entry_id.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entry_name.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entry_price.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entry_quantity.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

# Enter button
button_enter = Button(root, text="Enter", padx=5, pady=5, width=5, bd=3, font=('Arial', 15), bg="#0099ff", command=insert_data)
button_enter.grid(row=5, column=1, columnspan=1)
# Update button
button_update = Button(root, text="Update", padx=5, pady=5, width=5, bd=3, font=('Arial', 15), bg="#ffff00", command=update_data)
button_update.grid(row=5, column=2, columnspan=1)
# Delete button
button_delete = Button(root, text="Delete", padx=5, pady=5, width=5, bd=3, font=('Arial', 15), bg="#e62e00", command=delete_data)
button_delete.grid(row=5, column=3, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("ID", "Name", "Price", "Quantity")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=100)
my_tree.column("Name", anchor=W, width=200)
my_tree.column("Price", anchor=W, width=150)
my_tree.column("Quantity", anchor=W, width=150)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)
    
for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid='0', text = "", values=(result), tag="orow")
    
my_tree.tag_configure('orow', background="#EEEEEE", font=('Arial bold', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)


root.mainloop()