import sys
mapperoutputlist = []
for line in sys.stdin:
  line = line.strip()
  data = line.split('\t')
  if len(data) != 2:
      continue

  mapperoutputlist.append(data)
di = {}
key_list = []
for i in mapperoutputlist :
    if i[0] in key_list:
        di[i[0]] += int(i[1])
    else:
        key_list.append(i[0])
        di.update({i[0]:int(i[1])})
for key in di:
    print(key,'\t',di[key])

