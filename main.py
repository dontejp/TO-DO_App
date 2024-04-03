todos = []

while True:
    user_action = input("Type add , show or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for task in todos:
                print(todos)
        case 'exit':
            break
print ("Program exited!")