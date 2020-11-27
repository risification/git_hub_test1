''' bd_username = 'ruslan'
bd_password = '12345'


def auth(tries: int):
    count = 0
    while count < tries:
        username = input('введите имя пользователя: ')
        password = input('введите пароль: ')
        if username == bd_username and password == bd_password:
            print('добро пожаловать')
            break
        else:
            print('ввели неверные данные! Попробуйте еще раз')
        count += 1


auth(3)
'''

'''def register_to_bd(username, password, check_password):
    if password == check_password:
        file1 = open('database.txt', 'w')
        result = username + "\n" + password
        file1.write(result)


register_to_bd('ruslan', '123', '123')
'''

'''file1 = open('database.txt')
list1 = file1.readlines()
my_input = input('я хочу ')
if my_input in list1:
    print('в наличии')
else:
    print('нет в наличии! На складе!')
'''

'''with open('database.txt') as file1:
    ban = 'ban_word' + '\n'
    check_ban = ''
    streamer_words = file1.readlines()
    i = 0
    while i < len(streamer_words):
        if streamer_words[i] == ban:
            check_ban = streamer_words[i]
            print(streamer_words[i], streamer_words.index(streamer_words[i]) + 1)

        i += 1
    if check_ban in streamer_words:
        print('найдено')
    else:
        print('ok')'''

'''spisok = [1, 2, 3, 4, 5, 6]
print(spisok[1:4:2])'''
