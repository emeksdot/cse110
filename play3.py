# friends = []
# # name = ""
# name = input("Enter the name of a friend: ")

# while(name != 'end'):
#     friends.append(name)
#     name = input("Enter the name of a friend: ")
#     if(name == 'end'):
#         break

# for friend in friends: 
#     print(f"Your friends are: {friend}")

items = []
# name = ""
item = input("Enter the item: ")

while(item != 'quit'):
    items.append(item)
    item = input("Enter the item: ")
    if(item == 'quit'):
        break

for item in items: 
    print(f"item: {item}")


print(f"The shopping list is: ")
for item in items:
    print(f"{item}")

print(f"The shopping list with indexes is: ")
for i in range(len(items)):
    print(f"{i}. {items[i]}")
