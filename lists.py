# # Список - list
# # Список - это набор значений образующих упорядоченную последовательность. Весь набор трактуется как единое значение,
# # которое можно сохранить в переменной или передать в функцию.
# # ['кот', 'мышь', 'крыса', 'слон']
# spam = ['кот', 'мышь', 'крыса', 'слон']
# print(spam)
# print(type(spam))
#
#
#
# # Доступ к элементам списка с помощью индектов
# # Целое число, указываемое в квадратных скобках после имени списка, называется индексом. Первому из значений, входящих
# # в список, соответствующий индекс 0, второму - индекс 1, третьему - индекс 2 и т.д.
# # spam = ['кот', 'мышь', 'крыса', 'слон']
# # spam[0] - 'кот', spam[1] - 'мышь', spam[2] - 'крыса', spam[3] - 'слон'
# spam = ['кот', 'мышь', 'крыса', 'слон']
# print(spam[0])
# print(spam[1])
# print(spam[2])
# print(spam[3])
# print(spam[0] + ' съедает ' + spam[1] + '.')
#
#
#
# # Если попытаться использовать индекс, значение которого превышает количество элементов в списке, будет выдано исключение
# spam = ['кот', 'мышь', 'крыса', 'слон']
# #print(spam[1000])
#
#
#
# # Индексы могут иметь только целочисленные значения (не вещественные). Иначе возникает ошибка TypeError.
# spam = ['кот', 'мышь', 'крыса', 'слон']
# print(spam[1])
# #print(spam[1.0])
# print(spam[int(1.0)])
#
#
#
# # Элементы списков сами могут быть списками. Доступ к значениям в таких вложенных списках осуществляется с помощью
# # нескольких индексов
# spam = [['кот', 'мышь'], [10, 20, 30, 40, 50]]
# print(spam[0])
# print(spam[0][1])
# print(spam[1][4])
# # Первый индекс указывается, какой из вложенных списков следует использовать, а второй - к какому элементу в этом
# # вложенном списке осуществляется доступ
#
#
#
# # Отрицательные индексы
# # Отрицательному значению -1 соответствует последний элемент списка, значению -2 - предпоследний и т.д.
# spam = ['кот', 'мышь', 'крыса', 'слон']
# print(spam[-1])
# print(spam[-3])
# print(spam[-1] + ' боятся ' + spam[-3] + '.')
#
#
#
# # Получение фрагмента списка с помощью среза
# # С помощью индексов можно извлекать из списка одиночные элементы, тогда как срезы позволяют получать сразу несколько
# # значений в виде нового списка. Срез, как и индекс, обозначается в квадратных скобкахв которых указывается два индекса,
# # разделенных двоеточиемм.
# # spam[2] - элемент списка с указаным индексом (одно целое число)
# # spam[1:4] - срез списка (два целых числа)
# # Первое целое число в квадратных скобках - это индекс, с которого начинается срез. Второе целое число - это индекс, на
# # котором срез заканчивается (сам индекс в срез не включается). Значением среза является новый список
# spam = ['кот', 'мышь', 'крыса', 'слон']
# print(spam[0:4])
# print(spam[1:3])
# print(spam[0:-1])
#
# # Допускается сокращенная запись среза с пропуском одного или обоих индексов по обе стороны от двоеточия. Отсутствующий
# # первый индекс равносилен значению 0, т.е. соответствует началу списка. Отсутствующий второй индекс означает расширение
# # среза до конца списка
# spam = ['кот', 'мышь', 'крыса', 'слон']
# print(spam[:2])
# print(spam[1:])
# print(spam[:])
#
#
#
# # Определение длины списка с помощью функции len()
# # Функция len() возвращает количество элементов в переданном ей списке, а в случае строкового значения - количество
# # символов в строке
# spam = ['кот', 'мышь', 'крыса', 'слон']
# print(len(spam))
#
#
#
# # Изменение элементов списка с помощью индексов
# # Слева от оператора присваивания указывается имя переменной, например spam = 42. Но это может быть и элемент списка
# # с заданным индексом. Например, инструкция spam[1] = 'трубкозуб'. Новое значение перезатирает старое.
# spam = ['кот', 'мышь', 'крыса', 'слон']
# spam[1] = 'трубкозуб'
# print(spam[1])
# spam[2] = spam[1]
# print(spam)
# spam[-1] = 12345
# print(spam)
#
#
#
# # Конкатенация и репликация списков
# # С помощью оператора + можно объединить два списка в новый список(КОНКАТЕНАЦИЯ). Оператор *, применяемый к списку и
# # целому числу, позволяет продублировать список заданное количество раз
# print([1, 2, 3] + ['A', 'B', 'C'])
# print(['X', 'Y', 'Z'] * 3)
# spam = [1, 2, 3]
# spam = spam + ['A', 'B', 'C']
# print(spam)
#
#
#
# # Удаление значений из списка с помощью инструкции del
# # Инструкция del удаляет из списка элемент с заданным индексом. Все значения, находящиеся после удаленного, сдвигаются
# # к началу списка на одну позицию
# spam = ['кот', 'мышь', 'крыса', 'слон']
# del spam[2]
# print(spam)
# del spam[2]
# print(spam)
# # Инструкция del может также удалять простые переменные. Если попытаться обратиться к удаленной переменной, будет
# # получено сообщение об ошибке NameError, поскольку такой переменной больше не существует. На практике такая возможность
# # требуется очень редко. Основное назначение инструкции del - удаление элементов из списков
#
#
#
# # Работа со списками
# # У новичков возникает соблазн создавать множество отдельных переменных для группы родственных значений
# cat_name1 = 'Софи'
# cat_name2 = 'Питер'
# cat_name3 = 'Саймон'
# cat_name4 = 'Леди Макбет'
# cat_name5 = 'Толстяк'
# cat_name6 = 'Мисс Клео'
# # Если, например, количество кошек в доме изменится, программа не сможет сохранить имен больше, чем имеется переменных.
# # К тому же в программах такого типа часто происходит дублирование почти идентичных фрагментов кода
# # print('Укажите имя кота или кошки 1:')
# # cat_name1 = input()
# # print('Укажите имя кота или кошки 2:')
# # cat_name2 = input()
# # print('Укажите имя кота или кошки 3:')
# # cat_name3 = input()
# # print('Укажите имя кота или кошки 4:')
# # cat_name4 = input()
# # print('Укажите имя кота или кошки 5:')
# # cat_name5 = input()
# # print('Укажите имя кота или кошки 6:')
# # cat_name6 = input()
# # print('Имена котов и кошек:')
# # print(cat_name1 + ' ' + cat_name2 + ' ' + cat_name3 + ' ' + cat_name4 + ' ' + cat_name5 + ' ' + cat_name6)
# # Вместо множества однотипных переменных лучше использовать одну переменную - список. Ниже приведена улучшенная версия
# # программы. Здесь используется всего один список, в котором может храниться любое количество имен, введенных
# # пользователем.
# cat_names = []
# while True:
#     print('Укажите имя кота или кошки ' + str(len(cat_names) + 1) + ' (<Enter> для завершения):')
#     name = input()
#     if name == '':
#         break
#     cat_names = cat_names + [name]   #конкатенация списков
# print('Имена котов и кошек:')
# for name in cat_names:
#     print(' ' + name)
#
#
#
# # Использование циклов for со списками
# # С технической точки зрения цикл for выполняет блок кода по одному разу для каждого элемента указанного списка
# for i in range(4):
#     print(i)
# # Это происходит потому, что возвращаемое функцией range(4) значение трактуется как список: [0, 1, 2, 3].
# # Поэтому предыдущий код можно переписать так
# for i in [0, 1, 2, 3]:
#     print(i)
# #Популярный прием - использование выражения range(len(список)) в цикле for, что позволяет пройти по всем индексам
# #в списке
# supplies = ['ручки', 'степлеры', 'карандаши', 'скоросшиватели']
# for i in range(len(supplies)):
#     print('Индекс ' + str(i) + ': ' + supplies[i])
# # Использовать выражение range(len(supplies)) в цикле for очень удобно, так как это дает возможность последовательно
# # получить доступ ко всем индексам списка (переменная i) и к соответствующим элементам списка (выражение supplies[i]).
# # Самое главное, что выражение range(len(supplies)) возвращает правильный результат независимо от количества элементов
# # в списке
#
#
#
# # Операторы in и not in
# # С помощью операторов in и not in можно определить, имеется ли заданное значение в списке. Это бинарные операторы:
# # слева от оператора указывается проверяемое значение, справа список, в котором оно может находиться
# spam = ['привет', 'салют', 'здравствуй', 'эй']
# print('здравствуй' in spam)
# print('кот' in spam)
# print('здравствуй' not in spam)
# print('кот' not in spam)
#
# # Рассмотрим программу, которая предлагает пользователю ввести имя своего домашнего питомца и проверяет, содержится ли
# # оно в списке pets
# my_pets = ['Софи', 'Питер', 'Толстяк']
# print('Укажите имя домашнего питомца:')
# name = input()
# if name not in my_pets:
#     print('У меня нет домашнего питомца по имени ' + name)
# else:
#     print(name + ' - мой питомец.')
#
#
#
# # Трюк с групповым присваиванием
# # Используя трюк с групповым присваиванием, можно быстро присвоить значения сразу нескольким переменным в одной
# # строке кода
# cat = ['толстый', 'серый', 'громкий']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]
#
# # Ее можно переписать более компактно
# cat = ['толстый', 'серый', 'громкий']
# size, color, disposition = cat
# print(cat)
#
# # Количество переменных должно совпадать с длиной списка, иначе будет выдано исключение ValueError
# # cat = ['толстый', 'серый', 'громкий']
# # size, color, disposition, name = cat
# # print(cat)
#
#
#
# # Использование функции enumerate() со списками.
# # Вместо того чтобы использовать вызов range(len(список)) в цикле for для получения целочисленных индексов элементов
# # списка, можно вызвать функцию enumerate(). На каждой итерации цикла она будет возвращать два значения: индекс
# # элемента в списке и сам элемент.
# supplies = ['ручки', 'степлеры', 'карандаши', 'скоросшиватели']
# for index, item in enumerate(supplies):
#     print('Индекс' + str(index) + ': ' + item)
# # Функция enumerate() полезна, если в цикле нужен как элемент списка, так и его индекс
#
#
#
# # Использование функций random.choice() и random.shuffle() со списками
# # Модуль random содержит несколько функций, которые в качестве аргументов получают списки. Функция random.choice()
# # возвращает случайно выбранный элемент из списка
# import random
# pets = ['Собака', 'Кот', 'Лось']
# print(random.choice(pets))
# print(random.choice(pets))
# print(random.choice(pets))
#
# # Вызов random.choice(список) можно рассматривать как более короткую форму записи следующего выражения:
# print(pets[random.randint(0, len(pets) - 1)])
#
#
#
# # Функция random.shuffle() переупорядочивает элементы списка. Она изменяет исходный список, а не возвращает  новый.
# people = ['Алиса', 'Боб', 'Кэрол', 'Дэвид']
# random.shuffle(people)
# print(people)
# random.shuffle(people)
# print(people)
#
#
#
# # Комбинированные операторы присваивания
# # spam = spam + 1 -> spam += 1
# # spam = spam - 1 -> spam -= 1
# # spam = spam * 1 -> spam *= 1
# # spam = spam / 1 -> spam /= 1
# # spam = spam % 1 -> spam %= 1
#
#
#
# # Методы
# # Метод - это та же функция, с тем лишь отличием, что она вызывается для конкретного значения.
# # У каждого типа данных есть свой набор методов. В частности, для списков есть полезные методы, позволяющие искать,
# # добавлять и удалять элементы, а так же выполнять с ними другие манипуляции.
#
#
#
# # Поиск значения в списке с помощью метода index()
# # У списков есть метод index(), который возвращает индекс указанного значения при условии, что оно содержится в списке.
# # Если значение отсутствует в списке, генерируется исключение ValueError
# spam = ['привет', 'салют', 'здравствуй', 'эй']
# print(spam.index('привет'))
# print(spam.index('эй'))
# # print(spam.index('привет привет привет'))   Возникает ошибка ValueError из-за поиска отсутствующего элемента
# # При наличии дубликатов возвращается индеск первого из найденных элементов.
# spam = ['Софи', 'Питер', 'Толстяк', 'Питер']
# print(spam.index('Питер'))
#
#
#
# # Добавление значений в список с помощью методов append() и insert()
# # Метод append() добавляет элемент в конец списка
# spam = ['кот', 'собака', 'мышь']
# spam.append('лось')
# print(spam)
#
# # Метод insert() позволяет добавить в список элемент с конкретным индексом. Первый аргумент метода insert() - это индекс
# # нового элемента, а второй аргумент - вставляемое значение
# spam = ['кот', 'собака', 'мышь']
# spam.insert(1, 'курица')
# print(spam)
#
# # Методы связаны с конкретными типами данных. В частности, append() и insert() - это методы списков, которые могут
# # вызываться только в таком контексте. Вызвать их для других типов данных, например для строк или целых чисел, нельзя.
# # Иначе выпадет исключение AttributeError
#
#
#
# # Удаление значений из списка с помощью метода remove()
# # Метод remove() удаляет из списка указанное значение
# spam = ['кот', 'мышь', 'крыса', 'слон']
# spam.remove('мышь')
# print(spam)
# # При попытке удалить значение, отсутствующее в списке, будет сгенерировано исключение ValueError
# # Если в списке имеется несколько одиночных значений, будет удалено первое из них
# spam = ['кот', 'мышь', 'крыса', 'кот', 'шляпа', 'кот']
# spam.remove('кот')
# print(spam)
# # Иструкцию del удобно применять в тех случаях, когда известен индекс удаляемого значения, а метод remove() -
# # когда известно само удаляемое значение
#
#
#
# # Сортировка списка с помощью метода sort()
# # Для сортировки списков, содержащих числа или строки, применяется метод sort()
# spam = [2, 5, 3.14, 1, -7]
# spam.sort()
# print(spam)
# spam = ['муравьи', 'коты', 'собаки', 'барсуки', 'слоны']
# spam.sort()
# print(spam)
#
# # Чтобы выполнить сортировку в обратном порядке, следует передать методу sort() именованный аргумент reverse со
# # значением True
# spam.sort(reverse=True)
# print(spam)
#
# # Относительно метода sort() следует сделать три замечания:
# # Во-первых, он сортирует исходный список. Не пытайтесь использовать его в выражениях вида spam = spam.sort()
#
# # Во-вторых, невозможно отсортировать список, который содержит одновременно и числа, и строки, поскольку Python не
# # знает, как сравнивать разные типы данных.
# # spam = [1, 3, 2, 4, 'Алиса', 'Боб']
# # spam.sort()
#
# # В-третьих, метод sort() сортирует строки не в алфавитном порядке, а в соответствии с таблицей ASCII. Это означает,
# # что буквы в верхнем регистре предшествуют буквам в нижнем регистре.
# spam = ['Алиса', 'муравьи', 'Боб', 'барсуки', 'Кэрол', 'коты']
# spam.sort()
# print(spam)
#
# # Если необходимо отсортировать строку в обычном алфавитном порядке, то передайте методу sort() именованный аргумент
# # key со значением str.lower
# spam = ['а', 'я', 'А', 'Я']
# spam.sort(key=str.lower)
# print(spam)
#
#
#
# # Инверсия списка с помощью метода reverse()
# # Чтобы быстро инвертировать порядок элементов в списке, воспользуйтесь методом reverse()
# spam = ['кот', 'лось', 'собака']
# spam.reverse()
# print(spam)
# # Как и метод sort(), метод reverse() не возвращает список, поэтому необходимо писать spam.reverse(),
# # а не spam = spam.reverse().

# # Пример программы Magic 8 Ball без использования elif
# import random
# message = ['It is certaine',
#            'It is decidedly so',
#            'Yes',
#            'Reply hazy try again',
#            'Ask again later',
#            'Concentrate and ask again',
#            'My reply is no',
#            'Outlook not so good',
#            'Very doubtful']
# print(message[random.randint(0, len(message) - 1)])



# Списковые типы данных
# Список - не единственный тип данных, представляющий собой упорядоченную последовательность значений. Строки во многом
# напоминают списки, если рассматривать строку как список, состоящий из символов. К списковым типам данных относятся
# списки, строки, объекты диапазона, возвращаемые методом range(), и кортежи. Много из того, что можно делать со
# списками, можно делать и со строками, а также остальными списковыми типами. В частности, к ним применимы операции
# индексирования и получения срезов, операторы in и not in и функции наподобие len(). Также они могут использоваться в
# циклах for
name = 'Сократ'
print(name[0])
print(name[-2])
print(name[0:4])
print('Со' in name)
print('с' in name)
print('а' not in name)
for i in name:
    print('* * * ' + i + ' * * *')



# Изменяемые и неизменяемые типы данных
#












