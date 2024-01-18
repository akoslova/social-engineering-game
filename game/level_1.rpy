$ renpy.include("inventory.rpy")

define p = Character(_("Me"), color="#c8c8ff")

label level_1:
    "I should get out of here before anyone catches me."

    menu:

        "Leave building through the kitchen of the canteen":
            jump leavecanteen

        "Leave by yourself through main entrance with a group of people":
            jump leavemain

        "Wait until you don’t see anyone else to leave.":
            jump leavealone

label leavecanteen:

    "As you approach the security door, you notice that you would have needed an ID to scan for it to open."

#[Security guard will tap on your shoulder, you turn around]
    "SG: “Where is your ID card”"

    p "I must have lost it, it was right there on my pants"

    menu:

        "Punch him in the face":
            jump punch
        "I must have lost it, it was right there on my pants":
            jump apology
#only if true
        "Take the ID batch in your inventory":
            jump idcard



label leavemain:

    "You change back into your kitchen clothes and walk into the company's kitchen."

    "The kitchen is brimming with energy and hectic as chefs and kitchen staff hustle to prepare dishes for the employees. No one really pays attention to you. "
    "You feel safe and almost reach the exit door but suddenly a woman stops you in front of the door."

    "C: Hey, sorry but can you quickly help out with the dessert. It's so busy right now we can't keep up."

#[[P: “No sorry, I don’t have time right now."]]

#[[Yes sure, what do you need help with?]]


label leavealone:

    "You see a group of employees walking towards the exit. You run along with them inconspicuously and walk quickly behind one person through the security door."

#Security guard will tap on your shoulder, 
#SG: Hey there! Stop!
#You turn around
#SG: Hey you lost your wallet
#Player: Oh thank you Sir! 

#You rush out of the building