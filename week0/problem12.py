def count_vowels(str):
	vowels_count = 0
	vowels = "aeiouyAEIOUY"
	for vowel in vowels:
		for letter in str:
			if vowel == letter:
				vowels_count += 1
	return vowels_count


def main():
	print(count_vowels("Python"))
	print(count_vowels("Theistareykjarbunga"))
	print(count_vowels("grrrrgh!"))
	print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
	print(count_vowels("A nice day to code!"))

main()