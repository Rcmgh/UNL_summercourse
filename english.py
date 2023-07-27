# english.py : Contains the implementation of the English Module that reads the English sentence and splits to understand the verb and the entities associated with it.

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def identify_verbs_and_entities(english_sentence):
    words = word_tokenize(english_sentence)
    tagged_words = pos_tag(words)

    verbs = []
    entities = []

    for word, tag in tagged_words:
        if tag.startswith('VB'):
            verbs.append(word)
        elif tag.startswith('NN') or tag.startswith('PRP'):
            entities.append(word)

    return verbs, entities

import spacy
import pathlib
import lemminflect
from dataclasses import dataclass
import json

filename = "story1.txt"
# filename = "sent1.txt"
nlp = spacy.load("en_core_web_sm")	# To process English input
contents = pathlib.Path(filename).read_text(encoding="utf-8")
# sentences = doc.sents
# contents = "I had wanted food."


doc = nlp(contents)

# # Entities
# for ent in doc.ents:
# 	print(ent.text, ent.label_)


rows = []
rows.append([
	# "Word", "Position", "Lowercase", "Lemma", \
	"Word", "Lemma", \
	"POS", "Tag", "Tag explained", "Dependency label", "Dep explained", "Stopword"])#, "Alphanumeric", "Stopword"])

for token in doc:
	rows.append([
		token.text,				# original word
		# str(token.idx),			# position of word in text (use .i for word s.no)
		# token.lower_,			# lowercase of word
		token.lemma_,			# 'lemma' or basic/stem form
		token.pos_,				# POS (part-of-speech) tag
		token.tag_,
		str(spacy.explain(token.tag_)),
		token.dep_,				# dependency label
		str(spacy.explain(token.dep_)),
		#str(token.is_alpha),	# alphanumeric
		str(token.is_stop)		# if in list of English stop-words
	])

columns = zip(*rows)
column_widths = [max(len(item) for item in col) for col in columns]

for row in rows:
	print(''.join(' {:{width}} '.format(row[i], width=column_widths[i])
		for i in range(len(row))))

# print(json.dumps(rows, indent=2))



# Once there was a young woman named Vidya who lived in a village.


class Kriya:
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return self.value


# kriyas = []
# for token in doc:
# 	if (token.pos_ == "VERB"):
# 		kriya = Kriya(token.lemma_)
# 		kriya.kartr = 

tok_l = doc.to_json()['tokens']
relations = {} # dependency relations -> dictionary of dictionaries of key-value pairs
source, reln, target = "", "", ""

for t in tok_l:
	head = tok_l[t['head']]
	# print(f"'{contents[t['start']:t['end']]}' is {t['dep']} of '{contents[head['start']:head['end']]}'")
	"""
	'She' is nsubj of 'wanted'
	'wanted' is ROOT of 'wanted'
	'to' is aux of 'travel'
	'travel' is xcomp of 'wanted'
	'and' is cc of 'travel'
	'explore' is conj of 'travel'
	"""
	source = contents[head['start']:head['end']]
	reln = t['dep']
	target = contents[t['start']:t['end']]
	# if reln not in relations[source]:
	# 	relations[source][reln] = [target]
	# else:
	# 	relations[source][reln].append(target)

	if source not in relations:
		relations[source] = {}
	
	relations[source][reln] = target

# kriyas = []
# for t in tok_l:
# 	if t.pos_ == "VERB":
# 		kriya = Kriya(t.lemma_)
# 		kriya.kartr = 

# for t in doc:
# 	if "dative" in t.dep_:
# 		subtree = list(t.subtree)
# 		start = subtree[0].i
# 		end = subtree[-1].i + 1
# 		print(doc[start:end])
# 		break


kriyas = []
morphology_dicts = []
for tokno, t in enumerate(tok_l):
	# print(f"Token: {t}")
	# print(t['morph'])
	morph = t['morph'].split("|")
	morph_dict = {}
	if morph == [""]:
		pass
	else:
		for i in morph:
			iL = i.split("=")
			morph_dict[iL[0]] = iL[1]

	# print(f"{doc[tokno].text:<13} : {morph_dict}")	# TO GET MORPHOLOGY DICT FOR EACH TOKEN

	morphology_dicts.append(morph_dict)


	head = tok_l[t['head']]

	gender = "F"

	if t['pos'] == "VERB": # not .pos_ for json version
		# kriya = Kriya(t['lemma'])

		verb = t['lemma']

		# tense
		"""
		*VB  --  verb, base form
		*VBD  --  verb, past tense
		*VBG  --  verb, gerund or present participle
		*VBN  --  verb, past participle
		VBP  --  verb, non-3rd person singular present
		*VBZ  --  verb, 3rd person singular present
		"""

		kriya = { "name": t['lemma'] }
		# print(kriya)

		"""
		dep_reln = f"{contents[t['start']:t['end']]} {t['dep']} {contents[head['start']:head['end']]}".split()
		# print(dep_reln)
		if kriya.value in dep_reln and "attr" in dep_reln:
			kriya.kartr = dep_reln[0]
		"""

		
		if kriya['name'] in relations:
			if 'nsubj' in relations[kriya['name']]: # assuming only active voice
				kriya['kartr'] = relations[kriya['name']]['nsubj']



"""
print(json.dumps(relations, indent=2))
print(kriyas)
"""

# print(json.dumps(morphology_dicts, indent=2))

with open("./eng_to_san.json", "r") as readEngToSan:
	eng_to_san = json.load(readEngToSan)

# print(eng_to_san['be'])
