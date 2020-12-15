import os

def film():
    print("****WPROWADZ INFORMACJE O FILMIE****")
    i = 0
    baza = []
    baza.append([])

    while True:
        dane = input("Numer {}. Podaj tytul filmu: \n".format(i))
        if dane == "":
            break
        baza[i].append(dane)
        dane = input("Numer {}. Podaj rok produkcji: \n".format(i))
        baza[i].append(dane)
        dane = input("Numer {}. Podaj ocene filmu: \n".format(i))
        baza[i].append(dane)
        i +=1
        baza.append([])
    filmy = ''
    for i in range(len(baza)-1):
        filmy += "Numer" + str(i) + " " + baza[i][0] + ',' + baza[i][1] + ',' + baza[i][2]
        if(i != len(baza)-2):
            filmy +="\n"
    return filmy
    

def baza_filmow():
    fileslist = os.listdir(os.getcwd())
    if("csv_json.txt" not in fileslist):
        nowy_film = film()
        f = open("csv_json.txt", "w+", encoding='utf-8')
        f.write(nowy_film)
        f.close()
        return
    
    f = open("baza_filmow.txt", "r+", encoding='utf-8')
    text = f.read()
    f.close()
    list_of_lines = text.split("\n")
    print(text)

    while True:
        print("Podaj numer filmu, który chcesz usunąć: \n")
        do_usuniecia = input()
        if (do_usuniecia != ""):
            do_usuniecia = int(do_usuniecia)
            list_of_lines.pop(do_usuniecia)
            test = "\n".join(list_of_lines)
            print(test)
            f = open("baza_filmow.txt", "w+", encoding='utf-8')
            f.write(test)
            f.close()
            if(len(list_of_lines) == 0):
                break
        else:
            break
    f = open("baza_filmow.txt", "r+", encoding='utf-8')
    text = f.read()
    f.close()
    nowy_film = film()
    if(text == ""):
        nowy_film += text
    else:
        if(nowy_film != ""):
            nowy_film += text + "\n"
        else:
            nowy_film = text
    f = open("baza_filmow.txt", "w+", encoding='utf-8')
    f.write(nowy_film)
    f.close()

baza_filmow()
