lab = """
111111111111111111
1x0010000000000001
111011101111111101
101010000100000001
101011010101111111
101000010100001001
100011110101111101
101110010100000001
100000000101101111
101101111100100001
101001000000101001
101101111111101001
101000000000001001
101011110100101001
101000010111111001
111011110100000001
101000000101111111
101011110101010101
1000000101000000#1
111111111111111111""".split()
labirint2 = []
# превращение строки в список строк
for i in lab:
    labirint2.append(list(i))
#format
for i in range(len(labirint2)):
    for j in range(len(labirint2[i])):
        if labirint2[i][j]=='1':
            labirint2[i][j]='-1'

# печать списка в виде матрицы
for i in labirint2:
    for j in i:
        print("{:^3}".format(j), end=",")
    print("")

# поиск начальной точки
co_enter = [0, 0]
for i in range(len(labirint2)):
    for j in range(len(labirint2[i])):
        if labirint2[i][j] == 'x':
            co_enter = [i, j]
            y = co_enter[j]
            x = co_enter[i]
            print(co_enter)

tern = []


# функция поиска выхода
def Found(x0, y0):
    if labirint2[x0][y0] == '#':
        print('exit found')
    else:
        labirint2[x0][y0] = '2'

        if labirint2[x0][y0 + 1] == '0' or labirint2[x0][y0 + 1] == '#':
            tern.append('r')
            Found(x0, y0 + 1)
        if labirint2[x0][y0 - 1] == '0' or labirint2[x0][y0 - 1] == '#':
            tern.append('l')
            Found(x0, y0 - 1)
        if labirint2[x0 - 1][y0] == '0' or labirint2[x0 - 1][y0] == '#':
            tern.append('u')
            Found(x0 - 1, y0)
        if labirint2[x0 + 1][y0] == '0' or labirint2[x0 + 1][y0] == '#':
            tern.append('d')
            Found(x0 + 1, y0)


Found(x, y)
print(tern)
print()
for i in labirint2:
    for j in i:
        print("{:^3}".format(j), end=" ")
    print("")

