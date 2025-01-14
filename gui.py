import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button('Add')

list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))
while True:
    # read() method displays the window on the screen of our computer
    event, values = window.read()   # return the tuple(name_of_button, dictionary_{key_from_inputText: message})
    print(1, 'event = ', event)
    print(2, 'values = ', values)
    print(3, 'values = ', values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]   # existing todo
            new_todo = values['todo']    # new todo
            # print('todo_to_edit = ', todo_to_edit)

            todos = functions.get_todos()       # get the current todos
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED: # The case is when we press the red button on the window (when we try to close the window)
            break

window.close()
