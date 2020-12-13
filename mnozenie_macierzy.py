import random
import numpy as np


a = np.random.randint(0,500,(8,8))
print("Macierz a:", a)
b = np.random.randint(0,500,(8,8))
print("Macierz b:", b)

c = a*b
print("Iloczyn dwoch macierzy wynosi:", c)