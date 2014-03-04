def count_substrings(haystack, needle):
	occurences = 0
	substr = ''
	i = 0
	while i < len(haystack):
		if haystack[i] == needle[0] and len(haystack) - i >= len(needle):
			for j in range(len(needle)):
				if haystack[i + j] != needle[j]:
					substr = ''
					break
				else:
					substr += haystack[i + j]
				
				if substr == needle:
					occurences += 1
					substr = ''
					i += len(needle) - 1
					break
		i += 1
	return occurences


def main():
	print(count_substrings("This is a test string", "is"))
	print(count_substrings("babababa", "baba"))
	print(count_substrings("Python is an awesome language to program in!", "o"))
	print(count_substrings("We have nothing in common!", "really?"))
	print(count_substrings("This is this and that is this", "this"))

main()
