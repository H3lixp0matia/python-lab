import random
liczby = []
liczby_posortowane = []

for i in range (50):
    x = random.randint(0,500)
    liczby.append(x)
print ("Wylosowane liczby: ", liczby)

for k in range(len(liczby)):
    liczby_posortowane.append(max(liczby))
    liczby.remove(max(liczby))
print("Liczby posortowane malejaco:", liczby_posortowane)