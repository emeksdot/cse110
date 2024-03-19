"""
A Meal Price Calculator Milestone Project program created by Emeka Thomas Onwugbonu
on March 10, 2024
"""

# I added drinks and tips to the waiters using the following variables children_drinks_price, adults_drink_price, waiters_tip_rate, and waiters_tip
# I also added an if block to check if the amount paid is enough to cover the total bill

child_meal_price = float(input("Enter price of child's meal: "))
children_drinks_price = float(input("Enter price of child's drinks: "))
adult_meal_price = float(input("Enter price of adult's meal: "))
adults_drink_price = float(input("Enter price of adult's drinks: "))
number_of_children = int(input("Enter the number of children: "))
number_of_adults = int(input("Enter the number of adults: "))


tax_rate = float(input("Enter tax rate: "))

waiters_tip_rate = float(input("Enter waiter's tip rate: "))


subtotal_meal_price = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)
subtotal_drinks_price = (children_drinks_price * number_of_children) + (adults_drink_price * number_of_adults)

subtotal_meal_and_drinks = subtotal_meal_price + subtotal_drinks_price

print(f"Subtotal is ${subtotal_meal_and_drinks:.2f}")
print()
waiters_tip = subtotal_meal_and_drinks * waiters_tip_rate / 100
print(f"The waiters tip is ${waiters_tip:.2f}")
print()
sales_tax = (subtotal_meal_and_drinks * tax_rate / 100)
print(f"Sales tax is ${sales_tax:.2f}")
print()
total_bill = sales_tax + subtotal_meal_and_drinks + waiters_tip
print(f"Total is ${total_bill:.2f}")

payment_amount = float(input("Enter amount paid: "))
customer_change = payment_amount - total_bill

if(payment_amount > total_bill):
    print(f"Your change is ${customer_change:.2f}")
else:
    print(f"Your money is not enough, it's remaining ${(total_bill - payment_amount):.2f} please!")





