area = list(range(1, 10)) # создаем список от 0 до 9

def plaing_area(area):
    """
    Функция рисует игровое поле 3х3 и пронумеровывает каждую ячейку этого поля

    :param area: список чисел
    :return: None
    """
    print("=" * 13)
    for i in range(3):
        print("|", area[0 + i * 3], "|", area[1 + i * 3], "|", area[2 + i * 3], "|")
        print("=" * 13)


def check_player_input(player_letter):
    """
    Функция для ввода крестика или нолика в соответствующую клетку

    :param player_letter: число
    :return: None
    """
    shans = False
    while not shans:
        player_choice = input("В какую клетку поставим " + player_letter + "? ")
        try:
            player_choice = int(player_choice)
        except ValueError:
            print("Некорректный ввод. Нужно ввести число от 1 до 9!")
            continue
        if 1 <= player_choice <= 9:
            if str(area[player_choice - 1]) not in "XO":
                area[player_choice - 1] = player_letter
                shans = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def test_win(area):
    """
    Функция для проверки выйгрышной комбинации

    :param area: список чисел
    :return: True или False
     """
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 4, 8)) # Кортеж из выигрышных комбинаций
    for comb in win_comb:
         if area[comb[0]] == area[comb[1]] == area[comb[2]]:
             return area[comb[0]]
         return False


def game(area):
    """
    Функция для определения победителя

    :param area: список чисел
    :return: None
     """
    move = 0
    win = False
    while not win:
        plaing_area(area)
        if move % 2 == 0:
            check_player_input("Х")
        else:
            check_player_input("0")
        move += 1

        tw = test_win(area)
        if tw:
            print(tw, "Вы победитель!")
            win = True
            break
        if move == 9:
            print("Ничья! Попробуйте еще раз!")
            break



print(game(area))

input("Нажмите Enter для выхода!")
