import sys
import re

mapperoutputlist = []
for line in sys.stdin:
  line = line.strip()
  data = line.split('\t')
  if len(data) != 2:
      continue
  mapperoutputlist.append(data)
#print(mapperoutputlist)

di = {}
key_list = []
for i in mapperoutputlist :
    if i[0] in key_list:
        di[i[0]] += int(i[1])
    else:
        key_list.append(i[0])
        di.update({i[0]:int(i[1])})
sorted_d = sorted(di.items(), key=lambda x: x[1] , reverse=True)
f = open("ngramsoutput2.txt","a+")
for key in sorted_d[:10]:
    f.write("{}\t{}\n".format(key[0],key[1]))
    print(key[0],'\t',key[1])


