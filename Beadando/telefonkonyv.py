def start(): 
    print('Telefonkönyv\n-----------------------------------\n1. Telefonkönyv listázása\n2. Új adat bevitele\n3. Keresés név szerint\n4. Kilépés\n5. Segédlet\n-----------------------------------')

def choosenIsGood():
    while True:
        choosenOption = input('Választás (1-5): ')
        match choosenOption:
            case "1":
                firstOptionList(adatok)
                continue
            case "2":
                secondOption(adatok)
                continue
            case "3":
                thirdOption(adatok)
                continue
            case "4":
                quit()
            case "5":
                fifthOption()
            case _:
                print('Hibás menüpont választás\n')
                start()
                choosenIsGood()   

def firstOptionList(adatok):
    print('Név\t\tTelefonszám\n-----------------------------------')
    for adat in adatok:
        print(f'{adat['Nev']}\t{adat['Telefonszam']}\n')


def secondOption(adatok):
    nev, telszam, email = input('Adj meg egy nevet: '), input('Adj meg egy telefonszámot: '), input('Adj meg egy email címet: ')
    for adat in adatok:
        if adat['Nev'] == nev:
            print('Ez a név már szerepel az adatbázisban!')
            break
        else:
            secondOptionAppend(nev, telszam, email)


def secondOptionAppend(nev, telszam, email):
    with open('telefonkonyv.txt', 'a') as file:
        file.write(f'{nev};{telszam};{email}\n')


def thirdOption(adatok):
    nev = input('Kérem a nevet: ')
    for adat in adatok:
        if adat['Nev'] ==  nev:
            print(f'{adat['Nev']}   {adat['Telefonszam']}    {adat['Email']}')
            break    
    else:
        print('Nincs ilyen név a telefonkönyvben')

def fifthOption():
    with open('help.txt', 'r', encoding='utf-8') as file:
        help = []
        for adat in file:
            help.append(adat)
        print('\nEz egy segédlet a program működéséhez!\n-----------------------------------')
        for mondat in help:
            print(mondat)

start()
with open('./telefonkonyv.txt') as file:
        adatok = []
        for adat in file:
            sor = adat.strip().split(';')
            dictionary = dict()
            dictionary['Nev'] = sor[0]
            dictionary['Telefonszam'] = sor[1]
            dictionary['Email'] = sor[-1]
            adatok.append(dictionary)
choosenIsGood()