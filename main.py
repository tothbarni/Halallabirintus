import random
from Player import Player
# A játék kezdete
def start_game():
    print("Üdvözöllek a Halállabirintusban!")
    player_name = input("Mi a neved? ")
    player = Player(player_name)
    
    # Játék kezdése
    player.set_location("Kezdés")
    print("\nA játék elkezdődött! Haladj előre, és válassz a lehetőségek közül!")

    # Kezdeti döntés
    choice1 = input("\nMiután öt percet haladtál, egy kőasztalhoz érsz. Mit teszel?\n(a) Kinyitom a dobozt\n(b) Tovább haladok észak felé\n")
    
    if choice1 == 'a':
        player.set_location("270. oldal")
        player.gain_gold(2)
        print("A dobozban két aranypénzt találsz és egy üzenetet, amely Szukumvit-től szól.")
        print("A tanács: 'Keress és használj különféle tárgyakat!'")
        choice2 = input("Folytatod észak felé? (igen/nem): ")
        if choice2 == 'igen':
            player.set_location("66. oldal")
        else:
            print("Véget ér a kaland.")
            return

    elif choice1 == 'b':
        player.set_location("66. oldal")

    # 66. oldal következik
    choice3 = input("\nNéhány perc után egy elágazáshoz érsz. Mit teszel?\n(a) Nyugat felé megyek\n(b) Kelet felé megyek\n")
    if choice3 == 'a':
        player.set_location("293. oldal")
        print("Nyugat felé mész, és hamarosan egy újabb elágazáshoz érsz.")
        choice4 = input("Folytatod nyugat felé? (igen/nem): ")
        if choice4 == 'igen':
            player.set_location("137. oldal")
        else:
            print("Véget ér a kaland.")
            return
    elif choice3 == 'b':
        player.set_location("56. oldal")
        print("Kelet felé mész, és egy sziklaszerű tárggyal találkozol.")
        choice5 = input("Átmászol rajta? (igen/nem): ")
        if choice5 == 'igen':
            player.set_location("373. oldal")
        else:
            print("Véget ér a kaland.")
            return

    # 373. oldal következik
    print("\nA szikla puha és szivacsos. Nehéz átjutni rajta, de végül sikerül.")
    choice6 = input("Most kelet felé mész tovább? (igen/nem): ")
    if choice6 == 'igen':
        player.set_location("387. oldal")
        print("Hamarosan találkozol egy Barlangi Emberrel, aki támadni fog!")
        fight(player)
    else:
        print("Véget ér a kaland.")
        return

# Harc a Barlangi Emberrel
def fight(player):
    print("Egy Barlangi Ember közeledik, kardot rántasz és felkészülsz a harcra.")
    enemy_health = 7
    enemy_skill = 7
    
    while enemy_health > 0 and player.health > 0:
        action = input("Mit teszel? (a) Támadok (b) Védekezem\n")
        if action == 'a':
            damage = random.randint(1, 5)
            enemy_health -= damage
            print(f"Te támadsz! Sebzés: {damage}. Barlangi Ember életereje: {enemy_health}")
        elif action == 'b':
            print("Megpróbálsz védekezni!")
        
        if enemy_health > 0:
            enemy_attack = random.randint(1, 3)
            player.lose_health(enemy_attack)
            print(f"A Barlangi Ember támad! Sebzés: {enemy_attack}. Jelenlegi ÉLETERŐ: {player.health}")
    
    if player.health <= 0:
        print("Sajnálom, meghaltál a harcban. A kaland véget ért.")
    elif enemy_health <= 0:
        print("Győztél a Barlangi Ember felett! Tovább haladhatsz.")
        player.set_location("A kaland folytatódik...")

# Indítás
start_game()
