import math
import re
import nltk
from nltk.corpus import stopwords
import operator

txt=open('example','r')
text=txt.read()

#---------------------Sentence splitting---------------------------


tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
sentences=tokenizer.tokenize(text)
#sentence_delimiters=re.compile(u'[!?,;:.\t\\\\"\\(\\)\\\'\u2019\u2013]|\\s\\-\\s')
#sentences=sentence_delimiters.split(text)
#print sentences

#--------------------Word splitting--------------------------------

stop_word_list = stopwords.words('english')

stop_word_regex_list = []
for word in stop_word_list:
    word_regex = r'\b' + word + r'(?![\w-])'  # added look ahead for hyphen
    #print word_regex
    stop_word_regex_list.append(word_regex)
stop_word_pattern = re.compile('|'.join(stop_word_regex_list), re.IGNORECASE)
# print stop_word_pattern

#------------------------------------------------------------------

phrase_list=[]
for sent in sentences:
	sent=sent.strip()
	tmp=re.sub(stop_word_pattern,'|',sent.strip())
	phrases=tmp.split('|')
	for phrase in phrases:
		phrase=phrase.strip().lower()
		if phrase !='':
			phrase_list.append(phrase)
			


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



#-----------------------------------------------------------------

def calculate_word_score(phrase_list):
	word_freq={}
	word_deg={}
	for phrase in phrase_list:
		word_list=separate_words(phrase,0)
		if len(word_list)==0: continue
		word_list_deg=len(word_list)-1
		for word in word_list:
			word_freq.setdefault(word,0)
			word_freq[word]+=1
			word_deg.setdefault(word,0)
			word_deg[word]+=word_list_deg

	for item in word_freq:
		word_deg[item]=word_deg[item] + word_freq[item]

	#word score- deg/freq
	word_score={}
	for item in word_freq:
		word_score.setdefault(item,0)
		word_score[item]=word_deg[item]/(word_freq[item]*1.0)

	return word_score
#-------------------------------------------------------------------

def generate_candidate_keyword_scores(phrase_list, word_score):
	keyword_candidates={}
	for phrase in phrase_list:
		keyword_candidates.setdefault(phrase,0)
		word_list=separate_words(phrase,0)
		candidate_score=0
		for word in word_list:
			candidate_score+=word_score[word]
		keyword_candidates[phrase]=candidate_score
	return keyword_candidates


#------------------------------------------------------------------
#Calling Functions

word_scores=calculate_word_score(phrase_list)

keyword_candidates= generate_candidate_keyword_scores(phrase_list,word_scores)
sorted_keywords = sorted(keyword_candidates.iteritems(), key=operator.itemgetter(1), reverse=True)
for item in sorted_keywords[:20]:
	print item[0]









