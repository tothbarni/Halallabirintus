class Jatekos:
    def __init__(self, nev):
        self.nev = nev
        self.eletero = 10
        self.arany = 0
        self.helyszin = "Kezdés"
        self.targyak = []

    def eletero_vesztes(self, mennyiseg):
        self.eletero -= mennyiseg
        print(f"{self.nev} veszít {mennyiseg} ÉLETERŐ pontot. Jelenlegi ÉLETERŐ: {self.eletero}")

    def arany_nyeres(self, mennyiseg):
        self.arany += mennyiseg
        print(f"{self.nev} talált {mennyiseg} aranypénzt. Jelenlegi arany: {self.arany}")

    def targy_hozzaadas(self, targy):
        self.targyak.append(targy)
        print(f"{self.nev} talált egy {targy}. Jelenlegi tárgyak: {', '.join(self.targyak)}")

    def helyszin_beallitas(self, helyszin):
        self.helyszin = helyszin
        print(f"{self.nev} most a {self.helyszin} helyszínen tartózkodik.")
