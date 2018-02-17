import sys,webbrowser,pyperclip

sys.argv

if (len(sys.argv) > 1):
    location = ''.join(sys.argv[1:])
else:
    location = pyperclip.paste()
webbrowser.open('https://www.google.co.in/maps/place/'+location)

