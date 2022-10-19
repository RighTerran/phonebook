rfile = None

def import_file():
    global rfile
    with open('phone.txt', 'r') as file:
        rfile = file.readlines()

    with open('phonebook.txt', 'a') as bd:
        bd.writelines('\n')
        bd.writelines(rfile)




