A = str(input())
if A == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = ((a + b + c) / 2)
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif A == 'прямоугольник':
     a = int(input())
     b = int(input())
     print(a * b)
elif A == 'круг':
     r = int(input())
     print(3.14 * (r ** 2))