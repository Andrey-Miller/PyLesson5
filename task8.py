# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

def checkInput(str):
    while(True):
        arg = input(str)
        arg = arg.split(" ")
        if len(arg) !=3:
            print('Введены некорретные данные, повторите ввод')
        elif arg[0].isdigit() == False or arg[1].isdigit() == False or arg[2].isdigit() == False:
            print('Введены некорретные данные, повторите ввод')
        else:
            return [int(i) for i in arg]

def checkChocolate(arg):
    if arg[2] < arg[0]*arg[1] and (arg[2] % arg[0] == 0 or arg[2] % arg[1] == 0 ):
        print(f"От шолокадки {arg[0]}x{arg[1]} можно отломить {arg[2]} доли")
    else:
        print(f"От шолокадки {arg[0]}x{arg[1]} нельзя отломить {arg[2]} доли")

input = checkInput("Введи кол-во долек шоколадки n на m, и кол-во долек k, которое нужно отломить(3 числа через пробел) : ")
checkChocolate(input)

