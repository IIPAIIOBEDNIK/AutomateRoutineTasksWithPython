def first():
    name = 'Мэри'
    password = 'рыба-меч'
    if name == 'Мэри':
        print('Привет Мэри')
        if password == 'рыба-меч':
            print('Предоставлен доступ.')
        else:
            print('Неверный пароль.')

first()

def second():
    name = 'Carol'
    age = 3000
    if name == 'Alice':
        print('Hi, Alice.')
    elif age < 12:
        print('You are not Alice, kiddo.')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire.')
    elif age > 100:
        print('You are not Alice, grannie.')

second()

def third():
    spam = 0
    while spam < 5:
        print('Hello, world.')
        spam+=1

third()

def fourth():
    while True:
        print('Please type your name.')
        name = input()
        if name == 'your name':
            break
    print('Thank you!')





