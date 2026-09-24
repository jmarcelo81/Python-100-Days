#Code below
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

print("You walk one mile down a yellow brick street and you reach a Forest")
answer_one = input("You need to choose a direction to go. Would you rather go left or right?\n").strip().lower()

if answer_one == "right":
    print("You went right, entering the Derian Gap jungle. Lost, hungry, and weak, a jaguar finds and eats you. Game Over.")
    exit()  # Quit the game
elif answer_one == "left":
    print("You went left. You walk through a small path for two miles and you reach a stream of water. You see a small boat tied to a little pier and you see a tunnel across the water. You can see a very dim light coming from the tunnel.")
else:
    print("Invalid choice. Please enter 'left' or 'right'.")
    exit()  # Quit the game

answer_two = input("How do you want to proceed? Would you rather get into the boat or try and swim across the water and reach the tunnel? Answer 'boat' or 'swim'.\n").strip().lower()
if answer_two == "swim":
    print("You swim past the midpoint, growing tired. As you near the shore, you can feel relief already, but suddenly an alligator pulls you underwater. Game Over.")
    exit()  # Quit the game
elif answer_two == "boat":
    print("You enter the boat. You see a double paddle. Smiling you start paddling downstream. After a while you arrive at an island with three houses on it. ")
else:
    print("Invalid choice. Please enter 'boat' or 'swim'.")
    exit()  # Quit the game

answer_three = input("You need to choose which house to go into. The first one has a red door, the second one a blue door, and the third one has a yellow door. Please choose red, blue or yellow.\n").strip().lower()
if answer_three == "red":
    print("You open the red door, you hear the cracking sound of the door but can't see anything inside. As you step inside you realize there is no ground, you fall down a huge hole. You are trapped. Game Over.")
    exit()  # Quit the game
elif answer_three == "blue":
    print("You open the door, you notice that everything is new and clean, the furniture is very nice and comfortable. You can feel yourself getting richer and notice a chest on top of the table. You open the chest, see a note inside. A little confused you read it. You lost. Game Over.")
    exit()  # Quit the game
elif answer_three == "yellow":
    print("You open the door and see an empty house with a single light illuminating a green hatchet door. You open that green door and find the treasure. Congratulations. You win the game.")
else:
    print("Invalid choice. Please enter 'red', 'blue' or 'yellow'.")
    exit()  # Quit the game
