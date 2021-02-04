# Receive value and convert to float
score = input('Enter Score: ')
f_score = float(score)


# Conditional execution based on table
if f_score < 0:
    print('Error: Out of range.')
elif f_score < 0.6:
    print('F')
elif f_score > 1:
    print('Error: Out of range.')
elif f_score >= 0.9:
    print('A')
elif f_score >= 0.8:
    print('B')
elif f_score >= 0.7:
    print('C')
elif f_score >= 0.6:
    print('D')
