y = []
while True:
    u = input("Введите число (или 'end' для завершения): ")
    if u.lower() == 'end':
        break

    try:
        x = float(u)
        y.append(x)
    except ValueError:
        print("Ошибка, это не число, попробуйте снова.")

o = []
for x in y:
    if x % 2 != 0:
        o.append(x)
print(o)
