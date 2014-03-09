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
