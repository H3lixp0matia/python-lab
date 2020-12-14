import random
import numpy as np


a = np.random.randint(0,500,(8,8))
print("Macierz a:", a)
b = np.random.randint(0,500,(8,8))
print("Macierz b:", b)
c = np.zeros((8,8))

for i in range(len(a)):
    for j in range(len(b[0])):
        wynik = 0
        for k in range(len(a[0])):
            wynik += a[i][k]*b[k][j]
            c[i][j] = wynik



print("Iloczyn dwoch macierzy wynosi:", c)