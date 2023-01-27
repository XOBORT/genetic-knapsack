from lab_10 import *
from openpyxl import Workbook
import openpyxl

wb = openpyxl.load_workbook(filename = 'sample.xlsx') 
sheet = wb.active 

ABC = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
ip = [1, 2, 12, 13, 123, 23]
ip_enc = ['Случайный', 'Случайный с контролем ограничений', 'Случайный и Случайный с контролем ограничений', 'Случайный и Жадная эвристика', 'Случайный и Случайный с контролем ограничений и Жадная эвристика', 'Случайный с контролем ограничений и Жадная эвристика']
cc = [1, 2, 3]
cc_enc = ['Одноточечный', 'Двухточечный', 'Многоточечный']
mm = [1, 2, 3, 4, 5]
mm_enc = ['Точечная', 'Сальтация', 'Инверсия', 'Транслокация', 'Дополнение']
            # = (B1+C1+D1+E1+F1+G1+H1+I1+J1+K1+L1+M1+N1+O1+P1)/15
            # Способ формирования нач. попул., Оператор кроссовера, Оператор мутации
            # =МИН(Q3:Q92)
            # =МАКС(Q3:Q92)

iiii = 1
for ipi in range(0, 6):
    for ci in range(0, 3):
        for mi in range(0,5):
            c1 = sheet[f"A{str(iiii)}"]
            c1.value = f"{ip_enc[ipi]}, {cc_enc[ci]}, {mm_enc[mi]}"
            for j in range(0, 15):
                c3 = sheet[ABC[j+1]+str(iiii)] 
                c3.value = main(ip[ipi], cc[ci], mm[mi])
            iiii +=1

wb.save("sample.xlsx")