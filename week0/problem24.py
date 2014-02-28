def unique_words_count(arr):
    current = ""
    count = 0
    for word in arr:
        current = str(word)
        count += 1
        for other_word in arr:
            if current != str(other_word):
                count += 1
        break
        current = ""

    return count


def main():
    print(unique_words_count(["apple", "banana", "apple", "pie"]))
    print(unique_words_count(["python", "python", "python", "ruby"]))
    print(unique_words_count(["HELLO!"] * 10))


main()
