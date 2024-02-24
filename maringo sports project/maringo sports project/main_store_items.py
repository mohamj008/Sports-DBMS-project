import store_items
from store_items import *

import tkinter as tk
from tkinter import ttk, messagebox

# Create the main application window
app = tk.Tk()

##store items
def add_store():
    store_items.add_store_items()

def store_stuffs():
    stuff = store_items.show_store_items()

    if stuff:
        stuff_window = tk.Toplevel(app)
        stuff_window.title("Store Items")

        tree = ttk.Treeview(stuff_window)

        tree["columns"] = ("item", "price", "stock level")
        
        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Item", anchor="center")
        tree.heading("#2", text="Price", anchor="center")
        tree.heading("#3", text="Stock Level", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("item", width=200, anchor="center")
        tree.column("price", width=100, anchor="center")
        tree.column("stock level", width=50, anchor="center")

        for items in stuff:
            tree.insert("", "end", values=items)
        
        tree.pack(fill="both", expand=True)

        stuff_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No items", "No items found in the database")


##sales 
item_label = tk.Label(app, text="Item")
item_entry = tk.Entry(app)

qty_label = tk.Label(app, text="Quant")
qty_entry = tk.Entry(app)

mem_id_label = tk.Label(app, text="Member ID")
mem_id_entry = tk.Entry(app)

def sales_details():
    item_label.pack()
    item_entry.pack()

    qty_label.pack()
    qty_entry.pack()

    mem_id_label.pack()
    mem_id_entry.pack()

def sales_hide():
    item_label.pack_forget()
    item_entry.pack_forget()

    qty_label.pack_forget()
    qty_entry.pack_forget()

    mem_id_label.pack_forget()
    mem_id_entry.pack_forget()

def sales_insert():
    item = item_entry.get()
    qty = qty_entry.get()
    mem_id = mem_id_entry.get()
    store_items.insert_sales(item, qty, mem_id)
    store_items.discount_trigger()

##show all sales
def all_sales():
    all_sales = store_items.show_sales()
    if all_sales:
        sales_window = tk.Toplevel(app)
        sales_window.title("Sales")

        tree = ttk.Treeview(sales_window)
        tree["columns"] = ("Sales ID", "Item", "Qty", "Price", "Name", "Total")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Sales ID", anchor="center")
        tree.heading("#2", text="Item", anchor="center")
        tree.heading("#3", text="Quant", anchor="center")
        tree.heading("#4", text="Price", anchor="center")
        tree.heading("#5", text="Name", anchor="center")
        tree.heading("#6", text="Total", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Sales ID", width=100, anchor="center")
        tree.column("Item", width=200, anchor="center")
        tree.column("Qty", width=50, anchor="center")
        tree.column("Price", width=100, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("total", width=100, anchor="center")
        

        for sale in all_sales:
            tree.insert("", "end", values=items)
        
        tree.pack(fill="both", expand=True)

        sales_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No sales", "No sales found in the database")



items_label = tk.Label(app, text="Item")
items_entry = tk.Entry(app)

def show_sales_detail():
    item_label.pack()
    item_entry.pack()


def hide_sales_detail():
    item_label.pack_forget()
    item_entry.pack_forget()
    
def sales_for():
    item = items_entry.get()
    sales4 = store_items.show_sales4(item)
    if sales4:
        sales4_window = tk.Toplevel(app)
        sales4_window.title("Sales")

        tree = ttk.Treeview(sales4_window)
        tree["columns"] = ("Sales ID", "Item", "Qty", "Price", "Name", "Total")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Sales ID", anchor="center")
        tree.heading("#2", text="Item", anchor="center")
        tree.heading("#3", text="Quant", anchor="center")
        tree.heading("#4", text="Price", anchor="center")
        tree.heading("#5", text="Name", anchor="center")
        tree.heading("#6", text="Total", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Sales ID", width=100, anchor="center")
        tree.column("Item", width=200, anchor="center")
        tree.column("Qty", width=50, anchor="center")
        tree.column("Price", width=100, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("total", width=100, anchor="center")
        

        for sale4 in sales4:
            tree.insert("", "end", values=sales4)
        
        tree.pack(fill="both", expand=True)

        sales_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No sales", "No sales found in the database")


    

    
##purchases  
things_label = tk.Label(app, text="Item")
things_entry = tk.Entry(app)

qty_label = tk.Label(app, text="Quant")
qty_entry = tk.Entry(app)

price_label = tk.Label(app, text="Price")
price_entry = tk.Entry(app)

def purch_show():
    things_label.pack()
    things_entry.pack()

    qty_label.pack()
    qty_entry.pack()

    price_label.pack()
    price_entry.pack()

    
def purch_hide():
    things_label.pack_forget()
    things_entry.pack_forget()

    qty_label.pack_forget()
    qty_entry.pack_forget()

    price_label.pack_forget()
    price_entry.pack_forget()
    
def add_purchase():
    item = things_entry.get()
    qty = qty_entry.get()
    price = price_entry.get()

    store_items.insert_purchase(item, qty, price)


def show_purchase():
    purchd = store_items.show_purch()
    if purchd:
        purchase_window = tk.Toplevel(app)
        purchase_window.title("Purchases")

        tree = ttk.Treeview(purchase_window)
        tree ["columns"] = ("Purch ID", "Item", "Qty", "Price", "Total")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Purch ID", anchor="center")
        tree.heading("#2", text="Item", anchor="center")
        tree.heading("#3", text="Quant", anchor="center")
        tree.heading("#4", text="Price", anchor="center")
        tree.heading("#5", text="Total", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Purch ID", width=100, anchor="center")
        tree.column("Item ID", width=100, anchor="center")
        tree.column("qty", width=50, anchor="center")
        tree.column("Price", width=100, anchor="center")
        tree.column("Total", width=100, anchor="center")

        for item in purchd:
            tree.insert("", "end", values=item)
        
        tree.pack(fill="both", expand=True)

        purchase_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No Purchases", "No Purchases found in the database")



item_label = tk.Label(app, text="Item")
item_entry = tk.Entry(app)

def show_purch_details():
    item_label.pack()
    item_entry.pack()

def hide_purch_details():
    item_label.pack_forget()
    item_entry.pack_forget()

    
def purhase_for():
    item = item_entry.get()
    purch4 = store_items.show_purch4(item)

    if purch4:
        purch4_window = tk.Toplevel(app)
        purch4e_window.title("Purchases")

        tree = ttk.Treeview(purch4_window)
        tree ["columns"] = ("Purch ID", "Item", "Qty", "Price", "Total")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Purch ID", anchor="center")
        tree.heading("#2", text="Item", anchor="center")
        tree.heading("#3", text="Quant", anchor="center")
        tree.heading("#4", text="Price", anchor="center")
        tree.heading("#5", text="Total", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Purch ID", width=100, anchor="center")
        tree.column("Item ID", width=100, anchor="center")
        tree.column("qty", width=50, anchor="center")
        tree.column("Price", width=100, anchor="center")
        tree.column("Total", width=100, anchor="center")

        for things in purch4:
            tree.insert("", "end", values=things)
        
        tree.pack(fill="both", expand=True)

        purch4_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No Purchases", "No Purchases found in the database")



##discounts      
def show_discounts():
    disco = store_items.show_disc()
    if disco:
        disc_window = tk.Toplevel(app)
        disc_window.title("Discounts")

        tree = ttk.Treeview(disc_window)
        tree ["columns"] = ("Disc ID", "Name", "Disc Amnt")

        tree.heading("#0", text="", anchor="w")
        tree.heading("#1", text="Disc ID", anchor="center")
        tree.heading("#2", text="Name", anchor="center")
        tree.heading("#3", text="Disc Amount", anchor="center")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Disc ID", width=50, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("Disc Amnt", width=100, anchor="center")

        for thing in disco:
            tree.insert("", "end", values=thing)
        
        tree.pack(fill="both", expand=True)

        disc_window.geometry("1200x1200")
        
    else:
        messagebox.showinfo("No Discounts", "No Discounts found in the database")

        
