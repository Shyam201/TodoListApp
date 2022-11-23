

todos = []

while 1 < 6:

    user_choice = input("Type 'add' or 'show' or 'exit' or 'edit' : ")

    match user_choice:
        case 'add':
            todo = input("Enter a todo :").capitalize()
            todos.append(todo)

        case 'show':
            for item in todos:
                print(item)

        case 'edit':
            index = int(input("enter the number of the todo to edit :"))

            index = index - 1
            index_item = todos[index]
            print(f"You are going to edit {index_item}")
            new_todo = input("Enter new todo :")
            todos[index] = new_todo


        case 'exit':
            break

        case _:
            print("Sorry you entered wrong command. Please check your input !!!!")

print("Bye...")







