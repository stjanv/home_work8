s = "spam and eggs or eggs with spam"
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
