# # Поиск образцов текста без использования регулярных выражений
# def is_phone_number(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True
# print('415-555-4242 - это телефонный номер?')
# print(is_phone_number('415-555-4242'))
# print('Moshi moshi - это телефонный номер?')
# print(is_phone_number('Moshi moshi'))


# Поиск образцов текста с помощью регулярных выражений
# Компактное описание текстовых шаблонов можно создать с помощью регулярных выражений. Например, регулярному
# выражению \d соответствует любой цифровой символ, т.е. любая одиночная цифра от 0 до 9. Регулярное выражение
# \d\d\d-\d\d\d-\d\d\d\d позволяет находить текстовые строки того же формата. В то же время регулярные выражения
# могут быть гораздо более сложными. Например, указав 3 в фигурных скобках после шаблона({3}), мы сообщаем следующее:
# "Искать троекратное соотвествие данному шаблону". По-этому корректному телефонному номеру будет соответствовать
# корректный шаблон: \d{3}-\d{3}-\d{4}/


# # Создание объектов Regex
# # В Python все функции, предназначенные для работы с регулярными выражениями , содержатся в модуле re
# import re
#
#
# # Функция re.compile() возвращает объект Regex, соответствующий переданной строке регулярного выражения.
# phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


# Поиск соответствий объектам regex
# # Метод search() объекта Regex ищет в переданной ему строке любые совпадения с регулярным выражением. В случае
# # отсутствия совпадений возвращается значение None. Если совпадения обнаружены, то возвращается объект Match. У такого
# # объекта есть метод group(), который возвращает найденные соответствия шаблону.
# import re
# phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phone_num_regex.search('Мой номер: 415-555-4242.')
# print('Найденный номер телефона: ' + mo.group())


# Пошаговая процедура
# 1. Импортируйте модуль регулярных выражений с помощью инструкции import re
# 2. Создайте объект Regex с помощью функции re.compile(). (Ему должна быть передана необработанная строка поискового
# шаблона регулярного выражения.)
# 3. Передайте строку, в которой выполняется поиск, методу search() объекта Regex. Этот метод возвращает объект Match.
# 4. Вызовите метод group() объекта Match, чтобы получить строку, которая содержит найденный текст, соответствующий
# заданному регулярному выражению.


# # Создание групп с помощью круглых скобок
# # Предположим, вы хотите отделить код региона от остальной части телефонного номера. Добавление круглых скобок
# # приводит к созданию групп в регулярном выражении: (\d\d\d)-(\d\d\d-\d\d\d\d). Теперь можно использовать метод
# # group() объекта Match для получения текста, соответствующего только одной группе. Первый набор круглых скобок в
# # строке регулярного выражения будет группой 1, второй набор - группой 2 и т.д. Передавая целые числа 1 или 2 методу
# # group(), вы сможете отбирать различные фрагменты совпавшего текста. Если метод group вызывается с аргументом 0 или
# # вообще без аргументов, то он возвращает весь найденный текст, соответствующий шаблону.
# import re
# phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phone_num_regex.search('Мой номер: 415-555-4242')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group(0))
#
# # Если нужно извлечь сразу все группы, используйте метод groups().
# print(mo.groups())
# area_code, main_number = mo.groups()
# print(area_code)
# print(main_number)


# # Круглые скобки трактуются как спецсимволы в регулярных выражениях, но что если нужно найти в тексте сами скобки?
# # Например, в телефонных номерах круглые скобки часто используются для выделения кода региона. В таких случаях символы
# # ( и ) должны экранироваться с помощью обратной косой черты.
# import re
# phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phone_num_regex.search('Мой номер: 415-555-4242.')
# mo.group(1)
# mo.group(2)


# # Экранированные символы \( и \) в необработанной строке, передаваемой методу re.compile(), означают соответствие
# # фактическим символам круглых скобок. В регулярных выражениях следующие символы имеют специальное значение:
# # . ^ $ * + ? { } [ ] \ | ( )
# # Если требуется найти их в текстовом шаблоне, нужно экранировать их с помощью обратной косой черты:
# # \. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)


# # Выбор альтернативных групп с помощью канала
# # Символ | в регулярном выражении называется каналом(pipe). Его можно использовать, когда требуется найти
# # соответствие одному из нескольких альтернативных выражений. Например, регулярному выражению r'Юэтмен|Тина Фей'
# # будут соответствовать как строка 'Бэтмен', так и строка 'Тина Фей'. Если в тексте найдены обе эти строки, то в
# # объект Match будет записана та из них, которая встретится первой.
# import re
# hero_regex = re.compile(r'Бэтмен|Тина Фей')
# mo1 = hero_regex.search('Бэтмен и Тина Фей')
# print(mo1.group())
# mo2 = hero_regex.search('Тина Фей и Бэтмен')
# print(mo2.group())

# # Для поиска всех совпадений с шаблоном можно использовать метод findall()


# # С помощью канала удобно выбирать альтернативные варианты при поиске совпадений. Предположим, к примеру, что ищется
# # совпадение с любой из следующих строк: 'Бэтмен', 'Бэтмобиль', 'Бэткоптер' и 'Бэтбэт'. Поскольку все они начинаются
# # с 'Бэт', желательно задать префикс лишь один раз. Это можно сделать с помощью круглых скобок.
# import re
# bat_regex = re.compile(r'Бэт(мен|мобиль|коптер|бэт)')
# mo = bat_regex.search('Бэтмобиль потерял колесо')
# print(mo.group())
# print(mo.group(1))
# # Метод mo.group() возвращает весь совпавший с шаблоном текст, т.е. строку 'Бэтмобиль', тогда как метод mo.group(1)
# # возвращает лишь фрагмент совпавшего текста, соответствующий первой группе в круглых скобках, т.е. 'мобиль'.
# # Используя символ канала и группирующие скобки, можно задать несколько альтернативных шаблонов для поиска
# # соответствий с помощью единственного регулярного выражения.
# # Если требуется найти в строке сам символ канала, то его необходимо экранировать с помощью обратной косой черты: \|




# # Указание необязательной группы с помощью вопросительного знака
# # Иногда встречаются шаблоны, содержащие необязательные символы. Другими словами, регулярное выражение должно найти
# # совпадение независимо от того, содержится ли в строке определенный фрагмент текста. Символ ? означает, что
# # предшествующая ему группа представляет собой необязательную часть поискового шаблона.
# import re
# bat_regex = re.compile(r'Бэт(ву)?мен')
# mo1 = bat_regex.search('Мой герой - Бэтмен')
# mo1.group()
# mo2 = bat_regex.search('Моя героиня - Бэтвумен')
# mo2.group()
#
# # Символ ? имеет следующий смысл: "Искать соответствие тексту, в котором группа, предшествующая вопросительному
# # знаку, встречается null или один раз". Если требуется найти в строке сам вопросительный знак, то его необходимо
# # экранировать с помощью обратной косой черты \?




# # Указание группы, повторяющейся null или несколько раз, с помощью звездочки
# # Символ * (звездочка) означает "найти нулевое или большее количество экземпляров", т.е. группа, предшествующая
# # звездочке, может встречаться в тексте любое количество раз
# import re
# bat_regex = re.compile(r'Бэт(ву)*мен')
# mo1 = bat_regex.search('Мой герой - Бэтмен')
# print(mo1.group())
# mo2 = bat_regex.search('Моя героиня - Бэтвумен')
# print(mo2.group())
# mo3 = bat_regex.search('Моя героиня Бэтвувувувумен')
# print(mo3.group())




# # Указание группы, повторяющейся один или несколько раз с помощью знака "плюс"
# # Если символ * в регулярном выражении означает совпадение с нулевым или большим количеством экземпляров, то символ
# # + означает совпадение с единичным или большим количеством экземпляров. В отличие от символа *, который не требует
# # появления предшествующей ему группы в исследуемой строке, группа, предшествующая знаку +, должна появиться в
# # строке хотя бы один раз. Такая группа не является необязательной
# import re
# bat_regex = re.compile(r'Бэт(ву)+мен')
# mo1 = bat_regex.search('Моя героиня - Бэтвумен')
# print(mo1.group())
# mo2 = bat_regex.search('Моя героиня - Бэтвувувувумен')
# print(mo2.group())
# mo3 = bat_regex.search('Мой герой - Бэтмен')
# print(mo3 == None)




# # Указание количества повторений с помощью фигурных скобок
# # Если имеется группа, которая должна повторяться определенное количество раз, укажите за ней число повторений в
# # фигурных скобках. (Ha){3}
# # Вместо одного числа можно указать диапазон, записав фигурных скобках минимальное и максимальное число допустимых
# # повторений.
# # Как первое, так и второе из чисел в фигурных скобках можно опустить, оставив минимальное или максимальное
# # количество повторений неограниченным.
# import re
# ha_regex = re.compile(r'(Ha){3}')
# mo1 = ha_regex.search('HaHaHa')
# print(mo1.group())
# mo2 = ha_regex.search('Ha')
# print(mo2 == None)




# # Жадный и нежадный виды поиска
# # Регулярные выражения Python по умолчанию жадные в том смысле, что в неоднозначных ситуациях они будут пытаться
# # соответствовать как можно более длинной строке. Не жадная версия выражения с фигурными скобками, которая пытается
# # соответствовать самой короткой из возможных строк, помечается вопросительным знаком после закрывающей фигурной
# # скобки.
# import re
# greedy_ha_regex = re.compile(r'(Ha){3, 5}')
# mo1 = greedy_ha_regex.search('HaHaHaHaHa')
# print(mo1.group())
# nongreedy_ha_regex = re.compile(r'(Ha){3, 5}?')
# mo2 = nongreedy_ha_regex.search('HaHaHaHaHa')
# print(mo2.group())
# # Следует учитывать, что в регулярных выражениях вопросительный знак имеет двойное назначение: он может обозначать
# # как нежадный поиск, так и необязательную группу. Эти две его функции никак не связаны между собой.




# # Метод findall()
# # Помимо метода search(), у объектов Regex есть метод findall(). Если метод search() возвращает объект Match первого
# # совпадения, найденного в тестируемой строке, то метод findall() возвращает строки каждого из найденных совпадений.
# import re
# phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phone_num_regex.search('Мобильный: 415-555-9999 \
#                             Рабочий: 212-555-0000')
# print(mo.group())
#
#
# # В то же время метод findall() возвращает не объект Match, а список строк, если в регулярных выражениях
# # отсутствуют группы.
# import re
# phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # нет группы
# print(phone_num_regex.findall('Мобильный: 415-555-9999 \
#                         Рабочий: 212-555-0000'))
#
#
# # При наличии групп метод findall() вернет список кортежей. Каждый кортеж представляет найденное совпадение, а его
# # элементы - совпавшие строки для каждой группы в регулярном выражении.
# import re
# phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # нет группы
# print(phone_num_regex.findall('Мобильный: 415-555-9999 \
#                         Рабочий: 212-555-0000'))
#
#
# # Выжимка метода findall()
# # Будучи вызванным для регулярного выражения, не содержащего групп, например \d\d\d-\d\d\d-\d\d\d\d, метод findall()
# # возвращает список совпавших строк: ['415-555-9999', '212-555-0000']
# # Будучи вызванным для регулярного выражения, содержащего группы, например (\d\d\d)-(\d\d\d)-(\d\d\d\d), метод
# # findall() возвращает список строковых кортежей (по одной строке для каждой группы):
# # [('415', '555', '1122'), ('212', '555', '0000')]




# # Символьные классы
# # \d    Любая цифра в диапазоне от 0 до 9
# # \D    Любой символ, не являющийся цифрой в диапазоне от 0 до 9
# # \w    Любая буква, цифра или символ подчеркивания
# # \W    Любой символ, не являющийся буквой, цифрой или символом подчеркивания
# # \s    Пробел, табуляция или символ новой строки (так называемые пробельные символы)
# # \S    Любой символ, не являющийся пробелом, табуляцией или символом новой строки
# # Например, классу [0-5] будет соответствовать любая одиночная цифра в диапазоне от 0 до 5. Отметим, что не
# # существует символьного класса только для букв. Можно разве что использовать запись [azA-Z]
# import re
# xmas_regex = re.compile(r'\d+\s\w+')
# print(xmas_regex.findall('12 барабанщиков, 11 волынщиков, 10 лордов, 9 леди, 8 горничных, 7 лебедей, 6 гусей, \
#                          5 колец, 4 птицы, 3 курицы, 2 голубя, 1 куропатка'))
# # Регулярному выражению \d+\s\w+ будет соответствовать текст, содержащий одну или несколько цифр(\d+), за которыми
# # следует пробельный символ (\s), а за ним - один или несколько алфавитно-цифровых символов: буква, цифра или символ
# # подчеркивания(\w+). Метод findall() возвращает все совпавшие строки шаблона регулярного выражения в виде списка.



# # Создание собственных символьных классов
# # Иногда возникает необходимость сопоставить регулярное выражение символам из определенного набора, для которого
# # сокращенные символьные классы (\d, \w, \s т.п.) оказываются слишком широкими. В таком случае можно определить
# # собственный символьный класс, используя квадратные скобки. Например, символьному классу [aeiouAEIOU] будет
# # соответствовать любая гласная буква в нижнем или верхнем регистре.
# import re
# vowel_regex = re.compile(r'[aeiouAEIOU]')
# print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))
# # В классы можно также включать диапазоны букв и цифр, используя дефис. Например, классу [a-zA-Z0-9] будут
# # соответствовать все буквы в нижнем и верхнем регистрах, а так же цифры. Учтите, что внутри квадратных скобок
# # обычные символы регулярных выражений как таковые не интерпретируются. Это означает, что перед символами
# # ., *, ?, ( и ) не следует ставить обратную косую черту. Например, классу [0-5.] будут соответствовать
# # цифры от 0 до 5 и точка. Не следует записывать этот класс как [0-5\.]
#
#
# # Поместив сразу за открывающей квадратной скобкой символ ^, можно создать инвертированный символьный класс.
# # Такому классу будет соответствовать любой символ, не входящий в исходный класс.
# import re
# consonant_regex = re.compile(r'[^aeiouAEIOU]')
# print(consonant_regex.findall('RoboCop eats baby food. BABY FOOD.'))




# Символ ^ и знак доллара $
# Поставив в начале регулярного выражения символ ^(карет), вы тем самым указываете, что соответствие регулярному
# выражению следует искать в начале текста. Аналогичным образом знак доллара($) в конце регулярного выражения
# указывает на то, что строка должна заканчиваться данным шаблоном регулярного выражения. Можно также использовать
# символы ^ и $ совместно. Это означает, что данному регулярному выражению должна соответствовать вся строка, т.е.
# совпадения подстроки будет недостаточно.
import re
begins_with_hello = re.compile(r'^Здравствуй')
print(begins_with_hello.search('Здравствуй, мир!'))
print(begins_with_hello.search('Он сказал здравствуй.') == None)


# Регулярному выражению r'\d$' будут соответствовать строки, оканчивающиеся любой цифрой в диапазоне от 0 до 9
import re
ends_with_number = re.compile(r'\d$')
print(ends_with_number.search('Ваше число - 42'))
print(ends_with_number.search('Ваше число - срок два.') == None)


# Регулярному выражению r'^\d+$' будут соответствовать строки, которые состоят из одной или нескольких цифр.
import re
whole_string_is_num = re.compile(r'^\d+$')
print(whole_string_is_num.search('1234567890'))
print(whole_string_is_num.search('12345xyz67890') == None)
print(whole_string_is_num.search('12 34567890') == None)




# Символ подстановки





























































