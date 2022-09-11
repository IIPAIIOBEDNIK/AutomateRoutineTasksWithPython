# Строковые литералы
# Строки в Python начинаются и заканчиваются одинарными кавычками. Но как быть, если кавычка стоит в самой строке?
# Вводить строки вида 'That is Alice's cat.' нельзя, поскольку Python интерпретируется апостроф как закрывающую
# кавычку, и оставшаяся часть текста(s cat.') будет воспринята как недопустимый код.


# Двойные кавычки
# Начало и конец строки можно обозначать не только одинарными, но и двойными кавычками. Преимущество двойных кавычек
# в том, что они позволяют трактовать одинарные кавычки как апостроф.
spam = "That is Alice's cat"
# Поскольку строка начинается с двойной кавычки, Python считает одинарную кавычку апострофом в составе строки и не
# помечает оставшийся текст как ошибочный. Если же в строке нужны одинарные, так и двойные кавычки, то необходимо
# прибегнуть к экранированию символов.


# Экранирование символов
# Благодаря экранированию в строке можно использовать символы, вставить которые по-другому невозможно. Экранированный
# символ предваряется обратной косой чертой(\), за которой следует сам символ, добавляемый в строку.
spam = 'Say hi to Bob\'s mother.'
# \'    Одинарная кавычка(апостроф)
# \"    Двойная кавычка
# \t    Табуляция
# \n    Новая строка(разрыв строки)
# \\    Обратная косая черта

print("Hello there!\nHow are you?\nI\'m doing fine.")


# Необработанные строки
# Поместив символ r перед открывающей кавычкой, вы помечаете строку как необработанную. В такой строке экранирование
# полностью игнорируется, поэтому на экран выводятся все символы обратной косой черты, которые встречаются в строке.
print(r'That is Carol\'s cat')
# Поскольку это необработанная строка, Python считает все символы обратной косой черты ее частью, а не началом
# экранированного символа. Такая возможность удобна в тех случаях, когда вводятся строки, содержащие множество
# символов обратной косой черты.


# Многострочные текстовые блоки с тройными кавычками
# Несмотря на то, что в строку всегда можно добавить экранированный символ новой строки(\n), во многих случаях
# удобнее использовать многострочные блоки. В Python многострочный текст представляет собой группу строк, заключенных
# в тройные кавычки (три одинарные или двойные). Любые кавычки, табуляции или символы новой строки в блоке,
# ограниченном тройными кавычками, считаются частью строки. Правила Python, регламентирующие форматирование блоков
# кода с помощью отступов, в отношении многострочных блоков не действуют.
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# Обратите внимание на то, что для апострофа в слове Eve's не понадобилось экранирование. В многострочных блоках
# экранировать одинарные и двойные кавычки необязательно.
print('Dear Alice, \n\nEve\'s cat has been arrested for catnapping, cat burglary,\nand extortion.\n\nSincerely, '
      '\nBob')


# Многострочные комментарии










































































