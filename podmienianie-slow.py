plik = open(r'C:\Users\mkale\Desktop\Python-lab\text_files\poland\4_3.txt')
tekst = plik.read()
plik.close()

slownik = {"Poland": "Portugal", "voivodeship": "district", "podkarpackie": "swietokrzyskie", "Bieszczady": "Pieniny"}


for i in slownik:
 if i in tekst:  
     tekst = tekst.replace(i, slownik[i])

plik2 = open(r'C:\Users\mkale\Desktop\Python-lab\4_3.txt', 'w')

plik2.write(tekst)
plik2.close()