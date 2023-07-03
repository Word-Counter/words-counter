import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import functionList


window = ttk.Window(themename="litera")

window.geometry("600x500")

def getParagraph():
    content = text_box.get("1.0", tk.END)
    output(content)

def clear_button():
    text_box.delete("1.0", tk.END)
    result_words_countedLBL.config(text="")
    result_vowel_countedLBL.config(text="")
    result_character_countedLBL.config(text="")
    result_sentence_countedLBL.config(text="")
    result_readTime_lbl.config(text="")
    result_speakTime_lbl.config(text="")
    result_mostCommonWords.config(text="")



def output(words):
    # print(functionList.wordsCounter(words))
    result_words_countedLBL.config(text=functionList.wordsCounter(words))
    result_vowel_countedLBL.config(text=functionList.vowelCounter(words))
    result_character_countedLBL.config(text=functionList.characterCounter(words))
    result_sentence_countedLBL.config(text=functionList.sentenceCounter(words))
    result_readTime_lbl.config(text=functionList.readingTime(words))
    result_speakTime_lbl.config(text=functionList.speakingTime(words))
    result_mostCommonWords.config(text=functionList.mostCommonWords(words))



window.geometry("600x500")
window.title("Words Counter")

label_1 = ttk.Label(window, text="Enter your paragraph")
label_1.place(x=20,y=45)

text_box = tk.Text(window, height=17, width=40)
text_box.place(x=20,y=75)

submit_button = ttk.Button(window, text="Submit", command=getParagraph)
submit_button.place(x=100,y=440)

clear_button = ttk.Button(window, text="Clear",command=clear_button)
clear_button.place(x=200,y=440)

words_countedLBL = ttk.Label(window, text="words counted:")
words_countedLBL.place(x=385, y=70)
result_words_countedLBL = ttk.Label(window)
result_words_countedLBL.place(x=490, y=70)

vowel_countetLBL = ttk.Label(window, text="vowel counted: ")
vowel_countetLBL.place(x=385, y=100)
result_vowel_countedLBL = ttk.Label(window)
result_vowel_countedLBL.place(x=490, y=100)

character_countedLBL = ttk.Label(window, text="character counted: ")
character_countedLBL.place(x=385, y=130)
result_character_countedLBL = ttk.Label(window)
result_character_countedLBL.place(x=510,y=130)

sentence_countedLBL = ttk.Label(window, text="sentence counted: ")
sentence_countedLBL.place(x=385, y=160)
result_sentence_countedLBL = ttk.Label(window)
result_sentence_countedLBL.place(x=510,y=160)

readTime_lbl = ttk.Label(window, text="estimate read time: ")
readTime_lbl.place(x=385, y=190)
result_readTime_lbl = ttk.Label(window)
result_readTime_lbl.place(x=516,y=190)

speakTime_lbl = ttk.Label(window, text="estimate speaking time: ")
speakTime_lbl.place(x=385, y=220)
result_speakTime_lbl = ttk.Label(window)
result_speakTime_lbl.place(x=545,y=220)

mostCommonWords = ttk.Label(window, text="Common words: ")
mostCommonWords.place(x=385, y=250 )
result_mostCommonWords = ttk.Label(window)
result_mostCommonWords.place(x=385,y=275)


window.mainloop()