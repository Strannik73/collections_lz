input_data = open('input.txt', 'r')
output_data = open('output.txt', 'w')

n = input_data.readline()
#----------------------------------------------------------------------------------

f1 = 0
f2 = 1
k = 0 #количество элементов больше медианного значения
# Выводим значения двух первых членов последовательности через запятую
list = []
list.append(0)
list.append(1)

for i in range(2, int(n) + 1):
    # Переприсваеваем n-ому и n+1-ому члену значения n+1-ого и n+2-ого
    f1, f2 = f2, f1 + f2
    # Выводим в файл новое значение переменной f2 (она сейчас равна n+2-ому члену)
    list.append(f2)
    
        

for i in range(0, len(list)): 
    if list[i] % 2 == 0:
        list[i] *= 2 
    else: list[i] **= 2

minP = min(list)
maxP = max(list)
lenP = len(list)
medz = (minP + maxP)/2
for i in range(0, lenP):
    if int(list[i]) > medz:
        k += 1 #проверяем, сколько чисел бедет больше мидианного значения
output_data.write(str('min - ') + str(minP) + str('\nmax - ') + str(maxP) + str('\nlen - ') + str(lenP) + str('\n> median - ') + str(k))

#--------------------------------------------------------------------------------------------
input_data.close()
output_data.close()