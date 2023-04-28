# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4 

def checkInput(str):
    while(True):
        arg = input(str)
        arg = arg.split(" ")
        if len(arg) !=2:
            print('Введены некорретные данные, повторите ввод')
        elif arg[0].isdigit() == False or arg[1].isdigit() == False:
            print('Введены некорретные данные, повторите ввод')
        else:
            return [int(i) for i in arg]
        
def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a+1,b-1)
    
input = checkInput("Введи два целых неотрицательных числа (через пробел): ")
print(f"Сумма {input[0]} и {input[1]} равна {sum(input[0],input[1])}")
