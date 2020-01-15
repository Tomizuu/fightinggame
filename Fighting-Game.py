from time import sleep
from time import ctime
import random
from random import randint
import os
import sys
player_name = input("What is your name? ")
datat = "Your character: "
player_attack = " Attack 10,"
player_heal = " Healing 1," 
health = " Health 100" 
player = {'name': player_name, 'attack': 5, 'heal': 5, 'health': 50}
monster = {'name': 'Monster1', 'attack': 10, 'health': 100}
print(player)
start = input("Select difficulty. 1, 2, 3: ")
if start == "1":
    print("Selected difficulty 1")
    player = {'name': player_name, 'attack': 45, 'heal': 10, 'health': 120}
    sleep(2)
if start == "2":
    print("Selected difficulty 2")
    player = {'name': player_name, 'attack': 20, 'heal': 6, 'health': 100}
    sleep(2)
if start == "3":
    print("Selected difficulty 3")
    player = {'name': player_name, 'attack': 10, 'heal': 4, 'health': 65}
    sleep(2)
if start == "blyat":
    print("oh.. you found the secret. make sure you have vodka cooling installed.")
    player = {'name': player_name, 'attack': 5, 'heal': 50, 'health': 6969}
    sleep(3)
os.system("cls")
events = ['1', '2']   
lost_count = 0
win_count = 0
print("Starting time: " + ctime())
ready_player = input("Are you ready to start? (Yes/No) ")
if ready_player == "Yes":
    game_Running = True
    os.system("cls")
elif ready_player == "No":
    print("Exiting the game")
    sleep(3)
    sys.exit(0)


while game_Running:
    new_round = True
    while new_round:
            randomEvent = random.randint(1, 2)
            if win_count >= 50:
                randomEvent = 99
            if randomEvent == 1:
                fight = True
                monster = {'name': 'Jack', 'attack': 12, 'health': 325}
                print("Jack is approaching you.")
                print("What do you want to do?")
                sleep(2)
                while fight:
                    print(monster)
                    print(player)
                    print("---------------------------------------")
                    print("Rounds lost: ")
                    print(lost_count)
                    print("---------------------------------------")
                    print("Rounds won: ")
                    print(win_count)
                    print("---------------------------------------")
                    print("1) Run away")
                    print("2) Attack")
                    print("3) Heal")
                    fightChoice = input()
                    if fightChoice == "1":
                        print("You tried to run away.")
                        print("Jack was faster than you.")
                        print("He attacked you.")
                        player['health'] = player['health'] - monster['attack']
                        sleep(3)
                        os.system("cls")
                    if fightChoice == "2":
                        print("You attacked Jack.")
                        print("He attacked back")
                        monster['health'] = monster['health'] - player['attack']
                        player['health'] = player['health'] - monster['attack']
                        sleep(3)
                        os.system("cls")
                    if fightChoice == "3":
                        print("You healed")
                        player['health'] = player['health'] + player['heal']
                        sleep(3)
                        os.system("cls")
                    if player['health'] <= 0:
                        fight = False
                        lost_count = lost_count + 1
                        print("You lose")
                        player['health'] = 50
                        sleep(5)
                        os.system("cls")
                    if monster['health'] <= 0:
                        fight = False
                        win_count = win_count + 1
                        print("You win")
                        sleep(5)
                        os.system("cls")
            
            if randomEvent == 2:
                fight = True
                monster = {'name': 'Mr. Cake', 'attack': 10, 'health': 500}
                print("Someone gave you a cake and it transformed into a big cake. It took your gun and points you with it")
                print("What do you want to do?")
                print("---------------------------------------")
                sleep(4)
                while fight:
                    print(monster)
                    print(player)
                    print("---------------------------------------")
                    print("Rounds lost: ")
                    print(lost_count)
                    print("---------------------------------------")
                    print("Rounds won: ")
                    print(win_count)
                    print("---------------------------------------")
                    print("1) Try to take the gun back")
                    print("2) Attack")
                    print("3) Heal")
                    fightChoice = input()
                    if fightChoice == "1":
                        print("You tried to take the gun back")
                        print("Mr. Cake shot you.")
                        print("He missed.")
                        os.system("cls")
                    if fightChoice == "2":
                        print("You attacked Mr. Cake")
                        print("Mr. Cake attacked back")
                        monster['health'] = monster['health'] - player['attack']
                        player['health'] = player['health'] - monster['attack']
                        sleep(3)
                        os.system("cls")
                    if fightChoice == "3":
                        print("You healed")
                        player['health'] = player['health'] + player['heal']
                        sleep(3)
                        os.system("cls")
                    if player['health'] <= 0:
                        lost_count = lost_count + 1
                        print("You lose")
                        sleep(5)
                        fight = False
                        os.system("cls")
                    if monster['health'] <= 0:
                        win_count = win_count + 1
                        print("You win")
                        sleep(5)
                        fight = False
                        os.system("cls")
            
            if randomEvent == 3:
                fight = True
                monster = {'name': 'Potato Chip', 'attack': 0, 'health': 50}
                print("You dropped a potato chip while eating.")
                print("What do you want to do?")
                sleep(4)
                while fight:
                    print(monster)
                    print("-----------------------------------------------------------------------")
                    print(player)
                    print("---------------------------------------")
                    print("Rounds lost: ")
                    print(lost_count)
                    print("---------------------------------------")
                    print("Rounds won: ")
                    print(win_count)
                    print("---------------------------------------")
                    extraDamage = random.randint(5, 10)
                    print("1) Stomp on the chip (Extra damage)")
                    print("2) Leave the potato chip under your desk.")
                    fightChoice = input()
                    if fightChoice == "1":
                        print("You stomped on the potato chip.")
                        randomencouterwithnewcharater = random.randint(1, 2)
                        if randomencounter_count == 1:
                            randomencouterwithnewcharater = 0
                        if randomencouterwithnewcharater == 1:
                            randomencounter_count = randomencounter_count + 1
                            sleep(2)
                            print("oh no.. a shadow appeared in your room, hit you with a sword and disappeared ")
                            player['health'] = player['health'] - 20
                        player['attack'] = player['attack'] + extraDamage
                        monster['health'] = monster['health'] - player['attack']

                        os.system("cls")
                    if fightChoice == "2":
                        print("You can always clean later..")
                        sleep(3)
                        os.system("cls")
                        fight = False
                    if player['health'] <= 0:
                        lost_count = lost_count + 1
                        print("You lose")
                        sleep(5)
                        fight = False
                        os.system("cls")
                    if monster['health'] <= 0:
                        win_count = win_count + 1
                        print("You win")
                        sleep(5)
                        fight = False
                        os.system("cls")
            if randomEvent == 99:
                print("huh.. 50 wins. i'm gonna reset them... and then kill you")
                win_count = 0
                monster = {'name': 'Boss', 'attack': 61, 'health': 5000}
                print("EXTRA ATTACK ACTIVATED")
                player['attack'] = 250
                fight = True
                while fight:
                    energyWeapon = 50
                    print(monster)
                    print("-----------------------------------------------------------------------")
                    print(player)
                    print("-----------------------------------------------------------------------")
                    print("Secret weapon energy: ")
                    print(energyWeapon)
                    print("-----------------------------------------------------------------------")

                    print("What do you want to do?")
                    print("1) Secret weapon")
                    print("2) Attack")
                    print("3) Heal")
                    fightChoice = input()
                    os.system("cls")
                    if fightChoice == "1":
                        if energyWeapon <= 5:
                            print("Cannot use secret weapon. No energy")
                            print("While you tried to shoot the Boss with secret weapon. It attacked you.")
                            player['health'] = player['health'] - monster['attack']
                        if energyWeapon >= 5:
                            print("Used secret weapon")
                            print("Secret weapon stats: ")
                            print("Attack: 450, Energy consumption: 5")
                            print("Boss attacked you.")
                            energyWeapon = energyWeapon - 5
                            sleep(2)
                            monster['health'] = monster['health'] - 450
                            player['health'] = player['health'] - monster['attack']
                    if fightChoice == "2":
                        print("You attacked Boss")
                        print("Boss attacked back")
                        monster['health'] = monster['health'] - player['attack']
                        player['health'] = player['health'] - monster['attack']
                        sleep(3)
                        os.system("cls")  
                    if fightChoice == "3":
                        print("You healed")
                        player['health'] = player['health'] + player['heal']
                        sleep(3)
                        os.system("cls")
                    if player['health'] <= 0:
                        lost_count = lost_count + 1
                        print("You lost..")
                        sleep(5)
                        fight = False
                        os.system("cls")
                    if monster['health'] <= 0:
                        win_count = win_count + 1
                        print("Congratulations! You won")
                        sleep(5)
                        game_complete = True
                        fight = False
                        os.system("cls")
                    if game_complete == True:
                        os.system("cls")
                        cleartime = "Game cleared at: " + ctime()
                        print("Game cleared at" + ctime())
                        print("Congratulations and thank you for playing!")
                        sleep(7)
                        with open('cleared.txt', 'w') as f:
                            f.write('Fighting Game cleared\n')
                            f.write('Game cleared at: \n' + ctime())
                        sleep(2)
                        quit()
                        

