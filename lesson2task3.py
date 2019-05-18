s = input()
l = len(s)
l = l // 2
for i in range(l):
    if s[i] != s[-1 - i]:
        print('its not polindrom')
        quit()
print('its polindrom')
