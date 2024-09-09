try:
    in_temp_val = int(input("Enter a temperature value you would like to convert: "))
except ValueError:
    print(f'ValueError: Please enter a temperature value in integer')
else:
    in_temp_unit = input("Enter a temperature unit you would like to convert: ")
    in_temp_out = input("Enter a temperature unit you would like to get: ")


    def celsius_to_fahrenheit(C):
        F = (9 / 5 * C) + 32
        print(f'Celsius: {C}C to Fahrenheit: {F}F')


    def fahrenheit_to_celsius(F):
        C = (F - 32) * 5 / 9
        print(f'fahrenheit: {F}F to Celsius: {C}C')


    def celsius_to_kelvin(C):
        K = C + 273.15
        print(f'celsius: {C}C to Kelvin: {K}K')


    if in_temp_unit == "celsius" and in_temp_out == "fahrenheit":
        celsius_to_fahrenheit(in_temp_val)
    elif in_temp_unit == "fahrenheit" and in_temp_out == "celsius":
        fahrenheit_to_celsius(in_temp_val)
    elif in_temp_unit == "celsius" and in_temp_out == "kelvin":
        celsius_to_kelvin(in_temp_val)

finally:
    print(f'Your temperature conversion is completed!!!!')


