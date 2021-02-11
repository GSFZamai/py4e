fname = input('Enter a file: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

try:
    fh = open(fname)
except:
    print('File not found,', fname)
    exit()

hours = dict()
for line in fh:
    words = line.split()
    if len(words) < 1 or words[0] != 'From':
        continue
    else:
        hour = words[5].split(':')
        hours[hour[0]] = hours.get(hour[0], 0) + 1

for k, v in sorted(hours.items()):
    print(k, v)
