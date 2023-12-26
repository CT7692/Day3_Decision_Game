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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You stand before an old, abandoned house beside an entrance to a dark forest.")
print("Type 'house' to go into the house. Type 'forest' to walk into the forest.")
dec1 = input("What do you do?\n")

if (decision1 := dec1.lower()) == "house":
    print("\nYou walk into the house and begin to feel very cold.\nA terrible smell fills the air coming from upstairs, but you realize it gets colder in the house as you keep walking.")
    print("Type 'upstairs' to walk upstairs. Type 'walk' to walk deeper inside the house.")
    dec2 = input("What do you do?\n")

    if (decision2 := dec2.lower()) == "walk":
        print("\nYou begin to feel even colder as you walk.\nYou see and hear what appears to be a woman kneeling on the floor, sobbing, and mourning the loss of her loved one in the laundrey room.\nAcross from the laundrey room is the kitchen.")
        print("Type 'kitchen' to check out the kitchen. Type 'console' to investigate the condition of the woman.")
        dec3 = input("What do you do?\n")
        decision3 = dec3.lower()

        if dec3 == "kitchen":
            print("\nAs you enter the kitchen, you find a treasure chest with a million dollars and a teleporter that takes you back to your house. \nCongratulations! You Win!!! :D")
        else:
            print("\nAs you approach the woman and inquire her condition, she turns around with whitened eyes and bites your neck. \nGame Over.")
    else:
        print("\nYou notice a shadow on the wall that manifests into a human-like figure. It pushes you out of the window and you fall. \nGame Over.")
else:
    print("\nAfter walking for several minutes you encounter a giant spider that catches you in its web and drags you away to its lair. \nGame Over.")
