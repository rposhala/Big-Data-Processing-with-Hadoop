import sys
import pandas as pd
import numpy as np
index = []
dis = []
labels = []
#c = 0
for line in sys.stdin :
    data = line.strip().split(':')
    value = data[1][3:-2].split('), (')
    temp_dis = []
    temp_label = []
    for i in value :
        d,l = i.split(', ')
        temp_dis.append(float(d))
        temp_label.append(int(l))
    if int(data[0]) not in index :
        index.append(int(data[0]))

        dis.append(temp_dis)
        labels.append(temp_label)
    else:
        dis[index.index(int(data[0]))].extend(temp_dis)
        labels[index.index(int(data[0]))].extend(temp_label)
#print(dis)
#print(labels)
#print(index)
c = len(index)
labels = np.asarray(labels)
k = 15
sorted_labels = labels[np.arange(c)[:, np.newaxis],np.argsort(dis , axis = 1)][:,:k]
pred_labels = np.argmax(np.apply_along_axis(np.bincount, axis=1, arr= sorted_labels,minlength = np.amax(sorted_labels)+1),axis = 1)
dat = pd.read_csv("/home/cse587/knn/Test.csv", header = None , skiprows = 1)
dataframe = pd.DataFrame()
dataframe = pd.DataFrame(dat)
test_data = dataframe.to_numpy()
#print(pred_labels)
#print(index)

for i in range(len(index)):
   # print('{}\t{}'.format(test_data[index[i]],pred_labels[i]))
    print('{}\t{}'.format(index[i],pred_labels[i]))



