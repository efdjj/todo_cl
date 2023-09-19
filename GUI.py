import PySimpleGUI as gu
label = gu.Text("Type in a to-do")
input_box = gu.InputText(tooltip="Enter todo")
add_button = gu.Button("Add")

window = gu.Window("To_Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()