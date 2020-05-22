# ngrams mapper
import sys
import os
import nltk
#from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
#porter = PorterStemmer()
p = []
key = []
dic1 = dict()

for fp in sys.stdin:

   # p.append(os.path.abspath(__file__))
   # p.append(os.listdir(os.getcwd()))
    key.extend(fp.strip().split())
keywords = ['science','fire','sea']
keywords = [wordnet_lemmatizer.lemmatize(i) for i in keywords]

d = []
for i in key :
    temp = (''.join(j for j in i if j.isalpha())).lower()
    if temp != '':
        d.append(temp)
grams = []
for i in range(len(d)):
    temp = wordnet_lemmatizer.lemmatize(d[i])
    if keywords[0] == temp or keywords[1] == temp or keywords[2] == temp:
    #if keywords[0] == porter.stem(d[i]) or keywords[1] == porter.stem(d[i]) or keywords[2] == porter.stem(d[i]) :
        if i > 1 :
            grams.append(d[i-2]+'_'+d[i-1]+'_$')
        if i > 0 and i < (len(d)-1):
            grams.append(d[i-1]+'_$_'+d[i+1])
        if i < (len(d)-2):
            grams.append('$_'+d[i+1]+'_'+d[i+2])
value = [1]*len(d)
dic1 = list(zip(grams,value))
#hello = open("ngram.txt","w+")

for eachword in dic1:
    #hello.write
    print("{}\t{}\n".format(eachword[0],eachword[1]))


