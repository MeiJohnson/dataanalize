import math
from prettytable import PrettyTable


def print_list(l,size):
  for i in range(size):
   print(l[i])

def main():
 n = int(input('Введите количество элементов '))
 lst=[]

 data = open('a.in')
 for i in range(n):
    lst.append(int(data.readline()))
 lst.sort()
 print_list(lst,n)

 k = 1+1.4*math.log(n)
 print('Коэффициент ', k)
 k_round = round(k)+1
 print(k_round)
 delta = (lst[len(lst)-1]-lst[0])/k_round
 print('Длиина интервалов',delta)

 ends = []
 ends.append((lst[0]+delta))
 begins = []
 begins.append(lst[0])
 begins.append(ends[0])
 for i in range(1,k_round):
     ends.append((ends[i-1]+delta))
     if i != k_round-1:
        begins.append(ends[i])
 mi_list = []
 middle = []
 mxi_list = []
 wxi_list = []

 for i in range(k_round):
   mi_list.append(0)

 for i in range(k_round):
   for j in range(len(lst)):
     if lst[j] >= begins[i] and lst[j] <  ends[i]:
       mi_list[i] +=1

 mxi_list.append(mi_list[0])

 for i in range(k_round):
   middle.append((begins[i]+ends[i])*0.5)

 for i in range(1,k_round):
    mxi_list.append(mxi_list[i-1]+mi_list[i])
 mxi_list[len(mxi_list)-1]+=1

 for i in range(k_round):
    wxi_list.append(mxi_list[i]/n)

 var_table = PrettyTable()
 
 var_table.add_column('Варианты',lst)
 
