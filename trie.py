import sys

arguments = sys.argv[1:]

if len(arguments) < 3:
	sys.exit("Merci d'au moins donner 3 arguments")
     
numbers = []

for argument in arguments:
    if not argument.isdigit():
        sys.exit("Veuillez saisir des nombres")
    numbers.append(int(argument))


isSort = True

for number in range(1, len(numbers)):
    if numbers[number] < numbers[number - 1]:
        isSort = False
        print(isSort)
        break

if isSort == True:
     print("C'est trié")