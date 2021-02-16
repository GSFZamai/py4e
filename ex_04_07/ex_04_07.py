import random
#score = input('Enter escore: ')
fscore = float(score)

# Pontuação Nota
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

def computaNota(nota):
    print(nota)
    score = None
    if nota < 0:
        score = 'Error: Out of Range'
    elif nota > 1:
        score = 'Error: Out of Range'
    elif nota >= 0.9:
        score = 'A'
    elif nota >= 0.8:
        score = 'B'
    elif nota >= 0.7:
        score = 'C'
    elif nota >= 0.6:
        score = 'D'
    elif nota < 0.6:
        score = 'F'
    
    return score

print(computaNota(fscore))