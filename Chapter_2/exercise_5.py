#Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
celsius = float(input('How many degrees Celsius is it? '))

fahrenheit = (celsius * 9 / 5) + 32

print('It is', fahrenheit, 'degrees Fahrenheit outside!')