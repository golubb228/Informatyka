#zad 1
print("Co potrzebne jest do programowania:\n1.Wytrwalość\n2.Systemetyczność\n3.Ćwieczemia")
#zad 2
print("\nTechnicum nr 19\nim. Marszałka Józwfa\nw Poznaniu")
#zad 3
a=str(input("\nNapisz swoje imię: "))
print(a)
#Zad 4
b=int(input("\nNapisz liczbę: "))
print(b)
#zad 5
w="w"
print(type(w))
#zad 6
dzielna=6
dzienik=3
wynik=dzielna-dzienik
print(type(wynik))
#zad 7
d=int(input("\nNapisz liczbę: "))
if d % 2 == 0:
  print("Liczba jest parzysta")
else:
  print("Liczba nie jest parztsta")
#zad 8
s=int(input("\nNapisz liczbę: "))
l=int(input("Napisz liczbę: "))
if s==0 or l==0:
  print("Błąd")
else:
  print(s/l)



#zad 2.1
q=int(input("\nNapisz minuty: "))
print(q*60)
# zad 2
e=int(input("\nNapisz podstawę: "))
e2=int(input("Napisz wysokośc: "))
e3=(e*e2)/2
print("Pole: ", e3)
#zad 3
y=int(input("\nNapisz godziny: "))
y2=y*3600
print("Masz ", y2," s")
#zad 4
t=int(input("\nNapisz 1 bok: "))
t2=int(input("Napisz 2 bok: "))
t3=t+t2-1
print("3 bok: ", t3)
#zad 5
o=int(imput("\nNapisz 1 bok: "))
o2=int(input("Napisz 2 bok: "))
o3=o+o+o2+o2
print("Obwód:", o3)
#zad 6
n=int(input("\nNapisz kąt: "))
n2=(n-2)·180
print("Suma: ", n2)
