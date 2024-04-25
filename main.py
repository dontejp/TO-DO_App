while True:
    user_action = input("Type add , complete, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"                                           #adding \n to input allows .txt file to

            file = open('todos.txt','r')                                                    #because writing destroys file we must save it in a list first
            todos = file.readlines()                                                        #type(file.readlines()) returns list
            file.close()                                                                    #always close file after opening

            todos.append(todo)                                                              #adds string to a list

            file = open('todos.txt', 'w')                                                   #opens .txt file ... open( 'path to file','w'|'r' )... writing destroys file and creates a new one
            file.writelines(todos)                                                          #writes the list to the txt file
            file.close()
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
            todos.pop(number - 1)

        case 'exit':
            break

print ("Program exited!")