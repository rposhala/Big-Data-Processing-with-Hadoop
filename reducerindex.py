import sys


mapperoutputlist = []
for line in sys.stdin:
  line = line.strip()
  data = line.split('\t')
  mapperoutputlist.append(data)


di = {}
key_list = []
for i in mapperoutputlist :
    if i[0] in key_list:
      try :
        di[i[0]][i[1]] += int(i[2])
      except :
        di[i[0]].update({i[1]:int(i[2])})
    else:
        key_list.append(i[0])
        di.update({i[0]:{i[1]:int(i[2])}})
for key in di.keys():
  u = ''
  for j in di[key].keys():
    u += '|'
    u += j+':'+str(di[key][j])
  print(key+u)

