A = int(input())
B = int(input())
H = int(input())

if A <= H <= B:
    print('Это нормально')
else:
    if A < H > B:
        print('Пересып')
    else:
        print('Недосып')