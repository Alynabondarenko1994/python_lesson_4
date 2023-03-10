# Задача 2
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9

n=int(input('Введите количество кустов n:'))
while n<3  :
    n=int(input('Введите число большее 2 :' ))
     
n_list=[]
for i in range(n):
    num=int(input(f'Введите количество ягод на {i+1} кусте:'))
    n_list.append(num)
max=0
for i in range(0,len(n_list)): 
    if (i==len(n_list)-1): 
        if n_list[0]+n_list[i]+n_list[i-1]>=max: 
            max=n_list[0]+n_list[i]+n_list[i-1] 
    elif n_list[i-1]+n_list[i]+n_list[i+1]>=max: 
        max=n_list[i-1]+n_list[i]+n_list[i+1]

print(f'Максимальное число ягод, которое может собрать за один заход собирающий модуль, равно {max}')

