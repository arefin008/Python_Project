class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.orders = []

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class OnlineShop:
    def __init__(self, default_products=None):
        self.users = {
            'arefin': User('arefin', '1234'),
            'rounok': User('rounok', '123'),
            'rakibul': User('rakibul', '12')
        }
        if default_products is None:
            self.products = []
        else:
            self.products = default_products

    def sign_up(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose another one.")
        else:
            self.users[username] = User(username, password)
            print("Sign up successful!")

    def log_in(self, username, password):
        if username in self.users and self.users[username].password == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def add_product(self, product_id, name, price, quantity):
        self.products.append(Product(product_id, name, price, quantity))
        print("Product added successfully!")

    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("Products:")
            for product in self.products:
                print(f"Product ID: {product.product_id}, Name: {product.name}, Price: Tk.{product.price}, Quantity: {product.quantity}")

    def remove_products(self):
        self.products.clear()
        print("Products removed successfully!")

    def delete_product_by_id(self, product_id):
      for product in self.products:
        if product.product_id == product_id:
          self.products.remove(product)
          print(f"ID {product_id} deleted successfully.")
          return
      print(f"No product found with ID {product_id}")

    def place_order(self, username, product_ids):
        if username not in self.users:
            print("User not found. Please sign up or log in.")
            return

        user = self.users[username]
        ordered_products = [product for product in self.products if product.product_id in product_ids]
        total_price = sum(product.price for product in ordered_products)

        if total_price == 0:
            print("No products selected for order.")
            return

        order_id = len(user.orders) + 1
        user.orders.append((order_id, ordered_products, total_price))
        print("Order placed successfully!")

    def view_orders(self, username):
        if username not in self.users:
            print("User not found. Please sign up or log in.")
            return

        user = self.users[username]
        if not user.orders:
            print("No orders available.")
        else:
            print("Orders:")
            for order in user.orders:
                print(f"Order ID: {order[0]}, Total Price: Tk.{order[2]}")

    def view_order_details(self, username, order_id):
        if username not in self.users:
            print("User not found. Please sign up or log in.")
            return

        user = self.users[username]
        for order in user.orders:
            if order[0] == order_id:
                print(f"Order ID: {order[0]}, Total Price: Tk.{order[2]}")
                print("Products:")
                for product in order[1]:
                    print(f"Product ID: {product.product_id}, Name: {product.name}, Price: Tk.{product.price}")
                return
        print(f"Order with ID {order_id} not found.")

    def cancel_order(self, username, order_id):
        if username not in self.users:
            print("User not found. Please sign up or log in.")
            return

        user = self.users[username]
        for order in user.orders:
            if order[0] == order_id:
                user.orders.remove(order)
                print(f"Order with ID {order_id} cancelled successfully!")
                return
        print(f"Order with ID {order_id} not found.")
default_products = [
    Product("1", "Apple", 120000.00, 10),
    Product("2", "Nokia", 5000.00, 20),
    Product("3", "Samsung", 15000.00, 30),
    Product("4", "Xiaomi", 30000.00, 15)
]

shop = OnlineShop(default_products)

while True:
    print("************************************************")
    print("Welcome to the Online Shop Management System!")
    print("1. Log In")
    print("2. Sign Up")
    print("3. Exit")
    print("************************************************")

    choice = input("Please enter your choice: ")

    if choice == '1':
        username = input("Username: ")
        password = input("Password: ")
        if shop.log_in(username, password):
            while True:
                print("***************************************")
                print("1. View Products")
                print("2. Add Product")
                print("3. Remove All Products")
                print("4. Products Removed by ID.")
                print("5. Place Order")
                print("6. My Orders")
                print("7. View Order Details")
                print("8. Cancel Order")
                print("9. Log Out")

                print("***************************************")

                choice = input("Please enter your choice: ")

                if choice == '1':
                    shop.view_products()
                elif choice == '2':
                    product_id = input("Product ID: ")
                    name = input("Name: ")
                    price = float(input("Price: "))
                    quantity = int(input("Quantity: "))
                    shop.add_product(product_id, name, price, quantity)
                elif choice == "3":
                    shop.remove_products()
                elif choice == "4":
                   product_id = input("Enter the ID of the product to delete: ")
                   shop.delete_product_by_id(product_id)

                elif choice == "5":
                  product_ids = input("Enter product ID: ").split(',')
                  shop.place_order(username, product_ids)
                elif choice == "6":
                  shop.view_orders(username)
                elif choice == "7":
                  order_id = int(input("Enter order ID: "))
                  shop.view_order_details(username,order_id)
                elif choice =="8":
                 order_id = int(input("Enter order ID: "))
                 shop.cancel_order(username,order_id)
                elif choice == '9':
                    break
                else:
                    print("Invalid choice. Please try again.")


    elif choice == '2':
        username = input("Username: ")
        password = input("Password: ")
        shop.sign_up(username, password)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
