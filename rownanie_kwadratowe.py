import math

a = int(input("Podaj wsploczynnik a rownania kwadratowego: "))
b = int(input("Podaj wsploczynnik b rownania kwadratowego: "))
c = int(input("Podaj wsploczynnik c rownania kwadratowego: "))

delta = b*b-4*a*c
print("Delta wynosi: ", delta)

if delta < 0:
    print("Rownanie nie ma rozwiazan rzeczywistych")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    print("Rownanie ma jedno rozwiazanie: ", x)
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    print("Rownanie ma dwa rozwiazania: ", x1, "and", x2)