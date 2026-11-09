import FreeSimpleGUI as sg

label1 = sg.Text("Select files for compress:")
box1 = sg.Input()
button_select1 = sg.FileBrowse("choose")

label2 = sg.Text("Select destinaton folder:")
box2 = sg.Input()
button_select2 = sg.FolderBrowse("choose")

compress_button = sg.Button("compress")

window = sg.Window("Compress File", layout=[[label1, box1, button_select1], [label2, box2, button_select2], [compress_button]])
window.read()
window.close()