from random import randint


def trap(n):
    unique = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                unique += str(i) + str(j)
    return f'{n} - {unique}\nПоздравляю, вас не раздавят шипы'

n = int(input("Введите число и если оно будет кратно сумме каждой пары то вы будете жить: "))

indian_jones = trap(n)
print(indian_jones)