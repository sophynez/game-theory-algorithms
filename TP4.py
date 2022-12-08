import numpy as np


mat1 = np.array([[2, 9, 2, 7],
                 [1, 3, 1, 4],
                 [0, 1, -1, 2]])
mat2 = np.array([[2, 9, 7, 2, 7, 6],
                 [1, 3, 4, 1, 8, 1]])
mat3 = np.array([[2, -1, 5, -1, 4, 3],
                 [1, -2, 2, -2, 3, 1]])

Rmat = np.zeros(mat1.shape)

#print(np.where((mat1[:, 0] == max(mat1[:, 0])))[0][0])

for i in range(4):
    c = np.where((mat1[:, i] == max(mat1[:, i])))[0][0]
    Rmat[c][i] = 1

for i in range(3):
    x = False
    if Rmat[i].all() == 1:
        x = True
        print("la stratégie dominante est :"+ str(mat1[i]))
        break
if not x:
    print("pas de stratégie dominante")
