

todos = []

while 1 < 6:

    user_choice = input("Type 'add' or 'show' or 'exit' or 'edit' or 'complete' : ")

    match user_choice:
        case 'add':
            todo = input("Enter a todo :").capitalize()
            todos.append(todo)

        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            index = int(input("enter the number of the todo to edit :"))

            index = index - 1
            index_item = todos[index]
            print(f"You are going to edit {index_item}")
            new_todo = input("Enter new todo :")
            todos[index] = new_todo

        case 'complete':
            number = int(input("Number of the todo to complete :"))
            todos.pop(number - 1)


        case 'exit':
            break

        case _:
            print("Sorry you entered wrong command. Please check your input !!!!")

print("Bye...")







