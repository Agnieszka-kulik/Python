import pyperclip
import re

schowek = str(pyperclip.paste())

pattern = re.compile(r'>+|\.{3}')
matches = re.sub(pattern, '', schowek)

pyperclip.copy(matches)