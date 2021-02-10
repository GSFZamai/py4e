#gets file name or default mbox-short.txt
fname = input('File name: ')
if (len(fname)) < 1 : fname = 'mbox-short.txt'

#open file
fh = open(fname)

#look for From lines and count mail adresses
mails = dict()
for line in fh:
    words = line.split()
    if (len(words)) == 0 or words[0] != 'From':
        continue
    else:
        mails[words[1]] = mails.get(words[1], 0) + 1
#print(mails)

#count mails
big_mail = None
big_count = None
for k in mails:
    if big_count is None or mails[k] > big_count:
        big_mail = k
        big_count = mails[k]
    else:
        continue


print(big_mail, big_count)