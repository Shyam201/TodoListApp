#while loop to run programme until user advises to stop

while True:

#Asking user's choice

    user_choice = input("Type 'add' or 'show' or 'exit' or 'edit' or 'complete' : ")

#Using match-case to identify user's choice

    match user_choice:

        #add item
        case 'add':
            todo = input("Enter a todo :").capitalize() + "\n"

            #adding todo items to file.txt

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            #adding new items to file without overriding

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        # show the complte todo list
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)

        #to edit the todo list
        case 'edit':
            index = int(input("enter the number of the todo to edit :"))
            index = index - 1
            index_item = todos[index]
            print(f"You are going to edit {index_item}")
            new_todo = input("Enter new todo :")
            todos[index] = new_todo

        #to show complete list with indexes
        case 'complete':
            number = int(input("Number of the todo to complete :"))
            todos.pop(number - 1)

        #to end the programme
        case 'exit':
            break

        case _:
            print("Sorry you entered wrong command. Please check your input !!!!")

print("Bye...")







