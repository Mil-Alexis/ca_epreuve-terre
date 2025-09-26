import sys

alphabet = ""
arguments = sys.argv
numberArguments = len(arguments)
firstArgument = argument[1]
numberCharacter = len(firstArgument)


if(numberArgument >= 3):
	sys.exit("Veuillez ne donner qu'un seul argument")

if (numberCharacter == 0 or numberCharacter >= 2):
	sys.exit("Veuillez donner une seule lettre")

firstLetter = ord(firstArgument)
lastLetter = ord("z")

if firstLetter <= 97 and lastLetter:
	sys.exit("Merci de donner une lettre de l'alphabet en minuscule!")

for i in range(firstLetter, lastLetter + 1):
	alphabet = alphabet + chr(i)

print(alphabet)