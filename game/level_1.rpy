$ renpy.include("inventory.rpy")

define p = Character(_("Me"), color="#c8c8ff")
define l = Character(_("LaptopGuy"), color="#c8fff3")
define c = Character (_("Christian"), color="#db8941")
define s = Character (_("Security Officer"), color="#3939f5")
define r = Character (_("Receptionist"), color="#633aeb")
define e1 = Character (_("Employee 1"), color="#6fd066")
define e2 = Character (_("Employee 2"), color="#6fd066")
define e3 = Character (_("Employee 3"), color="#6fd066")

label level_1:

"After a long ride in the subway you finally reach N 42 Street which is very busy at that time. You notice small firms like 1940paper.inc, SmrtWays and many more having their unique blinking Signs and advertisements and the big banks and firms residing in massive Skyscrapers.
And also your target. It is right across the Metro Exit indicated by the big lettering on the glass front above the entrance. CORE it reads in big red letters."

    menu:

        "Look around and inspect the building":
            jump Building_options
        
        "Stand in front of the building and observe who enters and leaves it":
            jump Collect_information

        "You notice that a lot of them go to the coffee shop across the street. You decide to follow them and get a coffee yourself":
            jump Follow_people

label Building_options:

"You notice that there are different entrances besides the main entrance with a lobby. An underground parking garage where black limousines come and go. A back entrance which is used by staff from their canteen for example."

    menu:

        "Check the main entrance":
            jump Main_entrance
        
        "Go towards the parking garage":
            jump Parking_garage

        "Look around the back for an entrance":
            jump Back_entrance


label Main_entrance:

    #scene bg main entrance

"When you enter the lobby, you are greeted by a receptionist, a security guard who looks at you without suspicion, and a few notices informing you about the company and a job opening in the business department."

    menu:

        "Pretend to be there for an interview":
            jump interview

        "Ask about CORE":
            jump basic_core

        "Try flirting with the attractive receptionist":
            jump flirt

label interview:

    show Me with easeinright
    show Receptionist with easeinleft

    p "Hello, I am here because I am interested in the position in the Customer Service department. Where do I have to go to talk to the appropiate person?"

    r "Do you have a job interview? I have not received any information that applicants are coming for an interview today!"

    p "No I was the area and wanted to swing by see how it goes"

    r "Ohh wow you have to submit an application online and then you might get invited for the interview Sir! So If you have no other questions please leave the lobby."

    menu:

        "Ask about CORE":
            jump basic_core
        "Leave":
            jump leaving_lobby

label basic_core:

    p "What can you tell me about CORE?"

    r "We are an international construcing buisness tasked to build and demolish buildings. For the rest, please check our homepage."

    menu:

        "Pretend to be there for an interview":
            jump interview

        "Try flirting with the attractive receptionist":
            jump flirt

label flirt:

    p "How you doin? "

    #show Receptionist angry

    r "Stop your inappropriate advances at once, or I will call the security guards to have you removed from this property!"

    "I better get going now!"

    jump leaving_lobby


label leaving_lobby:

    "You decide that you are not going to get anywhere or even get in trouble by staying in the lobby longer and you go back out."

    jump Building_options

    #Needs to count 1 for Main entrance so it cant be chosen again! Ideally jump directly to the 3 choices

label Parking_garage:

    # sceen bg garage (with surveillance)

    "You decide to go towards the Driveway of the parking garage.
    While approaching you notice the security cameras and the closed garage doors. There is no way you can or should try to access the company here!"

    jump Building_options

    #Needs to count 1 for Parking Garage so it cant be chosen again! Ideally jump directly to the 3 choices

label Back_entrance:

    # sceen bg back entrance View from further away on to people working at back entrance

    "You see some people moving boxes and shouting at each other while working. They are dressed in branded overalls in beige colors. You notice that in the back of the truck with the boxes there is one of these overalls hanging unattended."

    #Needs to count 1 for Back entrance so it cant be chosen again!

    menu:

        "Try your luck and grab it!":
            jump success
        

        "Maybe that's too risky I should head back to observe other parts of the building":
            jump Building_options

        #If the counter is 1 for every option (Building is explored! Now only from two options can be chosen)
            jump level_1


label success:

    "Succes! You pull it off and get the overall unnoticed"

#Update Inventory: Have the beige overall with the branding
        jump Building_options

        #If the counter is 1 for every option (Building is explored! Now only from two options can be chosen)
        jump level_1



label Collect_information:

    #IF this Option is not chosen the Information of John Doe is not usable troughout this plot!!! Needs to be included in the code
    # When chosen set counter to 1 for watch the people so it cant be chosen again

"As you watch people leaving the building, you notice a member of staff wearing his badge on the outside of his trouser pocket.
You manage to read his full name, John Doe, and the department: Arithmetic Department. You make a note in your notebook.
You also notice that the employees usually wear suits and that the security guards have a grey uniform."


    menu:

        "Look around and inspect the building":
            jump Building_options

        "Follow them and get a coffee yourself":
            jump Follow_people


label Follow_people:

"You enter the coffee shop and get yourself a nice hot steaming coffee. Now you start looking around."

    menu:

        "You choose to sit on a table with a guy on his laptop in close proximity":
            jump Laptop_observation
        
        "You decide to sit near a table and listen to 3 employees talking":
            jump Employee_conversation
        
        "You leave the shop beacuse nothing here seems interesting":
            jump leave_shop


label Laptop_observation:


label Employee_conversation:
    

label leave_shop:




















label Leaving_building:

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