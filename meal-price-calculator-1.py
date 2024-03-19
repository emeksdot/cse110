"""
A Meal Price Calculator program created by Emeka Thomas Onwugbonu
on March 2, 2024
"""

# I added drinks and tips to the waiters using the following variables children_drinks_price, adults_drink_price, waiters_tip_rate, and waiters_tip

child_meal_price = float(input("Enter price of child's meal: "))
children_drinks_price = float(input("Enter price of child's drinks: "))
adult_meal_price = float(input("Enter price of adult's meal: "))
adults_drink_price = float(input("Enter price of adult's drinks: "))
number_of_children = int(input("Enter the number of children: "))
number_of_adults = int(input("Enter the number of adults: "))

payment_amount = float(input("Enter amount paid: "))
tax_rate = int(input("Enter tax rate as an integer: "))
waiters_tip_rate = int(input("Enter waiter's tip rate as an integer: "))


subtotal_meal_price = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)
subtotal_drinks_price = (children_drinks_price * number_of_children) + (adults_drink_price * number_of_adults)

subtotal_meal_and_drinks = subtotal_meal_price + subtotal_drinks_price

waiters_tip = subtotal_meal_and_drinks * waiters_tip_rate / 100

sales_tax = (subtotal_meal_and_drinks * tax_rate / 100)
total_bill = sales_tax + subtotal_meal_price + waiters_tip
customer_change = payment_amount - total_bill

print(f"Your change is ${customer_change:.2f}")


