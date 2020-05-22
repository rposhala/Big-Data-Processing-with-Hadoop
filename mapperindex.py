import sys
import os
import re
#import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

p = []
key = []
dic1 = dict()

for line in sys.stdin:


    # Get the file path
    doc_id = os.environ["map_input_file"]

    # Get the name of the file from the path
    doc_id = re.findall(r'\w+', doc_id)[-2]

    # Get an array of all the words inside the document
    line_list = line.strip().split()
    #words = re.findall(r'\w+', line.strip())
    words = []
    for word in line_list :
        a = (''.join(j for j in word if j.isalpha())).lower()
        if a != '':
            print("%s\t%s.txt\t1" %(wordnet_lemmatizer.lemmatize(a), doc_id))
