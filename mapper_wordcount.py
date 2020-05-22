import sys
#import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

key = []

for line in sys.stdin:
    key.extend(line.strip().split())
d = []
for i in key:
    a = (''.join(j for j in i if j.isalpha())).lower()
    if a not in ['']:
        d.append(wordnet_lemmatizer.lemmatize(a))
c = 1
for v in d :
    print("{}\t{}\n".format(v,c))

