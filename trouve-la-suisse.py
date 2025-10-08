import sys

arguments = sys.argv[1:]

if len(arguments) != 3:
	sys.exit("Merci de donner 3 arguments")

for argument in arguments:
    if not argument.isdigit():
        sys.exit("Veuillez saisir 3 nombres")

firstNumber, secondNumber, thirdNumber = arguments[0], arguments[1], arguments[2]

if firstNumber == secondNumber or firstNumber == thirdNumber or secondNumber == thirdNumber:
	sys.exit("Merci de donner des nombres différents")

if secondNumber < firstNumber < thirdNumber or thirdNumber < firstNumber < secondNumber:
	print(firstNumber)
elif thirdNumber < secondNumber < firstNumber or firstNumber < secondNumber < thirdNumber:
	print(secondNumber)
else:
	print(thirdNumber)