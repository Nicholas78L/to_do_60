import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button('Add')

list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
print('type(list_box) = ', type(list_box))
# где enable_events=True -> отображает в поле input_box выбранное в listbox дело (to_do), кот. будем редактировать
edit_button = sg.Button('Edit')
complite_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complite_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    # read() method displays the window on the screen of our computer
    event, values = window.read()
    # window.read() -> return the tuple(string, dictionary),
    # где string - это name_of_button или key_of_listbox,
    # a dictionary -> {key_of_inputText: added to_do, key_of_listbox: chosen to_do to edit})
    print(1, 'event = ', event)
    print(2, 'values = ', values)
    print(3, 'values = ', values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()       # get the current todos list
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)       # rewrite the todos in todos_store.txt
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]   # existing todo
            new_todo = values['todo']    # new todo
            # print('todo_to_edit = ', todo_to_edit)

            todos = functions.get_todos()       # get the current todos list
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)       # rewrite the todos in todos_store.txt
            window['todos'].update(values=todos)
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()       # get the current todos list
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Exit':
            break   # The case is when we press the exit_button on the window (when we try to close the window this way)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED: # The case is when we press the red button on the window (when we try to close the window)
            break

window.close()
