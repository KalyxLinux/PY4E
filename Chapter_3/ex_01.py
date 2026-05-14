# Exercise 1:
# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
fh = float(sh)
fr = float(sr)

if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 1.5)
    xp = reg + otp 
else:
    xp = fh * fr
print('Pay:',xp)

