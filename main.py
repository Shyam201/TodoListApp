#while loop to run programme until user advises to stop

while True:

#Asking user's choice

    user_choice = input("Type 'add' or 'show' or 'exit' or 'edit' or 'complete' : ")



    #add item
    if 'add' in user_choice:
        todo = user_choice[4:]

        #adding  to file
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        #adding new items to file without overriding
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    # show the complte todo list
    elif 'show' in user_choice:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    #to edit the todo list
    elif 'edit' in user_choice:
        index = int(user_choice[5:])
        index = index - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo :")
        todos[index] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)



    #to show complete list with indexes
    elif 'complete' in user_choice:
        number = int(user_choice[9:])

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
    elif 'exit' in user_choice:
        break

    else:
        print("Sorry you entered wrong command. Please check your input !!!!")

print("Bye...")







