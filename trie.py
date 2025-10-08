import sys

arguments = sys.argv[1:]

if len(arguments) != 3:
	sys.exit("Merci de donner 3 arguments")

for argument in arguments:
    if not argument.isdigit():
        sys.exit("Veuillez saisir 3 nombres")

numbers = [int(arguments[0]), int(arguments[1]), int(arguments[2])]

isSort = True

for number in range(1, len(numbers)):
    if numbers[number] < numbers[number - 1]:
        isSort = False
        print(isSort)
        break

if isSort == True:
     print("C'est trié")