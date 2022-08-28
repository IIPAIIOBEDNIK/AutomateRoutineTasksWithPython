# def spam(divideBy):
#     return 42 / divideBy
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

#Ошибки можно обрабатывать с помощью инструкции try и except. Если в определенном фрагменте программы потенциально
#может возникнуть ошибка, следует поместить этот код в блок try. В случае возникновения ошибки выполнения в начало
#блока except
# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except:
#         print('Error: Invalid argument')
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# def spam(divideBy):
#     return 42 / divideBy
#
# try:
#     print(spam(2))
#     print(spam(12))
#     print(spam(0))
#     print(spam(1))
# except ZeroDivisionError:
#     print('Error: Invalid argument')

import time, sys
indent = 0
indent_increasing = True

try:
    while True:   #Главный цикл программы
        print(' ', indent, end='')
        print('********')
        time.sleep(0.1)   #пауза длительностью 1/10 секунды

        if indent_increasing:
            #Увеличение количества пробелов
            indent += 1
            if indent == 20:
                #Изменение направления
                indent_increasing = False
        else:
            #Уменьшение количества пробелов
            indent -= 1
            if indent == 0:
                #Изменение направления
                indent_increasing = True

except KeyboardInterrupt:
    sys.exit()









