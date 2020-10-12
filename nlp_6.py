from pathlib import Path
import spacy

nlp = spacy.load('en_core_web_sm')

doc1 = nlp(Path('RomeoAndJuliet.txt').read_text())
doc2 = nlp(Path('EdwardTheSecond.txt').read_text())

print(doc1.similarity(doc2)) #how close the texts are to each other, can tell if same author