# Day 3 of 100 - Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

cross_road_choice = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")

if cross_road_choice == "left":
    lake_choice = input("You come to a lake. There is an island in the middle. Type \"wait\" to wait for a boat. Type \"swim\" to swim.\n")

    if lake_choice == "wait":
        island_choice = input("You arive at the island unharmed. There is a house with three doors inside. One red, one yellow, and one blue. Which color do you choose?\n")

        if island_choice == "yellow":
            print("Congratulations! You found the treasure! You win the game.")
        elif island_choice == "blue":
            print("You were eaten by a beast. GAME OVER!")
        elif island_choice == "red":
            print("You were burned by fire. GAME OVER!")
        else:
            print("GAME OVER!")
    else:
        print("You were attack by a giant trout. GAME OVER!")
else:
    print("You fell into a hole. GAME OVER!")
