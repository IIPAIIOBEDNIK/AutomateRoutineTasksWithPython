# # Строковые литералы
# # Строки в Python начинаются и заканчиваются одинарными кавычками. Но как быть, если кавычка стоит в самой строке?
# # Вводить строки вида 'That is Alice's cat.' нельзя, поскольку Python интерпретируется апостроф как закрывающую
# # кавычку, и оставшаяся часть текста(s cat.') будет воспринята как недопустимый код.
#
#
# # Двойные кавычки
# # Начало и конец строки можно обозначать не только одинарными, но и двойными кавычками. Преимущество двойных кавычек
# # в том, что они позволяют трактовать одинарные кавычки как апостроф.
# spam = "That is Alice's cat"
# # Поскольку строка начинается с двойной кавычки, Python считает одинарную кавычку апострофом в составе строки и не
# # помечает оставшийся текст как ошибочный. Если же в строке нужны одинарные, так и двойные кавычки, то необходимо
# # прибегнуть к экранированию символов.
#
#
# # Экранирование символов
# # Благодаря экранированию в строке можно использовать символы, вставить которые по-другому невозможно. Экранированный
# # символ предваряется обратной косой чертой(\), за которой следует сам символ, добавляемый в строку.
# spam = 'Say hi to Bob\'s mother.'
# # \'    Одинарная кавычка(апостроф)
# # \"    Двойная кавычка
# # \t    Табуляция
# # \n    Новая строка(разрыв строки)
# # \\    Обратная косая черта
#
# print("Hello there!\nHow are you?\nI\'m doing fine.")
#
#
# # Необработанные строки
# # Поместив символ r перед открывающей кавычкой, вы помечаете строку как необработанную. В такой строке экранирование
# # полностью игнорируется, поэтому на экран выводятся все символы обратной косой черты, которые встречаются в строке.
# print(r'That is Carol\'s cat')
# # Поскольку это необработанная строка, Python считает все символы обратной косой черты ее частью, а не началом
# # экранированного символа. Такая возможность удобна в тех случаях, когда вводятся строки, содержащие множество
# # символов обратной косой черты.
#
#
# # Многострочные текстовые блоки с тройными кавычками
# # Несмотря на то, что в строку всегда можно добавить экранированный символ новой строки(\n), во многих случаях
# # удобнее использовать многострочные блоки. В Python многострочный текст представляет собой группу строк, заключенных
# # в тройные кавычки (три одинарные или двойные). Любые кавычки, табуляции или символы новой строки в блоке,
# # ограниченном тройными кавычками, считаются частью строки. Правила Python, регламентирующие форматирование блоков
# # кода с помощью отступов, в отношении многострочных блоков не действуют.
# print('''Dear Alice,
#
# Eve's cat has been arrested for catnapping, cat burglary, and extortion.
#
# Sincerely,
# Bob''')
#
# # Обратите внимание на то, что для апострофа в слове Eve's не понадобилось экранирование. В многострочных блоках
# # экранировать одинарные и двойные кавычки необязательно.
# print('Dear Alice, \n\nEve\'s cat has been arrested for catnapping, cat burglary,\nand extortion.\n\nSincerely, '
#       '\nBob')
#
#
# # Индексирование строк и извлечение срезов
# # В случае строк операции индексирования и извлечения срезов выполняются точно так же, как и в случае списков.
# # Например, строку 'Hello, world!' можно рассматривать как список, в котором каждый символ имеет соответствующий
# # индекс.
# spam = 'Hello, world!'
# print(spam[0])
# print(spam[4])
# print(spam[-1])
# print(spam[0:5])
# print(spam[:5])
# print(spam[7:])
# # Указав индекс, вы получаете символ, находящийся в соответствующей позиции строки. В случае диапазона индексов, т.е.
# # среза, элемент с начальным индексом включается в срез, а элемент с конечным индексом - нет.
# # Имеется ввиду, что операция создания среза не сопровождается изменением исходной строки. Срез, извлеченный из одной
# # переменной, можно сохранить в другой переменной.
# spam = 'Hello, world'
# fizz = spam[0:5]
# print(fizz)


# # Использование операторов in и not in со строками
# # Операторы in и not in применяются к строкам точно так же, как и к спискам. Результатом операции будет булево
# # значение True или False.
# print('Hello' in 'Hello, World')
# print('Hello' in 'Hello')
# print('HELLO' in 'Hello, World')
# print('' in 'spam')
# print('cats' not in 'cats and dogs')
# # В этих выражениях проверяется, содержится ли первая строка во второй строке(с учетом регистра)


# # Вставка строк в другие строки
# # В программах часто приходится вставлять строки в другие строки. До сих пор мы применялидля этого оператор +,
# # выполняющий конкатенацию строк.
# name = 'Эл'
# age = 4000
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет.')


# # Более простой способ - строковая интерполяция(подстановка), при которой оператор %s внутри строки действует как
# # маркер, который следует заменить значениями, указанными после строки. Одно из преимуществ интерполяции заключается
# # в том, что нет необходимости вызывать функцию str() для преобразования чисел в строки.
# name = 'Эл'
# age = 4000
# print('Меня зовут %s. Мне %s лет.' % (name, age))
#
# # В Python 3.6 появились f-строки, имеющие аналогичное назначение, за исключением того, что вместо оператора %s в
# # строку включаются выражения в фигурных скобках. Подобно необработанным строкам, f-строки предваряются префиксом f
# # перед открывающей кавычкой.
# name = 'Эл'
# age = 4000
# print(f'Меня зовут {name}. В следующем году мне будет {age + 1}.')
#
# # Не забывайте добавлять префикс f, в противном случае фигурные скобки и их содержимое станут частью строки
# print('Меня зовут {name}. В следующем году мне будет {age + 1}.')




# # Полезные методы для работы со строками.
# # Существует целый ряд методов, позволяющих анализировать строки и выполнять над ними различные преобразования.
#
#
# # Методы upper(), lower(), isupper() и islower()
# # Методы upper() и lower() возвращают новую строку, в которой все буквы исходной строки преобразованы соответственно
# # в верхний или нижний регистр. Небуквенные символы не затрагиваются.
# spam = 'Здравствуй, мир!'
# spam = spam.upper()
# print(spam)
#
# spam = spam.lower()
# print(spam)
#
# # Имейте в виду, что эти методы возвращают новые строковые значения, не изменяя исходную строку. Чтобы изменить саму
# # строку, необходимо вызвать для нее метод upper() или lower() и присвоить результат той же переменной, в которой
# # хранилась исходная строка.
# print('Как дела?')
# feeling = input()
# if feeling.lower() == 'отлично':
#     print('Я тоже чувствую себя отлично.')
# else:
#     print('Я надеюсь, что остаток дня будет лучше.')

# Методы isupper() и islower() возвращают булево значение True, если в строке имеется хотя бы одна буква и все
# буквы записаны соответственно в верхнем или нижнем регистре. В противном случае возвращается значение False.
spam = 'Здравствуй, мир!'
print(spam.islower())
print(spam.isupper())
print('ПРИВЕТ'.isupper())
print('abc12345'.islower())
print('12345'.islower())
print('12345'.isupper())


# Поскольку методы upper() и lower() сами возвращают строки, для этих строк тоже можно вызвать строковые методы.
# Соответствующие выражения выглядят как цепочки вызовов.
print('Привет'.upper())
print('Привет'.upper().lower())
print('Привет'.upper().lower().upper())
print('ПРИВЕТ'.lower())
print('ПРИВЕТ'.lower().islower())




# Строковые методы isX()







































