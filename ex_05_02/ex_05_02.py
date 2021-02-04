#Define variables
largest = None
smallest = None

#Loop until done
while True:
    #Try for a valid integer or done
    try :
        num = input('Enter a number: ')
        i_num = int(num) #Convert string to int
    except :
        if num == 'done' : #break if the input is done
            break
        else :
            print('Invalid input') #asks for a valid number
            continue 
    if largest is None or i_num > largest : #checks if the input is larger
        largest = i_num
    if smallest is None or i_num < smallest : #checks if the input is smaller
        smallest = i_num

print('Maximum is', largest) #print largest
print('Minimum is', smallest) #print smallest