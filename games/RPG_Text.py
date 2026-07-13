
import random

def play_sound(file_path):
    playsound(file_path)

class DefinePlayer:
    def __init__(self,health,mana,sword,gold,items,armor,poisonActive):
        self.health = health
        self.mana = mana
        self.sword = sword
        self.gold = gold
        self.items = items
        self.armor = armor
        self.poisonActive = poisonActive
        
Player = DefinePlayer(100,10,{'name' : 'Wooden Sword', 'minAtackDamage' : 10, 'maxAtackDamage' : 30},0,[],{'name' : "No armor", 'defence' : 0},False)
print("Hello adventurer")

PlayerInput = input("Would you like to play in\n1) Hard mode\n2) Normal mode")
HardMode = False
wonTheGame = False
turnsTillDoom = 30

if PlayerInput == "1":
    HardMode = True
else:
    HardMode = False

def showItems():
    print("Your items:")
    for i,v in enumerate(Player.items):
        print(f"{i + 1}) {v}")
        
def ItemHandler():
    print("Your items:")
    for i,v in enumerate(Player.items):
        print(f"{i + 1}) {v}")
    
    print("\n")
    PlayerInput = input("What item would you like to choose?")
    try:
        if Player.items[int(PlayerInput) -1] == "healing potion":
            print("You healed 20 HP!")
            Player.health += 20
        elif Player.items[int(PlayerInput)] == "dinamite":
            Player.items.pop(int(PlayerInput) -1)
            return "Used dinamite"
        elif Player.items[int(PlayerInput)] == "poison":
            Player.items.pop(int(PlayerInput) -1)
            return "Used poison"
        Player.items.pop(int(PlayerInput) -1)
       
    except:
        print("?")
        pass
            
def fightCreature(turnsTillDoom):
    rand = random.randint(1,100)
    print("\n")
    if turnsTillDoom <= 0 and HardMode == True:
        print("It's a Super-Mega-Octopus!!!!")
        CreatureHealth = 400
        CreatureMaxHealth = 400
        CreatureMaxDamage = 100
        SomeOneWon = False
        
        while CreatureHealth > 0 and Player.health > 0:
            rand = random.randint(1,CreatureMaxDamage)
            rand = round(rand - (rand * (Player.armor['defence'] / 100)))
            print(f"The god Dealt {rand} damage to you")
            Player.health -= rand
            print(f"Yor health: {Player.health} The unholy god health: {CreatureHealth}")
        
            rand = random.randint(1,4)
            if rand == 1:
                print('"What a pity!"')
            elif rand == 2:
                print('"You peasant!"')
            elif rand == 3:
                print('"Week fly, you shall die!"')
            elif rand == 4:
                print('"Youre nothing against the fearsome me!"')

            PlayerInput = input("What would you like to do?\n1) Fight!\n2) Use an item: ")
        
            if PlayerInput == "1":
                rand = random.randint(Player.sword['minAtackDamage'],Player.sword['maxAtackDamage'])
                print(f"you have dealt {rand} Damage to the beast")
                CreatureHealth -= rand
        
                rand = random.randint(1,4)
                if rand == 1:
                    print('"What a pity!"')
                elif rand == 2:
                    print('"You peasant!"')
                elif rand == 3:
                    print('"Week fly, you shall die!"')
                elif rand == 4:
                    print('"Youre nothing against the fearsome me!"')
                
                if random.randint(1,5) == 5:
                    print('"The creature has given itself 200 health!"')
                    CreatureHealth += 200
                    if CreatureHealth > CreatureMaxHealth:
                        CreatureHealth = CreatureMaxHealth
                
                print(f"Your health {Player.health} The unholy god health {CreatureHealth}")
                
            else:
                Output = ItemHandler() 
                print(Output)
                if Output == "Used dinamite":
                    print("\n... did it all end with just a simple item?\n\n\nThe creature laying down seems as it has something in it's mouth,\n and it's glowing.\nOnce you looked closer you saw that it's still brithing\nbut when you tried to finish it, it started levetating\nThe creature started glowing red as it's eyes opened, it seems as it grew enen stronger!\nIt took the energy out of the dinamite")
                    CreatureMaxHealth = 600
                    CreatureHealth = 600
                    CreatureMaxDamage = 150
                    print(f"Your health {Player.health} The unholy god health {CreatureHealth}")
                elif Output == "Used poison":
                    print("He gulped it like bear")
        if Player.health > 0:
            print("You won the game!") #You won
            return "You sussy backa"
    elif rand > 0 and rand < 60:
        
            
        print("Its a snake!")
        CreatureHealth = 20
        if Player.poisonActive == True:
            Player.poisonActive = False
            CreatureHealth -= round( CreatureHealth * 0.75 )
        SomeOneWon = False
        while not SomeOneWon:
            
            rand = random.randint(0,5)
            rand = round(rand - (rand * (Player.armor['defence'] / 100)))
            if rand == 0:
                print("He missed!")
            else:
                print("He bit you!")
                print(f"You took {rand} damage!")
                Player.health -= rand
            print(f"your health: {Player.health} it's health: {CreatureHealth}\n")
            
            print("Your turn!")
            PlayerInput = input("What would you like to do?\n1) Fight!\n2) Run...\n3)Use an item: ")
            if PlayerInput == "1":
                rand = random.randint(Player.sword['minAtackDamage'],Player.sword['maxAtackDamage'])
                print(f"It took {rand} damage!\n")
                CreatureHealth -= rand
            
            elif PlayerInput == "2":
                print("You run off!")
                SomeOneWon = True
            
            elif PlayerInput == "3":
                Output = ItemHandler()
                if Output == "Used dinamite":
                    CreatureHealth = 0
                elif Output == "Used poison":
                    CreatureHealth -= round(CreatureHealth * 0.5)
                    Player.poisonActive = True
                
            if CreatureHealth <= 0:
                rand = random.randint(5,20)
                print(f"You won and got {rand} Gold")
                Player.gold += rand
                SomeOneWon = True
            elif Player.health <= 0:
                print("You died!")
                SomeOneWon = True
                
    elif rand > 59 and rand < 80:
        print("Its a Goblin!!")
        CreatureHealth = 50
        CreatureHealth = 20
        if Player.poisonActive == True:
            Player.poisonActive = False
            CreatureHealth -= round( CreatureHealth * 0.75 )
        SomeOneWon = False
        while not SomeOneWon:
            rand = random.randint(0,10)
            rand = round(rand - (rand * (Player.armor['defence'] / 100)))
            if rand == 0:
                print("He missed!")
            else:
                print("He bit you!")
                print(f"You took {rand} damage!")
                Player.health -= rand
            print(f"your health: {Player.health} it's health: {CreatureHealth}\n")

            print("Your turn!")
            PlayerInput = input("What would you like to do?\n1) Fight!\n2) Run...\n3)Use an item: ")
            if PlayerInput == "1":
                rand = random.randint(Player.sword['minAtackDamage'],Player.sword['maxAtackDamage'])
                print(f"It took {rand} damage!\n")
                CreatureHealth -= rand
                
            elif PlayerInput == "2":
                print("You run off!")
                SomeOneWon = True
            
            elif PlayerInput == "3":
                Output = ItemHandler()
                if Output == "Used dinamite":
                    CreatureHealth = 0
                elif Output == "Used poison":
                    CreatureHealth -= round(CreatureHealth * 0.5)
                    Player.poisonActive = True
                
            if CreatureHealth <= 0:
                rand = random.randint(10,40)
                print(f"You won and got {rand} Gold")
                Player.gold += rand
                SomeOneWon = True
            elif Player.health <= 0:
                print("You died!")
                SomeOneWon = True
                
    elif rand > 79 and rand < 95:
        print("Its a Dragon!!!")
        CreatureHealth = 100
        CreatureHealth = 20
        if Player.poisonActive == True:
            Player.poisonActive = False
            CreatureHealth -= round( CreatureHealth * 0.75 )
        SomeOneWon = False
        while not SomeOneWon:
            rand = random.randint(0,30)
            rand = round(rand - (rand * (Player.armor['defence'] / 100)))
            if rand == 0:
                print("He missed!")
            else:
                print("He bit you!")
                print(f"You took {rand} damage!")
                Player.health -= rand
            print(f"your health: {Player.health} it's health: {CreatureHealth}\n")

            print("Your turn!\n")
            PlayerInput = input("What would you like to do?\n1) Fight!\n2) Run...\n3)Use an item: ")
            print(PlayerInput)
            print(PlayerInput == "1")
            if PlayerInput == "1":
                rand = random.randint(Player.sword['minAtackDamage'],Player.sword['maxAtackDamage'])
                print(f"It took {rand} damage!\n")
                CreatureHealth -= rand
            
            elif PlayerInput == "2":
                print("You run off!")
                SomeOneWon = True
                
            elif PlayerInput == "3":
                Output = ItemHandler()
                if Output == "Used dinamite":
                    CreatureHealth = 0
                elif Output == "Used poison":
                    CreatureHealth -= round(CreatureHealth * 0.5)
                    Player.poisonActive = True

            if CreatureHealth <= 0:
                rand = random.randint(20,60)
                print(f"You won and got {rand} Gold")
                Player.gold += rand
                SomeOneWon = True
            elif Player.health <= 0:
                print("You died!")
                SomeOneWon = True
    
    elif rand > 95 and rand < 99:
        print("Its a Cutie-Pie!!... ")
        CreatureHealth = 1
        SomeOneWon = False
        
        PlayerInput = input("1) Hurt the little guy\n2)Hug it\n3)Run away")
        
        if PlayerInput == "1":
            print("once your knife touched it, you coulndn't go back\nyou didn't close your eyes but it all turned black\nyou felt like you are being dragged to The Underworld\nthat's all for you\nYou coward...")
            Player.health = 0
        elif PlayerInput == "2":
            print("you suddenly feel a relief, like the angels came from above, te little guy smiles at you, and says hi,\nI am Coots, an angel from above, and you my royal friend, won my love.\n Take infinite health.\n You shall not die")
            Player.health = 9999999999999999
        else:
            print("The little guy looks at you with a friendly smile, then continues to wonder away")
        
    elif rand > 98 and rand < 100:
        print("It's a Super-Mega-Octopus!!!!")
        CreatureHealth = 400
        CreatureMaxHealth = 400
        CreatureMaxDamage = 100
        SomeOneWon = False
        
        while CreatureHealth > 0 and Player.health > 0:
            rand = random.randint(1,CreatureMaxDamage)
            print(f"The god Dealt {rand} damage to you")
            Player.health -= round(rand - (rand * (Player.armor['defence'] / 100)))
            print(f"Yor health {Player.health} The unholy god health {CreatureHealth}")
        
            rand = random.randint(1,4)
            if rand == 1:
                print("What a pity!")
            elif rand == 2:
                print("You peasant!")
            elif rand == 3:
                print("Week fly, you shall die!")
            elif rand == 4:
                print("You're nothing against the fearsome me!")

            PlayerInput = input("What would you like to do?\n1) Fight!\n2) Use an item: ")
        
            if PlayerInput == "1":
                rand = random.randint(Player.sword['minAtackDamage'],Player.sword['maxAtackDamage'])
                print(f"you have dealt {rand} Damage to the beast")
                CreatureHealth -= rand
        
                rand = random.randint(1,4)
                if rand == 1:
                    print("What a pity!")
                elif rand == 2:
                    print("You peasant!")
                elif rand == 3:
                    print("Week fly, you shall die!")
                elif rand == 4:
                    print("You're nothing against the fearsome me!")
                
                if random.randint(1,5) == 5:
                    print("The creature has given itself 200 health!")
                    CreatureHealth += 200
                    if CreatureHealth > CreatureMaxHealth:
                        CreatureHealth = CreatureMaxHealth
                
                print(f"Your health {Player.health} The unholy god health {CreatureHealth}")
                
            else:
                Output = ItemHandler() 
                print(Output)
                if Output == "Used dinamite":
                    print("\n... was it that simple? did you finish the beast with a stick of explosives?\n\n\nThe creature laying down seems as if it has something in it's mouth,\n and it's glowing.\nUpon close inspection you saw that it's still breathing\nBut when you tried to deal the final blow, it started levitating\nThe creature started glowing red as it's eyes opened, it seems as it grew even stronger!\nIt took the energy from the dinamite")
                    CreatureMaxHealth = 600
                    CreatureHealth = 600
                    CreatureMaxDamage = 150
                    print(f"Your health {Player.health} The unholy god health {CreatureHealth}")
                elif Output == "Used poison":
                    print("He gulped it like bear")

        if Player.health > 0:
            print("\nYou won the game!") #You won
            return "You sussy backa"
def turn(turnsTillDoom):
    turnsTillDoom -= 1
    if Player.health <= 0:
        print("Game Over")
        return True
    
    print("\nYou start moving...")
    print(f"Your stats: {Player.gold} Gold, {Player.health} health")

    rand = random.randint(1,3)
    if rand == 1:
        print("You've encountered a creature...")
        Output = fightCreature(turnsTillDoom)
        if Output == True:
            return True
        if Output == "You sussy backa":
            return "You sussy backa"
    elif rand == 2:
        PlayerInput = input("You found a market,\n would you like to go in?\n yes/no: ")
        Player.poisonActive = False
        
        if PlayerInput == "yes":
            PlayerInput = input("In the market there is\n1) healing potion: Cost: 4 gold info: Heals 20 HP\n2) dinamite: Cost: 15 gold info: instakills ANY entity\n 3) poison: Cost: 8 Info: lowers your aponent's health by 50%,\n then, if the turn after is a incounter again,\nit lowers the enemys health by 25%\n4) leave:")
            
            if PlayerInput == "1":
                if Player.gold >= 4:
                    Player.gold -= 4
                    Player.items.append("healing potion")
                    showItems()
                    
            elif PlayerInput == "2":
                if Player.gold >= 15:
                    Player.gold -= 15
                    Player.items.append("dinamite")
                    showItems()
            
            elif PlayerInput == "3":
                if Player.gold >= 8:
                    Player.gold -= 8
                    Player.items.append("poison")
                    showItems()
            else:
                print("You left the shop")
               
    elif rand == 3:
        PlayerInput = input("You found an armory,\n would you like to go in?\n yes/no: ")
        Player.poisonActive = False

        if PlayerInput == "yes":
            print(f"Your Current Sword: {Player.sword['name']}: {Player.sword['minAtackDamage']}-{Player.sword['maxAtackDamage']} damage")
            print(f"Your Current Armor: {Player.armor['name']}: {Player.armor['defence']} defence")
            PlayerInput = input("Shop for\n1) swords\n2) armor")
            if PlayerInput == "1":
                PlayerInput = input("What sword would you like to buy?\n1) Stone Sword: 30-60 damage, Cost: 30\n2) iron Sword: 50-80 damage, Cost: 80\n3) Diamond Sword: 100 Damage, Cost: 200")
            
                if PlayerInput == "1":
                    if Player.gold >= 30:
                        print("Have now have the 'Stone Sword'")
                        Player.gold -= 30
                        Player.sword = {'name' : 'Stone Sword','minAtackDamage' : 30, 'maxAtackDamage' : 60}
                elif PlayerInput == "2":
                    if Player.gold >= 50:
                        print("Have now have the 'Iron Sword'")
                        Player.gold -= 50
                        Player.sword = {'name' : 'Iron Sword','minAtackDamage' : 50, 'maxAtackDamage' : 80}
                elif PlayerInput == "3":
                    if Player.gold >= 200:
                        print("Have now have the 'Diamond Sword'")
                        Player.gold -= 200
                        Player.sword = {'name' : 'Diamond Sword','minAtackDamage' : 100, 'maxAtackDamage' : 100}
                print(f"Your Current Sword: {Player.sword['name']}: {Player.sword['minAtackDamage']}-{Player.sword['maxAtackDamage']} damage")
                
            else:
                PlayerInput = input("What armor would you like to buy?\n1) wooden armor Cost:50 defence:10\n2) chain armor Cost:200 defence:20\n3) steel armor Cost:500 defence:50")
                
                if PlayerInput == "1":
                    if Player.gold >= 50:
                        Player.gold -= 50
                        Player.armor = {'name' : 'wooden armor', 'defence' : 10}
                elif PlayerInput == "2":
                    if Player.gold >= 200:
                        Player.gold -= 200
                        Player.armor = {'name' : 'wooden armor', 'defence' : 20}
                elif PlayerInput == "3":
                    if Player.gold >= 500:
                        Player.gold -= 500
                        Player.armor = {'name' : 'wooden armor', 'defence' : 50}
                print(f"Your Current Armor: {Player.armor['name']}: {Player.armor['defence']} defence")
    
    if wonTheGame == True:
        return True
    return turnsTillDoom
while True:
    if HardMode:
        print(f"Turns Until Your Final Destination: {turnsTillDoom}")
    gameOver = turn(turnsTillDoom)
    
    if gameOver == True and Player.health <= 0 or gameOver == "You sussy backa":
        PlayerInput = input("Would you like to play again? yes/no: ")
        
        if PlayerInput == "yes":
            Player.health = 100
            Player.mana = 10
            Player.sword = {'name' : 'Wooden Sword', 'minAtackDamage' : 20, 'maxAtackDamage' : 40}
            Player.gold = 0
            Player.items = []
            Player.armor = {'name' : "No armor", 'defence' : 0}
        else:
            break
    elif turnsTillDoom != None:
        turnsTillDoom = gameOver