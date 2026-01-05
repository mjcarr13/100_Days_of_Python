print(r'''
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
print("Welcome to a scorching hot desert")
print("Your mission is to find the treasure in the tomb.")
q1_response = input("I am the Mummy which protects the tomb\n "
                    "Only the most worthy travellers may reach the treasure. "
                    "URGHHHHHHH. Which way will you go, 'left' or 'right?'\n").lower()

if q1_response == "left":
    q2_response = input("A fine choice, for you have avoided a pit of snakes. "
                        "You reach an oasis? "
                        "'Drink water', or 'wait?'\n").lower()
    if q2_response == "wait" or q2_response == "Wait":
        q3_response = input("A finer choice, for there are pirhannas everywhere."
                            "The ghost of Cleopatra with three treasure boxes, one small, one medium, one large. "
                            "In one lies the key to the tomb, in the others, a fate worse than death. "
                            "Pick a box, 'small', 'medium', or 'large'.\n").lower()
        if q3_response == "small":
            print("Within the box lies the key to the tomb! go and get the treasure!")
        elif q3_response == "large":
            print("This box is cursed!"
                  "It coils around and suffocates ye. Arrrrrrrr!")
        elif q3_response == "medium":
            print("Ye have found the treasure, and with it, many a capital gains tax obligation. Arrrrr!")
        else:
            print("Ye make no sense to me. Arrrrr!")
    else:
        print("Arrrr. A shark nibbles upon ye. Arrr.")
else:
    print("Alas, ye have fallen down a well. Arrr!")







