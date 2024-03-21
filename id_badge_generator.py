"""
An ID Badge Generator program by Emeka Thomas Onwugbonu
created on March 2, 2024.
"""
line = "-"*40

first_name = input("Enter First name: ")
last_name = input("Enter Last name: ")
email_address = input("Enter Email Address: ")
phone_number = input("Enter Phone Number: ")
job_title = input("Enter Job Title: ")
id_number = input("Enter ID Number: ")
hair_color = input("Enter hair color: ")
eye_color = input("Enter eye color: ")
month = input("Enter month: ")
training = input("Enter yes or no: ")

print(f"The ID Card is:")
print(line)
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{job_title.title()}")
print(f"ID: {id_number}")
print()
print(f"{email_address.lower()}")
print(f"{phone_number}")
print()
print(f"Hair: {hair_color.capitalize().ljust(15)} Eyes: {eye_color.capitalize()}")
print(f"Month: {month.capitalize().ljust(12)}   Training: {training.capitalize()}")
print(line)



