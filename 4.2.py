#------------miarka---------------------------
def rysujmiarke():
    miarka = ""
    i = 0
    for i in range(liczba1):
        if (i == '0') or ((i % 5) == 0):
            miarka += "|"
            #print(miarka)
        else:
            miarka += "."
    miarka += "\n"
    num = 0
    j=0
    for num in range(liczba+1):
        if num < 9:
            miarka += str(num)+"    "
        else:
            miarka += str(num)+"   "
    return(miarka)
#---------------------------------------------

#-------------prostokat-----------------------
def rysujprostokat():
    rysunek = ""
    for i in range(szerokosc):
        if i > 0:
            rysunek += "\n"
        for j in range(dlugosc):
            if (i % 2) == 0:
                if (j == '0') or ((j % 4) == 0):
                    rysunek += "+"
                else:
                    rysunek += "-"
            else:
                if (j == '0') or ((j % 4) == 0):
                   rysunek += "|"
                else:
                    rysunek += " "
    return(rysunek)
#---------------------------------------------

liczba = int(input("podaj maksymalna liczbe na miarce(liczba calkowita): "))
liczba1 = liczba*5 +1 #6 bo liczymy od 0
print(rysujmiarke())


print("podaj rozmiar prostokata:")
dlugosc, szerokosc = int(input("dlugosc: ")),int(input("szerokosc: "))
dlugosc = dlugosc*4+1
szerokosc = szerokosc*2+1
print(rysujprostokat())
