# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

myFile = open("C:\Users\Hp_Bell\Videos\TempletePython\FilesPython\osama.txt", "w")
myFile.write("Hello\n")
myFile.write("Third Line")

myFile = open(r"C:\Users\Hp_Bell\Videos\TempletePython\FilesPython\fun.txt", "w")
myFile.write("Elzero Web School\n" * 1000)

myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

myFile = open("C:\Users\Hp_Bell\Videos\TempletePython\FilesPython\\osama.txt", "w")
myFile.writelines(myList)

myFile = open("C:\Users\Hp_Bell\Videos\TempletePython\FilesPython\\osama.txt", "a")
myFile.write("Elzero")