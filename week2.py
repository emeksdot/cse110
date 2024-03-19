"""

Sample program to display numerical data to the user based on prompts Created by Emeka Thomas Onwugbonu for the CSE110 course on March 4, 2024
"""
age = int(input("Enter your age as an integer: "))
print(f"You will be {age + 1}years on your next birthday")
print()
number_of_cartons = int(input("Enter the number of cartons you have: "))
print(f"You have  {number_of_cartons * 12} eggs.")
print()
cookies = int(input("Enter the number of cookies you have as an integer: "))
number_of_persons = int(input("Enter the number of persons as an integer: "))
print(f"Each person gets {cookies / number_of_persons} cookies.")