alphabet = ""

firstLetter = ord("a")
lastLetter = ord("z")


for i in range(firstLetter, lastLetter + 1):
	alphabet = alphabet + chr(i)

print(alphabet)