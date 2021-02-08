#open file romeo.txt
file = 'romeo.txt' #constant only for tests
fh = open(file)
wlist = list()

for line in fh: #read line by line
    twl = line.split() #for each line, split the line into a list of words
    for word in twl: 
        if word in wlist: #for each word, check if the worD alredy exists in the list
            continue
        else:
            wlist.append(word) #if not, appends to the list

wlist.sort() #when it´s done print the sorted(alphabetical order) list
print(wlist) 
