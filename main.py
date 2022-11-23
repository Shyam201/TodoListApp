#while loop to run programme until user advises to stop

while True:

#Asking user's choice

    user_choice = input("Type 'add' or 'show' or 'exit' or 'edit' or 'complete' : ")

#Using match-case to identify user's choice

    match user_choice:

        #add item
        case 'add':
            todo = input("Enter a todo :").capitalize() + "\n"

            #adding  to file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            #adding new items to file without overriding
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        # show the complte todo list
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        #to edit the todo list
        case 'edit':
            index = int(input("enter the number of the todo to edit :"))
            index = index - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo :")
            todos[index] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)



        #to show complete list with indexes
        case 'complete':
            number = int(input("Number of the todo to complete :"))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"This Todo {todo_to_remove} was removed from the list"
            print(message)

        #to end the programme
        case 'exit':
            break

        case _:
            print("Sorry you entered wrong command. Please check your input !!!!")

print("Bye...")







