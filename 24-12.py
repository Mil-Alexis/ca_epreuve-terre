import sys
import re

arguments = sys.argv[1:]

if len(arguments) != 1:
	sys.exit("Veuillez saisir un horaire")

time = arguments[0]

timePattern = r"^([0-1]?[0-9]|2[0-3]):([0-5][0-9])$"

if not re.match(timePattern, time):
	print("Le format 24h n'est pas respecté")

hour, minute = time.split(":")
hour, minute = int(hour), int(minute)
period = "AM"

if hour == 0:
	hour += 12

elif hour == 12:
	period = "PM"

elif hour > 12:
	period = "PM"
	hour = hour - 12

time = f"{hour}:{minute} {period}"
print(time)