#translator_app.py: Contains the interface of Python Tkinter Module to display the result obtained of the translation.
import tkinter as tk
from tkinter import messagebox
from translation import translate_to_hindi
from english_data import EnglishData



def on_translate():
    english_sentence = entry.get()
    if english_sentence:
        english_data = EnglishData()
        # Assuming you have the identified verbs and entities here (you can replace this with your data)
        verbs = ['was', 'named', 'lived']
        entities = ['woman', 'Vidya', 'village']
        for verb in verbs:
            english_data.add_verb(verb)
        for entity in entities:
            english_data.add_entity(entity)

            english_to_hindi = {
  "Once": "एक बार",
  "there": "वहाँ",
  "was": "था",
  "a": "एक",
  "young": "जवान",
  "woman": "महिला",
  "named": "नामित",
  "Vidya": "विद्या",
  "who": "जो",
  "lived": "रहती थी",
  "in": "एक",
  "village": "गाँव",
  "She": "वह",
  "wanted": "चाहती थी",
  "to": "को",
  "travel": "यात्रा करना",
  "and": "और",
  "explore": "खोजना",
  "the": "दुनिया",
  "world": "संसार",
  "but": "लेकिन",
  "couldn't": "नहीं कर सकी",
  "speak": "बोलना",
  "English": "अंग्रेज़ी",
  "So": "तो",
  "joined": "शामिल हुई",
  "an": "एक",
  "course": "कोर्स",
  "her": "उसके",
  "Vidya": "विद्या",
  "learned": "सीखी",
  "grammar": "व्याकरण",
  "vocabulary": "शब्दावली",
  "and": "और",
  "how": "कैसे",
  "to": "करें",
  "pronounce": "उच्चारण करना",
  "words": "शब्द",
  "She": "वह",
  "practised": "अभ्यास किया",
  "talking": "बातचीत",
  "with": "साथ",
  "her": "उसके",
  "classmates": "सहपाठी",
  "and": "और",
  "understood": "समझी",
  "simple": "सरल",
  "conversations": "बातचीत",
  "Vidya": "विद्या",
  "felt": "महसूस किया",
  "more": "अधिक",
  "confident": "आत्मविश्वासी",
  "and": "और",
  "decided": "निर्णय किया",
  "to": "को",
  "travel": "यात्रा करना",
  "alone": "अकेले",
  "an": "एक",
  "English-speaking": "अंग्रेज़ी बोलने वाले",
  "country": "देश",
  "She": "वह",
  "visited": "आयी",
  "big": "बड़े",
  "cities": "शहर",
  "talked": "बातचीत की",
  "to": "से",
  "local": "स्थानीय",
  "people": "लोग",
  "and": "और",
  "learned": "सीखा",
  "about": "के बारे में",
  "different": "विभिन्न",
  "cultures": "संस्कृतियों",
  "Vidya": "विद्या",
  "realized": "समझी",
  "that": "कि",
  "learning": "सीखना",
  "English": "अंग्रेज़ी",
  "opened": "खोल दिया",
  "doors": "दरवाजे",
  "to": "को",
  "new": "नए",
  "experiences": "अनुभव",
  "and": "और",
  "helped": "मदद की",
  "her": "उसे",
  "connect": "जुड़ना",
  "with": "से",
  "people": "लोग",
  "from": "से",
  "all": "सभी",
  "over": "उपर",
  "the": "दुनिया",
  "world": "संसार",
  "Her": "उसकी",
  "journey": "यात्रा",
  "showed": "दिखाई",
  "that": "कि",
  "with": "साथ",
  "determination": "निर्धारण",
  "and": "और",
  "learning": "सीखना",
  "anything": "कुछ भी",
  "is": "संभव",
  "possible": "संभव।"
}

        translated_hindi = translate_to_hindi(english_sentence, english_data, english_to_hindi)
        output_label.config(text="Translated Hindi Sentence:     " + translated_hindi)
    else:
        messagebox.showwarning("Input Error", "Please enter an English sentence.")

# Rest of the code remains unchanged...

""" def on_translate():
    english_sentence = entry.get()
    if english_sentence:
        translated_hindi = translate_to_hindi(english_sentence)
        output_label.config(text="Translated Hindi Sentence: " + translated_hindi)
    else:
        messagebox.showwarning("Input Error", "Please enter an English sentence.") """

# Create the main tkinter window
window = tk.Tk()
window.title("English to Hindi Translator")

# Input Entry
entry = tk.Entry(window, width=100)
entry.pack(pady=10)

# Translate Button
translate_button = tk.Button(window, text="Translate", command=on_translate)
translate_button.pack()

# Output Label
output_label = tk.Label(window, text="", wraplength=400, justify="left")
output_label.pack(pady=100)

# Run the tkinter main loop
window.mainloop()
