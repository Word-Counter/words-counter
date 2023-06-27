import tkinter as tk

window = tk.Tk()

window.geometry("600x500")
window.title("Words Counter")

label_1 = tk.Label(window, text="Enter your paragraph")
label_1.place(x=20,y=50)

text_box = tk.Text(window, height=20, width=40)
text_box.place(x=20,y=75)

submit_button = tk.Button(window, text="Submit")
submit_button.place(x=150,y=410)

words_countedLBL = tk.Label(window, text="words counted:")
words_countedLBL.place(x=385, y=70)

vowel_countetLBL = tk.Label(window, text="vowel counted: ")
vowel_countetLBL.place(x=385, y=100)

character_countedLBL = tk.Label(window, text="character counted: ")
character_countedLBL.place(x=385, y=130)

sentance_countedLBL = tk.Label(window, text="sentance counted: ")
sentance_countedLBL.place(x=385, y=160)

readTime_lbl = tk.Label(window, text="estimate read time: ")
readTime_lbl.place(x=385, y=190)

speakTime_lbl = tk.Label(window, text="estimate speaking time: ")
speakTime_lbl.place(x=385, y=220)


window.mainloop()
