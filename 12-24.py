import sys
import re

arguments = sys.argv[1:]

if len(arguments) != 2:
	sys.exit("Veuillez saisir un horaire")

time = arguments[0]
period = arguments[1]

timePattern = r"^(1[0-2]|0?[1-9]):([0-5][0-9])$"
periodPattern = r"^(AM|PM)$"

timeMatch = re.match(timePattern, time)
periodMatch = re.match(periodPattern, period)

if not timeMatch or not periodMatch:
	print("Le format 12h n'est pas respecté")

hour, minute, period = int(timeMatch.group(1)), int(timeMatch.group(2)), periodMatch.group(1)


if hour != 12 and period == "PM":
	hour += 12

elif hour == 12 and period == "AM":
	hour = 0

time = f"{hour}:{minute}"
print(time)