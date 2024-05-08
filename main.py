while True:
    user_action = input("Type add , complete, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"                                           #adding \n to input allows .txt file to

            with open('todos.txt','r') as file:                                             #with context manager allows us to open and close file without
                todos = file.readlines()                                                    #having to explicitly type it

            todos.append(todo)                                                              #adds string to a list

            with open('todos.txt','w') as file:
                file.writelines(todos)

        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todos = [item.strip('\n') for item in todos]                                #list comprehension makes the lines underneath quicker

            #new_todos = []

            #for item in todos:                                                              we added a new line to ensure the txt file had separations
            #    new_item = item.strip('\n')                                                 removes the new line character from the todos list
            #    new_todos.append(new_item)

            for index, task in enumerate(new_todos):
                rows = f"{index + 1}-{task}"
                print(rows)
        case 'edit':
            number = int(input("Enter the number of the todo item you want to edit: "))
            number = number - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            print('Here is todos exiting', todos)

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            print('Here is how it will be', todos)

            with open('todos.txt','w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Enter the number of the task you'd like to remove: "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt",'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"

            print(message)
        case 'exit':
            break

print ("Program exited!")