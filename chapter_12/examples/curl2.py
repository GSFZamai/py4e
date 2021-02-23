import urllib.request

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3_2.jpg', 'wb')
size = 0

while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    print(size)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close()