# Exercise 2:
# Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

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