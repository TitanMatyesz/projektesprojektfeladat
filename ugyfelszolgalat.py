def mpbe(ora,perc,masodperc):
    return ora*60*60+perc*60+masodperc

hivasok = []
f = open("hivas.txt", "rt", encoding="utf-8")

for sor in f:
    sor = sor.strip().split(" ")
    sor = list(map(int, sor))
    sor.append(mpbe(sor[0], sor[1], sor[2]))
    sor.append(mpbe(sor[3], sor[4], sor[5]))
    hivasok.append(sor)

ido = {}

for hivas in hivasok:
    if hivas[0] not in ido.keys():
        ido[hivas[0]] = 0
    
for hivas in hivasok:
    ido[hivas[0]] += 1

print("3. feladat")

for ido, darabhivas in ido.items():
    print(f"{ido} óra {darabhivas} hívás")

print("4. feladat")

maxhivas = 0
maxHivasSorszam = 0
hivasSorszam = 1

for hivas in hivasok:
    hivashossz = mpbe(hivas[3], hivas[4], hivas[5]) - mpbe(hivas[0], hivas[1], hivas[2])
    if maxhivas < hivashossz:
        maxhivas = hivashossz
        maxHivasSorszam = hivasSorszam
    hivasSorszam += 1

print(f"A legtovább tartó hívás a {maxHivasSorszam} sorban van, a hívás {maxhivas} másodperc hosszú volt.")

print("5. feladat")
idopont = input("Kérek egy időpontot!(óra, perc, másodperc)")
idopont = list(map(int, idopont.strip().split(" ")))
idomasodperc = mpbe(idopont[0], idopont[1], idopont[2])

i = 0

while i < len(hivasok) and not(mpbe(hivasok[i][0], hivasok[i][1], hivasok[i][2]) <= idomasodperc and idomasodperc < mpbe(hivasok[i][3], hivasok[i][4], hivasok[i][5])):
    i += 1

if i < len(hivasok):
    telefonalo = i + 1
else:
    telefonalo = 0

if telefonalo:
    varakozok = -1
    for hivas in hivasok:
        if mpbe(hivas[0], hivas[1], hivas[2]) <= idomasodperc and idomasodperc < mpbe(hivas[3], hivas[4], hivas[5]) :
            varakozok +=1
    print(f"A várakozók száma: {varakozok} a beszélő a {telefonalo}. hívó.")
else:
    print("Nem volt beszélő")

print("6. feladat")
utolsohivas = 0
utolsoelotti = 0
muszakvege = mpbe(12,0,0)
i = 0
for hivas in hivasok:
    kezdet = mpbe(hivas[0],hivas[1],hivas[2])
    veg = mpbe(hivas[3],hivas[4],hivas[5])
    if kezdet <= muszakvege and veg > mpbe(hivasok[utolsohivas][3],hivasok[utolsohivas][4],hivasok[utolsohivas][5]):
        utolsoelotti = utolsohivas
        utolsohivas = i
    i +=1

utolsoelottivege = mpbe(hivasok[utolsoelotti][3],hivasok[utolsoelotti][4],hivasok[utolsoelotti][5])
utolsokezdet = mpbe(hivasok[utolsohivas][0],hivasok[utolsohivas][1],hivasok[utolsohivas][2])
varakozas = utolsoelottivege - utolsokezdet

if varakozas < 0:
    varakozas = 0

print(f"Az utolsó telefonáló adatai a(z) {utolsohivas+1}. sorban vannak, {varakozas} másodpercig várt.")
