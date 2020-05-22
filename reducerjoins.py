import sys

join = {}
primary_key = []

for line in sys.stdin:
    
    
    # splitting the data and storing it in a list
    mapped_data = line.strip().split("\t")
    
    
    if mapped_data[0] in primary_key :
        if join[mapped_data[0]][0] == '_':
            join[mapped_data[0]][0] = mapped_data[1]
        else :
            join[mapped_data[0]][1] = mapped_data[2]
            join[mapped_data[0]][2] = mapped_data[3]
            join[mapped_data[0]][3] = mapped_data[4]
    else :
        if mapped_data[0] != '_':
            primary_key.append(mapped_data[0])
            join.update({mapped_data[0]:[mapped_data[1],mapped_data[2],mapped_data[3],mapped_data[4]]})
print('Employee ID','Name','Salary','Country','Passcode')
for i in join.keys():
    
    temp = join[i][0]+'|'+join[i][1]+'|'+join[i][2]+'|'+join[i][3]
    print(i+'|'+temp)


