# # # # # # string = "GAG"
# # # # # # yet = "Prog"
# # # # # # fast = '{:<10}'.format(string)
# # # # # # fast2 = '{:>10}'.format(yet)
# # # # # # print(string, fast2)
# # # # # # print("garri".ljust(15), fast2)
# # # # # # # print("beanstalk".ljust(15), fast2)
# # # # # # print(type(fast))

# # # # # # cars = 3
# # # # # # people = 8
# # # # # # persons_per_car = people/cars
# # # # # # print(f"{persons_per_car}")
# # # # # # print(f"{persons_per_car:.3f}")
# # # # # # print(f"{persons_per_car:.3e}")
# # # # # # print(f"{persons_per_car:,.4f}")
# # # # # # print(f"{persons_per_car:6}")
# # # # # # print(f"{persons_per_car}")
# # # # # # print(f"")
# # # # # # print(f"")
# # # # # # print(f"")
# # # # # play = 5
# # # # # if play >= 2:
# # # # #     print("It is true")

# # # # # x = 5
# # # # # y = 10

# # # # # if x == 5:
# # # # #     print('a')
# # # # #     if y == 6:
# # # # #         print('b')
# # # # # else:
# # # # #     print('c')
# # # # #     if y == 10:
# # # # #         print('d')

# # # # x = 5
# # # # y = 6

# # # # if x == 5:
# # # #     print("a")

# # # #     if y == 6:
# # # #         print("b")
# # # # else:
# # # #     print("c")

# # # #     if y == 10:
# # # #         print("d")        

# # # x = 5

# # # if x = 5:
# # #     print("first")
# # # else:
# # #     print("second")
# # # "plate"
# # items = ['rice', 'beans', 'corn', 'pepper', 'meat']
# # prices = [2.4, 3.6, 7.45, 4.44, 8.90]
# # prices[1] = 6
# # # for i in range(len(prices)):
# # #     jam = prices[i]
# # #     print(i, jam, items[i])
# # # prices.pop(0)
# # # print(prices)
# # print(prices)

# line_list = []
# life_expectancy_values = []
# values_list = []

# with open("./life-expectancy.csv") as life_expectancy:
#     for line in life_expectancy:
#         # line_list.append(line.strip())
#         line1 = line.strip()
#         line2 = line1.split(",")
#         line_list.append(line2)
#         values_list.append(line2[-1])


# values_list.pop(0)
# values_list.sort()

# lowest_value = float(values_list[0])
# highest_value = float(values_list[-1])

# print(f"The lowest value for life expectancy was {lowest_value:.2f} while the highest value for life expectancy was {highest_value:.2f}.")



# line_list = []
# life_expectancy_values = []

# with open("./life-expectancy.csv") as life_expectancy:
#     for line in life_expectancy:
#         line_list.append(line.strip())

# for x in line_list:
#     value_list = x.split(',')
#     life_expectancy_values.append(value_list[len(value_list) - 1])
# life_expectancy_values.pop(0)         
# life_expectancy_values.sort()  

# lowest_value = float(life_expectancy_values[0])
# highest_value = float(life_expectancy_values[len(life_expectancy_values) - 1])

# print(f"The lowest value for life expectancy was {lowest_value:.2f} while the highest value for life expectancy was {highest_value:.2f}.")

place_list_for_year = ['Afghanistan', 'Africa', 'Albania', 'Algeria', 'American Samoa', 'Americas', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Asia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Democratic Republic of Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Europe', 'Faeroe Islands', 'Falkland Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latin America and the Caribbean', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia (country)', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North Korea', 'Northern America', 'Northern Mariana Islands', 'Norway', 'Oceania', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Barthlemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Virgin Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican', 'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara', 'World', 'Yemen', 'Zambia', 'Zimbabwe']


values_for_year_of_interest = ['64.13', '62.472', '78.333', '76.499', '73.636', '76.62993096', '83.443', '60.379', '81.568', '76.752', '76.372', '74.797', '76.01', '73.15', '83.122', '81.34', '72.693', '73.554', '77.032', '72.052', '78.981', '74.34', '81.305', '74.365', '61.174', '82.316', '71.129', '70.945', '77.42', '77.128', '68.812', '75.456', '78.742', 
'75.585', '74.815', '60.768', '60.898', '69.289', '58.511', '82.21', '72.57', '83.633', '52.24', '53.712', '82.766', '79.909', '76.47', '76.925', '63.912', '63.954', '75.845', '79.914', '57.017', '78.197', '78.662', '78.587', '80.672', '79.058', '60.026', '80.681', '65.893', '74.597', '73.689', '76.584', '71.656', '72.872', '58.061', '65.538', '78.354', '65.872', '78.25', '80.383', '81.163', '67.252', '81.561', '82.432', '79.731', '77.251', '65.839', '61.44', '73.414', '81.039', '63.463', '79.63', '81.901', '71.565', '72.388', '81.708', '79.631', '73.81', '60.706', '57.673', '69.624', '63.29', '74.898', '84.493', '76.498', '82.725', '69.165', '71.282', '76.271', '70.294', '81.872', '81.112', '82.663', '83.184', '74.267', '84.29', '74.292', '72.728', '65.909', 
'67.851', '75.311', '71.193', '67.277', '75.169', '75.048', '78.833', '52.947', '63.295', '72.52', '82.228', '75.507', '81.955', '83.989', '75.589', '66.311', '63.279', '75.828', '78.325', '58.452', '82.221', '73.278', '82.164', '64.464', '74.743', '79.405', '74.947', '67.618', '71.717', '86.325', '69.509', '76.667', '74.501', '76.218', '59.309', '66.558', '63.021', '59.805', '70.169', '82.004', '77.196', '82.002', '74.068', '61.599', '53.95', '73.424', '71.91', '79.198', '76.089', '82.146', '78.336', '77.393', '66.947', '73.32', '73.74', '78.149', '64.01', '73.992', '76.286', '70.952', '78.338', '81.655', '79.806', '79.981', '80.052', '75.79', '72.139', '68.341', '81.599', '80.321', '75.91', '75.907', '81.622', '80.783', '72.3', '73.046', '84.699', '69.933', 
'74.874', '67.38', '75.684', '73.276', '53.895', '83.279', '78.644', '77.219', '81.016', '72.645', '56.709', '63.538', '82.628', '57.365', '83.294', '76.648', '64.881', '71.463', '58.319', '82.516', '83.473', '70.967', '80.107', '70.647', '64.479', '76.683', '69.007', '60.489', '81.476', '70.701', '73.245', '76.31', '77.161', '67.956', '79.884', '67.089', '62.516', '71.84', '77.647', '81.168', '78.861', '80.26', '77.632', '71.388', '70.172', '74.749', '72.246', '75.241', '79.605', '69.762', '72.169', '66.086', '63.043', '60.812']

# print(len(values_for_year_of_interest))
# print(len(place_list_for_year))
# print(values_for_year_of_interest.index('81.168'))

values_for_year_of_interest.sort()
# print(values_for_year_of_interest)
print(values_for_year_of_interest.index("86.325"))
print(place_list_for_year)

values_for_year_of_interest2 = ['64.13', '62.472', '78.333', '76.499', '73.636', '76.62993096', '83.443', '60.379', '81.568', '76.752', '76.372', '74.797', '76.01', '73.15', '83.122', '81.34', '72.693', '73.554', '77.032', '72.052', '78.981', '74.34', '81.305', '74.365', '61.174', '82.316', '71.129', '70.945', '77.42', '77.128', '68.812', '75.456', '78.742', 
'75.585', '74.815', '60.768', '60.898', '69.289', '58.511', '82.21', '72.57', '83.633', '52.24', '53.712', '82.766', '79.909', '76.47', '76.925', '63.912', '63.954', '75.845', '79.914', '57.017', '78.197', '78.662', '78.587', '80.672', '79.058', '60.026', '80.681', '65.893', '74.597', '73.689', '76.584', '71.656', '72.872', '58.061', '65.538', '78.354', '65.872', '78.25', '80.383', '81.163', '67.252', '81.561', '82.432', '79.731', '77.251', '65.839', '61.44', '73.414', '81.039', '63.463', '79.63', '81.901', '71.565', '72.388', '81.708', '79.631', '73.81', '60.706', '57.673', '69.624', '63.29', '74.898', '84.493', '76.498', '82.725', '69.165', '71.282', '76.271', '70.294', '81.872', '81.112', '82.663', '83.184', '74.267', '84.29', '74.292', '72.728', '65.909', 
'67.851', '75.311', '71.193', '67.277', '75.169', '75.048', '78.833', '52.947', '63.295', '72.52', '82.228', '75.507', '81.955', '83.989', '75.589', '66.311', '63.279', '75.828', '78.325', '58.452', '82.221', '73.278', '82.164', '64.464', '74.743', '79.405', '74.947', '67.618', '71.717', '86.325', '69.509', '76.667', '74.501', '76.218', '59.309', '66.558', '63.021', '59.805', '70.169', '82.004', '77.196', '82.002', '74.068', '61.599', '53.95', '73.424', '71.91', '79.198', '76.089', '82.146', '78.336', '77.393', '66.947', '73.32', '73.74', '78.149', '64.01', '73.992', '76.286', '70.952', '78.338', '81.655', '79.806', '79.981', '80.052', '75.79', '72.139', '68.341', '81.599', '80.321', '75.91', '75.907', '81.622', '80.783', '72.3', '73.046', '84.699', '69.933', 
'74.874', '67.38', '75.684', '73.276', '53.895', '83.279', '78.644', '77.219', '81.016', '72.645', '56.709', '63.538', '82.628', '57.365', '83.294', '76.648', '64.881', '71.463', '58.319', '82.516', '83.473', '70.967', '80.107', '70.647', '64.479', '76.683', '69.007', '60.489', '81.476', '70.701', '73.245', '76.31', '77.161', '67.956', '79.884', '67.089', '62.516', '71.84', '77.647', '81.168', '78.861', '80.26', '77.632', '71.388', '70.172', '74.749', '72.246', '75.241', '79.605', '69.762', '72.169', '66.086', '63.043', '60.812']

print(values_for_year_of_interest2.index("86.325"))
print(place_list_for_year[140])

