class Liczby_zespolone:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def liczba(self):
        if self.imag >= 0:
            print("{}+{}i".format(self.real, self.imag))
        else:
            print("{}-{}i".format(self.real, abs(self.imag)))

    def dodawanie(z1,z2):
        print("Suma dwoch liczb zespolonych wynosi: ")
        return Liczby_zespolone(z1.real + z2.real, 
                                z1.imag + z2.imag)
    
    def odejmowanie(z1,z2):
        print("Roznica dwoch liczb zespolonych wynosi: ")
        return Liczby_zespolone(z1.real - z2.real, 
                                z1.imag - z2.imag)

    def mnozenie(z1,z2):
        print("Iloczyn dwoch liczby zespolonych wynosi: ")
        return Liczby_zespolone(z1.real*z2.real - z1.imag*z2.imag, 
                                z1.real*z2.imag + z1.imag*z2.real)

    def dzielenie(z1,z2):
        licznik_real = z1.real*z2.real - z1.imag*z2.imag
        licznik_imag = z1.real*z2.imag + z1.imag*z2.real
        mianownik = z2.real**2 + z2.imag**2
        print("Iloraz dwoch liczb zespolonych wynosi: ")
        return Liczby_zespolone(licznik_real/mianownik, 
                                licznik_imag/mianownik)

a = int(input("Podaj czesc rzeczywista pierwszej liczby zespolonej: "))
b = int(input("Podaj czesc urojona pierwszej liczby zespolonej: "))
c = int(input("Podaj czesc rzeczywista drugiej liczby zespolonej: "))
d = int(input("Podaj czesc urojona drugiej liczby zespolonej: "))

z1 = Liczby_zespolone(a,b)
z2 = Liczby_zespolone(c,d)

opcja = int(input("Wybierz dzialanie, jakie chcesz wykonac: 1-dodawanie, 2-odejmowanie, 3-mnozenie, 4-dzielenie: "))

if opcja == 1:
    Liczby_zespolone.dodawanie(z1,z2).liczba()
elif opcja == 2:
    Liczby_zespolone.odejmowanie(z1,z2).liczba()
elif opcja == 3:
    Liczby_zespolone.mnozenie(z1,z2).liczba()
elif opcja == 4:
    Liczby_zespolone.dzielenie(z1,z2).liczba()
else:
    print("Nie ma takiego dzialania")
