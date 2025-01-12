# from functions import get_todos, write_todos      # if functions are a lot, you can forget to add one of them.
import functions            # This way import is better: you don't forget to add one of many functions.
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()  # created the list with the items which are existing yet

        print('todos = ', todos, type(todos), 'hello there!')

        todos.append(todo + '\n')

        # we use our list (todos) as argument to store (write down) it in file object:
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()         # created the list with the items which are existing yet (now for case 'show')

        for index, item in enumerate(todos):
            # item = item.title()
            item = item.strip('\n')
            row = f'{index + 1}-{item}'
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)   # update the list with new items.

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            remove_todo = todos.pop(number - 1)

            functions.write_todos(todos)

            message = f'Todo "{remove_todo.strip("\n")}" was removed from the list.'
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Hey, you entered an unknown command.")

# print(todos)
print('Bye!')

