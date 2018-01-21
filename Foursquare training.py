import numpy as numpy

def read_training_data():
    train_data = open(train_file, 'r').readlines()
    training_tuples = list()
    for eachline in train_data:
        uid, lid, val = eachline.strip().split()
        uid, lid , val = int(uid), int(lid), int(val)
        training_tuples.append([uid, lid, val])
    return training_tuples


def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = numpy.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))
        if e < 0.001:
            break
    return P, Q.T



train_file = "Foursquare_train.txt"
raw_data=read_training_data()
zero = numpy.zeros((24941,28593))
for i,j,FNum in raw_data:
    zero[i][j] = FNum


print(zero)
numpy.savetxt("zero.txt",zero,fmt='%2d')


R = zero

N = len(R)
M = len(R[0])
K = 2

P = numpy.random.rand(N,K)
Q = numpy.random.rand(M,K)

nP, nQ = matrix_factorization(R, P, Q, K)
nR = numpy.dot(nP, nQ.T)

print (R)

print (nR)

print("Error")
