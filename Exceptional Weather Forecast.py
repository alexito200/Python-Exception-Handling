# Task 1: Start

temperature = input("Tell me the temperature in Fahrenheit: ")

# Task 2: Temperature Conversion 
# Write a function that converts the Fahrenheit temperature to Celsius.
# Remember that the formula is (Fahrenheit - 32) * 5/9.
# Use a try block to catch any potential errors during the conversion process.
# What happens if they type out "thirty" instead of doing 30?

def temperature_conversion(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
    except ValueError:
        print("Invalid input. Please enter a valid number.")
# Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
    else:
        print(f'{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.')
# Task 4: Finally
    finally:
        print('Thank you for using our weather app!')

temperature_conversion(temperature)