# # Как правило, мы выполняем проверку ввода, неоднократно запрашивая данные у пользователя, пока он не введет
# # корректный текст.
# while True:
#     print('Укажите ваш возраст:')
#     age = input()
#     try:
#         age = int(age)
#     except:
#         print('Пожалуйста, введите цифры.')
#         continue
#     if age < 1:
#         print('Пожалуйста, введите положительное число.')
#         continue
#     break
# print(f'Вам {age} лет.')
# # Программа предлагает ввести возраст до тех пор, пока не будет введено правильное значение.




# # Модуль PyInputPlus
# # Модуль PyInputPlus содержит функции, аналогичные input(), которые предназначены для ввода различных типов данных:
# # чисел, дат, адресов электронной почты и т.п. Если пользователь введет недопустимое значение, например неверно
# # отформатированную дату или число за пределами допустимого диапазона, модуль PyInputPlus предложит ввести данные
# # повторно, как в приведенном выше примере. В модуле PyInputPlus реализованы и другие полезные возможности, такие
# # как ограничение количества повторных запросов или тайм-аут, если пользователь должен уложиться в определенные
# # временные рамки. Модуль PyInputPlus не является частью стандартной библиотеки Python, поэтому его нужно установить
# # отдельно с помощью утилиты pip
# #pip install --user pyinputplus
# # Чтобы проверить, корректно ли установлен модуль PyInputPlus, импортируйте его в интерактивной оболочке:
# import pyinputplus
#
# # Модуль PyInputPlus содержит несколько функций, предназначенных для обработки различных типов вводимых данных.
# # inputStr(). Аналогична встроенной функции input(), но поддерживает расширенные возможности модуля PyInputPlus.
# #   Ей можно передать пользовательскую функцию для проверки введенных данных.
# # inputNum(). Гарантирует ввод числа и возвращает значение типа int или float, в зависимости от того, содержит ли
# #   введенное число десятичную точку.
# # inputChoice(). Гарантирует выбор одного из предложенных вариантов.
# # inputMenu(). Аналогична функции inputChoice(), но отображает меню с числовыми и буквенными вариантами.
# # inputDatetime(). Гарантирует ввод значений даты и времени.
# # inputYesNo(). Гарантирует, что пользователь введет ответ "да/нет".
# # inputBool(). Аналогична функции inputYesNo(), но распознает ответ "True" или "False" и возвращает соответствующее
# #   булево значение.
# # inputEmail(). Гарантирует ввод корректного адреса электронной почты.
# # inputFilepath(). Гарантирует ввод правильного имени файла (включая путь) и может дополнительно проверять,
# #   существует ли файл с таким именем.
# # inputPassword(). Аналогична встроенной функции input(), но отображает символы * вместо вводимых символов, что
# #   позволяет безопасно вводить пароли и другую конфиденциальную информацию.


# # Эти функции автоматически выводят новый запрос до тех пор, пока не будут введены корректные данные.
# import pyinputplus as pyip
# response = pyip.inputNum()
# print(response)
# # Выражение as pyip в инструкции import избавляет от необходимости указывать pyinputplus каждый раз, когда нужно
# # вызвать функцию из этого модуля.

# # Как и в случае функции input(), функциям модуля PyInputPlus можно передать строку приглашения с помощью
# # именованного аргумента prompt.
# response = input('Введите число: ')
# print(response)
# import pyinputplus as pyip
# response = pyip.inputInt(prompt='Введите число: ')
# print(response)
# # В отличие от встроенной функции input(), функции модуля PyInputPlus имеет ряд дополнительных возможностей проверки




# # Именованные аргументы min, max, greaterThan и lessThan
# # Функции inputNum(), inputInt() и inputFloat(), которые работают с целыми числами и числами с плавающей точкой,
# # поддерживают именованные аргументы min, max, greaterThan и lessThan, с помощью которых можно задать диапазон
# # допустимых значений
# import pyinputplus as pyip
# response = pyip.inputNum('Введите число: ', min=4)
# print(response)
# response = pyip.inputNum('Введите число: ', greaterThan=4)
# print(response)
# response = pyip.inputNum('>', min=4, lessThan=6)
# print(response)
# # Это необязательные аргументы, но если они указаны, то вводимые значения не могут быть меньше аргумента min или
# # больше аргумента max(но могут быть равны им). Кроме того, вводимые значения должны быть больше, чем аргумент
# # greaterThan, и меньше, чем аргумент lessThan(т.е. они не могут быть равны им).




# # Именованный аргумент blank
# # По умолчанию ввод пустой строки не допускается, если только для аргумента blank не задано значение True.
# import pyinputplus as pyip
# response = pyip.inputNum('Введите число: ')
# print(response)
# response = pyip.inputNum(blank=True)
# print(response)
# # Используйте аргумент blank = True в том случае, когда пользователю разрешается ничего не вводить




# # Именованные аргументы limit, timeout и default
# # По умолчанию функции модуля PyInputPlus будут продолжать запрашивать у вас корректные данные бесконечно долго
# # (ну или до тех пор, пока выполняется программа). Если хотите, чтобы функция перестала запрашивать данные после
# # определенного количества попыток или по истечении определенного времени, используйте именованные аргументы limit
# # и timeout. Целочисленный аргумент limit определяет, сколько попыток будет предпринято функцией для получения
# # корректных данных, прежде чем она завершит работу, а целочисленный аргумент timeout определяет, сколько секунд
# # отведено пользователю для ввода корректных данных, прежде чем функция завершится. Если пользователь так и не
# # введет корректных данных за указанное количество попыток или отведенное время, функции сгенерируют исключение
# # RetryLimitException или TimeoutException.
# import pyinputplus as pyip
# response = pyip.inputNum('Введите число:', limit=2)
# print(response)
# response = pyip.inputNum('Введите число:', timeout=10)
# print(response)


# # Если помимо этих аргументов указан также аргумент default, функция не сгенерирует исключение, а вернет значение,
# # переданное ей с помощью этого аргумента
# import pyinputplus as pyip
# response = pyip.inputNum('Введите число: ', limit=2, default='N/A')
# print(response)
# # Вместо генерации исключения RetryLimitException, функция inputNum() возвращает строку 'N/A'




# # Именованные аргументы allowRegexes и blockRegexes
# # Указывать допустимые значения можно также с помощью регулярных выражений. Именованные аргументы allowRegexes и
# # blockRegexes позволяют задать списки регулярных выражений, определяющих, какие значения функция принимает в
# # качестве допустимых, а какие - отклоняет.
# import pyinputplus as pyip
# response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# print(response)
# response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
# print(response)
# # Конечно, эти регулярные выражения задают только буквы, которые разрешается вводить пользователю. Порядок цифр в
# # числе может оказаться неправильным, например "XVX", потому что регулярное выражение r'(I|V|X|L|C|D|M)+'
# # допускает такое число.


# # С помощью именованного аргумента blockRegexes можно также указать список регулярных выражений, которые функция
# # не будет принимать.
# import pyinputplus as pyip
# response = pyip.inputNum(blockRegexes=[r'[02468]$'])
# print(response)


# Если указать оба аргумента - и allowRegexes, и blockRegexes, - то список разрешений перекрывает список блокировок.
# Например, код разрешает ввод слов 'caterpillar', 'category', но блокирует любые другие строки, содержащие слово 'cat'.
import pyinputplus as pyip
response = pyip.inputStr('Введите текст: ', allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
print(response)




# Передача пользовательской функции проверки в функцию inputCustom()
# Можно написать функцию, реализующую требуемую логику проверки, и передать ее функции inputCustom(). Допустим,
# необходимо, чтобы пользователь ввел последовательность цифр, в сумме равных 10. Функции
# puinputplus.inputAddsUpToTen() не существует, но можно создать свою собственную функцию, которая:
# имеет один строковый аргумент (значение, введенное пользователем);
# генерирует исключение, если строка не проходит проверку;
# возвращает None (инструкция return может быть опущена), если функция inputCustom() должна вернуть строку без
# изменений;
#  возвращает значение, отличное от None, если функция inputCustom() должна вернуть строку, отличную от той, которую
#  ввел пользователь
# передается в качестве первого аргумента функции inputCustom().
# Например, можно создать пользовательскую функцию add_up_to_ten() и передать ее функцию inputCustom(). При этом
# вызов должен выглядеть как inputCustom(dd_to_ten), а не input_custom(add_to_ten()), потому что мы передаем ссылку
# на функцию add_to_ten(), а не возвращаемое ею значение.
import pyinputplus as pyip
def adds_up_to_ten(numbers):
    number_list = list(numbers)
    for i, digit in enumerate(number_list):
        number_list[i] = int(digit)
    if sum(number_list) != 10:
        raise Exception('Сумма должна быть 10, а не %s.' % (sum(number_list)))
    return int(numbers) # вернуть целое число
print(response = pyip.inputCustom(adds_up_to_ten)) # без скобок после имени
print(response)
print(response = pyip.inputCustom(adds_up_to_ten))
print(response)
