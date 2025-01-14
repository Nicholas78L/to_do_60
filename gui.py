import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))
while True:
    # read() method displays the window on the screen of our computer
    event, values = window.read()   # return the tuple(name_of_button, dictionary_{key_from_inputText: message})
    print(event, values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED: # The case is when we press the red button on the window (when we try to close the window)
            break

window.close()
