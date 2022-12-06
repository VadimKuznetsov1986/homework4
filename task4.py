# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов(значения от 0 до 100)* многочлена
# и записать в файл многочлен степени k.

import random

k = int(input('Введите k: '))
coeff = [random.randint(-100, 100) for i in range(0, k + 1)]

res_polynom = ''
for i in range(k + 1):
    if coeff[i] == 0:
        res_polynom += ''
    elif k - i > 1:
        res_polynom += f'{coeff[i]} * x^{k - i} + '
    elif k - i == 1:
        res_polynom += f'{coeff[i]} * x + '
    else:
        res_polynom += f'{coeff[i]} = 0'
with open('res_polynom_task4.txt', 'w') as data:
    data.write(res_polynom.replace('+ -', '- '))

