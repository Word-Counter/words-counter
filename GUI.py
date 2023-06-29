import tkinter as tk
import functionList



window = tk.Tk()

def getParagraph():
    content = text_box.get("1.0", tk.END)
    output(content)

def output(words):
    # print(functionList.wordsCounter(words))
    result_words_countedLBL.config(text = functionList.wordsCounter(words))
    result_vowel_countedLBL.config(text = functionList.vowelCounter(words))
    result_character_countedLBL.config(text = functionList.characterCounter(words))
    result_sentence_countedLBL.config(text = functionList.sentenceCounter(words))
    result_readTime_lbl.config(text = functionList.readingTime(words))
    result_speakTime_lbl.config(text = functionList.speakingTime(words))
    result_mostCommonWords.config(text = functionList.mostCommonWords(words))


window.geometry("600x500")
window.title("Words Counter")

label_1 = tk.Label(window, text="Enter your paragraph")
label_1.place(x=20,y=50)

text_box = tk.Text(window, height=20, width=40)
text_box.place(x=20,y=75)

submit_button = tk.Button(window, text="Submit", command=getParagraph)
submit_button.place(x=150,y=410)

words_countedLBL = tk.Label(window, text="words counted:")
words_countedLBL.place(x=385, y=70)
result_words_countedLBL = tk.Label(window)
result_words_countedLBL.place(x=475, y=70)

vowel_countetLBL = tk.Label(window, text="vowel counted: ")
vowel_countetLBL.place(x=385, y=100)
result_vowel_countedLBL = tk.Label(window)
result_vowel_countedLBL.place(x = 475, y = 100)

character_countedLBL = tk.Label(window, text="character counted: ")
character_countedLBL.place(x=385, y=130)
result_character_countedLBL = tk.Label(window)
result_character_countedLBL.place(x=490,y=130)

sentence_countedLBL = tk.Label(window, text="sentence counted: ")
sentence_countedLBL.place(x=385, y=160)
result_sentence_countedLBL = tk.Label(window)
result_sentence_countedLBL.place(x=490,y=160)

readTime_lbl = tk.Label(window, text="estimate read time: ")
readTime_lbl.place(x=385, y=190)
result_readTime_lbl = tk.Label(window)
result_readTime_lbl.place(x=495,y=190)

speakTime_lbl = tk.Label(window, text="estimate speaking time: ")
speakTime_lbl.place(x=385, y=220)
result_speakTime_lbl  = tk.Label(window)
result_speakTime_lbl.place(x=520,y=220)

mostCommonWords = tk.Label(window, text="Common words: ")
mostCommonWords.place(x=385, y=250 )
result_mostCommonWords = tk.Label(window)
result_mostCommonWords.place(x=490,y=250)


window.mainloop()
