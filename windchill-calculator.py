

# wind_chill_in_fahrenheit = 35.74 + 0.6215T - 35.75(v ** 0.16) + 0.4275T(v ** 0.16)
# where T = air Temperature in Fahrenheit V = Wind Speed(mph)



Temp = float(input("Enter temperature: "))
scale = input("Enter 'F' for Fahrenheit or 'C' for Celsius: ")

def windchill_calc(Temperature, V, T_in_fahrenheit=True):
    """ Function to calculate the windchill given Air Temperature and Wind speed"""
    if scale == 'f' or scale == 'F':
        T = Temperature
    else:
        T = ((9 * Temperature) /5) + 32


    A = 35.74
    B = 0.6215 * T
    C = -35.75 * (V ** 0.16)
    D = 0.4275 * T * (V ** 0.16)

    return (A + B + C + D)


for x in range(5, 65, 5):
    if scale == 'f' or scale == 'F':
        print(f"At temperature {Temp}F, and wind speed {x} mph, the windchill is: {windchill_calc(Temp, x):.2f}F")
    else:
        print(f"At temperature {Temp}F, and wind speed {x} mph, the windchill is: {windchill_calc(Temp, x, False):.2f}F")
    

