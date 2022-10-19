def view():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print(file.read())
