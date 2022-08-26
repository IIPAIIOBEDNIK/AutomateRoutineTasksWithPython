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

#fourth()

def fifth():
    while True:
        print('Who are you?')
        name = input()
        if name != 'Alex':
            continue
        print("Hello, Alex. What's the password? (It's a fish.)")
        password = input()
        if password == 'swordfish':
            break
    print('Access granted')

#fifth()

def sixth():
    print('My name is')
    for i in range (5):
        print("Jimmy Five Times (" + str(i) + ")")

sixth()

def seventh():
    total = 0
    for num in range (101):
        total += num
    print(total)

seventh()

def eight():
    for i in range(12, 16):
        print(i)

eight()

def ninth():
    for i in range(0, 10,2):
        print(i)

ninth()

def tenth():
    for i in range(5, -1, -1):
        print(i)

tenth()
