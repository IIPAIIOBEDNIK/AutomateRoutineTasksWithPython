#Список - list
#Список - это набор значений образующих упорядоченную последовательность. Весь набор трактуется как единое значение,
# которое можно сохранить в переменной или передать в функцию.
# ['кот', 'мышь', 'крыса', 'слон']
spam = ['кот', 'мышь', 'крыса', 'слон']
print(spam)
print(type(spam))



#Доступ к элементам списка с помощью индектов
#Целое число, указываемое в квадратных скобках после имени списка, называется индексом. Первому из значений, входящих
#в список, соответствующий индекс 0, второму - индекс 1, третьему - индекс 2 и т.д.
#spam = ['кот', 'мышь', 'крыса', 'слон']
#spam[0] - 'кот', spam[1] - 'мышь', spam[2] - 'крыса', spam[3] - 'слон'
spam = ['кот', 'мышь', 'крыса', 'слон']
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print(spam[0] + ' съедает ' + spam[1] + '.')



#Если попытаться использовать индекс, значение которого превышает количество элементов в списке, будет выдано исключение
spam = ['кот', 'мышь', 'крыса', 'слон']
#print(spam[1000])



#Индексы могут иметь только целочисленные значения (не вещественные). Иначе возникает ошибка TypeError.
spam = ['кот', 'мышь', 'крыса', 'слон']
print(spam[1])
#print(spam[1.0])
print(spam[int(1.0)])



#Элементы списков сами могут быть списками. Доступ к значениям в таких вложенных списках осуществляется с помощью
# нескольких индексов
spam = [['кот', 'мышь'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])
#Первый индекс указывается, какой из вложенных списков следует использовать, а второй - к какому элементу в этом
# вложенном списке осуществляется доступ



#Отрицательные индексы
#Отрицательному значению -1 соответствует последний элемент списка, значению -2 - предпоследний и т.д.
spam = ['кот', 'мышь', 'крыса', 'слон']
print(spam[-1])
print(spam[-3])
print(spam[-1] + ' боятся ' + spam[-3] + '.')



#Получение фрагмента списка с помощью среза



























