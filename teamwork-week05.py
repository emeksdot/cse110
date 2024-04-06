# # list_of_numbers = []

# # number = int(input("Enter any number: "))

# # list_of_numbers.append(number)

# # print(list_of_numbers)

# list_of_numbers = []

# number = int(input("Enter any number: "))
# while(number != 0):
#     list_of_numbers.append(number)
#     number = int(input("Enter any number: "))
#     if(number == 0):
#         break

# print(list_of_numbers)

list_of_numbers = []

number = int(input("Enter any number: "))
while(number != 0):
    list_of_numbers.append(number)
    number = int(input("Enter any number: "))
    if(number == 0):
        break

print(list_of_numbers)

new_list = list_of_numbers

sum_of_numbers = 0
for num in new_list:
    sum_of_numbers += num

print(sum_of_numbers)

average = sum_of_numbers / len(new_list)
print(average)
