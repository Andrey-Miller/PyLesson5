# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


size = int(input("Введи кол-во элементов в массиве: ")) # ЗАЧЕМ ВВОДИТЬ РАЗМЕР МАССИВА, ЕСЛИ ДАЛЕЕ ВВОДИМ МАССИВ С КЛАВИАТУРЫ?
array = tuple(int(i) for i in input("Введи элементы массива(через пробел): ").split(" "))
elem = int(input("Введи искомое число: "))
count = 0
for i in array:
    if i==elem:
        count+=1
print(f"Число {elem} встречается в массиве {array} - {count} раз")