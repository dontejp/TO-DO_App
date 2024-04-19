todos = []

while True:
    user_action = input("Type add , complete, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, task in enumerate(todos):
                print( f"{index + 1}-{task}")
        case 'edit':
            number = int(input("Enter the number of the todo item you want to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Enter the number of the taskw you'd like to remove: "))
            todos.pop(number-1)

        case 'exit':
            break

print ("Program exited!")