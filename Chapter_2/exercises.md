Exercises

---

Exercise 1:
Type the following statements in the Python interpreter to see what they do:

5
x = 5
x + 1

Answer:
6

---

Exercise 2:
Write a program that uses input to prompt a user for their name and then welcomes them.

Enter your name: Chuck
Hello Chuck

Answer:

```Python
name = input('whats your name? ')

print('Welcome on in',(name))
```

---

Exercise 3:
Write a program to prompt the user for hours and rate per hour to compute gross pay.

Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
We won’t worry about making sure our pay has exactly two digits after the decimal place for now. If you want, you can play with the built-in Python round function to properly round the resulting pay to two decimal places.

Answer:

```Python
hours = float(input('Hours: '))
rate = float(input('Rate: '))

print(hours * rate)
```
---

Exercise 4:
Assume that we execute the following assignment statements:

width = 17
height = 12.0
For each of the following expressions, write the value of the expression and the type (of the value of the expression).

width//2

width/2.0

height/3

1 + 2 * 5

Use the Python interpreter to check your answers.

Answer:

```Python
>>> width = 17
>>> height = 12.0
>>> float(width) // 2
8.0
>>> float(width) / 2.0
8.5
>>> float(height) / 3
4.0
>>> 1 + 2 * 5 
11
```

---

Exercise 5:
Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

Answer:

```Python
celsius = float(input('How many degrees Celsius is it? '))

fahrenheit = (celsius * 9 / 5) + 32

print('It is', fahrenheit, 'degrees Fahrenheit outside!')
```

---