# Список - list
# Список - это набор значений образующих упорядоченную последовательность. Весь набор трактуется как единое значение,
# которое можно сохранить в переменной или передать в функцию.
# ['кот', 'мышь', 'крыса', 'слон']
spam = ['кот', 'мышь', 'крыса', 'слон']
print(spam)
print(type(spam))



# Доступ к элементам списка с помощью индектов
# Целое число, указываемое в квадратных скобках после имени списка, называется индексом. Первому из значений, входящих
# в список, соответствующий индекс 0, второму - индекс 1, третьему - индекс 2 и т.д.
# spam = ['кот', 'мышь', 'крыса', 'слон']
# spam[0] - 'кот', spam[1] - 'мышь', spam[2] - 'крыса', spam[3] - 'слон'
spam = ['кот', 'мышь', 'крыса', 'слон']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print(spam[0] + ' съедает ' + spam[1] + '.')



# Если попытаться использовать индекс, значение которого превышает количество элементов в списке, будет выдано исключение
spam = ['кот', 'мышь', 'крыса', 'слон']
#print(spam[1000])



# Индексы могут иметь только целочисленные значения (не вещественные). Иначе возникает ошибка TypeError.
spam = ['кот', 'мышь', 'крыса', 'слон']
print(spam[1])
#print(spam[1.0])
print(spam[int(1.0)])



# Элементы списков сами могут быть списками. Доступ к значениям в таких вложенных списках осуществляется с помощью
# нескольких индексов
spam = [['кот', 'мышь'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])
# Первый индекс указывается, какой из вложенных списков следует использовать, а второй - к какому элементу в этом
# вложенном списке осуществляется доступ



# Отрицательные индексы
# Отрицательному значению -1 соответствует последний элемент списка, значению -2 - предпоследний и т.д.
spam = ['кот', 'мышь', 'крыса', 'слон']
print(spam[-1])
print(spam[-3])
print(spam[-1] + ' боятся ' + spam[-3] + '.')



# Получение фрагмента списка с помощью среза
# С помощью индексов можно извлекать из списка одиночные элементы, тогда как срезы позволяют получать сразу несколько
# значений в виде нового списка. Срез, как и индекс, обозначается в квадратных скобкахв которых указывается два индекса,
# разделенных двоеточиемм.
# spam[2] - элемент списка с указаным индексом (одно целое число)
# spam[1:4] - срез списка (два целых числа)
# Первое целое число в квадратных скобках - это индекс, с которого начинается срез. Второе целое число - это индекс, на
# котором срез заканчивается (сам индекс в срез не включается). Значением среза является новый список
spam = ['кот', 'мышь', 'крыса', 'слон']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])

# Допускается сокращенная запись среза с пропуском одного или обоих индексов по обе стороны от двоеточия. Отсутствующий
# первый индекс равносилен значению 0, т.е. соответствует началу списка. Отсутствующий второй индекс означает расширение
# среза до конца списка
spam = ['кот', 'мышь', 'крыса', 'слон']
print(spam[:2])
print(spam[1:])
print(spam[:])



# Определение длины списка с помощью функции len()
# Функция len() возвращает количество элементов в переданном ей списке, а в случае строкового значения - количество
# символов в строке
spam = ['кот', 'мышь', 'крыса', 'слон']
print(len(spam))



# Изменение элементов списка с помощью индексов
# Слева от оператора присваивания указывается имя переменной, например spam = 42. Но это может быть и элемент списка
# с заданным индексом. Например, инструкция spam[1] = 'трубкозуб'. Новое значение перезатирает старое.
spam = ['кот', 'мышь', 'крыса', 'слон']
spam[1] = 'трубкозуб'
print(spam[1])
spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)



# Конкатенация и репликация списков
# С помощью оператора + можно объединить два списка в новый список(КОНКАТЕНАЦИЯ). Оператор *, применяемый к списку и
# целому числу, позволяет продублировать список заданное количество раз
print([1, 2, 3] + ['A', 'B', 'C'])
print(['X', 'Y', 'Z'] * 3)
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)



# Удаление значений из списка с помощью инструкции del
# Инструкция del удаляет из списка элемент с заданным индексом. Все значения, находящиеся после удаленного, сдвигаются
# к началу списка на одну позицию
spam = ['кот', 'мышь', 'крыса', 'слон']
del spam[2]
print(spam)
del spam[2]
print(spam)
# Инструкция del может также удалять простые переменные. Если попытаться обратиться к удаленной переменной, будет
# получено сообщение об ошибке NameError, поскольку такой переменной больше не существует. На практике такая возможность
# требуется очень редко. Основное назначение инструкции del - удаление элементов из списков



# Работа со списками
# У новичков возникает соблазн создавать множество отдельных переменных для группы родственных значений
cat_name1 = 'Софи'
cat_name2 = 'Питер'
cat_name3 = 'Саймон'
cat_name4 = 'Леди Макбет'
cat_name5 = 'Толстяк'
cat_name6 = 'Мисс Клео'
# Если, например, количество кошек в доме изменится, программа не сможет сохранить имен больше, чем имеется переменных.
# К тому же в программах такого типа часто происходит дублирование почти идентичных фрагментов кода
# print('Укажите имя кота или кошки 1:')
# cat_name1 = input()
# print('Укажите имя кота или кошки 2:')
# cat_name2 = input()
# print('Укажите имя кота или кошки 3:')
# cat_name3 = input()
# print('Укажите имя кота или кошки 4:')
# cat_name4 = input()
# print('Укажите имя кота или кошки 5:')
# cat_name5 = input()
# print('Укажите имя кота или кошки 6:')
# cat_name6 = input()
# print('Имена котов и кошек:')
# print(cat_name1 + ' ' + cat_name2 + ' ' + cat_name3 + ' ' + cat_name4 + ' ' + cat_name5 + ' ' + cat_name6)
# Вместо множества однотипных переменных лучше использовать одну переменную - список. Ниже приведена улучшенная версия
# программы. Здесь используется всего один список, в котором может храниться любое количество имен, введенных
# пользователем.
cat_names = []
while True:
    print('Укажите имя кота или кошки ' + str(len(cat_names) + 1) + ' (<Enter> для завершения):')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]   #конкатенация списков
print('Имена котов и кошек:')
for name in cat_names:
    print(' ' + name)



# Использование циклов for со списками
# С технической точки зрения цикл for выполняет блок кода по одному разу для каждого элемента указанного списка
for i in range(4):
    print(i)
# Это происходит потому, что возвращаемое функцией range(4) значение трактуется как список: [0, 1, 2, 3].
# Поэтому предыдущий код можно переписать так
for i in [0, 1, 2, 3]:
    print(i)
#Популярный прием - использование выражения range(len(список)) в цикле for, что позволяет пройти по всем индексам
#в списке
supplies = ['ручки', 'степлеры', 'карандаши', 'скоросшиватели']
for i in range(len(supplies)):
    print('Индекс ' + str(i) + ': ' + supplies[i])
# Использовать выражение range(len(supplies)) в цикле for очень удобно, так как это дает возможность последовательно
# получить доступ ко всем индексам списка (переменная i) и к соответствующим элементам списка (выражение supplies[i]).
# Самое главное, что выражение range(len(supplies)) возвращает правильный результат независимо от количества элементов
# в списке



# Операторы in и not in
# С помощью операторов in и not in можно определить, имеется ли заданное значение в списке. Это бинарные операторы:
# слева от оператора указывается проверяемое значение, справа список, в котором оно может находиться
spam = ['привет', 'салют', 'здравствуй', 'эй']
print('здравствуй' in spam)
print('кот' in spam)
print('здравствуй' not in spam)
print('кот' not in spam)

# Рассмотрим программу, которая предлагает пользователю ввести имя своего домашнего питомца и проверяет, содержится ли
# оно в списке pets
my_pets = ['Софи', 'Питер', 'Толстяк']
print('Укажите имя домашнего питомца:')
name = input()
if name not in my_pets:
    print('У меня нет домашнего питомца по имени ' + name)
else:
    print(name + ' - мой питомец.')



# Трюк с групповым присваиванием
# Используя трюк с групповым присваиванием, можно быстро присвоить значения сразу нескольким переменным в одной
# строке кода
cat = ['толстый', 'серый', 'громкий']
size = cat[0]
color = cat[1]
disposition = cat[2]

# Ее можно переписать более компактно
cat = ['толстый', 'серый', 'громкий']
size, color, disposition = cat
print(cat)

# Количество переменных должно совпадать с длиной списка, иначе будет выдано исключение ValueError
# cat = ['толстый', 'серый', 'громкий']
# size, color, disposition, name = cat
# print(cat)



# Использование функции enumerate() со списками.
# Вместо того чтобы использовать вызов range(len(список)) в цикле for для получения целочисленных индексов элементов
# списка, можно вызвать функцию enumerate(). На каждой итерации цикла она будет возвращать два значения: индекс
# элемента в списке и сам элемент.
supplies = ['ручки', 'степлеры', 'карандаши', 'скоросшиватели']
for index, item in enumerate(supplies):
    print('Индекс' + str(index) + ': ' + item)
# Функция enumerate() полезна, если в цикле нужен как элемент списка, так и его индекс



# Использование функций random.choice() и random.shuffle() со списками
# Модуль random содержит несколько функций, которые в качестве аргументов получают списки. Функция random.choice()
# возвращает случайно выбранный элемент из списка
import random
pets = ['Собака', 'Кот', 'Лось']
print(random.choice(pets))
print(random.choice(pets))
print(random.choice(pets))

# Вызов random.choice(список) можно рассматривать как более короткую форму записи следующего выражения:
print(pets[random.randint(0, len(pets) - 1)])



# Функция random.shuffle() переупорядочивает элементы списка. Она изменяет исходный список, а не возвращает  новый.
people = ['Алиса', 'Боб', 'Кэрол', 'Дэвид']
random.shuffle(people)
print(people)
random.shuffle(people)
print(people)



# Комбинированные операторы присваивания
# spam = spam + 1 -> spam += 1
# spam = spam - 1 -> spam -= 1
# spam = spam * 1 -> spam *= 1
# spam = spam / 1 -> spam /= 1
# spam = spam % 1 -> spam %= 1










