plik = open(r'C:\Users\mkale\Desktop\Python-lab\text_files\usa\1. FC Union Berlin.txt')
tekst = plik.read()
plik.close()

delete_list = {"to": "", "in": "","is": "", "club": ""}


for i in delete_list:
 if i in tekst:  
     tekst = tekst.replace(i, delete_list[i])

plik2 = open(r'C:\Users\mkale\Desktop\Python-lab\Union_Berlin_deleted.txt', 'w')

plik2.write(tekst)
plik2.close()