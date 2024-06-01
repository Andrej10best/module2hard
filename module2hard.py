import math
import random

n = random.randint(3, 20)

print('Выпавшее число:', n)
print('Пароль к выпавшему числу:')

for i in range(1, math.ceil(n / 2)):
    for j in range(i+1, n):
        if (i + j) % n == 0 or n % (i + j) == 0:
            print(i, j, end='', sep='')
