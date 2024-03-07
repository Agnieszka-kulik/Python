#! python3
#C:\Users\Dell\Desktop\Agnieszka\python\utomatyzacjs_ks\wyszukiwanie_numeru_telefonu_lub_maila_ze_schowka.py

import pyperclip
import re

num_tel = re.compile(r'''(\+\d*|00\d*)? #numer kierunkowy, np +48, +420, 0048
                          (\s|-)?            #spacja pomiędzy
                          (\d{3})
                          (\s|-)            #spacja pomiędzy
                          (\d{3})
                          (\s|-)            #spacja pomiędzy
                          (\d{3})''',re.VERBOSE)
adres_mail = re.compile(r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''',re.VERBOSE) #adres e-mail

schowek = str(pyperclip.paste())
matches = []

for groups in num_tel.findall(schowek):
    numer = '-'.join([groups[2],groups[4],groups[6]])
    matches.append(numer)

for groups in adres_mail.findall(schowek):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("skopiowano do schowka")
    print('\n'.join(matches))
else:
    print("Nie ma żadnego numeru tel. ani maila")



#pyperclip.paste(tel_lub_mail)