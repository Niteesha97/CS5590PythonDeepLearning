def main():
    sentence = input("Enter a sentence:")

    wordCount = len(sentence.split())

    dig = letter = 0
    for s in sentence:
        if s.isdigit():
            dig = dig + 1
        elif s.isalpha():
            letter = letter + 1
        else:
            pass
    print("Letters", letter)
    print("Digits", dig)
    print("words: %s"% wordCount)

main()
