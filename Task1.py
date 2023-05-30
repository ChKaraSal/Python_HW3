# Задача 16: 
# Требуется вычислить, 
# сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

#     5
#     1 2 3 4 5
#     3
#     -> 1

number_N = int(input('Enter number N: '))
list_N = input('Enter number Ai: ').split()
my_array = list(map(int, list_N))
number_X = int (input('Enter number X: '))
count = 0

for i in range(number_N):
    if my_array[i] == number_X:
        count += 1
        
print('->', count)