import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button('Add')

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()   # read() method displays the window on the screen of our computer
window.close()
