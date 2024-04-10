todos = []

while True:
    user_action = input("Type add , show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            i = 1
            for task in todos:
                print( str(i) + " " + task)
                i = i + 1
        case 'edit':
            number = int(input("Enter the number of the todo item you want to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case 'exit':
            break

print ("Program exited!")