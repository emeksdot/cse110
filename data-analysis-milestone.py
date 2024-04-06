"""
A Data Analysis program to evaluate life-expectancies created by Emeka Thomas Onwugbonu for the CSE110 week 06 milestoneproject using data stored in the life-expectancy.csv file from OurWorldInData.org website.
"""

line_list = []
life_expectancy_values = []
values_list = []

with open("./life-expectancy.csv") as life_expectancy:
    for line in life_expectancy:
        line1 = line.strip()
        line2 = line1.split(",")
        line_list.append(line2)
        values_list.append(line2[-1])

year_of_interest = input("Enter year of interest: ")

place_list_for_year = []
values_for_year_of_interest = []
for x in line_list:
    if year_of_interest in x:
        place_list_for_year.append(x[0])
        values_for_year_of_interest.append(x[3])
print(place_list_for_year)
print()
print(values_for_year_of_interest)
print()
new_value_list = []
for i in values_for_year_of_interest:
    new_value_list.append(float(i))
print(new_value_list)
print()

new_value_list.sort()
print(new_value_list)

min_value_for_year = float(new_value_list[0])
max_value_for_year = float(new_value_list[-1])

max_value_place = place_list_for_year[values_for_year_of_interest.index(str(max_value_for_year))]
min_value_place = place_list_for_year[values_for_year_of_interest.index(str(min_value_for_year))]

print(f"For the year {year_of_interest}:")
print(f"The overall max life expectancy is: {max_value_for_year:.2f} from {max_value_place} in {year_of_interest} ")
print(f"The overall min life expectancy is: {min_value_for_year:.2f} from {min_value_place} in {year_of_interest} ")

average_life_expectancy = ""
for i in line_list:
    if i[0] == 'World' and i[2] == year_of_interest:
        average_life_expectancy = float(i[3])
print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")




