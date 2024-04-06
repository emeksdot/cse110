"""
A Data Analysis program to evaluate life-expectancies created by Emeka Thomas Onwugbonu for the CSE110 week 06 midweek assignment using data stored in the life-expectancy.csv file from OurWorldInData.org website.
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


values_list.pop(0)
values_list.sort()

lowest_value = float(values_list[0])
highest_value = float(values_list[-1])

print()
print(f"The lowest value for life expectancy was {lowest_value:.2f} while the highest value for life expectancy was {highest_value:.2f}.")








