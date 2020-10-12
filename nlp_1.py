from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob.sentences) #broke it up as list of two objects, break up by sentences

#print(blob.words) #list of all the words in the paragraph sep as a list

#print(blob.tags) #NN = singular noun, DT= determiner, etc.

#print(blob.noun_phrases)

#print(round(blob.sentiment.polarity,3)) #polarity-1/+1
#print(round(blob.sentiment.subjectivity,3))
'''
sentences = blob.sentences

for sentence in sentences: #can break down sentences and get their sentiment
    print(sentence)
    print(sentence.sentiment)
    print(round(sentence.sentiment.polarity,3)) 
    print(round(sentence.sentiment.subjectivity,3))
'''
from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer = NaiveBayesAnalyzer())

#print(blob.sentiment)

sentences = blob.sentences

#for sentence in sentences:
#    print(sentence.sentiment)

#print(blob.detect_language())

spanish = blob.translate(to='es')
#print(spanish)

viet = blob.translate(to='vi')
#print(viet.translate())
#print(spanish.translate())

from textblob import Word

index = Word('index')
#print(index.pluralize())

animals = TextBlob('dog cat fish sheep bird').words
#print(animals.pluralize())

cacti = Word('cacti')
#print(cacti.singularize())

word = Word('theyr')
#print(word.spellcheck())
#or word = word.correct()
#print(word.correct())

sentence =  TextBlob('Ths sentense has missplled wrds.')
sentence = sentence.correct()
#print(sentence)

