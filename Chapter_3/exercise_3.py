# Exercise 3:
# Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0,

# print a grade using the following table:

# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
# < 0.6      F

score = float(input('What score did you get? '))

if score > 1.0 or score < 0.0:
    print('Error: Score is out of range.')

elif score >= 0.9:
    print('Your grade is an A!')

elif score >= 0.8:
    print('Your grade is a B!')

elif score >= 0.7:
    print('Your grade is a C!')

elif score >= 0.6:
    print('Your grade is a D!')

else:
    print('Your grade is a F!')