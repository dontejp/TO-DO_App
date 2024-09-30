def get_todos():
    with open('todos.txt','r') as file:                             #having to explicitly type it
        todos = file.readlines()
    return todos

while True:
    user_action = input("Type add , complete, show, edit or exit: ")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4: ]

        todos = get_todos()

 
        todos.append(todo + '\n')                                                              #adds string to a list

        with open('todos.txt','w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]                                #list comprehension makes the lines underneath quicker

        #new_todos = []

        #for item in todos:                                                              we added a new line to ensure the txt file had separations
        #    new_item = item.strip('\n')                                                 removes the new line character from the todos list
        #    new_todos.append(new_item)

        for index, task in enumerate(new_todos):
            rows = f"{index + 1}-{task}"
            print(rows)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            with open('todos.txt','w') as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid.")
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt",'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"

            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("That is not a number")
    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command")

print ("Program exited!")