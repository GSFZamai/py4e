#get file name from user
fname = input('Enter the file name: ')

#handle file with try/except
try:
    hfile = open(fname)
except:
    print('File', fname, 'not found')
    print('quit()')
    quit()

#wanted line counter starting at 0
wlcounter = 0
wl = 0

#iterate each line of the file
for line in hfile:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    spos = line.find('0')
    wlcounter = wlcounter + 1
    number = line[spos:].strip()
    fnumber = float(number)
    wl = wl + fnumber

print('Average spam confidence:', wl/wlcounter)

