"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import random


class Miner:
    def __init__(self, sleepiness=0, thirst=0, hunger=0, whisky=0, gold=0, turn=0):
        self.sleepiness = sleepiness
        self.thirst = thirst
        self.hunger = hunger
        self.whisky = whisky
        self.gold = gold
        self.turn = turn

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1
        print("Morris is sleeping!")

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5
        print("Morris is mining!")

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2
        print("Morris is eating!")

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1
        print("Morris is buying whisky!")

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1
        print("Morris is drinking!")

    def dead(self):
        return self.sleepiness > 100 or self.thirst > 100 or self.hunger > 100

    def __str__(self): # AI herfra
        return f"Turn: {self.turn}, Sleepiness: {self.sleepiness}, Thirst: {self.thirst}, Hunger: {self.hunger}, Whisky: {self.whisky}, Gold: {self.gold}"


# Initialiser Morris med standardværdier
morris = Miner()


# Funktionen til at vælge en handling for Morris
def choose_action(miner):
    # Hvis Morris er meget træt, skal han sove
    if miner.sleepiness > 50:
        miner.sleep()
    # Hvis Morris er meget tørstig, skal han drikke
    elif miner.thirst > 50:
        miner.drink()
    # Hvis Morris er meget sulten, skal han spise
    elif miner.hunger > 50:
        miner.eat()
    # Hvis han har penge og whisky er lav, køb whisky
    elif miner.gold > 0 and miner.whisky < 3:
        miner.buy_whisky()
    # Ellers mine guld
    else:
        miner.mine()


# Kør spillet i op til 1000 runder
while not morris.dead() and morris.turn < 1000:
    morris.turn += 1
    choose_action(morris)
    print(morris)

    # Pauser for at gøre det lettere at følge med (f.eks. hver 100. runde)
    if morris.turn % 100 == 0:
        input("Tryk på Enter for at fortsætte til næste runde...")

# Når spillet slutter, print Morris' status
if morris.dead():
    print("\nMorris er død! Spillet er slut.")
else:
    print("\nMorris har overlevet 1000 runder!")