input_string = input()
values = input_string.split()
count = len(values)
if count == 1:
    r = int(input_string)
    if r <= 0:
        print("Такой круг не существует")
    else:
        r = int(input_string)
        from math import pi
        p = 2 * pi * r
        s = pi * r ** 2
        print(f"Круг: рудиус: {r}; периметр: {p} площадь: {s}")
elif count == 2:
    a, b = values
    a1 = int(a)
    b1 = int(b)
    if a1 <= 0 or b1 <= 0:
        print("Такого прямоугольника не существует")
    else:
        p = 2 * (a + b)
        s = a * b
        print(f"Прямоугольник: a = {a}, b = {b}, переиметр: {p}; площадь: {s}")
elif count == 3:
    a, b, c = values
    a1 = int(a)
    b1 = int(b)
    c1 = int(c)
    if a1 <= 0 or b1 <= 0 or c1 <= 0:
        print("Такого треугольника не существует")
    elif a1 + b1 <= c1 or b1 + c1 <= a1 or a1 + c1 <= b1:
        print("Такого треугольника не существует")
    else:
        p = (a1 + b1 + c1)
        p_p = (a1 + b1 + c1) / 2
        from math import sqrt
        s = sqrt(p_p * (p_p - a1) * (p_p - b1) * (p_p - c1))
        print(f"Треугольник: a = {a}, b = {b}, c = {c}; периметр:{p}; площадь: {s}")
