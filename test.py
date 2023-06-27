import functionList

sentance = str(input("your sentance: \n"))

print("Words counted:", functionList.wordsCounter(sentance))
print("Vowel counted:", functionList.vowelCounter(sentance))
print("character counted:", functionList.characterCounter(sentance))
print("sentance counted:", functionList.sentanceCounter(sentance))
print("estimate read time:", functionList.readingTime(sentance), "minutes")
print("estimate speaking time:", functionList.speakingTime(sentance), "minutes")
functionList.mostCommonWords(sentance)
functionList.wordRange(sentance, 1, 100)
