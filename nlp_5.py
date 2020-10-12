import spacy

#nlp = spacy.load('en')
nlp = spacy.load('en_core_web_sm')

##gives entities of the paragraph
document = nlp('In 1994, Tim Berners-Lee founded the World Wide Web\
    Consortium (WSC), devoted to developing web technologies')

for entity in document.ents:
    print(entity.text,':', entity.label_)
