import function
import FreeSimpleGUI as sg

label = sg.Text("Enter Todo")
box1 = sg.InputText(tooltip="enter your todo")
button = sg.Button("add")
window = sg.Window("To Do List", layout=[[label], [box1, button]])
window.read()
window.close()