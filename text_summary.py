import nltk
from nltk.corpus import stopwords
import re
from collections import Counter
import math
import operator
# from nltk.stem import WordNetLemmatizer
# wordnet_lemmatizer = WordNetLemmatizer()
# word=wordnet_lemmatizer.lemmatize('compression')
# print word

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()


#--------Loading text file-------------------------------

txt=open('example','r')
text=txt.read()
text=text

#----------------Sentence tokenization---------------------------------

sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
sentences=sent_tokenizer.tokenize(text)

# sentence_delimiters=re.compile(u'[!?;:.\t\\\\"\\(\\)\\\'\u2019\u2013]|\\s\\-\\s')
# sentences=sentence_delimiters.split(text)
S=len(sentences)


#------------------------------------------------------------------

#word splitter
def separate_words(text, min_word_size):
	splitter=re.compile('[^a-zA-Z0-9_\\+\\-/]')
	words=[]
	for single_word in splitter.split(text):
		current_word=single_word.strip().lower()
		if len(current_word)>min_word_size and current_word !='' and not current_word.isdigit():
			words.append(current_word)
	return words

#----------------word tokenization---------------------------------------

# stop_word_list = stopwords.words('english')
# def word_tokenize(sent):
# 	words=nltk.word_tokenize(sent)
# 	return words


#-----------------calculating idf values of words------------------------

isf={}
proper_sent={}

k=1
for sent in sentences:
	word_list=separate_words(sent,1) #list of words in sentence 'sent'
	#print set(word_list)
	for word in set(word_list):
		isf.setdefault(word,0)
		isf[word]+=1
	proper_sent[k]=(' ').join(word_list)
	k+=1

#-----------------calculating sentences score---------------------------
sent_score={}
k=1
for sent in sentences:
	sent_score.setdefault(proper_sent[k],0)
	word_list=separate_words(sent,1) #list of words in sentence 'sent'
	print word_list
	for word in set(word_list):
		sent_score[proper_sent[k]]+=(word_list.count(word))*(math.log(S/isf[word]))
		sent_score[proper_sent[k]]=sent_score[proper_sent[k]]/len(word_list)
	k+=1

sorted_keywords = sorted(sent_score.iteritems(), key=operator.itemgetter(1), reverse=True)
k=1
for item in sorted_keywords[:20]:
	print str(k)+':) '+item[0] + '\n'
	k+=1

# for score in sent_score:
# 	print score + ':' + str(sent_score[score]) 
	

		


	














