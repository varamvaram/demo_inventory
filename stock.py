"""
    the sqlite3 module installed. 
    The script will present a menu where you can choose different options to 
    add products, filter products, display the inventory, or quit the program. 
    The products and their information will be stored in the in-memory 
    SQLite database created at the beginning.
"""
import sqlite3
from datetime import datetime, timedelta

# Create the database connection
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create the product table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        name TEXT,
        price REAL,
        quantity INTEGER,
        date_added TEXT
    )
""")
# Function to add a product to the database
def add_product(category, name, price, quantity, date_added):
    """
        add products get user input
    s"""
    cursor.execute("""
        INSERT INTO products (category, name, price, quantity, date_added)
        VALUES (?, ?, ?, ?, ?)
    """, (category, name, price, quantity, date_added))
    conn.commit()
    print("Product added to the inventory.")
# Function to filter products by category
def filter_by_category(category):
    """
        select category enter category name
    """
    cursor.execute("SELECT * FROM products WHERE category=?", (category,))
    products = cursor.fetchall()
    _display_products(products)
# Function to filter products by product name
def filter_by_product_name(product_name):
    """
        Function to filter products by name added
    """
    cursor.execute("SELECT * FROM products WHERE name=?", (product_name,))
    products = cursor.fetchall()
    _display_products(products)
def filter_by_date_added(days):
    """
        Function to filter by date added
    """
    date_limit = datetime.now() - timedelta(days=days)
    cursor.execute(
        "SELECT * FROM products WHERE date_added < ?", (date_limit.strftime("%Y-%m-%d"),))
    products = cursor.fetchall()
    _display_products(products)

def _display_products(products):
    """
        display the filter products
    """
    if products:
        print("Filtered Products:")
        for product in products:
            print(
                 f"Category: {product[1]}",
                 f" Name: {product[2]}", 
                 f"Price: {product[3]}",
                 f" Quantity: {product[4]}",
                 f"Date Added: {product[5]}")
    else:
        print("No products found.")
def display_inventory():
    """
        disply the inventory products
    """
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    if products:
        print("Current Inventory:")
        for product in products:
            print(
                f"Category: {product[1]}",
                f" Name: {product[2]}", 
                f"Price: {product[3]}",
                f" Quantity: {product[4]}",
                f"Date Added: {product[5]}")
    else:
        print("Inventory is empty.")
def main():
    """
        and select the choice 1.Add product 2.Filter by category
        3.Filter by product name
        4.Filter by date added , 5.Display inventory and 5.Quit 
    """
    while True:
        print("\n1. Add product")
        print("2. Filter by category")
        print("3. Filter by product name")
        print("4. Filter by date added")
        print("5. Display inventory")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category name: ")
            name = input("Enter product name: ")
            price = float(input("Enter unit price: "))
            quantity = int(input("Enter quantity: "))
            date_added = input("Enter date added (dd/mm/yyyy): ")
            add_product(category, name, price, quantity, date_added)
        elif choice == "2":
            category = input("Enter category name: ")
            filter_by_category(category)
        elif choice == "3":
            product_name = input("Enter product name: ")
            filter_by_product_name(product_name)
        elif choice == "4":
            days = int(input("Enter the number of days: "))
            filter_by_date_added(days)
        elif choice == "5":
            display_inventory()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    