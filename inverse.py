import sys

arguments = sys.argv[1:]
numberCharacter = -len(arguments[0])

if len(arguments) > 1:
	sys.exit("Veuillez ne saisir qu'un seul argument")

reverseArguments = ""

for char in range (numberCharacter, 0):
	reverseArguments = arguments[0][char] + reverseArguments

print(reverseArguments)