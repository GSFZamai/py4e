import re
#handle = open('regex_sum_42.txt') test file
handle = open('regex_sum_1140871.txt')

soma = 0
count = 0

for line in handle:
    trim = line.rstrip()
    x = re.findall('[0-9]+', trim)
    
    if len(x) > 0:
        for n in x:
            int_n = int(n)
            soma = int_n + soma
            count = count + 1

print(count, soma)


