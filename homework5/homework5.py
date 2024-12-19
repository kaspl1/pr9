import random

def generate_random_list():
    l = random.randint(1, 20)
    return [random.randint(1, 100) for i in range(l)]

def is_number(e):
    return isinstance(e, (int, float))

def are_all_elements_equal(y):
    for x in y:
        if x != y[0]:
            return False
    return True

def find_elements_greater_than_previous(y):
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

    print("Элементы, которые больше предыдущего:")
    if y[0] > y[-1]:
        print(y[0])

    for i in range(1, len(y)):
        if y[i] > y[i - 1]:
            print(y[i])

r = generate_random_list()

print("Сгенерированный список:", r)

find_elements_greater_than_previous(r)