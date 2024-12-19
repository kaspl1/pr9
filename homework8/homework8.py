import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]


def get_user_choice():
    x = []
    y = list(range(5))

    print("Выберите по одному числу из каждой строки лотерейного билета.")

    while len(x) < 5:
        print("\nТекущий выбор:", x)
        print("Оставшиеся строки:", [row + 1 for row in y])

        try:
            r= int(input("Из какой строки выбрать число? (1-5): ")) - 1
            if r not in y:
                print("Вы уже выбрали число из этой строки или строка не существует. Попробуйте снова.")
                continue

            row = ticket[r]
            print(f"Числа в строке {r + 1}: {row}")
            number = int(input("Введите число из выбранной строки: "))
            if number not in row:
                print("Выберите число из указанной строки. Попробуйте снова.")
                continue

            x.append(number)
            y.remove(r)

        except ValueError:
            print("Введите корректное число.")

    return x


def get_random_choice():
    random_choice = [random.choice(row) for row in ticket]
    return random_choice


def compare_choices(x, random_choice):
    matches = len(set(x) & set(random_choice))
    return matches


def main():
    print("Добро пожаловать в лотерею!")

    user_choice = get_user_choice()

    random_choice = get_random_choice()

    print(f"\nВаш выбор: {user_choice}")
    print(f"Случайный выбор: {random_choice}")

    matches = compare_choices(user_choice, random_choice)

    print(f"\nКоличество совпадений: {matches}")
    if matches == 5:
        print("Поздравляем! Вы выиграли!")
    else:
        print("Попробуйте снова!")


main()
