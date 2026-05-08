Exercises

---

Exercise 1:
Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

```Python
sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fh > 40 :
    #print('Overtime')
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 1.5)
    #print(reg,otp)
    xp = reg + otp 
else:
    #print('Regular')
    xp = fh * fr
print('Pay:',xp)
```

---

Exercise 2:
Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input

```Python
sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
try:
    fh = float(sh)
    fr = float(sr)
except:
    print('Error, please enter numeric input')
    quit()

print(fh, fr)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 1.5)
    xp = reg + otp 
else:
    xp = fh * fr
print('Pay:',xp)
```

---

Exercise 3:
Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error message.
If the score is between 0.0 and 1.0,

print a grade using the following table:

 Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
 < 0.6     F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F

Run the program repeatedly as shown above to test the various different values for input.