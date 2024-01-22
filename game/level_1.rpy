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
        #jump Building_options

        #If the counter is 1 for every option (Building is explored! Now only from two options can be chosen)
        #jump level_1



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

    "You start looking around."

    menu:

        "You choose to sit on a table with a guy on his laptop in close proximity":
            jump Laptop_observation
        
        "You decide to sit near a table and listen to 3 employees talking":
            jump Employee_conversation
        
        "You leave the shop beacuse nothing here seems interesting":
            jump leave_shop


label Laptop_observation:

    #show LaptopGuy
    #scene

    "You choose to sit on a table with a guy on his laptop in close proximity."

    menu:

        "Turn around and talk to him while trying to read of his screen":
            jump Say_something
        
        "Try reading the screen of your smartphones screen reflection":
            jump Screen_reflection

        "Try looking over your shoulder to read the screen":
            jump Look_shoulder


label Say_something:

    p "Hey Paul, how are you?"

    l "I am not Paul!"

    p "Sorry I confused you with someone else."

    "He is eyeing you warily and closes his laptop and starts leaving the coffee shop.
    That did not went well lets try something else!"

    jump Laptop_observation


label Look_shoulder:

#scene 
    "You try to observe what he is doing on his laptop by looking over your shoulder."

    "No success: You can not really see anything!"

    menu:

        "Extend your head":
            jump Extend_head
        
        "Try something else":
            jump Laptop_observation

label Extend_head:

    "You extend your head and tilt your torso."
    "While trying to look you catch the eye of someone watching you"

    menu:

        "Act natural":
            jump Natural

        "Be cautious":
            jump Cautious

label Natural:

    "You react by looking over the other shoulder as well pretending as you would search for someone in the room."
    "You got away with it!"
    "Lets try the smartphone reflection now."

    jump Screen_reflection

label Cautious:

    "You feel you have been caught out and decide to leave the store quickly."

    jump leaving_hastly

label Screen_reflection:

    "You try to look at the screen with a reflection of your smartphone
    Success: You see his User Name for Outlook .. christian.baker@company.de"

    menu:

        "Continue watching":
            jump Watching_1
        
        "Stop observing":
            jump Stop_observing

label Watching_1:

    "He is logging in and made a mistake with his password..
    He clicks on the reveal icon you can see his wrong input: aS&MIavmc12356#13"

    
    menu:

        "Continue watching":
            jump Watching_2
        
        "Stop observing":
            jump Stop_observing

label Watching_2:

    "He corrected his mistake and is now checking his E-mails"

    menu:

        "Continue watching":
            jump Watching_3
        
        "Stop observing":
            jump Stop_observing

label Watching_3:

    "Suddenly someone grabs your shoulder!"

    s "Hey what are you doing! I saw you looking at your smartphone while it’s turned off the whole time!"

    menu:

        "Mind your own business I was just in my own thoughts!":
            jump Option_1

        "I have this match on Tinder I am trying to figure out what to write :) Man I am just unsure how to approach her, she looks stunning on all her pictures.":
            jump Option_2

        "I was doing nothing, do you think I am some spy or what.. trying to spy on this guy here?” (laughing)":
            jump Option_3
        
        "Ignore him stand up and leave":
            jump Option_4


label Option_1:

    s "Don't be cheeky! You see this is my security officer badge, you come with me now and we'll see what you've been doing all this time."
    jump Caught
    #Here the player gets caught - reset to a checkpoint

label Option_2:

    s "Oh ok I know that feeling. Good Luck with that man! Anyways I have to go."

    "After that close encounter you decide to leave the coffee shop."
    jump leave_shop

label Option_3:

    s "Hmm I dont know why i thought so but you are right. Sorry for that!"

    "After that close encounter you decide to leave the coffee shop."

label Option_4:

    s "Hey!! where are you going? I am a security officer stand still!"

    menu:

        "Continue walking":
            jump Continue_walking
        "Stop your escape":
            jump Caught

label Continue_walking:

    "You increase your walking speed and try to weave through the people at the entrance."

    jump leaving_hastly

label Caught:

    # here the Player gets caught - Checkpoint


label Stop_observing:

    "You stop observing a turned off Phone looks suspicious."
    "As you know his name now you try approaching him."

    jump Approach_guy

label Approach_guy:

    p "Hey, Christian How are you?"

    c " I am fine, just a bit stressed tho and who are you?"

    menu:

        "I am": #Playername
            jump Real_name

        #only possbile if John Doe is known
        "I am John Doe.":
            jump John_doe

label Real_name:

    p "What department are you working in? I remember seeing your face somewhere in the onboarding process."

    c "Ooh I am from public relations work."

    p "So I heard rumors that the company might be in trouble. Do you know anything about that? I just started here and I don't want to look again for a job. You know I have to care for my mom. She is already in elderly care and it is quite expensive."

    c "I am not supposed to talk about things like that! But don't worry we have our methods to stop allegations of pesky reporters. 
        What department are you from?"

    p "something with accounting."

    p "So is there something in the bush?"

    c "I dont know who you are I have to leave now!"

    "He gets up and leaves while giving you a mistrustful look."

    jump Stand_up
    
label John_doe:

    p "What department are you working in? I remember seeing your face somewhere in the onboarding process."

    c "Ooh I am from public relations work."

    p "So I heard rumors that the company might be in trouble. Do you know anything about that? I just started here and I don't want to look again for a job. You know I have to care for my mom. She is already in elderly care and it is quite expensive."

    c "I am not supposed to talk about things like that! But don't worry we have our methods to stop allegations of pesky reporters. 
        What department are you from?"

    p "I am in the accounting division
        So there is something in the bush?"
    
    c "I mean just the typical stuff supporting/buying politicians with money, not respecting the environment enough.. Nothing unheard off!"

    p "Ok thank you! That calms me down a bit, have a nice break and see you!"

    jump Stand_up

label Stand_up:

    "You got some information. Maybe you can try to observe something else now."

    menu:
            #If not done so already!
        "Eavesdrop employees conversation.":
            jump Employee_conversation
            
        "Leave the shop":
            jump leave_shop


label Employee_conversation:

#scene
#show

    e1 "Hey, have you guys heard about the charity event happening next week? It's for the local kids shelter. I'm thinking we should all go and show our support."

    e2 "Oh yeah, I saw the email about it. Count me in! It's great that the company is encouraging us to get involved in the community."

    e3 "I'm on board too. It's a fantastic cause. Plus, it'll be a nice break from work."

    e1 "Absolutely. Now, let's talk projects. How's everyone doing with their current assignments?"

    e2 "Well, the marketing team is gearing up for the product launch next month. We're working on some killer campaigns to create buzz."

    e1 "That's fantastic to hear, Morgan. And you, Taylor?"

    e3 "Our Project Phoenix, is in full swing. We're on track for the next milestone. The team's pulling together like a well-oiled machine."

    e2 "Project Phoenix, huh? The name itself sounds intriguing. What's it about?"

    e3 "It's a major software upgrade for our flagship product. We're incorporating cutting-edge features and revamping the user interface. It's pretty exciting stuff."

    e1 "Great work, Taylor. Now, have you guys noticed the increased security personnel around the office lately? It's been making me a bit uneasy."

    e2 "Yeah, I thought I was imagining things. What's going on?"

    e3 "I spoke to HR about it. They mentioned that there have been some security concerns, so they've decided to beef up our office security for the time being."

    e1 "Security concerns? That's a bit unnerving. I hope everything's okay."

    e3 "They didn't give many details, just said it's a precaution. But let's stay vigilant and report anything suspicious. And hey, maybe the charity event will be a good opportunity to unwind and take our minds off things."

    e2 "Agreed. Let's focus on making a positive impact both at work and in the community. And, of course, enjoy the charity event next week."

    e1 "Sounds like a plan. Let's make it a team outing. I'm looking forward to it! Anyways time is over guys time to leave!"

    "The trio finishes their lunch cleans up and leave their table."

    "That was interesting. Lets try observing something else now"

    jump Follow_people

label leave_shop:

    #scene
    #Update Inventory

    "While you leave the shop you notice an Employee Badge.
    It is difficult to recognize because it is peeking out from under a chest of drawers. 
    You take it without much thought."
    "Check your notebook for everything you leaned about."


label leaving_hastly:

    "You leave the store and don't look back. You probably shouldn't be seen here again any time soon"
    "Check your notebook for everything you leaned about."



















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