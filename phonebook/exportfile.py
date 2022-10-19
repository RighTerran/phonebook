rfile = None

def export_file():
    global rfile
    with open('phonebook.txt', 'r', encoding='utf-8') as bd:
        rfile = bd.readlines()
    print('Выбрать тип файла:\n\t 1. ТХТ\n\t 2. CSV\n', end='')
    choise = input('Ваш выбор: ')
    if choise == '1':
        extension ='.txt'
    elif choise == '2':
        extension ='.csv'
        rfile = [i.replace(' ', '; ') for i in rfile]   # перевод в формат csv
    fname = input('Введите имя файла: ')
    fname += extension

    with open(fname, 'a', encoding='utf-8') as new_file:
        new_file.writelines(rfile)

    return rfile