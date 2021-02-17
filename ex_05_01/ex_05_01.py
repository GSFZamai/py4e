count = 0
total = 0

while True:
    num = input('Enter a number: ')
    try:
        inum = int(num)
    except:
        if num.lower() != 'done' and num.lower() != 'pronto':
            print('Invalid entry')
            continue
        else:
            print(total, count, (total/count))
            break

    count = count + 1
    total = total + inum