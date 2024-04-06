
country_list = []
line_list = []
continent_list = []
year_list = []
life_expectancy_values = []

with open("./life-expectancy.csv") as life_expectancy:
    for line in life_expectancy:
        line_list.append(line)
        stripped_line = line.strip()
        splitted_line = stripped_line.split(",")
        # splitted_line = stripped_line.split()
        # splitted = splitted_line[0].split(',')
        # if splitted[3] not in life_expectancy_values:
            # life_expectancy_values.append(float(splitted[3]))
        # print(splitted[3])
        number_value_string = splitted_line[len(splitted_line)-1]
        if number_value_string not in life_expectancy_values:
            life_expectancy_values.append(number_value_string)

# print(life_expectancy_values[len(life_expectancy_values) - 1])
# print(type(life_expectancy_values[len(life_expectancy_values) - 1]))
# print(float(life_expectancy_values[len(life_expectancy_values) - 1]))

string_first_value = life_expectancy_values.pop(0)
print(string_first_value)
num_values = []
for x in life_expectancy_values:
    if x not in num_values:
        num_values.append(float(x))

print(num_values)
num_values.sort()

print(num_values[0])
for line in line_list:
    if str(num_values[0]) in line:
        print(line)