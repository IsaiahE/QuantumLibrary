import pypimplegui as sg

layout = [[sg.Text('Hello')], [sg.Button('OK')]]

# Create the Window
window = sg.Window("Demo", layout)

# Create even loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()
