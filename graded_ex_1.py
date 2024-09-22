# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    reverse = True if sort_order == "desc" else False
    return sorted(products_list, key=lambda x: x[1], reverse=reverse)


def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price}")

def display_categories():
    for index, category in enumerate(products, start=1):
        print(f"{index}. {category}")
        return None

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    if cart:
        print("Items in your cart:")
        total_cost = 0
        for product, price, quantity in cart:
            item_total = price * quantity
            print(f"{product} - ${price} x {quantity} = ${item_total}")
            total_cost += item_total
        print(f"Total cost: ${total_cost}")
    else:
        print("Your cart is empty.")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Receipt for {name} <{email}>")
    print(f"Delivery address: {address}")
    print("Items ordered:")
    for product, quantity in cart:
        print(f"{product} x {quantity}")
    print(f"Total cost: ${total_cost}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return '@' in email

def main():
    cart = []
    name = input("Please enter your name: ")
    email = input("Please enter your email address: ")
    
    while not validate_name(name):
        print("Invalid name. Please enter your name (First and Last name).")
        name = input("Please enter your name: ")
    
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Please enter your email address: ")
    
    display_categories()
    while True:
        try:
            category_choice = int(input("Please enter the category number you would like to explore: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    while category_choice < 1 or category_choice > len(products):
        print("Invalid category number. Please try again.")
        category_choice = int(input("Please enter the category number you would like to explore: "))
    
    selected_category = list(products.keys())[category_choice - 1]
    products_list = products[selected_category]
    display_products(products_list)
    
    while True:
        choice = input("1. Select a product to buy\n2. Sort the products according to the price.\n3. Go back to the category selection.\n4. Finish shopping\nPlease enter your choice: ")
        
        if choice == "1":
            try:
                product_number = int(input("Please enter the product number: "))
                quantity = int(input("Please enter the quantity: "))
                if 1 <= product_number <= len(products_list):
                    add_to_cart(cart, products_list[product_number - 1], quantity)
                else:
                    print("Invalid product number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == "2":
            sort_order = input("Enter 1 for ascending or 2 for descending order: ")
            sorted_products = display_sorted_products(products_list, int(sort_order))
            display_products(sorted_products)
        
        elif choice == "3":
            display_categories()
            category_choice = int(input("Please enter the category number you would like to explore: "))
            selected_category = list(products.keys())[category_choice - 1]
            products_list = products[selected_category]
            display_products(products_list)
        
        elif choice == "4":
            if cart:
                display_cart(cart)
                total_cost = sum([product[1] * quantity for product, quantity in cart])
                address = input("Please enter your delivery address: ")
                generate_receipt(name, email, cart, total_cost, address)
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
            break

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
