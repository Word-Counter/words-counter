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


def mostCommonWords(sentence: str):
    #Note: this function works if the list is not out of range, so not fully working yet!!!
    #It works for long text, but doesn't work for text like, "aa bb", since there is only top 2 instead of top 3


    #listing array of distinct words and its count
    oriListWords = sentence.split()
    listWords = []
    counterWords = []
    for word in oriListWords:
        if word.lower() not in listWords:
            listWords.append(word.lower())
            counterWords.append(1)
        else:
            pos = listWords.index(word.lower())
            counterWords[pos] += 1

    #find unique numbers in counterWords and ordered it
    #set in python: set elements are unique, and not ordered
    distinctCounter = set()
    for count in counterWords:
        distinctCounter.add(count)
    distinctCounterList = sorted(distinctCounter, reverse= True)

    listWords0 = []
    listWords1 = []
    listWords2 = []

    counter = 0
    for count in counterWords:
        if count == distinctCounterList[0]:
            listWords0.append(listWords[counter])
            counter += 1
        elif count == distinctCounterList[1] :
            listWords1.append(listWords[counter])
            counter += 1
        elif count == distinctCounterList[2] :
            listWords2.append(listWords[counter])
            counter += 1
        else:
            counter += 1
            pass

    print("The first most common words is/are: " + ','.join(listWords0) + " with " + str(counterWords[listWords.index(listWords0[0])])+ " words.")
    print("The second most common words is/are: " + ','.join(listWords1) + " with " + str(counterWords[listWords.index(listWords1[0])])+ " words.")
    print("The third most common words is/are: " + ','.join(listWords2) + " with " + str(counterWords[listWords.index(listWords2[0])])+ " words.")\

def wordRange(sentence :str, minNum :int, maxNum :int):
    listWords = sentence.split()
    wordCount = len(listWords)
    if (minNum <= wordCount <= maxNum):
        print("The number of words satisfy the requirement.")
    elif (wordCount < minNum):
        print("You need to add " + str(minNum - wordCount) + " word(s) more to satisfy the requirement.")
    else:
        print("You need to delete " + str(wordCount - maxNum) + " word(s) to satisfy the requirement.")