#Get variables
hrs = input('Enter hours: ')
rate = input('Enter rate: ')

#Convert to float
f_hrs = float(hrs)
f_rate = float(rate)

#Conditional calculation
if f_hrs > 40:
    pay = 40 * f_rate
    rest = f_hrs - 40
    extra_rate = f_rate * 1.5
    pay = pay + (rest * extra_rate)
else:
    pay = f_hrs * f_rate

print('Pay:', pay)

