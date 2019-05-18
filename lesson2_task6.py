s = 'English = 78 Science = 83 Math = 68 History = 65'
s = s.split()
print(s)
a = []
temp = 0
b = 0
for i in s:
    try:
        temp += int(i)
    except:
        continue
print(temp)
