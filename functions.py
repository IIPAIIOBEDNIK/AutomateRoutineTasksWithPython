import random
def hello():
    print('Hello!')
    print('Hello!!!')
    print('Привет всем.')

hello()
hello()
hello()

def hello_params(name):
    print('Привет, ' + name)

hello_params('Алиса')
hello_params('Боб')

def get_answer(answer_number):
    if answer_number == 1:
        return "It's certain"
    if answer_number == 2:
        return "It's decidedly so"
    if answer_number == 3:
        return "Yes"
    if answer_number == 4:
        return "Reply hazy try again"
    if answer_number == 5:
        return 'Ask again later'
    if answer_number == 6:
        return 'Concentrate and ask again'
    if answer_number == 7:
        return 'My reply is no'
    if answer_number == 8:
        return 'Outlook not so good'
    if answer_number == 9:
        return 'Very doubful'

r = random.randint(1, 9)
fourtune = get_answer(r)
print(fourtune)

def first():
    print('коты','собаки','мыши', sep = '; ')

first()


print('Стек вызовов')
def a():
    print('a() starts')
    b()
    d()
    print('a returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

