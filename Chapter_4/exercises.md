Exercises

---

Exercise 4:
What is the purpose of the “def” keyword in Python?

a) It is slang that means “the following code is really cool”
b) It indicates the start of a function
c) It indicates that the following indented section of code is to be stored for later
d) b and c are both true
e) None of the above

Answer: 
D

---

Exercise 5: What will the following Python program print out?

def fred():
   print("Zap")

def jane():
   print("ABC")

jane()
fred()
jane()
a) Zap ABC jane fred jane
b) Zap ABC Zap
c) ABC Zap jane
d) ABC Zap ABC
e) Zap Zap Zap

Answer:
D

---

Exercise 6:
Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0

hours = float(input('Hours: ')

```Python
hours = float(input('Hours: '))
rate = float(input('Rate: '))

if hours > 40:
    overtime_hours = hours - 40
    regular_hours = 40
    pay = (regular_hours * rate) + (overtime_hours * rate * 1.5)
else:
    pay = hours * rate

print('Pay:', pay)
```

---

Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

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
Run the program repeatedly to test the various different values for input.

```Python
def computegrade(score):
    if score > 1.0 or score < 0.6:
        return('Bad Score')
    elif score >= 0.9:
        return('Your grade is an A!')
    elif score >= 0.8:
        return('Your grade is a B!')
    elif score >= 0.7:
        return('Your grade is a C!')
    elif score >= 0.6:
        return('Your grade is a D!')
    else:
        return('Your grade is a F!')
    
try:
    score = float(input('Enter score: '))
    print(computegrade(score))
except:
    print('Bad score') 
        
```