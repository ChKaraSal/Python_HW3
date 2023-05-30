# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

#     5
#     1 2 3 4 5
#     6
#     -> 5

number_N = abs(int(input('Enter number N: ')))
numbers_Ai = input("Enter numbers Ai: ").split()
my_array = list(map(int, numbers_Ai))


X = int(input('Enter number X: '))
nearest_number = abs(X - my_array[0])
index = 0

for i in range(1, number_N):
    count = abs(X - my_array[i])
    if count < nearest_number:
        nearest_number = count
        index = i
print('->', my_array[index])