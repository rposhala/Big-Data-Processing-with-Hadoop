import sys
import numpy as np
import pandas as pd

data = pd.read_csv("/home/cse587/knn/Test.csv", header = None , skiprows = 1)
dataframe = pd.DataFrame()
dataframe = pd.DataFrame(data)
test_data = dataframe.to_numpy()
test_data = (test_data - np.mean(test_data,axis = 0)[np.newaxis,:])/np.std(test_data,axis=0)[np.newaxis,:]
c = len(test_data)
train = []
index = [str(i) for i in list(range(49))]
training_labels = []
for line in sys.stdin:
    train_sample = line.strip().split(',')
    if train_sample != index :
        training_labels.append(int(train_sample[-1]))
        train.append([float(i) for i  in train_sample[:-1]])
train_data = np.asarray(train)
train_data = (train_data - np.mean(train_data,axis = 0)[np.newaxis,:])/np.std(train_data,axis=0)[np.newaxis,:]

#print(len(train),len(train[0]),len(test_data[0]))
#print(test_data[0])
k = 5
dis = []
for i in test_data :
    dis.append(np.linalg.norm(i-train_data,axis=1))
nearest_labels = np.tile(training_labels,(c,1))[np.arange(c)[:, np.newaxis],np.argsort(dis , axis = 1)]#[:,:k]
sorted_distances = np.sort(dis,axis=1)#[:,:k]
c = 0
for i in range(len(test_data)):
    #temp = test_data[i][0]
    
    print(c,':',list(zip(sorted_distances[i],nearest_labels[i])))
    c+=1

#print(training_labels[dis[0].tolist().index(min(dis[0]))]),print(min(dis[0]))
#print(training_labels[:5])


