import sys

arguments = sys.argv[1:]

if len(arguments) > 1:
    sys.exit("Merci de ne founir qu'un seul argument")

if not arguments[0].isnumeric():
    sys.exit("Merci de saisir un nombre")

number = int(arguments[0])

hasSquareRoot = False

for squareRoot in range(number):
    if squareRoot * squareRoot == number:
        hasSquareRoot = True
        print(squareRoot)
        break

if  hasSquareRoot == False:
    print("Aucune racine carré")
