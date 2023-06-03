def mostCommonWords(sentence: str):
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
    print("The third most common words is/are: " + ','.join(listWords2) + " with " + str(counterWords[listWords.index(listWords2[0])])+ " words.")
 
    
#so this does not have an issue
mostCommonWords("Lists are a popular way for people to stay organized Perhaps you jot down grocery items or tasks you need to complete at work each day on a sticky note or your phone But, when you need to communicate lists in writing and speech you need to organize them in a manner to show importance and clarity to your audience")
#but this has an issue because it is out of range
#mostCommonWords("hi i")

def wordRange(sentence :str, minNum :int, maxNum :int):
    listWords = sentence.split()
    wordCount = len(listWords)
    if (minNum <= wordCount <= maxNum):
        print("The number of words satisfy the requirement.")
    elif (wordCount < minNum):
        print("You need to add " + str(minNum - wordCount) + " word(s) more to satisfy the requirement")
    else:
        print("You need to delete " + str(wordCount - maxNum) + " word(s) to satisfy the requirement.")
