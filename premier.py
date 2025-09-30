import sys

arguments = sys.argv[1:]

if len(arguments) > 1:
    sys.exit("Merci de ne founir qu'un seul argument")

if not arguments[0].isdigit():
    sys.exit("Merci de saisir un nombre")

number = int(arguments[0])

if number < 2:
    sys.exit("Merci de saisir un nombre supérieur à 1")
    
isPrimeNumber = True

for primeNumber in range(2, number):
    if number % primeNumber == 0:
        isPrimeNumber = False
        print(isPrimeNumber)
        break

if isPrimeNumber == True:
    print(f"{number} est un nombre premier")