from __future__ import print_function
import random
import os
import time

currentScreen = -4


def main():
    p = Player()
    n = Neighborhood()

    x = ""
    while True:
        x = paintScreen(currentScreen, p, n)
        if n.getMonsterCount() <= 0:
            clearScreen()
            print("\n\n\nYou won! You saved the neighborhood!!!\n\n\n")
            break
        if p.health <= 0:
            clearScreen()
            print("\n\n\nI hate to say it, but you died. At least you went down in a blaze of glory. Try again.\n\n\n")
            break
        if x == "q" or x == "Q":
            clearScreen()
            print("\n\n\nYou have ended the game. Thanks for playing.\n\n\n")
            break


def paintScreen(scn, p, n):
    clearScreen()
    global currentScreen
    cmd = ""
    if scn == -4:
        welcomeScreen(p, n)
        currentScreen = -3
    elif scn == -3:
        informScreen(p, n)
        cmd = raw_input("\n\n[press any key to continue...]\n--> ")
        currentScreen = -1
    elif scn == -2:
        candyMonScreen(p, n)
        cmd = raw_input("\n\n[press any key to return to game]\n--> ")
        currentScreen = -1
    elif scn == -1:
        mainScreen(p, n)
        cmd = raw_input("\n\n[Enter Command:]\n--> ")
        if cmd == "J" or cmd == "j":
            currentScreen = -2
        elif cmd == "V" or cmd == "v":
            currentScreen = -5
        elif cmd.isdigit():
            if 0 <= int(cmd) < n.numOfHomes:
                currentScreen = int(cmd)
    else:
        inhomeScreen(p, n)
        cmd = raw_input("\n\n[Enter Command:]\n--> ")
        if cmd == "J" or cmd == "j":
            currentScreen = -2
        elif cmd == "V" or cmd == "v":
            currentScreen = -5
        elif cmd == "L" or cmd == "l":
            currentScreen = -1
        elif cmd.isdigit():
            if 0 <= int(cmd) <= 9:
                if 0 < p.weapons[int(cmd)].ammo or p.weapons[int(cmd)].type == 0:
                    plyAttack = p.attack()
                    wpnMod = p.weapons[int(cmd)].getMod()
                    wpnType = p.weapons[int(cmd)].type
                    print("Attacked with " + p.weapons[int(cmd)].getName() + " with " + str(plyAttack*wpnMod))
                    p.weapons[int(cmd)].useWpn()
                    n.homes[currentScreen].subHealth(plyAttack, wpnType, wpnMod)
                else:
                    print("That weapon has no ammo!! Use another!")
                time.sleep(2)
                monAttk = n.homes[currentScreen].nonPersonAttk()
                if monAttk is not None:
                    p.subHealth(monAttk)
                    print("You were attacked you with " + str(monAttk))
                else:
                    print("There aren't anymore monsters in here!")
                p.heal(n.homes[currentScreen].cntPersons())
                print("You were healed by " + str(n.homes[currentScreen].cntPersons()))
                time.sleep(3)
    return cmd

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
def welcomeScreen(p,n):
    print("You have established a neighborhood with " + str(n.numOfHomes) + " homes. Good luck!")
    print("\nThe game will begin soon...")
    time.sleep(3)
def informScreen(p,n):
    print("YOUR NEIGHBORHOOD IS UNDER ATTACK!")
    print("Zombies, Vampires, Ghouls, and Werewolves are taking over the homes of the neighborhood. \nLuckily enough, your neighbors are trying to help you save the day!")
    print("Travel to each home in the neighborhood and use the Halloween candy you've collected to defeat the monsters \nand return them to their human form!")
    print("Once you eliminate all of the monsters, you win!")
    print("A few things to remember: ")
    print("\t(1) Certain candy is more/less effective on certain monsters-- check out your weapons page!.")
    print("\t(2) People are here to help! Each turn each Person in the home will heal you 1 HP.")
    print("\t(3) Use your candy wisely. It's all you've got!")
def candyMonScreen(p,n):
    print("CANDY")
    print("------------------")
    print("HersheyKisses:\n\tAttack Modifier: 1.00\n\tBase Ammo: UNLIMITED\n\tStrength: NONE\n\tWeakness: NONE")
    print("SourStraws:\n\tAttack Modifier: 1.00 - 1.75\n\tBase Ammo: 2\n\tStrength: Zombies(2x)\n\tWeakness: Werewolves (no effect)")
    print("ChocolateBars:\n\tAttack Modifier: 2.00 - 2.40\n\tBase Ammo: 4\n\tStrength: NONE\n\tWeakness: Vampires, Werewolves (no effect)")
    print("NerdBombs:\n\tAttack Modifier: 3.50 - 5.00\n\tBase Ammo: 1\n\tStrength: Ghouls(5x)\n\tWeakness: NONE")
    print("\n\n\n\n")
    print("MONSTERS")
    print("------------------")
    print("Zombies:\n\tAttack: 0 - 10 HP\n\tHealth: 50 - 100 HP\n\tStrength: NONE\n\tWeakness: SourStraws")
    print("Vampires:\n\tAttack: 10 - 20 HP\n\tHealth: 100 - 200 HP\n\tStrength: ChocolateBars\n\tWeakness: NONE")
    print("Ghouls:\n\tAttack: 15 - 30 HP\n\tHealth: 40 - 80 HP\n\tStrength: NONE\n\tWeakness: NerdBombs")
    print("Werewolves:\n\tAttack: 0 - 40 HP\n\tHealth: 200 HP\n\tStrength: ChocolateBars, SourStraws\n\tWeakness: SourStraws")
def mainScreen(p,n):
    print("%--------------------------------------------------------------------------------------------------------------------------------------------------------------------%")
    print("  Total Homes: " + str(n.numOfHomes) + "\t\t|   Monsters Remaining: " + str(n.getMonsterCount()) + "\t\t|   Health: " + str(p.health) +"\t\t|\t\t Commands: HomeID - (J)oural")
    print("%--------------------------------------------------------------------------------------------------------------------------------------------------------------------%")
    print("CANDY", end='')
    p.showWeapons()
    print("\n%--------------------------------------------------------------------------------------------------------------------------------------------------------------------%")
    print("\n%--------------------------------------------------------------------------------------------------------------------------------------------------------------------%")
    print("\n\nHOMES", end='')
    n.showHomes()
    print("\n\n\n%--------------------------------------------------------------------------------------------------------------------------------------------------------------------%")
def inhomeScreen(p,n):
    print("%--------------------------------------------------------------------------------------------------------------------------------------------------------------------%")
    print("  Total Homes: " + str(n.numOfHomes) + "\t\t|   Monsters Remaining: " + str(n.getMonsterCount()) + "\t\t|   Health: " + str(p.health) +"\t\t|\t\t Commands: HomeID - (J)oural - (V)iew")
    print("%--------------------------------------------------------------------------------------------------------------------------------------------------------------------%")
    print("CANDY", end='')
    p.showWeapons()
    print("\n%--------------------------------------------------------------------------------------------------------------------------------------------------------------------%")
    print("\n%--------------------------------------------------------------------------------------------------------------------------------------------------------------------%")
    print("\n\n[ HomeID: " + str(currentScreen) + " ]")
    print("\nMONSTERS")
    n.homes[currentScreen].showMonsters()



class Weapon:
    def __init__(self, id):
        self.id = id
        self.type = self.initType()
        self.ammo = self.initAmmo()

    def initType(self):
        return random.randrange(0, 4)

    def initAmmo(self):
        if self.type == 0: # HersheyKisses
            return '-'
        elif self.type == 1: # SourStraws
            return 2
        elif self.type == 2: # ChocolateBars
            return 4
        elif self.type == 3: # NerdBombs
            return 1

    def getName(self):
        if self.type == 0: # HersheyKisses
            return "HersheyKisses"
        elif self.type == 1: # SourStraws
            return "SourStraws   "
        elif self.type == 2: # ChocolateBars
            return "ChocolateBars"
        elif self.type == 3: # NerdBombs
            return "NerdBombs    "

    def getMod(self):
        if self.type == 0: # HersheyKisses
            return 1.00
        elif self.type == 1: # SourStraws
            return round(random.uniform(1.00, 1.75), 2)
        elif self.type == 2: # ChocolateBars
            return round(random.uniform(2.00, 2.40), 2)
        elif self.type == 3: # NerdBombs
            return round(random.uniform(3.50, 5.00), 2)

    def useWpn(self):
        if self.type == 0:
            pass
        else:
            self.ammo = self.ammo - 1

class Monster:
    def __init__(self, id):
        self.id = id
        self.type = self.initType()
        self.health = self.initHealth()

    def initType(self):
        return random.randrange(0, 5)

    def initHealth(self):
        if self.type == 0: # Person
            return 100
        elif self.type == 1: # Zombies
            return random.randrange(50, 100)
        elif self.type == 2: # Vampires
            return random.randrange(100, 200)
        elif self.type == 3: # Ghouls
            return random.randrange(40, 80)
        elif self.type == 4: # Werewolves
            return 200

    def getName(self):
        if self.type == 0: # Person
            return "Person  "
        elif self.type == 1: # Zombies
            return "Zombie  "
        elif self.type == 2: # Vampires
            return "Vampire "
        elif self.type == 3: # Ghouls
            return "Ghoul   "
        elif self.type == 4: # Werewolves
            return "Werewolf"

    def attack(self):
        if self.type == 0: # Person
            return -1
        elif self.type == 1: # Zombies
            return random.randrange(0, 11)
        elif self.type == 2: # Vampires
            return random.randrange(10, 21)
        elif self.type == 3: # Ghouls
            return random.randrange(15, 31)
        elif self.type == 4: # Werewolves
            return random.randrange(0, 41)

    def subHealth(self, pDamage, weaponType, wMod):
        if self.type == 0: # Person - take no damage
            pass
        elif self.type == 1: # Zombies - SourStraws 2x
            if weaponType == 1:
                self.health = self.health - (2 * (pDamage * wMod))
            else: self.health = self.health - (pDamage * wMod)
        elif self.type == 2: # Vampires - ChocolateBars 0x
            if weaponType == 2:
                pass
            else: self.health = self.health - (pDamage * wMod)
        elif self.type == 3: # Ghouls - NerdBombs 5x
            if weaponType == 3:
                self.health = self.health - (5 * (pDamage * wMod))
            else: self.health = self.health - (pDamage * wMod)
        elif self.type == 4: # Werewolves - ChocolateBars & SourStraws 0x
            if weaponType == 1 or weaponType == 2:
                pass
            else: self.health = self.health - (pDamage * wMod)
        if self.health <= 0:
            self.type = 0
            self.health = 100

class Home:
    def __init__(self, id):
        self.id = id
        self.monsters = []
        self.initMonsters()

    def initMonsters(self):
        for m in range(random.randrange(0, 11)):
            mon = Monster(m)
            self.monsters.append(mon)

    def showMonsters(self):
        for m in self.monsters:
            print("[ ID: " + str(m.id) + " | "+ m.getName() +" | Health: "+ str(m.health) + " ]\t")

    def subHealth(self, pDamage, weaponType, wMod):
        for m in self.monsters:
            m.subHealth(pDamage, weaponType, wMod)

    def nonPersonAttk(self):
        for m in self.monsters:
            if m.type != 0:
                return int(m.attack())

    def cntPersons(self):
        x = 0
        for m in self.monsters:
            if m.type == 0:
                x = x + 1
        return x



class Neighborhood:
    def __init__(self):
        self.welcome()
        self.gridX = self.setgridX()
        self.gridY = self.setgridY()
        self.numOfHomes = self.gridX * self.gridY
        self.homes = []
        self.initHomes()

    def welcome(self):
        print("Welcome to JT Kawaski's Halloween Eve Python Game!")
        print("\nTo begin, please enter the size of your neighborhood:")

    def setgridX(self):
        x = -1
        while 0 > x < 5:
            x = input("How wide is your neighborhood (ie. 2)?\n--> ")
        return x

    def setgridY(self):
        y = -1
        while 0 > y < 5:
            y = input("How long is your neighborhood (ie. 4)?\n--> ")
        return y

    def initHomes(self):
        for h in range(self.numOfHomes):
            home = Home(h)
            self.homes.append(home)

    def showHomes(self):
        for h in self.homes:
            if h.id % 5 == 0:
                print("\n")
            print("[ HomeID: " + str(h.id) + " | Occupancy: " + str(len(h.monsters)) + " ]\t", end='')

    def getMonsterCount(self):
        total = 0
        for h in self.homes:
            for m in h.monsters:
                if m.type != 0:
                    total = total + 1
        return total


class Player:
    def __init__(self):
        self.health = self.initHealth()
        self.weapons = []
        self.initWeapons()

    def initHealth(self):
        return random.randrange(100,126)

    def initWeapons(self):
        for w in range(10):
            wpn = Weapon(w)
            self.weapons.append(wpn)

    def attack(self):
        return random.randrange(10, 21)

    def subHealth(self, mDamage):
        self.health = self.health - mDamage;

    def heal(self, cnt):
        if self.health <= 150:
            self.health = self.health + int(cnt)

    def showWeapons(self):
        for w in self.weapons:
            if w.id % 5 == 0:
                print("\n")
            print("[ ID: "+ str(w.id) + " | " + w.getName() + " | " + str(w.ammo) + " ]\t", end='')


clearScreen()
main()
