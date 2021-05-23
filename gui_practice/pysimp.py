# %%
import PySimpleGUI as sg

layout = [ [sg.Text("First Name")],
          [sg.Input()],
          [sg.Button('Ok')] ]

window = sg.Window("Personal Information", layout)

event, values = window.read()

print(f'Hello {values[0]}! Thanks for the info!')

window.close()