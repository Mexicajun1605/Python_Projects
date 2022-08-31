#! weather checker

import pyperclip
import webbrowser, sys

if len(sys.argv) > 1:
    #Gets the city weather from the commandline
    city = ' '. join(sys.argv[1:])
else: 
    #Gets the city from the clipboard
    city = pyperclip.paste()
    
webbrowser.open('https://www.weatherbug.com/weather-forecast/10-day-weather/' + city)