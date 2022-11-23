

todos = []

while 1 < 6 :

    user_choice = input ("Type 'add' or 'show' : ")
    match user_choice :
        case 'add':
            todo = input("Enter a todo :").capitalize()
            todos.append(todo)

        case 'show' :
            print(todos)







