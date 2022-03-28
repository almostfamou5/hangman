import random

file = open('word_list_rus.txt', 'r', encoding='utf-8')
content = file.read()
word_list = content.split(',')
file.close()


def get_word():
    return random.choice(word_list).strip().upper()[1:-1]


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def symbol_check():
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    while True:
        suggest = input('Введите предполагаемую букву русского алфавита: ')
        if suggest.upper() not in alphabet or len(suggest) != 1:
            print('Введите не более ОДНОЙ предполагаемой БУКВЫ РУССКОГО алфавита!: ')
            continue
        else:
            return suggest.upper()


def new_game():
    x = input('Хотите сыграть снова?\nДа(Д) или Yes(Y): ')
    return x


def play():
    used_letters = []
    guessed_letters = []
    print('Давайте играть в угадайку слов!')
    word = get_word()
    tries = 6
    print(word_completion := '_' * len(word))
    while True:
        word_completion = '_' * len(word)
        word_new = word
        guess = symbol_check()
        used_letters.append(guess)
        if used_letters.count(guess) > 1:
            print('Вы уже использовали эту букву! Попробуйте снова.: ')
            continue
        if guess in guessed_letters:
            print('Вы уже отгадали эту букву! Попробуйте снова.: ')
            continue
        if guess in word:
            guessed_letters.append(guess)
        else:
            print(f'Буквы "{guess}" нет в загаданном слове, осталось {tries} попыток, попробуйте снова!')
            tries -= 1
        for s in word:
            if s not in guessed_letters:
                word_completion = word_new.replace(s, '_', 1)
                word_new = word_completion
        if '_' not in word_new:
            print(word)
            print('Поздравляем, вы угадали слово! Вы победили!')
            x = new_game()
            if x.upper() not in ('Y', 'YES', 'ДА', 'Д'):
                break
            else:
                play()
        if tries < 0:
            print(f'Вы использовали все доступные попытки!\nБыло загадано слово "{word}".')
            x = new_game()
            if x.upper() not in ('Y', 'YES', 'ДА', 'Д'):
                break
            else:
                play()
        print(display_hangman(tries))
        print(word_completion)


play()
