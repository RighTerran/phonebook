def view():
    with open('phone.txt', 'r') as file:
        print(file.read)

view()