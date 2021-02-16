# Get inputs from user
hrs = input('Enter hours: ')
rate = input('Enter rate: ')

# Define Function
def computepay(h,r):
    # Try for correct numeric input
    try:
        f_hours = float(h)
        f_rate = float(r)
    except:
        return 'Error: input a number.'
    
    # Conditional calculation
    if f_hours > 40:
        regular = 40 * f_rate
        extra = (f_hours - 40) * (f_rate * 1.5)
        pay = regular + extra
    else:
        pay = f_hours * f_rate
    
    return pay
# Print result
print('Pay', computepay(hrs,rate))