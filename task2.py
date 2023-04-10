# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

def checkInput(str):
    while(True):
        arg = input(str)
        if (arg.isdigit() == False) or (len(arg) != 3):
            print('Введены некорретные данные, повторите ввод')
        else:
            return arg

def sumOfDigits(num):
    return int(num[0]) + int(num[1]) + int(num[2])

input = checkInput("Введи трехзначное число: ")
print (f"Сумма цифр в числе {input} равна: {sumOfDigits(input)}")