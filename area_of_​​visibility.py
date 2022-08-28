# #Локальные переменные не могут использоваться в глобальной области видимости
# def spam():
#     eggs = 31337
#
# spam()
# #print(eggs)    -  Упадет с ошибкой из-за разной области видиммости
#
# #В локальных областях видимости не могут использоваться переменные из других областей видимости
# def spam1():
#     eggs = 99
#     bacon()
#     print(eggs)
#
# def bacon():
#     ham = 101
#     eggs = 0
#
# spam1()
#
# #Глобальные переменные доступны из локальной области видимости
# def spam2():
#     print(eggs)
#
# eggs = 42
# spam2()
# print(eggs)

#Локальные и глобальные переменные с одинаковыми именами
# def spam3():
#     eggs = 'spam local'
#     print(eggs)   #Выводится строка 'spam local'
#
# def bacon():
#     eggs = 'bacon local'
#     print(eggs)   #Выводится строка 'bacon local
#     spam3()
#     print(eggs)   #Выводится строка 'bacon local'
#
# eggs = 'global'
# bacon()
# print(eggs)

#Инструкция GLOBAL
# def spam4():
#     global eggs
#     eggs = 'spam'
#
# eggs = 'global'
# spam4()
# print(eggs)

def spam():
    global eggs
    eggs = 'spam'   #Это глобальная переменная

def bacon():
    eggs = 'bacon'   #это локальная переменная

def ham():
    print(eggs)   #Это глобальная переменная

eggs = 42   #это глобальная переменная
spam()
print(eggs)




