import random


def generate_random_list():
    l = random.randint(1, 20)
    return [random.randint(1, 100) for _ in range(l)]


def is_number(e):
    return isinstance(e, (int, float))


def are_all_elements_equal(y):
    for x in y:
        if x != y[0]:
            return False
    return True


def swap_min_max(y):
    for x in y:
        if not is_number(x):
            print(f"Ошибка: элемент {x} не является числом.")
            return

    if not y:
        print("Список пуст.")
        return

    if len(y) == 1:
        print("В списке только один элемент")
        return

    if are_all_elements_equal(y):
        print("Все элементы в списке одинаковые.")
        return

    min_index = y.index(min(y))
    max_index = y.index(max(y))

    y[min_index], y[max_index] = y[max_index], y[min_index]

    print("Список после замены минимального и максимального элементов:", y)


r = generate_random_list()

print("Сгенерированный список:", r)

swap_min_max(r)
