import math
def get_integer_squares(x, y):

    start = min(x, y)
    end = max(x, y)

    if start.is_integer() and end.is_integer():
        start = int(start) + 1
        end = int(end) - 1
    else:
        start = math.ceil(start)
        end = math.floor(end)

    s = [i ** 2 for i in range(start, end + 1)]
    return s

def main():
    while True:
        try:
            x = float(input("Введите первое число x: "))
            y = float(input("Введите первое число y: "))
            break
        except ValueError:
            print("Ошибка: пожалуйста, введите корректные числа.")

    s = get_integer_squares(x, y)

    print("Список квадратов целых чисел между x и y:", s)

if __name__ == "__main__":
    main()
