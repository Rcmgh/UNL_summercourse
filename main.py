# main.py : Contains the implementation of the data structure (dictionary) and the rules described for identification of the karakas, vocabulary and grammar rules.
# Team Members:
# Chaitanya Madhav R	: PES1UG20CS634
# SIDDHARTH ARVIND	: PES1UG21CS594
# SIMRAN MADHUP	:     PES1UG21CS595

from english import identify_verbs_and_entities
from english_data import EnglishData
from translation import translate_to_hindi

if __name__ == "__main__":
    # Assuming you have the English sentence already available
    english_sentence = "Once there was a young woman named Vidya who lived in a village. She wanted to travel and explore the world, but she couldn't speak English. So, she joined an English course in her village. Vidya learned grammar, vocabulary, and how to pronounce words. She practised talking with her classmates and understood simple conversations. Vidya felt more confident and decided to travel alone to an English-speaking country. She visited big cities, talked to local people, and learned about different cultures. Vidya realized that learning English opened doors to new experiences and helped her connect with people from all over the world. Her journey showed that with determination and learning, anything is possible.."

    # Identify verbs and entities from the English sentence
    verbs, entities = identify_verbs_and_entities(english_sentence)

    # Create EnglishData object and add verbs and entities
    english_data = EnglishData()
    for verb in verbs:
        english_data.add_verb(verb)
    for entity in entities:
        english_data.add_entity(entity)

    karak_to_english = {
    "कर्तृ": "agent",
    "कर्म": "object",
    "अधिकरण": "location",
    "करण": "instrument",
    "सम्प्रदान": "beneficiary",
    "अपाधान": "source",
}
    
   # कर्तृ (Karta) - Nominative (Subject)
#कर्म (Karman) - Accusative (Direct Object)
#करण (Karana) - Instrumental (Instrument)
#सम्प्रदान (Sampradana) - Dative (Indirect Object)
#अपादान (Apadana) - Ablative (Source or Origin)
#सम्बन्ध (Sambandha) - Genitive (Possession or Relationship)
#अधिकरण (Adhikarana) - Locative (Location or Place)


class SanskritKarakas:
    def __init__(self):
        self.karakas = {
            'nominative': [],
            'accusative': [],
            'instrumental': [],
            'dative': [],
            'ablative': [],
            'genitive': [],
            'locative': []
        }

    def add_nominative(self, noun):
        self.karakas['nominative'].append(noun)

    def add_accusative(self, noun):
        self.karakas['accusative'].append(noun)

    def add_instrumental(self, noun):
        self.karakas['instrumental'].append(noun)

    def add_dative(self, noun):
        self.karakas['dative'].append(noun)

    def add_ablative(self, noun):
        self.karakas['ablative'].append(noun)

    def add_genitive(self, noun):
        self.karakas['genitive'].append(noun)

    def add_locative(self, noun):
        self.karakas['locative'].append(noun)

    def display_karakas(self):
        for karaka, nouns in self.karakas.items():
            print(f"{karaka.capitalize()}: {', '.join(nouns)}")

    # Define English to Hindi word translations
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
  "possible": "संभव।",
  ".":"|",
}

        # Add more words and translations as needed
    

    # Translate the English sentence to Hindi
    translated_hindi = translate_to_hindi(english_sentence, english_data, english_to_hindi)

    # Display the translated Hindi sentence
    print("Translated Hindi Sentence:", translated_hindi)



""" import tkinter as tk
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
            "young": "युवा",
            "woman": "स्त्री",
            "named": "नामित",
            "Vidya": "विद्या",
            "who": "जो",
            "lived": "रहती थी",
            "in": "में",
            "village": "गांव"
                "but": "तथापि",
    "she": "ता",
    "couldn't": "न शक्ता अस्ति",
    "join": "सम्प्रवेशयति",
    "in": "अन्तर्गत",
    "her": "तस्याः",
    "and": "च",
    "how": "कथम्",
    "to": "अधिगन्तुम्",
    "practiceed": "अभ्यासत",
    "with": "सह",
    "more": "अधिक",
    "alone": "एका एव",
    "big": "विशाले",
    "people": "लोकैः",
    "different": "विविधानि",
    "cultures": "संस्कृतयः",
    "realized": "अवगच्छत्",
    "learning": "अधिगमः",
    "anything": "किंचित्",
    "is": "अस्ति",
    "possible": "सम्भवम्",
    "journey": "प्रयाणः",
    "showed": "प्रदर्शितः",
    "with": "सह",
    "determination": "आत्मसंयमः",
    "and": "च",
    "anything": "किंचित्",
    "is": "सक्षमम्",
    "possible": "सम्भवम्",
            # Add more words and translations as needed
        }

        translated_hindi = translate_to_hindi(english_sentence, english_data, english_to_hindi)
        output_label.config(text="Translated Hindi Sentence: " + translated_hindi)
    else:
        messagebox.showwarning("Input Error", "Please enter an English sentence.")

# Rest of the code remains unchanged. """
