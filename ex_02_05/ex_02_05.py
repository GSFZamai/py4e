#get celsius temperature
cstring = input('Temperature in celsius (ºC): ')
cfloat = float(cstring)

def to_fahrenheit(celsius):
    fahrenheit = (celsius * 9)/5 + 32
    return fahrenheit

print('The temperature is:', to_fahrenheit(cfloat), 'ºF') 