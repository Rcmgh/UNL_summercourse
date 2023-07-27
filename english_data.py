# english_data.py : class to define the mapping of the entities to the karakas.

class EnglishData:
    def __init__(self):
        self.verbs = []
        self.entities = []

    def add_verb(self, verb):
        self.verbs.append(verb)

    def add_entity(self, entity):
        self.entities.append(entity)

    def display_data(self):
        print("Verbs:", self.verbs)
        print("Entities:", self.entities)
