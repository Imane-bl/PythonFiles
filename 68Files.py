# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open("C:\Users\Hp_Bell\Videos\TempletePython\FilesPython\\osama.txt", "a")
myFile.truncate(5)

myFile = open("C:\Users\Hp_Bell\Videos\TempletePython\FilesPython\\osama.txt", "a")
print(myFile.tell())

myFile = open("C:\Users\Hp_Bell\Videos\TempletePython\FilesPython\\osama.txt", "r")
myFile.seek(11)
print(myFile.read())

os.remove("C:\Users\Hp_Bell\Videos\TempletePython\FilesPython\\osama.txt")