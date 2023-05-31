sentance = str(input("your sentance: \n"))


def wordsCounter():
    #make new variable and split the sentance with split() function
    listWords = sentance.split()
    wordsCounted = len(listWords)
    return wordsCounted

def vowelCounter():
    #make a list to store list of vowel words
    vowels = ["a", "e", "i", "o", "u"]
    #initiate the count program from 0
    count = 0
    for char in sentance:
        if char in vowels:
            count += 1
    return count

def characterCounter():
    count = len(sentance)
    return count

def sentanceCounter():
    dot = '.'
    count = 0
    for char in sentance:
        if char in dot:
            count += 1
    return count

def readingTime():
    words = wordsCounter()
    readTime = round(words / 200,3)
    return readTime

def speakingTime():
    words = wordsCounter()
    speakTime = round(words / 135, 3)
    return speakTime


print("Words counted:", wordsCounter(), )
print("Vowel counted:", vowelCounter())
print("character counted:", characterCounter())
print("sentance counted:", sentanceCounter())
print("estimate read time:", readingTime(), "minutes")
print("estimate speaking time:", speakingTime(), "minutes")

