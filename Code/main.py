import csv
from geopy.distance import geodesic
import time

# creating a separate csv file for fake restaurant data
restaurant_data = {
    'name': "Alice's Culinary Haven",
    'address': '123 Main Street, Wellesley, MA',
    'cuisine': 'American',
    'menu': {
        'appetizers':[
            {'item': 'Buffalo Wings', 'price': 7.99},
            {'item': 'Fried Pickles', 'price': 5.99},
            {'item': 'Loaded Nachos', 'price': 8.99},
            {'item': 'Calamari', 'price': 8.99},
            {'item': 'Mozerella Sticks', 'price': 6.99},
        ],
        'main_courses': [
            {'item': 'Grilled Salmon', 'price': 14.99},
            {'item': 'Burger', 'price': 16.99},
            {'item': 'Mushroom Risotto', 'price': 13.99},
            {'item': 'Meatballs & Spaghetti', 'price': 11.99},
            {'item': 'Chicken Caesar Salad', 'price': 11.99},
        ],
        'sides': [
            {'item': 'French Fries', 'price': 3.99},
            {'item': 'Sweet Potato Fries', 'price': 3.99},
            {'item': 'Side Salad', 'price': 4.99},
            {'item': 'Onion Rings', 'price': 4.99},
            {'item': 'Mashed Potatoes', 'price': 6.99},
        ],
        'desserts': [
            {'item': 'Strawberry Cheesecake', 'price': 7.99},
            {'item': 'Fruit Tart', 'price': 8.99},
            {'item': 'Chocolate Lava Cake', 'price': 8.99},
            {'item': 'Creme Brulee', 'price': 9.99},
            {'item': 'Ice Cream Sundae', 'price': 5.99},
        ],
        'drinks': [
            {'item': 'Fountain Soda', 'price': 1.99},
            {'item': 'Lemonade', 'price': 2.99},
            {'item': 'Iced Tea', 'price': 2.99},
            {'item': 'Ice Cream Shake', 'price': 4.99},
            {'item': 'Juice', 'price': 2.99},
        ],

    }
}


csv_file_path = 'code/restaurant_data.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Category', 'Item', 'Price'])
    for category, items in restaurant_data['menu'].items():
        for item in items:
            csv_writer.writerow([category.capitalize(), item['item'], item['price']])



with open('code/restaurant_data.csv', 'r') as file:
    reader = csv.reader(file)
    
def display_greeting():
    print(f"Welcome to Alice's Culinary Haven! Place your order now!")

def display_menu():
    print("\nMenu") # asked ChatGPT how to get headings for each menu section and each item on its own line by using "\n"
    for category, items in restaurant_data['menu'].items():
        print(f"\n{category.capitalize()}:")
        for item in items:
            print(f"{item['item']}: ${item['price']:.2f}")

def take_order():
    order = []
    while True:
        display_menu()
        item_name = input("\nEnter the name of the item you'd like to order (or type 'done' to finish): ")

        if item_name.lower() == 'done': # user needs to enter 'done' to finish placing their order 
            break

        quantity = int(input("Enter quantity: ")) # code asks user to enter quantity for each item ordered
        order.append({'item': item_name, 'quantity': quantity})

    return order

def get_user_address():
    address = input("\nEnter your delivery address: ")
    return address

def calculate_delivery_fee(user_address):
    restaurant_location = (42.1234, -71.5678)  # Coordinates of Wellesley
    user_location = get_coordinates_from_address(user_address)

    distance_mi = geodesic(restaurant_location, user_location).miles
    delivery_fee_per_mi = 1.0  # $1.00 delivery fee per mile
    delivery_fee = distance_mi * delivery_fee_per_mi

    return delivery_fee

def get_coordinates_from_address(address):
    return (42.3456, -71.0987)  

def generate_receipt(order, delivery_fee): # creating receipt with total order amount subtotal 
    total_amount = 0
    print("\nReceipt:") 
    print("\nOrdered Items:")
    for item in order:
        for category, items in restaurant_data['menu'].items():
            for menu_item in items:
                if menu_item['item'].lower() == item['item'].lower():
                    subtotal = menu_item['price'] * item['quantity']
                    print(f"{item['quantity']} x {menu_item['item']}: ${menu_item['price']:.2f} each \nSubtotal: ${subtotal:.2f}")
                    total_amount += subtotal
                    break

    print(f"\nDelivery Fee: ${delivery_fee:.2f}")
    total_amount += delivery_fee # adding delivery fee to order amount to generate total amount for order
    print(f"\nTotal Amount (including delivery fee): ${total_amount:.2f}")


def generate_order_confirmation():
    return "Thank you! Your order has been placed. Your delivery is coming in 30 minutes."

def delivery_process(): # used ChatGPT to help me come up with a time aspect for my project
    for minutes_left in range(30, 0, -1):
        print(f"Your delivery will arrive in {minutes_left} minutes...")
        time.sleep(60)  

    print("Your delivery has arrived! Enjoy your meal!")

confirmation_message = generate_order_confirmation() #generate order confirmation message

print(confirmation_message) #display order confirmation message

delivery_process()



def main():
    display_greeting()
    user_order = take_order() # get user's order
    user_address = get_user_address() # get user's address
    delivery_fee = calculate_delivery_fee(user_address) # calculate delivery fee based on distance
    generate_receipt(user_order, delivery_fee) # generate and display receipt of user's order total including delivery fee
    delivery_process()

if __name__ == "__main__":
    main()
