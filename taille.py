import sys

arguments = sys.argv[1:]

if len(arguments) > 1:
    sys.exit("Merci de ne founir qu'un seul argument")

if arguments[0].isnumeric():
    sys.exit("Merci de saisir une chaine de caractère")

stringGiven = arguments[0]

lengthString = 0

for char in stringGiven:
    lengthString = lengthString + 1

print(lengthString)