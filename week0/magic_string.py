def magic_string(s):
	count = 0
	if (len(s) % 2) != 0:
		return "String is not of even length"
	else:
		for char in range(int(len(s) / 2)):
			if s[char] == '<':
				count += 1

		for char in range(int(len(s) / 2), len(s)):
			if s[char] == '>':
				count += 1

	return count