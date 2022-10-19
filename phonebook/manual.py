snm = None
def manual():
    global snm
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    middlename = input('Введите отчество: ')
    tel = input('Введите телефон: ')
    comment = input('Комментарий: ')
    # snm = surname+'\t'+name+'\t'+middlename+'\t'+tel+'\t'+type
    #
    # with open('phonebook.txt', 'a', encoding='utf-8') as bd:
    #     bd.writelines('\n')
    #     bd.writelines(snm)

    print('Выберите формат записи данных: \n \t 1 - в строку \n \t 2 - в столбик')
    st = input('Ваш выбор: ')
    if st == '1':
        with open('phonebook.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n {surname} {name} {middlename} {tel} {comment}\n')
    if st == '2':
        with open('phonebook.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n\n {surname}\n\n {name}\n\n {middlename}\n\n {tel}\n\n {comment}')