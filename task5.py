# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def koef_polynom_to_lst(s):
    nums = s.split()
    nums1 = []
    for i in nums:
        if i.isdigit() or i == '-':
           nums1.append(i)
        if i == '=':
           break
    i = 0
    while nums1.count('-') != 0:
       if nums1[i] == '-':
            nums1[i] += nums1[i + 1]
            nums1.pop(i + 1)
            i = 0
       i += 1
    return nums1

with open('polynom1_task5.txt', 'r') as polynom1:
    lst1 = koef_polynom_to_lst(polynom1.read())
with open('polynom2_task5.txt', 'r') as polynom2:
    lst2 = koef_polynom_to_lst(polynom2.read())

res_lst = []
for i in range(len(lst1)):
    res_lst.append(int(lst1[i]) + int(lst2[i]))

with open('res_polynom_task5.txt', 'w') as data:
    data.write((f'{res_lst[0]} * x^2 + {res_lst[1]} * x + {res_lst[2]} = 0').replace('+ -', '- '))






