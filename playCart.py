
# print(f"Welcome to our shop")
# print(f"You are allowed to choose an option number from the list below")
# print(f"1. Add a new item")
# print(f"2. Display the contents of the shopping cart")
# print(f"3. Remove an item (only needed for the final project deliverable)")
# print(f"4. Compute the total (only needed for the final project deliverable)")
# print(f"5. Quit")


print(f"Welcome to our shop")
print(f"You are allowed to choose an option number from the list below")
print(f"1. Add a new item")
print(f"2. Display the contents of the shopping cart")
print(f"3. Quit")

option_number = int(input("Choose an option: "))
items_list = []
# if(option_number == 2):
    # 

while(option_number != 3):
    if (option_number == 1):
        item = input("Choose item: ")
        items_list.append(item)
        print(f"{item} has been added to list")
        
        print(f"Welcome to our shop")
        print(f"You are allowed to choose an option number from the list below")
        print(f"1. Add a new item")
        print(f"2. Display the contents of the shopping cart")
        print(f"3. Quit")
        option_number = int(input("Choose an option: "))
        if(option_number == 3):
            break
    elif(option_number == 2 and len(items_list) == 0):
        print(f"You have nothing in your cart to display.")
        break
    elif(option_number == 2 and len(items_list) != 0):
        print("Your cart contains: ")
        for item in items_list:
            print(item)
        option_number = int(input("Choose an option: "))
        if(option_number == 3):
            break

print(f"Thank you for shopping with us.")

# isinstance(number, int)