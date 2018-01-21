import numpy as np

def read_training_data():
    train_data = open(train_file, 'r').readlines()
    training_tuples = list()
    for eachline in train_data:
        uid, lid, val, _ = eachline.strip().split()
        uid, lid , val = int(uid), int(lid), int(val)
        training_tuples.append([uid, lid, val])
    return training_tuples

data_dir = "../data/"

train_file = "Foursquare_scaled_training_0.8.txt"
raw_data=read_training_data()
print(raw_data)

raw_data = np.array(raw_data)
print(raw_data)

#按uid升序排列
uid_index = np.lexsort([raw_data[:,1],raw_data[:,0]])
uid_sorted = raw_data[uid_index,:]


#去除空uid
num = 0
temp = uid_sorted[0][0]
for i in range(len(uid_sorted)):
    if temp == uid_sorted[i][0]:
        uid_sorted[i][0]= num
    else:
        num = num+1
        temp = uid_sorted[i][0]
        uid_sorted[i][0] = num


#按lid升序排列
lid_index = np.lexsort([uid_sorted[:,0],uid_sorted[:,1]])
lid_sorted = uid_sorted[lid_index,:]

#去除空lid
num = 0
temp = lid_sorted[0][0]
for i in range(len(lid_sorted)):
    if temp == lid_sorted[i][1]:
        lid_sorted[i][1]= num
    else:
        num = num+1
        temp = lid_sorted[i][1]
        lid_sorted[i][1] = num

#output
output_index = np.lexsort([lid_sorted[:,1],lid_sorted[:,0]]) #按第'1'列排序
output_data = lid_sorted[output_index,:]
np.savetxt("finalresult 0.8.txt",output_data,fmt='%10d')


##########################################################





train_file = "Foursquare_scaled_testing_0.2.txt"
raw_data=read_training_data()
print(raw_data)

raw_data = np.array(raw_data)
print(raw_data)

#按uid升序排列
uid_index = np.lexsort([raw_data[:,1],raw_data[:,0]])
uid_sorted = raw_data[uid_index,:]


#去除空uid
num = 0
temp = uid_sorted[0][0]
for i in range(len(uid_sorted)):
    if temp == uid_sorted[i][0]:
        uid_sorted[i][0]= num
    else:
        num = num+1
        temp = uid_sorted[i][0]
        uid_sorted[i][0] = num


#按lid升序排列
lid_index = np.lexsort([uid_sorted[:,0],uid_sorted[:,1]])
lid_sorted = uid_sorted[lid_index,:]

#去除空lid
num = 0
temp = lid_sorted[0][0]
for i in range(len(lid_sorted)):
    if temp == lid_sorted[i][1]:
        lid_sorted[i][1]= num
    else:
        num = num+1
        temp = lid_sorted[i][1]
        lid_sorted[i][1] = num

#output
output_index = np.lexsort([lid_sorted[:,1],lid_sorted[:,0]]) #按第'1'列排序
output_data = lid_sorted[output_index,:]
np.savetxt("finalresult 0.2.txt",output_data,fmt='%10d')


##############################################################


#第二列升序，第一列升序 输出(验证用)
lid_index = np.lexsort([raw_data[:,0],raw_data[:,1]]) #按第'1'列排序
lid_sorted = raw_data[lid_index,:]


#去除空lid
num = 0
temp = lid_sorted[0][0]
for i in range(len(lid_sorted)):
    if temp == lid_sorted[i][1]:
        lid_sorted[i][1]= num
    else:
        num = num+1
        temp = lid_sorted[i][1]
        lid_sorted[i][1] = num

    print(lid_sorted[i][1])





