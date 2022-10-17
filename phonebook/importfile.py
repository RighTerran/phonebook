rfile = None

def import_file():
    global rfile
    with open('phone.txt', 'r') as file:
        rfile = file.read()

    with open('phonebook.txt', 'a') as bd:
        bd.write(rfile)
    return rfile




