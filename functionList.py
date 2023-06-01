def wordsCounter(sentance: str) -> str:
    #make new variable and split the sentance with split() function
    listWords = sentance.split()
    wordsCounted = len(listWords)
    return wordsCounted

def vowelCounter(sentance: str) -> str:
    #make a list to store list of vowel words
    vowels = ["a", "e", "i", "o", "u"]
    #initiate the count program from 0
    count = 0
    for char in sentance:
        if char in vowels:
            count += 1
    return count

def characterCounter(sentance: str) -> str:
    count = len(sentance)
    return count

def sentanceCounter(sentance: str) -> str:
    dot = '.'
    count = 0
    for char in sentance:
        if char in dot:
            count += 1
    return count

def readingTime(sentance: str) -> str:
    listWords = sentance.split()
    wordsCounted = len(listWords)
    readTime = round(wordsCounted / 200,3)
    return readTime

def speakingTime(sentance: str) -> str:
    listWords = sentance.split()
    wordsCounted = len(listWords)
    speakTime = round(wordsCounted / 135, 3)
    return speakTime


