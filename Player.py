class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.gold = 0
        self.location = "Kezdés"
        self.items = []

    def lose_health(self, amount):
        self.health -= amount
        print(f"{self.name} veszít {amount} ÉLETERŐ pontot. Jelenlegi ÉLETERŐ: {self.health}")

    def gain_gold(self, amount):
        self.gold += amount
        print(f"{self.name} talált {amount} aranypénzt. Jelenlegi arany: {self.gold}")

    def add_item(self, item):
        self.items.append(item)
        print(f"{self.name} talált egy {item}. Jelenlegi tárgyak: {', '.join(self.items)}")

    def set_location(self, location):
        self.location = location
        print(f"{self.name} most a {self.location} helyszínen tartózkodik.")