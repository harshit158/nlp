from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
word=wordnet_lemmatizer.lemmatize('compression')
print word

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
word2=porter_stemmer.stem('provision','v')
print word2
