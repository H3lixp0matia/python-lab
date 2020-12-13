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

z1 = Liczby_zespolone(1,4)
z2 = Liczby_zespolone(6,7)
Liczby_zespolone.dodawanie(z1,z2).liczba()
Liczby_zespolone.odejmowanie(z1,z2).liczba()
Liczby_zespolone.mnozenie(z1,z2).liczba()
Liczby_zespolone.dzielenie(z1,z2).liczba()
