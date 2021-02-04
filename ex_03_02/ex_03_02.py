#Get variables
hrs = input('Enter hours: ')
rate = input('Enter rate: ')

#Convert to float
try:
    f_hrs = float(hrs)
    f_rate = float(rate)
except:
    print('Error: enter a numeric number')
    quit()

if f_hrs > 40:
    pay = 40 * f_rate
    extra_pay = (f_hrs - 40) * (f_rate * 1.5)
    pay = pay + extra_pay
else:
    pay = f_rate * f_hrs

print(pay)