#get file name
fname = input('Enter file name: ')

#set file name if epmty
if (len(fname)) < 1 : fname = 'mbox-short.txt'

#try if file exist
try:
    fh = open(fname)
except:
    print('Invalid file name:', fname)
    exit()

count = 0
for line in fh:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    else:
        print(words[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")

