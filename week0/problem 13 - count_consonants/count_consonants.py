def count_consonants(str):
	consonants_count = 0
	consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
	for consonant in consonants:
		for letter in str:
			if consonant == letter:
				consonants_count += 1
	return consonants_count


def main():
	print(count_consonants("Python"))
	print(count_consonants("Theistareykjarbunga"))
	print(count_consonants("grrrrgh!"))
	print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
	print(count_consonants("A nice day to code!"))

main()