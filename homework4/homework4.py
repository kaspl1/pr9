y = []

while True:
    user_input = input("Введите число (или 'end' для завершения): ")

    if user_input.lower() == 'end':
        break

    try:
        x = float(user_input)
        y.append(x)
    except ValueError:
        print("Ошибка это не число, попробуйте снова.")

even_count = 0
odd_count = 0

for x in y:
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Количество четных чисел: {even_count}")
print(f"Количество нечетных чисел: {odd_count}")
