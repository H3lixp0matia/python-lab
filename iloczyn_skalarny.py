a = (1, 2, 12, 4)
b = (2, 4, 2, 8)


scalar = 0

for i in range(len(a)):
    scalar = scalar + a[i]*b[i]

print("Iloczyn skalarny wektorow wynosi: ", scalar)