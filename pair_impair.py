import sys

arguments = sys.argv[1:]

if len(arguments) > 1:
	sys.exit("Merci de founir qu'un seul argument")

if not arguments[0].isnumeric():
	sys.exit("Merci de founir un nombre entier")

number = int(arguments[0])

isPair = False

if number % 2 == 0:
	isPair = True

print(isPair)
