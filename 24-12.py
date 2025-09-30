import sys
import datetime

arguments = sys.argv[1:]

if len(arguments) != 1:
	sys.exit("Veuillez saisir un horaire")

time = arguments[0]

if not time[:2].isdigit() or not time[3:].isdigit() or not time[2] == ":":
	sys.exit("Merci d'utiliser le format 'HH:mm'")

hour = int(time[:2])
minute = int(time[3:])
period = "AM"

if hour > 23 or minute > 59:
	sys.exit("Merci d'indiquer un horaire valide")

if hour == 0:
	hour += 12
	time = f"{hour}:{minute} {period}"

elif hour == 12:
	period = "PM"

elif hour > 11:
	period = "PM"
	for validFormat in range(0, 12):
		if validFormat + 12  == hour:
			hour = validFormat
			break

time = f"{hour}:{minute} {period}"
print(time)
