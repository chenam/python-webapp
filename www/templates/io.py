from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
# strip 类似于 trim
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())