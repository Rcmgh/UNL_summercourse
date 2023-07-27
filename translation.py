# translation.py: Contains the implementation of (Hindi Module) converting the English sentence to Hindi sentence via mapping the karaka framework through the dictionary.

def translate_to_hindi(english_sentence, english_data, dictionary):
    words = english_sentence.split()
    hindi_translation = []

    for word in words:
        # Handle basic grammar rules
        if word.endswith('ed'):
            hindi_word = dictionary.get(word[:-2], word) + "ा"
        elif word.endswith('ing'):
            hindi_word = dictionary.get(word[:-3], word) + "ा रहा"
        else:
            hindi_word = dictionary.get(word, word)

        hindi_translation.append(hindi_word)

    # Add verbs and entities to the Hindi translation
    for verb in english_data.verbs:
        hindi_translation.append(dictionary.get(verb, verb))
    for entity in english_data.entities:
        hindi_translation.append(dictionary.get(entity, entity))

    return " ".join(hindi_translation)
