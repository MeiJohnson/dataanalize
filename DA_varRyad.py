import math
from prettytable import PrettyTable


n = int(input('Введите количество элементов '))
lst=[]

data = open('a.in')
for i in range(n):
    lst.append(float(data.readline()))
lst.sort()
print('Вариационный ряд:')
for i in lst:
    print(i, end=' ')
print()

k = 1+1.4*math.log(n)
print('Количество интервалов по формуле Стерджерса:', k)
k_round = round(k)+1
print('Количество интервалов: ', k_round)
delta = (lst[len(lst)-1]-lst[0])/k_round
print('Длиина интервалов:', round(delta,3))
print()

ends = []
ends.append(round((lst[0]+delta), 3))
begins = []
begins.append(round(lst[0], 3))
begins.append(round(ends[0], 3))
for i in range(1, k_round):
    ends.append(round(ends[i-1]+delta, 3))
    if i != k_round-1:
        begins.append(round(ends[i], 3))

mi_list = []
middle = []
mxi_list = []
wxi_list = []

for i in range(k_round):
    mi_list.append(0)

for i in range(k_round):
    for j in range(len(lst)):
        if lst[j] >= begins[i] and lst[j] < ends[i]:
            mi_list[i] += 1

mxi_list.append(mi_list[0])

for i in range(k_round):
    middle.append((begins[i]+ends[i])*0.5)

for i in range(1, k_round):
    mxi_list.append(mxi_list[i-1]+mi_list[i])
mxi_list[len(mxi_list)-1] += 1

for i in range(k_round):
    wxi_list.append(round(mxi_list[i]/n,3))


inter_table = PrettyTable()
inter_table.add_column("Начала интервалов", begins)
inter_table.add_column("Концы интервалов", ends)
print('Данные об интервалах')
print(inter_table)

var_table = PrettyTable()
var_table.add_column("Среднее", middle)
var_table.add_column("Частоты", mi_list)
print('Таблица для гистограммы')
print(var_table)

mxi_table = PrettyTable()
mxi_table.add_column("Среднее", middle)
mxi_table.add_column("Накопленная частота", mxi_list)
print('Таблица для кумулянты')
print(mxi_table)

wxi_table = PrettyTable()
wxi_table.add_column("Среднее", middle)
wxi_table.add_column("Относительная частота", wxi_list)
print('Таблица для функции Эмпирического распределния')
print(wxi_table)
