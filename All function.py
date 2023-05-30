sentance = str(input("your sentance: \n"))


def wordsCounter():
    listWords = sentance.split()
    print("total words counted: ", len(listWords))


def vowelCounter():
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in sentance:
        if char in vowels:
            count += 1
    print("vowel counted: ", count)



vowelCounter()
wordsCounter()
