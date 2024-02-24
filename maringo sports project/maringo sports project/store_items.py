import sqlite3
import random
import membersdb

# Define the handle_error decorator
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            print("ValueError:", ve)
            # Custom error handling logic for ValueError
            # You can log, print, or raise a custom exception here
        except sqlite3.IntegrityError as ie:
            print("IntegrityError:", ie)
            # Custom error handling logic for IntegrityError
            # You can log, print, or raise a custom exception here
        except Exception as e:
            print("An unexpected error occurred:", e)
            # Custom error handling logic for other exceptions
            # You can log, print, or raise a custom exception here
    return wrapper


##create connection to a database
conn = sqlite3.connect('maringosports.db')

##create a cursor to modify the db
cur = conn.cursor()



# Function to add store items or update their prices
@handle_error
def add_store_items():
    item_amount = [
    ("Bloomer", 250),
    ("Games shorts", 750),
    ("Hockey stick", 2000),
    ("Socks", 350),
    ("Sports shoes", 1000),  # You can adjust the range based on specific shoe types
    ("Track suit", 1000),
    ("T-shirt", 800),
    ("Wrapper", 450)
]

    stock_level = 0
    
    for item, price in item_amount:
        
        try:
            cur.execute("INSERT INTO store_items (Item, Price, Stock_level) VALUES (?, ?, ?)", (item, price, stock_level))
        except sqlite3.IntegrityError:
            # Item already exists, update the price
            cur.execute("UPDATE store_items SET Price = ? WHERE Item = ?", (price, item))
    conn.commit()

def show_store_items():
    cur.execute("SELECT * FROM store_items")
    items = cur.fetchall()
    return items

# Function to insert saless
@handle_error
def insert_sales(item, qty,  mem_id):
    print('Sales')
    sales_id = random.randint(10000, 99999)
    cur.execute("SELECT Price FROM store_items WHERE Item = ?", (item,))
    price = cur.fetchone()[0]
    # Calculate total
    total = (int(qty) * price)
    cur.execute("SELECT Full_Name FROM members WHERE member_id = ?", (mem_id))
    name = cur.fetchone()[0]
    cur.execute("""INSERT INTO Sales (sale_id, item, Qty, Price, Member_name, Total)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (sales_id, item, qty, price, name, total))
    conn.commit()

    cur.execute("UPDATE store_items SET Stock_level = Stock_level - ? WHERE Item = ?", (qty, item))
    conn.commit()

##function to insert purchase of stock
@handle_error
def insert_purchase(item, qty, price):
    print('Purchase List')
    p_id = random.randint(10000, 999999)
    total = (int(qty) * price)
    cur.execute(""" INSERT INTO Purchases
        VALUES (?, ?, ?, ?, ?)
        """, (p_id, item, qty, price, total))
    conn.commit()
    # Update stock level in store_items after purchase
    cur.execute("UPDATE store_items SET Stock_level = Stock_level + ? WHERE Item = ?", (qty, item))
    conn.commit()


# Create a trigger to insert into discounts when sales > kshs. 100000
@handle_error
def discount_trigger():
    cur.execute("""CREATE TRIGGER IF NOT EXISTS disc_trigger
        AFTER INSERT ON Sales
        FOR EACH ROW BEGIN
            WHEN (SELECT SUM(Total) FROM Sales WHERE Member_name = NEW.Member_name) > 10000
            INSERT INTO discounts (member_name, discount_amount)
            VALUES (NEW.Member_name, (SELECT SUM(Total) * 0.05 FROM Sales WHERE Member_name = NEW.Member_name));
        END;
        """)




##show all purchases of stock
def show_purch():
    print('Show Purchases')
    cur.execute("SELECT * FROM Purchases")
    prch = cur.fetchall()
    return prch

##show purchase for item
@handle_error
def show_purch4(item):
    cur.execute("SELECT * FROM Purchases WHERE item = ?", item)
    purchd = cur.fetchall()
    return purchd

##show all sales of items
def show_sales():
    print('Show all sales')
    cur.execute("SELECT * FROM Sales")
    saleitem = cur.fetchall()
    return saleitem

##show sales for certain item
@handle_error
def show_sales4(thing):
    print('Show sales for item:')
    cur.execute("SELECT * FROM Sales WHERE item = ?", thing)
    items = cur.fetchall()
    return items

##show discounts
def show_disc():
    cur.execute("SELECT * FROM discounts")
    disc = cur.fetchall()
    return disc

conn.commit()        

