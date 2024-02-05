try:
    mode = 0
    quantity = s =i = j = 0
    move_counter = 0
    symbolX = "X"
    symbol0 = "0"
    print("Вітаю у грі хрестики-нулики")
    win = False
    draw = False

    def first_menu():
        try:
            global s
            s = int(input("Якщо ви хочете грати за Х - 1, за О - 2: "))
            if s != 1 and s != 2:
                s = int(input("Якщо ви хочете грати за Х - 1, за О - 2: "))
        except:
            global s
            s = int(input("Якщо ви хочете грати за Х - 1, за О - 2: "))
            if s != 1 and s != 2:
                s = int(input("Якщо ви хочете грати за Х - 1, за О - 2: "))

    first_menu()

    field = ["---------"]
    field0 = [" ", " | ", " ", " | ", " "]
    field1 = [" ", " | ", " ", " | ", " "]
    field2 = [" ", " | ", " ", " | ", " "]

    def all_field():
            for i in range(len(field0)):
                print(field0[i], end="")
            print(" ")
            for i in range(len(field)):
                print(field[i])
            for i in range(len(field1)):
                print(field1[i], end="")
            print(" ")
            for i in range(len(field)):
                print(field[i])
            for i in range(len(field2)):
                print(field2[i], end="")
            print(" ")

    def win_check():
        global win, move_counter
        if field0[0] == field0[2] == field0[4] and field0[0] != " ":
            win = True
            print("Перемогли " + field0[0])
        elif field1[0] == field1[2] ==field1[4] and field1[0] != " ":
            win = True
            print("Перемогли " + field1[0])
        elif field2[0] == field2[2] ==field2[4] and field2[0] != " ":
            win = True
            print("Перемогли " + field2[0])
        elif field0[0] == field1[0] ==field2[0] and field0[0] != " ":
            win = True
            print("Перемогли " + field0[0])
        elif field0[2] == field1[2] ==field2[2] and field0[2] != " ":
            win = True
            print("Перемогли " + field0[1])
        elif field0[4] == field1[4] ==field2[4] and field0[4] != " ":
            win = True
            print("Перемогли " + field0[2])
        elif field0[0] == field1[2] ==field2[4] and field0[0] != " ":
            win = True
            print("Перемогли " + field0[0])
        elif field0[4] == field1[2] ==field2[0] and field0[4] != " ":
            win = True
            print("Перемогли " + field0[0])
        elif move_counter == 9:
            print("Нічия")
            final_menu()

    def final_menu():
        global field0, field1, field2, move_counter, win
        r = int(input("Якщо ви хочете зіграти ще раз - 1, якщо хочете закінчити гру - 2: "))
        if r != 1 and r != 2:
            r = int(input("Якщо ви хочете зіграти ще раз - 1, якщо хочете закінчити гру - 2: "))
        if r == 1:
            first_menu()
            field0 = [" ", " | ", " ", " | ", " "]
            field1 = [" ", " | ", " ", " | ", " "]
            field2 = [" ", " | ", " ", " | ", " "]
            move_counter = 0
            win = False
        elif r == 2:
            exit(0)
    def move():
        global s, i, j, move_counter
        while move_counter < 9:
            move_counter += 1
            if s == 1:
                i = int(input("ведіть рядок в якому ви хочете поставити X (0, 1, 2) "))
                j = int(input("ведіть стовпчик в якому ви хочете поставити X (0, 1, 2) "))
                if i != 0 and i != 1 and i != 2:
                    i = int(input("ведіть рядок в якому ви хочете поставити X (0, 1, 2) "))
                if j != 0 and j != 1 and j != 2:
                    j = int(input("ведіть стовпчик в якому ви хочете поставити X (0, 1, 2) "))
                j = j * 2
                if i == 0:
                    if field0[j] != " ":
                        print("Ця комірка зайнята, спробуйте ще раз")
                        move_counter -= 1
                    else:
                        field0[j] = symbolX
                        s = 2
                elif i == 1:
                    if field1[j] != " ":
                        print("Ця комірка зайнята, спробуйте ще раз")
                        move_counter -= 1
                    else:
                        field1[j] = symbolX
                        s = 2
                elif i == 2:
                    if field2[j] != " ":
                        print("Ця комірка зайнята, спробуйте ще раз")
                        move_counter -= 1
                    else:
                        field2[j] = symbolX
                        s = 2
                all_field()
            elif s == 2:
                i = int(input("ведіть рядок в якому ви хочете поставити 0 (0, 1, 2) "))
                j = int(input("ведіть стовпчик в якому ви хочете поставити 0 (0, 1, 2) "))
                if i != 0 and i != 1 and i != 2:
                    i = int(input("ведіть рядок в якому ви хочете поставити 0 (0, 1, 2) "))
                if j != 0 and j != 1 and j != 2:
                    j = int(input("ведіть стовпчик в якому ви хочете поставити 0 (0, 1, 2) "))
                j = j * 2
                if i == 0:
                    if field0[j] != " ":
                        print("Ця комірка зайнята, спробуйте ще раз")
                        move_counter -= 1
                    else:
                        field0[j] = symbol0
                        s = 1
                elif i == 1:
                    if field1[j] != " ":
                        print("Ця комірка зайнята, спробуйте ще раз")
                        move_counter -= 1
                    else:
                        field1[j] = symbol0
                        s = 1
                elif i == 2:
                    if field2[j] != " ":
                        print("Ця комірка зайнята, спробуйте ще раз")
                        move_counter -= 1
                    else:
                        field2[j] = symbol0
                        s = 1
                all_field()
            win_check()
            if win == True:
                final_menu()

    move()

except Exception as e:
    print(e)
