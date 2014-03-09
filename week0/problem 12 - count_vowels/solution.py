def count_vowels(str):
	vowels_count = 0
	vowels = "aeiouyAEIOUY"
	for vowel in vowels:
		for letter in str:
			if vowel == letter:
				vowels_count += 1
	return vowels_count
