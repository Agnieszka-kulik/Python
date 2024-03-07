#! python3
#otwieranie_stron_internetowych.py 

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    print("Skopiowanie adresu")
    adres = ' '.join(sys.argv[1:])
else:
    adres = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/'+ adres)
