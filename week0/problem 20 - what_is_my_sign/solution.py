def what_is_my_sign(day, month):
	if month == 1:
		if day < 21:
			return "Capricorn"
		else:
			return "Aquarius"
	elif month == 2:
		if day < 20:
			return "Aquarius"
		else:
			return "Pisces"
	elif month == 3:
		if day < 21:
			return "Pisces"
		else:
			return "Aries"
	elif month == 4:
		if day < 21:
			return "Aries"
		else:
			return "Taurus"
	elif month == 5:
		if day < 22:
			return "Taurus"
		else:
			return "Gemini"
	elif month == 6:
		if day < 22:
			return "Gemini"
		else:
			return "Cancer"
	elif month == 7:
		if day < 23:
			return "Cancer"
		else:
			return "Leo"
	elif month == 8:
		if day < 23:
			return "Leo"
		else:
			return "Virgo"
	elif month == 9:
		if day < 24:
			return "Virgo"
		else:
			return "Libra"
	elif month == 10:
		if day < 24:
			return "Libra"
		else:
			return "Scorpio"
	elif month == 11:
		if day < 23:
			return "Scorpio"
		else:
			return "Sagitarius"
	elif month == 12:
		if day < 22:
			return "Sagitarius"
		else:
			return "Capricorn"
