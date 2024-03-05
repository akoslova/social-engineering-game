# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Boss")
define s = Character("Security Guard")
define m = Character("Me")
define e = Character("Employee")

label prototype:
    scene bg office:
        zoom 2.2

    show boss at left: 
        xzoom 1.6
        yzoom 1.6
        xalign 0.25
        yalign 1.0

    b "In the bustling metropolis of NeoCity, the Quantum Financial Corporation (QFC) stands as a symbol of modern finances. With its sleek glass façade and cutting-edge technology, QFC is known for being the most innovative and secure bank in the region."

    b "For your first assignment, you need to find a way into the building of QFC and insert a USB stick, containing a malware, on one employee computer. Try to not get caught!"

    hide boss

    scene bg bank:
        zoom 2.2

    "You are standing in front of the building. What do you do next?"

    menu:

        "You go in without any plan.":
            jump choice_2_1

        "You spy on the building as a whole.":
            jump choice_2_2

        "You talk to the first employee that walks out of the door.":
            jump choice_2_3

    label choice_2_1:

        scene bg inside:
            zoom 2.2

        "You are entering the building and walking around to see where you can enter. A security guard appears."

        show securityguard at left: 
            xzoom 2.2
            yzoom 2.2
            xalign 0.25
            yalign 1.0

        s "What are you doing here?"

        m "I...I..."

        s "You can not just wander around here. Please leave the premises."

        hide securityguard

        "You failed the mission."

        jump done

    label choice_2_2:
        scene hallway:
        
        "You find out, that the door to the IT is protected by a fingerprint sensor, but many employees have access to the room."
        "You would also decribe the working ambience as quiet, serious and hard working. This gives you an idea."

        menu:
            "You dress up as an employee with a broken arm and lots of documents in your arms and get all loud and annoyed that your fingerprint doesnt work, hoping that someone will just open the door for you.":
                jump choice_3_2
            "You dress up as an employee with a broken arm and lots of documents in your arms and quietly explain to a coworker that your fingerprint doesnt work, and you if they could just quickly open it for you.":
                jump choice_3_3

        label choice_3_2:
            "Success"
            "You get in because the employee simply wants to end the noisy situation as quickly as possible in order to get back to work."
        jump done
            
        label choice_3_3:
            "The employee has no time for you and refers you to IT Service to check your clearances."
            "Mission failed."
        jump done
    jump done

    label choice_2_3:

        scene bg bank:
            zoom 2.2

        show employee:
            xalign 0.25
            yalign 1.0
            xzoom 1.2
            yzoom 1.2

        m "Hi there! I am so sorry to bother you but I am a reporter doing an article on the working environment in the financial industry, and I would like to ask you some questions if you have a few minutes."

        e "Hi! Oh, wow! That's sounds interesting! I would be happy to answer some questions!"

        m "Amazing! Thank you. Could you please describe how it is like for you to work at QFC."

        e "I quite like it because we do things very professionally, and my coworkers are really nice to help each other out when needed."

        m "How is your relationship as an employee with management?"

        e "Well, I have my supervisor that I know personally and respond to. But the other managers, I only know their name as I receive emails from them."

        m "What do those emails contain?"

        e "Well, mostly just tasks that need to be done. Sometimes, they throw me off my work because those tasks need to be done urgently, no questions asked so I usually have to stop inbetween my work to follow up on the wishes of management."

        m "Interesting, so you do everyhing that management tells you to do, even if you don't know them in person?"

        e "Yes, of course. I mean they are ranked above me so I need to follow their orders."   

        m "Okay, thank you so much for your input. These were actually all of my questions already. Thank you so much! Have a great day!"

        e "Great! Have a wonderful day too!"

        hide employee

        "You realise from the conversation that all employees follow management strictly while not knowing all the managers in person. What do you do next?"

        menu:

            "You print out a letter allegedly from management that asks to leave the door open for the day. You go to the backdoor and hang it up.":
                jump choice_3_4

            "You dress up like a manager and enter the building, pretending to be a manager that is very late to a meeting with the CEO and forgot his key card at home.":
                jump choice_3_5

        label choice_3_4:

            scene bg backdoor:
                zoom 2.2

            "After waiting an hour, an employee reads the sign and opens the door."

            "You enter now and insert the USB stick into a computer inside QFC."

            "You completed the mission successfully!"

            jump done

        label choice_3_5:

            scene bg inside:
                zoom 2.2

            show securityguard at left: 
                xzoom 2.2
                yzoom 2.2
                xalign 0.25
                yalign 1.0

            s "How can I help you?"

            m "My name is Maximilian Sterling, and I one of the upper managers here."

            m "I have an urgent appointment with the CEO that started half an hour ago, and I just discovered that I forgot my keycard at home."

            m "You need to let me in NOW, the CEO is already upset enough."

            s "I need to check your appointment in the system first..."

            m "No! I don't have the time form it! Gosh, just let me in!"

            s "Sorry sir, you need to wait a second (checks appointment in computer)."

            s "Sir, you need to come with me, I did not find your name nor any appointment."

            hide securityguard

            "Your mission failed. You were caught."
            jump done

    label done:

    return
