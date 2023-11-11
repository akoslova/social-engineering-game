# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Boss")
define s = Character("Security Guard")
define m = Character("Me")

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show boss happy

    # These display lines of dialogue.

    b "In the bustling metropolis of NeoCity, the Quantum Financial Corporation (QFC) stands as a symbol of modern finances. With its sleek glass façade and cutting-edge technology, QFC is known for being the most innovative and secure bank in the region."

    b "For your first assignment, you need to find a way into the building of QFC and insert a USB stick, containing a malware, on one employee computer. Try to not get caught!"

    # This ends the game.

    hide boss

    "You are standing in front of the building. What do you do next?"

    menu:

        "You go in without any plan.":
            jump choice_2_1

        "You spy on the building as a whole.":
            jump choice_2_2

        "You talk to the first employee that walks out of the door.":
            jump choice_2_3

    label choice_2_1:

        "You are entering the building and walking around to see where you can enter. A security guard appears."

        show s

        s "What are you doing here?"

        m "I...I..."

        s "You can not just wander around here. Please leave the premises."

        hide s

        "You failed the mission."

        jump done

    label choice_2_2:
        jump done

    label choice_2_3:
        jump done

    label done:

    return
