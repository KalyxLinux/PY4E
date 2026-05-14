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
        