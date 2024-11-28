import random

# Képesség értékek
ugyesseg = 0
eletero = 0
szerencse = 0

# Funkció a képességek dobásához
def dobj_kockaval():
    return random.randint(1, 6)

# Képességek kezdeti beállítása
def inicializal_kepessegek():
    global ugyesseg, eletero, szerencse
    ugyesseg = dobj_kockaval() + 6  # Ügyesség dobás
    eletero = dobj_kockaval() + dobj_kockaval() + 12  # Életerő dobás
    szerencse = dobj_kockaval() + 6  # Szerencse dobás
    print(f"ÜGYESSÉG: {ugyesseg}, ÉLETERŐ: {eletero}, SZERENCSE: {szerencse}")

# A harc menete
def harc(ellenfel_ugyesseg, ellenfel_eletero):
    global ugyesseg, eletero, szerencse

    # Harc elkezdése
    print("Harcolni kell!")
    
    # Támadóerő kiszámítása
    tamadoero_jatekos = dobj_kockaval() + ugyesseg
    tamadoero_ellenfel = dobj_kockaval() + ellenfel_ugyesseg
    
    print(f"A te támadóerőd: {tamadoero_jatekos}")
    print(f"Az ellenfél támadóereje: {tamadoero_ellenfel}")

    if tamadoero_jatekos > tamadoero_ellenfel:
        print("Megsebezted az ellenfelet!")
        ellenfel_eletero -= 2
        if random.randint(1, 6) <= szerencse:
            print("Szerencséd volt, még több sebzést okoztál!")
            ellenfel_eletero -= 4
        else:
            print("Balszerencséd volt, kevesebb sebzést okoztál.")
    elif tamadoero_jatekos < tamadoero_ellenfel:
        print("Az ellenfél megsebezet téged!")
        eletero -= 2
        if random.randint(1, 6) <= szerencse:
            print("Szerencséd volt, kevesebb sebzést kaptál!")
            eletero -= 1
        else:
            print("Balszerencséd volt, több sebzést kaptál.")
            eletero -= 3
    else:
        print("Kivédtétek egymás csapását, folytassátok!")
    
    print(f"Játékos életereje: {eletero}")
    print(f"Ellenfél életereje: {ellenfel_eletero}")
    
    return ellenfel_eletero, eletero

# Kaland folytatása
def kaland():
    print("Üdvözöllek a Halállabirintusban!")
    
    # Kezdeti képességek dobása
    inicializal_kepessegek()
    
    # Kezdeti szituáció
    print("Miután öt percet haladtál lassan az alagútban, egy kőasztalhoz érsz...")
    print("1. Ki akarod nyitni a dobozt?")
    print("2. Továbbmész észak felé?")
    
    valasz = input("Válaszd a lehetőséget (1 vagy 2): ")
    
    if valasz == "1":
        print("A doboz teteje könnyedén nyílik...")
        print("Két aranypénzt találsz, és egy üzenetet...")
        print("Továbbmész észak felé.")
    elif valasz == "2":
        print("Tovább mész észak felé.")
    
    # Következő helyszín, választható lehetőség
    print("Néhány perc gyaloglás után egy elágazáshoz érsz...")
    print("1. Nyugat felé mész a lábnyomokat követve.")
    print("2. Kelet felé mész.")
        
    valasz = input("Válaszd a lehetőséget (1 vagy 2): ")
    if valasz == "1":
        print("A nyugati irányba haladsz...")
        print("Egy Barlangi Emberrel találkozol!")
        ellenfel_ugyesseg = 7
        ellenfel_eletero = 7
        ellenfel_eletero, eletero = harc(ellenfel_ugyesseg, ellenfel_eletero)
        if eletero <= 0:
            print("Sajnálom, meghaltál! A játék véget ért.")
            return
    elif valasz == "2":
        print("Kelet felé mész...")
        print("Egy másik kaland vár rád!")
    
    # Következő választási lehetőség
    print("Újabb választás elé kerülsz!")
    print("1. Tovább mész, hogy kincseket találj.")
    print("2. Visszafordulsz, mert félénk vagy.")
    
    valasz = input("Válaszd a lehetőséget (1 vagy 2): ")
    if valasz == "1":
        print("Rátalálsz egy elhagyott templomra!")
        print("Benne rejtett kincsek és titkok várnak!")
        print("De vigyázz, csapdák is lehetnek!")
    elif valasz == "2":
        print("Visszafordulsz, de eltévedsz az alagútban...")
        print("Az idő telik, és végül kimerülsz.")

    # Életerő ellenőrzés
    if eletero <= 0:
        print("Sajnálom, meghaltál! A játék véget ért.")
    else:
        print("A kaland folytatódik...")

# A program kezdete
kaland()
