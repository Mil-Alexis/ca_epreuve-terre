import sys

arguments = sys.argv[1:]

if len(arguments) > 2:
	sys.exit("Veuillez founir uniquement 2 arguments")

if arguments[0] < arguments[1] or arguments[0] == 0:
	sys.exit("Division impossible")

if not arguments[0].isnumeric() or not arguments[1].isnumeric():
	sys.exit("Merci de founir 2 nombres")

dividend = int(arguments[0])
divisor = int(arguments[1])

result = dividend / divisor
rest = dividend % divisor

decimal = str(result).split('.')[1][:1]
decimal = int(decimal)


if decimal >= 5:
	result += 1
	decimal = 00
	result = str(result).split('.')[0]
	result = result + "." + str(decimal)
	result = float(result)
else:
	result = str(result).split('.')[0]
	result = result + "." + "0"
	result = float(result)

print(f"Résultat: {result}")
print(f"Reste: {rest}")