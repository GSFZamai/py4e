text = "X-DSPAM-Confidence:    0.8475"

start_pos = text.find('0')

number = text[start_pos : ]

f_number = float(number)

print(f_number)
