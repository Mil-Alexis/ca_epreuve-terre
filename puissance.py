import sys

arguments = sys.argv[1:]

if len(arguments) != 2:
     sys.exit("Veuillez saisir 2 arguments")

for argument in arguments:
     if not argument.isnumeric():
          sys.exit("Veuillez saisir 2 nombres")

number = int(arguments[0])
power = int(arguments[1])
result = number

if power < 0:
     sys.exit("Veuillez saisir un exposant positif")

for power in range(1, power):
     result = result * number

print(result)