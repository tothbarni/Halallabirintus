from Jatekos import Jatekos

def elso_oldal(jatekos):
    print("Miután öt percet haladtál lassan az alagútban, egy kőasztalhoz érsz, amely a bal oldali fal mellett áll. Hat doboz van rajta, egyikükre a te neved festették.")
    print("Ha ki akarod nyitni a dobozt, lapozz a 270-re.")
    print("Ha inkább tovább haladsz észak felé, lapozz a 66-ra.")

def oldal_56(jatekos):
    print("Látod, hogy az akadály egy széles, barna, sziklaszerű tárgy. Megérinted, és meglepve tapasztalod, hogy lágy, szivacsszerű.")
    print("Ha át szeretnél mászni rajta, lapozz a 373-ra.")
    print("Ha ketté akarod vágni a kardoddal, lapozz a 215-re.")

def oldal_66(jatekos):
    print("Néhány perc gyaloglás után egy elágazáshoz érsz az alagútban. Egy, a falra festett fehér nyíl nyugatfelé mutat. A földön nedves lábnyomok jelzik, merre haladtak az előtted járók.")
    print("Ha nyugat felé kívánsz menni, lapozz a 293-ra.")
    print("Ha keletnek, lapozz a 56-ra.")

def oldal_137(jatekos):
    print("Ahogy végigmész az alagúton, csodálkozva látod, hogy egy jókora vasharang csüng alá a boltozatról.")

def oldal_215(jatekos):
    print("Kardod könnyedén áthatol a spóragolyó vékony külső burkán. Sűrű barna spórafelhő csap ki, és körülvesz. Némelyik spóra a bőrödhöz tapad, és rettenetes viszketést okoz.")
    jatekos.eletero_vesztes(2)
    print("Vadul vakarózva átléped a leeresztett golyót, és keletnek veszed az utad.")

def oldal_270(jatekos):
    print("A doboz teteje könnyedén nyílik. Benne két aranypénzt találsz, és egy üzenetet, amely egy kis pergamenen neked szól.")
    jatekos.arany_nyeres(2)
    print("Előbb zsebre vágod az aranyakat, aztán elolvasod az üzenetet: - „Jól tetted. Legalább volt annyi eszed, hogy megállj és elfogadd az ajándékot.”")
    print("Lapozz a 66-ra.")

def oldal_293(jatekos):
    print("A három pár nedves lábnyomot követve az alagút nyugati elágazásában hamarosan egy újabb elágazáshoz érsz.")
    print("Ha továbbmész nyugat felé a lábnyomokat követve, lapozz a 137-re.")
    print("Ha inkább észak felé mész a harmadik pár lábnyom után, lapozz a 387-re.")

def oldal_373(jatekos):
    print("Fölmászol a lágy sziklára, attól tartasz, hogy bármelyik pillanatban elnyelhet. Nehéz átvergődni rajta, de végül átvergődsz rajta. Megkönnyebbülten érsz újra szilárd talajra, és fordulsz kelet felé.")

def oldal_387(jatekos):
    print("Hallod, hogy elölről súlyos lépések közelednek. Egy széles, állatbőrökbe öltözött, kőbaltás, primitív lény lép elő.")
    print("Ahogy meglát, morog, a földre köp, majd a kőbaltát felemelve közeledik, és mindennek kinéz, csak barátságosnak nem.")
    print("Barlangi Ember ÜGYESSÉG 7 ÉLETERŐ 7")

def vege_kiir(jatekos):
    print(f"Vége! {Jatekos.eletero} ÉLETERŐ pontod maradt, {Jatekos.arany} aranyat gyűjtöttél, és ezeket szerezted: {', '.join(Jatekos.targyak)}.")

def oldal_allitas(jatekos, oldal):
    if oldal == 270:
        oldal_270(jatekos)
        oldal_allitas(jatekos, 66)
    elif oldal == 66:
        oldal_66(jatekos)
    elif oldal == 56:
        oldal_56(jatekos)
    elif oldal == 215:
        oldal_215(jatekos)
    elif oldal == 373:
        oldal_373(jatekos)
    elif oldal == 387:
        oldal_387(jatekos)
    elif oldal == 293:
        oldal_293(jatekos)
    elif oldal == 137:
        oldal_137(jatekos)
    else:
        print("Nincs ilyen oldal! Kérlek, adj meg egy érvényes oldalszámot.")

def jatekmenet():
    jatekos = Jatekos("Kalandor")
    print("Egy versenyre nevezel, aminek a lényege, hogy át kell kelni a halállabirintuson.")
    print("A labirintusban tárgyakat találhatsz és szörnyekkel kell harcolnod.")
    elso_oldal(jatekos)
    while True:
        try:
            oldal = int(input("Hova szeretnél lapozni? : "))
            oldal_allitas(jatekos, oldal)
        except ValueError:
            print("Kérlek, számot adj meg!")
        except KeyboardInterrupt:
            print("\nA játék megszakadt.")
            break