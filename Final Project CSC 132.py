from Tkinter import *
from random import *



class Fighter(object):
    def __init__(self, name, avatar):
        # every character has health bar
        # moves
        # name
        # avatar img
        self.name = name
        self.avatar = avatar
        self.maxHealth = 0
        self.health = 10
        self.moves = {}
        self.inventory = []
        self.potion = 0
        self.opponent = ""
        self.wins = 0
        self.maxMana = 50
        self.mana = 50
        self.mainChar = False

    # decorators
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def opponent(self):
        return self._opponent

    @opponent.setter
    def opponent(self, value):
        self._opponent = value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value > self.maxMana:
            self._mana = self.maxMana
        else:
            self._mana = value

    @property
    def maxHealth(self):
        return self._maxHealth

    @maxHealth.setter
    def maxHealth(self, value):
        self._maxHealth = value

    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, value):
        self._wins = value

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value > self.maxHealth:
            self._health = self.maxHealth
        else:
            self._health = value

    @property
    def potion(self):
        return self._potion

    @potion.setter
    def potion(self, value):
        self._potion = value

    @property
    def moves(self):
        return self._moves

    @moves.setter
    def moves(self, value):
        self._moves = value

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory = value

    def setHealth(self, health):
        self._health = health

    # base attack function
    #def attack(self):
    #    self.enemy.health -= 10

    # key = move/ value= health
    def addMove(self, move, dmg, cost):
        self._moves[move] = dmg, cost

    # add item to the inventory
    def addDrop(self, items):
        self.items = ["sword", "gun", "healthkit"]
        self.inventory.append(items[randint(0, len(items))])


    def __str__(self):
        num = 1
        s = ""
        if self.mainChar != False:
            s = "{} vs {}\n\n".format(self.name, self.opponent)
            s += "Your move set: "
            for move in self.moves.keys():
                if num == len(self.moves):
                    s += move
                else:
                    s += move + " - "
                    num += 1
            s += "\n\n"
            s += "Current health: {} / {}\n\n".format(self.health, self.maxHealth)
            s += "\n\n"
            s += "Current mana: {} / {}\n\n".format(self.mana, self.maxMana)
            if self.potion == 1:
                s += "You have " + str(self.potion) + " potion left"
            else:
                s += "You have " + str(self.potion) + " potions left"
            s += "\n\n"
            s += "You have beaten " + str(self.wins) + " barbarians"
            s += "\n\n"

        else:
            s += "Their move set: "
            for move in self.moves.keys():
                if num == len(self.moves):
                    s += move
                else:
                    s += move + " - "
                    num += 1
            s += "\n\n"
            s += "Enemy health: {} / {}\n\n".format(self.health, self.maxHealth)


        return s


##########################################################################################################
# the GUI and main gameplay mechanics
class Main(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.mainCharacter = None
        self.enemyChar = None


        # layout of the main menu
        self.title = Label(parent, text="Welcome to Fighthon!", font=("Comic Sans", 30, "bold"), pady=40, bg="white",
                           fg="black")
        self.title.pack()

        # starts the game
        self.start = Button(parent, text="Start Game", command=self.start, pady=20, width=60)
        self.start.pack()

        # exits the game
        self.exit = Button(parent, text="Exit", command=exit, pady=2, width=10)
        self.exit.pack(side=BOTTOM)

    # enemy function who you will fight
    def enemy(self):
        x = randint(0, 4)
        h = ["barbarian.gif", "goblin.gif", "thief.gif", "wild wolf.gif", "???.gif"]
        y = ["Barbarian", "Goblin", "Thief", "Wild Wolf", "???"]
        enemy1 = Fighter(y[0], h[0])
        enemy1.setHealth(randint(50, 100))
        enemy1.maxHealth = enemy1.health
        enemy1.addMove("charge", 35, 0)
        enemy1.addMove("quick slash", 20, 0)
        self.enemyChar = enemy1

    def attackMove(self, ability = None):
        if ability == None:
            self.enemyChar.health -= 10
            self.mainCharacter.health -= randint(1, 2)
            statsList.delete("1.0", "end")

            if self.mainCharacter.health <= 0:
                statsList.insert(END, "You lost!" + "\n\n" + "You have defeated " + str(self.mainCharacter.wins) + " barbarians!")
                buttonPanel.destroy()

            elif self.enemyChar.health <= 0:
                self.enemy()
                self.mainCharacter.enemy = self.enemyChar
                self.mainCharacter.wins += 1
                self.mainCharacter.potion += 1
                statsList.insert(END, self.mainCharacter)
                statsList.insert(END, self.enemyChar)

            else:
                statsList.insert(END, self.mainCharacter)
                statsList.insert(END, self.enemyChar)
        else:
            h, c = self.mainCharacter.moves[ability]
            if self.mainCharacter.mana >= c:
                self.enemyChar.health -= h
                self.mainCharacter.mana -= c
                self.mainCharacter.health -= randint(1, 2)
                statsList.delete("1.0", "end")

                if self.mainCharacter.health <= 0:
                    statsList.insert(END, "You lost!" + "\n\n" + "You have defeated " + str(self.mainCharacter.wins) + " barbarians!")
                    buttonPanel.destroy()


                elif self.enemyChar.health <= 0:
                    self.enemy()
                    self.mainCharacter.enemy = self.enemyChar
                    self.mainCharacter.wins += 1
                    self.mainCharacter.potion += 1
                    statsList.insert(END, self.mainCharacter)
                    statsList.insert(END, self.enemyChar)


                else:
                    statsList.insert(END, self.mainCharacter)
                    statsList.insert(END, self.enemyChar)
            else:
                statsList.delete("1.0", "end")
                statsList.insert(END, self.mainCharacter)
                statsList.insert(END, self.enemyChar)
                statsList.insert(END, "You don't have enough mana for that ability!")

    def abilityButtons(self):

        global buttonPanel
        buttonPanel.destroy()
        secondButton = Frame(fight)
        buttonPanel = secondButton
        buttonPanel.pack(side=LEFT)

        attackButton = Button(buttonPanel, text="Attack", command=self.attackMove, pady=25, width=50, state=ACTIVE)
        attackButton.pack()

        potionButton = Button(buttonPanel, text="Potion", command=self.usePotion, pady=25, width=50)
        potionButton.pack()

        abilitiesButton = Button(buttonPanel, text="Abilities", command=self.useAbilities, pady=25, width=50)
        abilitiesButton.pack()

    def updateStats(self):
        global statsList

        statsList.delete("1.0", "end")
        statsList.insert(END, self.mainCharacter)
        statsList.insert(END, self.enemyChar)
        statsList.config(state=NORMAL)



    def usePotion(self):
        statsList.delete("1.0", "end")
        if self.mainCharacter.potion > 0:
            self.mainCharacter.potion -= 1
            self.mainCharacter.health += 15
            statsList.insert(END, self.mainCharacter)
            statsList.insert(END, self.enemyChar)
        else:
            statsList.insert(END, self.mainCharacter)
            statsList.insert(END, self.enemyChar)
            statsList.insert(END, "You can't use a potion you don't have!")

    def useAbilities(self):
        global buttonPanel
        buttonPanel.destroy()
        secondButton = Frame(fight)
        buttonPanel = secondButton
        buttonPanel.pack(side=LEFT)
        for i in self.mainCharacter.moves:
            a, c = self.mainCharacter.moves[i]
            abilityButton = Button(buttonPanel, text=str(i) + "\n\n" + "mana cost: " + str(c), command= lambda: (self.attackMove(i)), pady=25, width=50, state=ACTIVE)
            abilityButton.pack()
        backButton = Button(buttonPanel, text="back", command=self.abilityButtons, pady=25, width=50, state=ACTIVE)
        backButton.pack()




    # starts the game, changing the window
    # the gameplay window
    def start(self):
        global window
        menu.destroy()
        window = Tk()
        window.title("Fighthon - Now Playing")
        window.configure(background="white", cursor="arrow")
        window.attributes("-fullscreen", True)


        # blank space followed by choose your fighter text
        self.blank = Label(window, text="", pady=50, bg="white")
        self.blank.pack()

        self.choice = Label(window, text="CHOOSE YOUR FIGHTER", font=("Comic Sans", 45, "bold", "italic"), pady=75,
                            bg="white", fg="black")
        self.choice.pack()

        # choose your fighter buttons: gunsmith, magician, brawler, or demolitionist
        self.gunsmith = Button(window, text="Gunsmith", command=self.chooseGunsmith, pady=25, width=60)
        self.gunsmith.pack()

        self.magician = Button(window, text="Magician", command=self.chooseMagician, pady=25, width=60)
        self.magician.pack()

        self.brawler = Button(window, text="Brawler", command=self.chooseBrawler, pady=25, width=60)
        self.brawler.pack()

        self.demo = Button(window, text="Demolitionist", command=self.chooseDemo, pady=25, width=60)
        self.demo.pack()

        # exits the game
        self.exit = Button(window, text="Exit", command=exit, pady=2, width=10)
        self.exit.pack(side=BOTTOM)

        window.mainloop()

    def fightWindow(self):
        global window
        global fight
        window.destroy()
        fight = Tk()
        fight.title("Fighthon - In Game")
        fight.configure(background = "red")
        fight.attributes("-fullscreen", True)
        #mixer.music.init()
        #mixer.music.load("song.wav")
        #mixer.play()


        self.exit = Button(fight, text="Exit", command=exit, pady=2, width=10)
        self.exit.pack(side=BOTTOM)

        img = PhotoImage(file=self.mainCharacter.avatar)
        imgScreen = Label(fight, image=img)
        imgScreen.pack(side=BOTTOM)
        imgScreen.pack_propagate(False)

        img1 = PhotoImage(file=self.enemyChar.avatar)
        imgScreen1 = Label(fight, image=img1)
        imgScreen1.pack(side=RIGHT)
        imgScreen1.pack_propagate(False)

        statPanel = Frame(fight)
        statPanel.pack(side=RIGHT)

        global statsList
        statsList = Text(statPanel, bg="white")
        statsList.pack()
        statsList.insert(END, self.mainCharacter)
        statsList.insert(END, self.enemyChar)
        statsList.config(state=NORMAL)

        global buttonPanel
        buttonPanel = Frame(fight)
        buttonPanel.pack(side=LEFT)


        self.abilityButtons()

        statPanel = Frame(fight)
        statPanel.pack(side=RIGHT)



        fight.mainloop()

    # button commands
    # choose gunsmith
    def chooseGunsmith(self):
        c1 = Fighter("Gunsmith", "gunsmith.gif")
        Main.character = c1



        # Gunsmith stats
        c1.maxHealth = 65
        c1.setHealth(65)
        c1.addMove("Buckshot", 25, 10)
        c1.addMove("Pistol Whip", 50, 25)
        c1.potion = 3

        self.enemy()
        c1.opponent = self.enemyChar.name
        c1.mainChar = True
        self.mainCharacter = c1
        self.fightWindow()


    # choose magician
    def chooseMagician(self):
        c2 = Fighter("Magician", "magician.gif")
        Main.character = c2

        # Magician stats
        c2.maxHealth = 75
        c2.setHealth(75)
        c2.addMove("Wind Blast", 30, 15)
        c2.addMove("Lightning Bolt", 40, 25)
        c2.potion = 5
        c2.maxMana = 75
        c2.mana = 75

        self.enemy()
        c2.opponent = self.enemyChar.name
        c2.mainChar = True
        self.mainCharacter = c2
        self.fightWindow()


    # choose brawler
    def chooseBrawler(self):
        c3 = Fighter("Brawler", "brawler.gif")
        Main.character = c3
        # Brawler stats
        c3.maxHealth = 100
        c3.setHealth(100)
        c3.addMove("Flying Knee", 35, 10)
        c3.addMove("Swift Jab", 20, 5)
        c3.potion = 2
        c3.maxMana = 30
        c3.mana = 30

        self.enemy()
        c3.opponent = self.enemyChar.name
        c3.mainChar = True
        self.mainCharacter = c3
        self.fightWindow()


    # choose demolitionist
    def chooseDemo(self):
        c4 = Fighter("Demolitionist", "demo.gif")
        Main.character = c4

        # Demolitionist stats
        c4.maxHealth = 80
        c4.setHealth(80)
        c4.addMove("Shell Shock", 60, 5)  # 20 damage but -15 health to self
        c4.potion = 4
        c4.maxMana = 10
        c4.mana = 10


        self.enemy()
        c4.opponent = self.enemyChar.name
        c4.mainChar = True
        self.mainCharacter = c4
        self.fightWindow()


#########################################################################
# create the window
menu = Tk()
menu.title("Fighthon")
menu.geometry("800x500")
menu.configure(background="white", cursor="arrow")

# create the GUI as a Tkinter canvas inside the window
g = Main(menu)

# wait for the window to close
menu.mainloop()