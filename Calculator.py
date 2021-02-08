# Calculator

# Imports
import PySimpleGUI as sg
import os, sys, re
ans = 0

# Sets the theme of the GUI
sg.theme('DarkPurple2')

# Variable initilization
CalculatorString = ""
prevAns = 0
buttonSize = (4,2)
borderWidth = 3

calcEvents = ["1","2","3","4","5","6","7","8","9","0",".","=","ANS","DEL","AC","+","-","/","*"]

# Main Layout
layout = [
    [sg.Frame("Calculator",[[sg.Text("",key="-FRAMETEXT-",auto_size_text=True,size=(30,1), text_color="Violet")]],size=(50,1), title_color="Violet",key="-FRAME-")],
    [sg.Button("1", enable_events=True,size=buttonSize,border_width=borderWidth),sg.Button("2", enable_events=True,size=buttonSize,border_width=borderWidth),sg.Button("3", enable_events=True,size=buttonSize,border_width=borderWidth),sg.Button("DEL", button_color=("white", "dark red"), enable_events=True, size=buttonSize,border_width=borderWidth),sg.Button("AC", button_color=("white", "dark red"), enable_events=True, size=buttonSize,border_width=borderWidth)],
    [sg.Button("4", enable_events=True,size=buttonSize,border_width=borderWidth),sg.Button("5", enable_events=True,size=buttonSize,border_width=borderWidth),sg.Button("6", enable_events=True,size=buttonSize,border_width=borderWidth),sg.Button("*", enable_events=True, size=buttonSize,border_width=borderWidth),sg.Button("/", enable_events=True, size=buttonSize,border_width=borderWidth)],
    [sg.Button("7", enable_events=True,size=buttonSize,border_width=borderWidth),sg.Button("8", enable_events=True,size=buttonSize,border_width=borderWidth),sg.Button("9", enable_events=True,size=buttonSize,border_width=borderWidth),sg.Button("-", enable_events=True, size=buttonSize,border_width=borderWidth),sg.Button("+", enable_events=True, size=buttonSize,border_width=borderWidth)],
    [sg.Button("0", enable_events=True,size=(11,2),border_width=borderWidth),sg.Button(".", enable_events=True,size=buttonSize,border_width=borderWidth),sg.Button("=", enable_events=True,size=buttonSize,border_width=borderWidth, bind_return_key=True),sg.Button("ANS", enable_events=True, size=buttonSize,border_width=borderWidth)]
]

# Window Creation
window = sg.Window("Calculator by Embat", return_keyboard_events=True, layout=layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event in calcEvents and (event != "=" and event != "DEL" and event != "AC") and len(CalculatorString) < 34:
        CalculatorString = f"{CalculatorString}{event}"
        window["-FRAMETEXT-"].update(CalculatorString)
    elif event == "=":
        if CalculatorString == "":
            continue
        try:
            ans = eval(CalculatorString.replace("ANS", str(prevAns)))
        except Exception as e:
            exc_type = re.sub(r"(\w)([A-Z])", r"\1 \2", sys.exc_info()[0].__name__)
            window["-FRAMETEXT-"].update(exc_type.upper())
            CalculatorString = ""
            continue
        ans = str(ans).removesuffix(".0") if str(ans).endswith(".0") else ans
        if len(str(ans)) >= 34:
            window["-FRAMETEXT-"].update("Math Error".upper())
            CalculatorString = ""
            continue
        window["-FRAMETEXT-"].update(ans)
        prevAns = int(ans)
        CalculatorString = "ANS"
    elif (event == "DEL" or event == "BackSpace:8") and len(CalculatorString) > 0:
        CalculatorString = CalculatorString[:len(CalculatorString)-1] if not CalculatorString[len(CalculatorString)-1].isalpha() else CalculatorString[:len(CalculatorString)-3]
        window["-FRAMETEXT-"].update(CalculatorString)
    elif event == "AC" or event == "Delete:46":
        CalculatorString = ""
        window["-FRAMETEXT-"].update(CalculatorString)
