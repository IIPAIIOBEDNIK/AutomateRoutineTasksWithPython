# # Словарь - это изменяемая коллекция значений. Однако в словарях, в отличие от списков, индексами могут
# # быть не только целые числа, но и другие типы данных. Индексы в словарях называются ключами, а ключ вместе с
# # соответствующим ему значением - парой "ключ - значение".
# # В Python словари обозначаются фигурными скобками ({})
# my_cat = {'размер': 'толстый', 'цвет': 'серый', 'характер': 'шумный'}
#
# # Доступ к значениям осуществляется с помощью ключей
# print(my_cat['размер'])
# print('У моего кота ' + my_cat['цвет'] + ' мех.')
#
# # Индексами в словарях, как и в списках, могут служить целые числа, однако их отсчет необязательно должен начинаться
# # с нуля.
# spam = {12345: 'Код замка', 42: 'Ответ'}


# # Сравнение словарей и списков
# # В отличие от списков, в словарях элементы не упорядочены. Первым элементом в списке spam был spam[0]. Однако к
# # словарям понятие первый элемент не применимо. Порядок элементов важен при проверке идентичности двух списков, но для
# # словарей не имеет значения, в каком порядке в них были включены пары "ключ - значение".
# spam = ['коты', 'собаки', 'лоси']
# bacon = ['собаки', 'лоси', 'коты']
# print(spam == bacon)
#
# eggs = {'имя': 'Софи', 'вид': 'кот', 'возраст': '8'}
# ham = {'вид': 'кот', 'возраст': '8', 'имя': 'Софи'}
# print(eggs == ham)
# # Поскольку словари не упорядочены, для них нельзя создавать срезы, в отличие от списков.


# # При попытке обратиться к ключу, отсутствующему в словаре, будет сгенерировано исключение KeyError, напоминающее
# # исключение IndexError, которое возникает при выходе за пределы допустимого диапазона индексов в списке.
# spam = {'имя': 'Софи', 'возраст': 7}
# print(spam['цвет'])


# # Несмотря на то, что словари не упорядочены, возможность извлечь произвольное значение по его ключу делает их очень
# # удобными структурами
# birthdays = {'Алиса': 'Апрель 1', 'Боб': 'Декабрь 12', 'Кэрол': 'Март 4'}
# while True:
#     print('Введите имя (<Enter> для выхода) :')
#     name = input()
#     if name == '':
#         break
#     if name in birthdays:
#         print(name + ': день рождения - ' + birthdays[name])
#     else:
#         print('Я не знаю, когда день рождения у ' + name)
#         print('Когда день рождения у этого человека?')
#         bday = input()
#         birthdays[name] = bday
#         print('Обновлена информация о днях рождения.')
# # Разумеется, по завершении работы программы все введенные вами данные теряются


# # Методы keys(), values() и items()
# # Для работы со словарями предусмотрены методы keys(), values() и items(), которые возвращают соответственно ключи,
# # значения и пары "ключ - значение". Возвращаемые этими методами коллекции не являются списками: их нельзя изменять,
# # и у них нет метода append(). В то же время эти типы данных(dict_keys, dict_values и dict_items соответственно) можно
# # использовать в циклах for.
# spam = {'цвет': 'красный', 'возраст': 42}
# for v in spam.values():
#     print(v)
#
# # Здесь цикл for проходит по всем значениям, содержащимся в словаре spam. То же самое можно сделать для ключей и пар
# # "ключ - значение"
# for k in spam.keys():
#     print(k)
#
# for i in spam.items():
#     print(i)
# # Используя методы keys(), value() и items(), можно организовать перебор ключей, значений и пар "ключ - значение"
# # соответственно. Обратите внимание на то, что значение типа dict_items, возвращаемые методом items(), представляют
# # собой кортежи образуемые ключами и связанными с ними значениями словаря.


# # Если необходимо получить результат в виде списка, передайте функции list() значение, возвращаемое любым из этих
# # трех методов
# spam = {'цвет': 'красный', 'возраст': 42}
# print(spam.keys())
# print(list(spam.keys()))
# # В строке list(spam.keys()) значение типа dict_keys(), возвращаемое функцией keys(), передается функции list(),
# # которая формирует список ['цвет', 'возраст'].


# # Кроме того, можно воспользоваться групповым присваиванием в цикле for для присваивания ключей и связанных с ними
# # значений отдельным переменным.
# spam = {'цвет': 'красный', 'возраст': 42}
# for k, v in spam.items():
#     print('Ключ: ' + k + ', значение: ' + str(v))


# # Проверка наличия ключа или значения в словаре.
# # Как вам уже известно, операторы in и not in позволяют проверить, содержится ли указанное значение в списке.
# # Эти же операторы можно использовать и для того, чтобы проверить, содержится ли в словаре заданный ключ или значение.
# spam = {'имя': 'Софи', 'возраст': 7}
# print('имя' in spam.keys())
# print('Софи' in spam.values())
# print('цвет' in spam.keys())
# print('цвет' not in spam.keys())
# print('цвет' in spam)
# # Выражение 'цвет' in spam представляет собой сокращенную запись выражения 'цвет' in spam.keys(). Это общее правило:
# # если нужно проверить, является ли данное значение ключом в словаре, то после ключевого слова in(или not in)
# # достаточно указать только имя словаря.
#
#
#
#
# # Метод get()
# # Было бы слишком утомительно каждый раз проверять наличие ключа в словаре перед обращением к нему. К счастью, для
# # словарей предусмотрен метод get(), имеющий два аргумента: ключ извлекаемого значения и значение по умолчанию,
# # возвращаемое в случае отсутствия данного ключа в словаре.
# picnicItems = {'яблоки': 5, 'чашки': 2}
# print('Я несу ' + str(picnicItems.get('чашки', 0)) + ' чашки.')
# print('Я несу ' + str(picnicItems.get('яйца', 0)) + ' яйца.')
# # Поскольку в словаре picnicItems нет ключа 'яйца', метод get() возвращает заданное по умолчанию значение 0. Если не
# # использовать метод get(), то будет сгенерирована ошибка.
# picnicItems = {'яблоки': 5, 'чашки': 2}
# print('Я несу ' + str(picnicItems('яйца')) + ' яйца.')


# # Метод setdefault()
# # Зачастую нужно установить значение для определенного ключа лишь в том случае, если этому ключу еще не присвоено
# # значение.
# spam = {'имя': 'Питер', 'возраст': 5}
# if 'цвет' not in spam:
#     spam['цвет'] = 'черный'
# # С помощью метода setdefault() то же самое можно сделать в одной строке кода. У данного метода два аргумента. Первый
# # из них - это проверяемый ключ, а второй - значение, устанавливаемое для ключа в случае его отсутствия в словаре.
# # Если же ключ существует, метод setdefault() возвращает его значение
# spam = {'имя': 'Питер', 'возраст': 5}
# spam.setdefault('цвет', 'черный')
# print(spam)
# spam.setdefault('цвет', 'белый')
# print(spam)
# # При первом вызове метод setdefault() изменяет словарь, который теперь выглядит так {'цвет': 'черный', 'возраст': 5,
# # 'имя': 'Питер'}. Метод возвращает значение 'черный', которое было назначено ключу 'цвет'. При втором вызове -
# # spam.setdefault('цвет', 'белый') - значение ключа не меняется, поскольку в словаре уже есть ключ 'цвет'
#
#
# # Метод setdefault() удобно использовать в ситуациях, когда требуется гарантировать наличие ключа. Ниже приведена
# # короткая программа, которая подсчитывает, сколько раз в строке встречается каждая из входящих в нее букв
# message = 'It was a bright cold day in April, and the clocks were striking thirteen'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# print(count)


# # Красивый вывод
# # Импортировав модуль pprint, вы получите доступ к функции pprint() и pformat(), которые обеспечивают красивый вывод
# # значений словаря. Это может понадобиться, если нужно расширить возможности функции print()
# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# print(count)


# # Функция pprint.pprint() особенно полезна в тех случаях, когда словарь содержит вложенные списки и словари. Если нужно
# # получить аккуратно оформленный текст в виде строки, а не выводить его на экран, то воспользуйтесь функцией
# # pprint.pformat(). Следующие две инструкции эквивалентны.
# pprint.pprint(someDictionaryValue)
# print(pprint.pprint(someDictionaryValue))


# # Использование структур данных для моделирования реальных объектов.
# the_board = {'top-l': '', 'top-m': '', 'top-r': '',
#              'mid-l': '', 'mid-m': '', 'mid-r': '',
#              'low-l': '', 'low-m': '', 'low-r': ''}
# # Дописать


# Вложенные словари и списки
# Моделировать игру в "крестики-нолики" относительно легко: для описания игрового поля требуется всего один словарь
# с девятью парами "ключ - значение". В более сложных играх могут потребоваться словари и списки, содержащие другие
# списки и словари. Списки удобны для хранения упорядоченных последовательностей, а словари - для сопоставления
# значений с ключами. Ниже приведена программа, в которой используются вложенные словари для описания того, что
# приносит собой каждый из гостей, приглашенных на пикник. Функция totalBrought() считывает эту структуру данных и
# вычисляет общее количество предметов, принесенных гостями.
all_guests = {'Алиса': {'яблоки': 5, 'конфеты': 12},
              'Боб': {'бутерброды': 3, 'яблоки': 2},
              'Кэрол': {'чашки': 3, 'пироги': 1},
              'Ганс': {'пироги': 4, 'яблоки': 6}}


def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
        return num_brought


print('Количество принесенных предметов:')
print(' - Яблоки ' + str(total_brought(all_guests, 'яблоки')))
print(' - Чашки ' + str(total_brought(all_guests, 'чашки')))
print(' - Булочки ' + str(total_brought(all_guests, 'булочки')))
print(' - Бутерброды ' + str(total_brought(all_guests, 'бутерброды')))
print(' - Пироги ' + str(total_brought(all_guests, 'пироги')))
# Может показаться, что эта модель слишком простая, чтобы обременять себя написанием программы для нее. Однако
# задумайтесь над тем, что функция total_brought() способна с легкостью обрабатывать словари, включающие тысячи
# гостей с тысячами различных предметов. Наличие функций для такой огромной структуры данных сохранит вам массу
# времени.










































































