def count_consonants(str):
	consonants_count = 0
	consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
	for consonant in consonants:
		for letter in str:
			if consonant == letter:
				consonants_count += 1
	return consonants_count
