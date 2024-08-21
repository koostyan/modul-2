def draw_area():
    for i in area:
        print(*i)
    print()

area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("добро пожаловать в крестики-нолики")
print("__________________________________")
draw_area()
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = "0"
        print("Ходят нолики")
    else:
        turn_char = "X"
        print("Ходят крестики")
    row = int(input("Введите номер строки (1,2,3) "))-1
    colum = int(input("Введите номер столбца (1,2,3) "))-1
    if area[row][colum] == "*":
        area[row][colum] = turn_char
    else:
        print("Ячейка уже занята, вы пропускаете ход")
        draw_area()
        continue
    draw_area()



