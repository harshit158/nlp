# using WORD-NET to find sentence similarity 
# used for calculating similarity between very short pieces of text 

from nltk.corpus import wordnet as wn

from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import word_tokenize
from nltk.wsd import lesk

#-----------------------------------------------
dog=wn.synset('eat.v.01')
cat=wn.synset('drink.v.01')
print dog.path_similarity(cat)	
print dog.wup_similarity(cat)
print dog.lch_similarity(cat)

#-----------------------------------------------
sent = word_tokenize("He should be happy".lower())