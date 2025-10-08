import sys
import re

arguments = sys.argv[1:]

if len(arguments) != 1:
	sys.exit("Veuillez saisir un horaire")

time = arguments[0]

timePattern = r"^(1[0-2]|0?[1-9]):([0-5][0-9])((a|A|p|P)(m|M))$"

timeMatch = re.match(timePattern, time)

if not timeMatch:
	print("Le format 12h n'est pas respecté")

hour, minute, period = int(timeMatch.group(1)), int(timeMatch.group(2)), timeMatch.group(3).upper()


if hour != 12 and period == "PM":
	hour += 12

elif hour == 12 and period == "AM":
	hour = 0

time = f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"
print(time)