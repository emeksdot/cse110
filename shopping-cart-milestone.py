"""
A shopping cart program created by Emeka Thomas Onwugbonu for the CSE110 week05 milestone project. 
"""

# Both the list of items and price list can be changed using the 
# the following variables created for the purpose of introducing a product: new_item,
# new_item_price


print(f"Welcome to our shop")
print(f"You are allowed to choose an option number from the list below")
print(f"1. Add a new item")
print(f"2. Display the contents of the shopping cart")
print(f"3. Remove an item (only needed for the final project deliverable)")
print(f"4. Compute the total (only needed for the final project deliverable)")
print(f"5. Quit")

option_number = int(input("Choose an option: "))
items_list = []
price_list = []

while(option_number != 5):
    if (option_number == 1):
        item = input("Choose item: ")
        items_list.append(item.capitalize())
        price = float(input("Enter price: "))
        price_list.append(price)
        print(f"{item} has been added to list")
        
        print(f"Welcome to our shop")
        print(f"You are allowed to choose an option number from the list below")
        print(f"1. Add a new item")
        print(f"2. Display the contents of the shopping cart")
        print(f"3. Remove an item")
        print(f"4. Compute the total")
        print(f"5. Quit")

        option_number = int(input("Choose an option: "))
        if(option_number == 5):
            break
    elif(option_number == 2 and len(items_list) == 0):
        print(f"You have nothing in your cart to display.")
        break
    elif(option_number == 2 and len(items_list) != 0):
        print("Your cart contains: ")
        for i in range(len(items_list)):
            print(f"{i + 1}. {items_list[i]} - ${price_list[i]:.2f}")
        option_number = int(input("Choose an option: "))
        if(option_number == 5):
            break
    elif(option_number == 3 and len(items_list) == 0):
        print(f"You have nothing in your cart to delete.")
        break
        
    elif(option_number == 3 and len(items_list) != 0):
        delete_number = int(input("Enter item number to be changed: "))
        delete_number -= 1
        new_item = input("Enter the new item: ")
        new_item_price = float(input("Enter the new item's price: "))
        items_list[delete_number] = new_item
        price_list[delete_number] = new_item_price
        
        option_number = int(input("Choose an option: "))
        if(option_number == 5):
            break

    elif(option_number == 4 and len(items_list) == 0):
        print(f"You have not started shopping.")
        break
    elif(option_number == 4 and len(items_list) != 0):
        sum_total = 0
        for price in price_list:
            sum_total += price
        print(f"Your total is ${sum_total:.2f}")
        option_number = int(input("Choose an option: "))
        if(option_number == 5):
            break
        

print()
print(f"Thank you for shopping with us.")