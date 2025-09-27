import sys

arguments = sys.argv[1:]

if (len(arguments) <= 1 or len(arguments) >  2):
     sys.exit("Veuillez saisir 2 arguments")

if not arguments[0].isnumeric() or not arguments[1].isnumeric:
     sys.exit("Veuillez saisir 2 nombres")

if int(arguments[1]) < 0:
     sys.exit("Veuillez saisir un exposant positif")

number = int(arguments[0])
power = int(arguments[1])
result = number

for power in range(1, power):
     result = result * number

print(result)