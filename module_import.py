import random, sys, os, math

def first():
    for i in range(5):
        print(random.randint(1, 10))

first()

def second():
    while True:
        print('Введите "exit" для выхода.')
        response = input()
        if response == 'exit':
            sys.exit()
        print("Вы ввели" + response + '.')

#second()

def third():
    #Игра в угадывание чисел
    secret_number = random.randint(1, 20)
    print('Я загадал число от 1 до 20.')
    #Игроку дается 6 попыток
    for guesses_taken in range(1, 7):
        print('Угадайте число.')
        guess = int(input())

        if guess < secret_number:
            print('Я загадал большее число.')
        elif guess > secret_number:
            print('Я загадал меньшее число')
        else:
            break #Число угадано!

    if guess == secret_number:
        print('Отлично! Количество попыток: ' + str(guesses_taken) + '.')
    else:
        print('Вам не повезло. Я загадал число ' + str(secret_number))

#third()


def fourth():
    print("Камень, ножницы, бумага")
    #В этих переменных накапливается количество побед, поражений и ничьих
    wins = 0
    losses = 0
    ties = 0

    while True: #Главный цикл игры
        print('%s побед, $s поражений, $s ничьих' % [wins, losses, ties])
        while True:
            print('Выберите ход: (к)амень, (н)ожницы, (б)умага или (в)ыход')
            player_move = input()
            if player_move == 'в':
                sys.exit() #выход из проограммы
            if player_move == 'к' or player_move == 'н' or player_move == 'б':
                break #выход из цикла выбора хода
            print('Введите "к", "н", "б" или "в".')
    #Отображение выбора пользователя:
        if player_move == 'к':
            print('Камень и ...')
        if player_move == 'н':
            print('Ножницы и ...')
        if player_move == 'б':
            print('Бумага и ...')
    #Отображение выбора компьютера
        random_number = random.randint(1, 3)
        if random_number == 1:
            computer_move = 'к'
            print('Камень')
        elif random_number == 2:
            computer_move = 'н'
            print('Ножницы')
        elif random_number == 3:
            computer_move = 'б'
            print('Бумага')
    #Отображение и учет результата
        if player_move == computer_move:
            print('Ничья')
            ties += 1
        elif player_move == 'к' and computer_move == 'н':
            print('Вы выиграли!')
            wins += 1
        elif player_move == 'б' and computer_move == 'к':
            print('Вы выиграли!')
            wins += 1
        elif player_move == 'н' and computer_move == 'б':
            print('Вы выиграли!')
            wins += 1
        elif player_move == 'к' and computer_move == 'б':
            print('Вы проиграли!')
            losses += 1
        elif player_move == 'б' and computer_move == 'н':
            print('Вы проиграли!')
            losses += 1
        elif player_move == 'н' and computer_move == 'к':
            print('Вы проиграли!')
            losses += 1

fourth()















