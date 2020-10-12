from pathlib import Path
from textblob import TextBlob

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

#print(blob.words.count('joy')) #shows count of word
#print(blob.noun_phrases.count('lady Capulet'))

from textblob import Word

happy = Word('happy')
#print(happy.definitions)
#print(happy.synsets)

