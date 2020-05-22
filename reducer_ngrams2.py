import sys


ngramsdict = {}
for line in sys.stdin:
  
  data = line.strip().split('\t')
  #print(data)
  if len(data) == 2:
        ngramsdict.update({data[0]:int(data[1])})
#print(ngramsdict)

sorted_ngramsdict = sorted(ngramsdict.items(), key=lambda x: x[1] , reverse=True)
for key in sorted_ngramsdict[:10]:
    print(key[0],'\t',key[1])

