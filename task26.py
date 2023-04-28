# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def checkInput(str):
    while(True):
        arg = input(str)
        arg = arg.split(" ")
        if len(arg) !=2:
            print('Введены некорретные данные, повторите ввод')
        elif arg[0].lstrip('-').isdigit() == False or arg[1].lstrip('-').isdigit() == False:
            print('Введены некорретные данные, повторите ввод')
        else:
            return [int(i) for i in arg]
        
def power(num, pow):
    if num == 0 and pow <=0:
        print("Нельзя возвести 0 в степень меньше 1")
        quit()
    if num == 0 or num == 1:
        return num
    if pow == 1:
        return num
    if pow > 1:
        return (num * power(num, pow-1))
    if pow < 1:
        return (1 / num * power(num, pow+1))


input = checkInput("Введи число M и степень N (два целых числа через пробел): ")
print(f"{input[0]} в степени {input[1]} = {power(input[0],input[1])}")

