kod_odbioru = input("Ustaw haslo: ")

for i in range (2):
    wprowadzony_kod = input("Podaj kod odbioru paczki: ")

    if wprowadzony_kod == kod_odbioru:
        print("Wprowadzono poprawny kod odbioru. Odbierz paczke")
        break
    else:
        print("Wprowadzony kod jest niepoprawny. Sprobuj ponownie")
        continue