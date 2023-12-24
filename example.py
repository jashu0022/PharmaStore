import tkinter as tk
import sqlite3


class Main_Window:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Window")

        # Create labels and buttons
        self.label1 = tk.Label(self.master, text="Label 1")
        self.label2 = tk.Label(self.master, text="Label 2")
        self.label3 = tk.Label(self.master, text="Label 3")
        self.butt1 = tk.Button(self.master, text="Button 1")
        self.butt2 = tk.Button(self.master, text="Button 2")

        # Layout labels and buttons
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)
        self.butt1.grid(row=3, column=0)
        self.butt2.grid(row=3, column=1)


class Product:
    def __init__(self, id, name, description, price, stock, order_date):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.order_date = order_date


class Order:
    def __init__(self, order_id, customer, products, date):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.date = date


class Customer:
    def __init__(self, name):
        self.name = name


class Order_Product:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


# Connect to the database
conn = sqlite3.connect("mydatabase.db")

# Create tables
conn.execute('''CREATE TABLE Product\
             (ID INT PRIMARY KEY     NOT NULL,\
             NAME           TEXT    NOT NULL,\
             DESCRIPTION    TEXT    NOT NULL,\
             PRICE          REAL    NOT NULL,\
             STOCK          INT     NOT NULL,\
             ORDER_DATE     TEXT);''')

conn.execute('''CREATE TABLE Order\
             (ORDER_ID       INT     PRIMARY KEY     NOT NULL,\
             CUSTOMER        TEXT    NOT NULL,\
             PRODUCTS        TEXT    NOT NULL,\
             DATE            TEXT    NOT NULL);''')

conn.execute('''CREATE TABLE Customer\
             (NAME           TEXT    PRIMARY KEY     NOT NULL);''')

conn.execute('''CREATE TABLE Order_Product\
             (PRODUCT        TEXT    NOT NULL,\
             QUANTITY        INT     NOT NULL);''')

# Create GUI
root = tk.Tk()
app = Main_Window(root)
root.mainloop()

# Close database connection
conn.close()
