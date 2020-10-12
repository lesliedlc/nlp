import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob
from pathlib import Path
from textblob import TextBlob

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

stops = stopwords.words('english')
#print(stops)

'''
blob = TextBlob('today is a beautiful day.')
print(blob.words)
blob_2 = [word for word in blob.words if word not in stops] 
print(blob_2)
'''
items = blob.word_counts.items() #word count of each word
#print(items)

items = {i for i in items if i[0] not in stops} #removes all stop words
#print(items)

from operator import itemgetter

sorted_items = sorted(items, key = itemgetter(1), reverse = True) #1 by number sorting
#print(sorted_items)

top20 = sorted_items[:20]
#print(top20)

import pandas as pd

df = pd.DataFrame(top20, columns = ['word','count'])
#print(df)

axes = df.plot.bar(x = 'word', y = 'count', legend = False)

import matplotlib.pyplot as plt

plt.gcf().tight_layout()
plt.show()


