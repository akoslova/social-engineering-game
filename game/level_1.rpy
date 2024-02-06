$ renpy.include("inventory.rpy")
$ renpy.include("tutorial_story.rpy")
#languageTool.language
define l = Character(_("LaptopGuy"), color="#c8fff3")
define c = Character (_("Christian"), color="#db8941")
define s = Character (_("Security Officer"), color="#3939f5")
define e1 = Character (_("Employee 1"), color="#6fd066")
define e2 = Character (_("Employee 2"), color="#6fd066")
define e3 = Character (_("Employee 3"), color="#6fd066")
define e4 = Character (_("Employee 4"), color="#6fd066")
define e5 = Character (_("Employee 5"), color="#6fd066")
define e6 = Character (_("Employee 6"), color="#6fd066")
define e7 = Character (_("Employee 7"), color="#6fd066")
define e8 = Character (_("Employee 8"), color="#6fd066")
define e9 = Character (_("Employee 9"), color="#6fd066")
define e10 = Character (_("Employee 10"), color="#6fd066")
define ivy = Character (_("Ivy P. Paperwork"), color="#6a5acd")
define burt = Character (_("Burt W. Mopbucket"), color="#20b2aa")
define staff = Character (_("IT Staff"), color="#ff6347")
define mr_johnson = Character (_("Mr. Johnson"), color="#4b0082")
define k1 = Character (_("Kitchen staff 1"), color="#6fd066")
define k2 = Character (_("Kitchen staff 2"), color="#6fd066")
define k3 = Character (_("Kitchen staff 3"), color="#6fd066")

define cat = Character (_("Cat"), color="#fffaf0") #Furry cat

image Receptionist2="receptionist2.png"
image Receptionist2 angry="receptionist2 angry.png"
image Receptionist2 smile="receptionist2 smile.png"
image k1 stressed="chef1 stressed.png"
image k1 happy="chef1 happy.png"
image Me canteen="playercanteen.png"
image Me chef="playerchef.png"
image e4="e4.png"
image e5="e5.png"
image e6="e6.png"
image e9="e9.png"
image e4 smile="e4 smile.png"
image k2 stressed="chef2 stressed.png"
image k2 happy="chef2 happy.png"
image k2 angry="chef2 angry.png"
image guard1 = "guard1.png"
image guard surprised = "guard surprised.png"
image guard wallet = "guard wallet.png"
image punch = "punch.png"

image bg n42="bg n42.jpg"
image bg coreback="bg coreback.jpg"
image bg coreback2="bg coreback2.jpg"
image bg coreback3="bg coreback3.jpg"
image bg main ent="bg main ent.jpg"
image bg main ent2="bg main ent2.jpg"
image bg garage="bg garage.jpg"
image bg cafe="bg cafe.jpg"
image bg cafe1="bg cafe1.jpg"
image bg cafe2="bg cafe2.jpg"
image bg badge="bg badge.jpg"
image bg canteendoor="bg canteendoor.jpg"
image bg kitchen="bg kitchen.jpg"
image bg whiskers="bg whiskers.jpg"
image bg cublicles="bg cubicles.jpg"
image bg office canteen="bg office canteen.jpg"
image bg office cat="bg office cat.jpg"
image bg office cat2="bg office cat2.jpg"
image bg office cat3="bg office cat3.jpg"
image bg room303="bg room303.jpg"
image bg fan="bg fan.jpg"
image bg computer="bg computer.jpg"
image bg locker="bg locker.jpg"
image bg elevator="bg elevator.jpg"
image bg elevator2="bg elevator2.jpg"
image bg elevator inst="bg elevator inst.jpg"
image bg checkpoint2="bg checkpoint2.jpg"
image bg checkpoint3="bg checkpoint3.jpg"
image bg camera="bg camera.jpg"
image bg cam alarm="bg cam alarm.jpg"
image bg caught="bg caught.jpg"
image bg staircase="bg staircase.jpg"
image bg call="bg call.jpg"

label level_1:
    scene bg n42
    show Me with easeinright
    "After a long ride in the subway you finally reach N 42 Street which is very busy at that time."
    "You notice small firms like 1940paper.inc, SmrtWays and many more having their unique blinking Signs and advertisements and the big banks and firms residing in massive Skyscrapers."
    "And also, your target. It is right across the Metro Exit indicated by the big lettering on the glass front above the entrance. CORE it reads in big red letters."

label investigate:
    scene bg n42
    show Me with easeinright    
    default full_building = False
    default john_doe_known = False
    default badge_found = False

    menu:

        "Look around and inspect the building" if not full_building:
            "You notice that there are different entrances besides the main entrance with a lobby. An underground parking garage where black limousines come and go. A back entrance which is used by staff from their canteen for example."
            jump Building_options
        
        "Stand in front of the building and observe who enters and leaves it":
            jump Leaving_building

        "You notice that a lot of them go to the coffee shop across the street. You decide to follow them and get a coffee yourself":
            jump Follow_people

label Building_options:

    default not_inspected_entrance = True
    default not_inspected_garage = True
    default not_inspected_back = True
    default overall_success = False

    menu:

        "Check the main entrance" if not_inspected_entrance:
            jump Main_entrance
        
        "Go towards the parking garage" if not_inspected_garage:
            jump Parking_garage

        "Look around the back for an entrance" if not_inspected_back:
            jump Back_entrance

        "You lost the level and need to restart" if not not_inspected_back and not not_inspected_garage and not not_inspected_entrance:
            jump level_1

        "You successfully explored the building! You can now further investigate." if not not_inspected_back and not not_inspected_garage and not not_inspected_entrance and overall_success:
            $ full_building = True
            jump investigate


label Main_entrance:

    #scene bg main entrance
    scene bg main ent
    show Me with easeinright
    "When you enter the lobby, you are greeted by a receptionist, a security guard who looks at you without suspicion, and a few notices informing you about the company and a job opening in the business department."
    show Receptionist2 with easeinleft

    menu:

        "Pretend to be there for an interview":
            jump interview

        "Ask about CORE":
            jump basic_core

        "Try flirting with the attractive receptionist":
            jump flirt

label interview:


    p "Hello, I am here because I am interested in the position in the Customer Service department. Where do I have to go to talk to the appropiate person?"
    show Receptionist2 smile 

    r "Do you have a job interview? I have not received any information that applicants are coming for an interview today!"

    p "No I was the area and wanted to swing by, see how it goes"

    r "Ohh wow! You have to submit an application online and then you might get invited for the interview Sir! So If you have no other questions please leave the lobby."

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

    p "How you doin?"

    #show Receptionist angry
    show Receptionist2 angry 

    r "Stop your inappropriate advances at once, or I will call the security guards to have you removed from this property!"

    "I better get going now!"

    jump leaving_lobby


label leaving_lobby:

    "You decide that you are not going to get anywhere or even get in trouble by staying in the lobby longer and you go back out."

    "You need to choose a different option."

    $ not_inspected_entrance = False

    jump Building_options

label Parking_garage:

    # sceen bg garage (with surveillance)
    scene bg garage
    show Me with easeinleft:
        xzoom -1.0
    
    "You decide to go towards the Driveway of the parking garage.
    While approaching you notice the security cameras and the closed garage doors. There is no way you can or should try to access the company here!"

    "You need to choose a different option."

    $ not_inspected_garage = False

    jump Building_options


label Back_entrance:

    # sceen bg back entrance View from further away on to people working at back entrance

    scene bg coreback
    show Me with easeinleft:
        xzoom -1.0
    "You see some people moving boxes and shouting at each other while working. They are dressed in branded overalls in beige colors. You notice that in the back of the truck with the boxes there is one of these overalls hanging unattended."

    $ not_inspected_back = False

    menu:

        "Try your luck and grab it!":
            jump success
        

        "Maybe that's too risky I should head back to observe other parts of the building":

            jump Building_options

label success:
    scene bg coreback2
    "Succes! You pull it off and can grab the overall unnoticed."

    define overall = InventoryData("New Item", "You own a beige overall with the CORE branding")

    $ inventory.add_data(overall)

    "{i}The beige overall was added in your notebook. {\i}"

    $ overall_success = True
  
    jump Building_options


label Collect_information:

    #IF this Option is not chosen the Information of John Doe is not usable troughout this plot!!! Needs to be included in the code
    # When chosen set counter to 1 for watch the people so it cant be chosen again
    scene bg main ent2
    show Me with easeinleft:
        xzoom -1.0

    "As you watch people leaving the building, you notice a member of staff wearing his badge on the outside of his trouser pocket."
    "You manage to read his full name, John Doe, and the department: Arithmetic Department."
    $ john_doe_known = True
    define john_doe = InventoryData("John Doe", "Employee at CORE, Arithmethic Department")

    $ inventory.add_data(john_doe)

    "{i} John Doe was added to your notebook. {\i}"

    "You also notice that the employees usually wear suits and that the security guards have a grey uniform."

    menu:

        "Look around and inspect the building" if not full_building:
            jump Building_options

        "Follow them and get a coffee yourself" if not full_building:
            jump Follow_people
    
    "You decide to follow the people and get a coffee for yourself." 

    jump Follow_people 


label Follow_people:

#Checkpoint as you can get caught 
    scene bg cafe

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
    #TO DO
    scene bg cafe1

    "You choose to sit on a table with a guy on his laptop in close proximity."

    #maybe also count choices and hide if they were already selected? YES
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

    jump Laptop_observation #This makes no sense as you can still proceed without the information from this -> Should Jump to Follow people and Laptop choice is gone


label Look_shoulder:

#TO DO
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

    "You have the feeling that you have been caught, and your decision is to leave the store quickly."

    jump leaving_hastly

label Screen_reflection:

    "You try to look at the screen with a reflection of your smartphone
    Success: You see his User Name for Outlook: christian.baker@company.de"

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
    jump leave_shop

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
    scene bg caught
    "You lost the level and need to restart"
    jump level_1
    # here the Player gets caught - Checkpoint should be before entering the coffee shop (No need to investigate building again if done so already)


label Stop_observing:

    "You stop observing a turned off Phone looks suspicious."
    "As you know his name now you try approaching him."

    jump Approach_guy

label Approach_guy:

    p "Hey, Christian How are you?"

    c "I am fine, just a bit stressed tho and who are you?"

    menu:

        "I am [povname]" if john_doe_known: 
            jump Real_name

        "I am John Doe." if john_doe_known:
            jump John_doe
    
    "I am [povname]"
    jump Real_name

label Real_name:

    p "What department are you working in? I remember seeing your face somewhere in the onboarding process."

    c "Ooh I am from public relations work."

    p "So I heard rumors that the company might be in trouble. Do you know anything about that? I just started here and I don't want to look again for a job. You know I have to care for my mom. She is already in elderly care and it is quite expensive."

    c "I am not supposed to talk about things like that! But don't worry we have our methods to stop allegations of pesky reporters. 
        What department are you from?"

    p "Something with accounting."

    p "So is there something in the bush?"

    c "I dont know who you are. I have to leave now!"

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
            #If not done so already! Count choice
        "Eavesdrop employees conversation.":
            jump Employee_conversation
            
        "Leave the shop":
            jump leave_shop


label Employee_conversation:

#scene
    scene bg cafe2

    show Me with easeinleft:
        xzoom -2.0
        yzoom 2.0
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

    "The trio finishes their lunch cleans up and leaves their table."

    "That was interesting. Lets try observing something else now."

    jump Follow_people

label leave_shop:

    #scene
    scene bg badge
    "While you leave the shop you notice an Employee Badge.
    It is difficult to recognize because it is peeking out from under a chest of drawers. 
    You take it without much thought."
    define badge = InventoryData("New Item", "Employee badge")

    $ inventory.add_data(badge)

    $ badge_found = True
    "{i}The badge was added in your notebook. {\i}"

    "Check your notebook for everything you learned about." #John Doe and christian baker should have an entry

    #TO DO - where do you jump to? Transition Blackscreen could be fine
    scene bg n42
    "It's the next day. You gathered a lot of information and now want to target CORE and try to get inside their head quarter."

    $ todo.update_aim("Get inside the CORE head quarter")
    "{i}Your goal was updated. {\i}"
    jump getinside


label leaving_hastly:
    scene bg n42

    "You leave the store and don't look back. You probably shouldn't be seen here again any time soon"
    "Check your notebook for everything you learned about." #Notebook should open highlight new entries and items
    #scene in front of office building
    
    #TO DO
    "It's the next day. You gathered a lot of information and now want to target CORE and try to get inside their head quarter."

    $ todo.update_aim("Get inside the CORE head quarter")
    "{i}Your goal was updated. {\i}"
    jump getinside

label getinside: #checkpoint 3
    


    menu:
        "Go to the company disguised as a canteen employee":
            jump canteendisguise
        "Go as an employee with the badge found" if badge_found: 
            jump withbadge
        "Dress as a security guard":
            jump securitydisguise

label withbadge:
    jump inside_building

label securitydisguise: #wear tshirt with security on it
    "You wear your self designed T-shirt that says security and walk towards the main entrance."
    s "Hey you! Stop! Who are you?"
    p "I am Drew, working for security of this company"
    s "That shirt is not part of our uniform. I will call the police."#goto checkpoint 3

label canteendisguise:
    scene bg coreback3
    show Me with easeinleft:
        xzoom -1.0

    "Disguised as canteen employee, you walk towards the back entrance that leads to the company’s canteen." 
    scene bg canteendoor
    show Me
    "Heavily loaded and appearing to be busy with work, you move toward the door and open it. Then suddenly a kitchen employee looks at you weirdly."
    scene bg kitchen
    show Me canteen
    show k1 stressed

    #[That person sees you Character canteen employee, surprised, stressed expression
    #TO DO
    menu:
        "Hide your face, and try not to drag too much attention on you":
            jump hideface
        "Act friendy and ask him for help with the box you are carrying" if badge_found: 
            jump askhelp
    

label hideface:
    "Employee: Hey I’ve never seen you here, who are you?"
    p "I’m Drew, just started working here."
    "Employee: I haven't heard of a new colleague starting here." 
    "I feel like you are just trying to sneak inside the office for some reason. I will call security"
    menu:
        "Run inside the building":
            jump runinside
        "Run outside the building ": 
            jump runoutside

label runinside:
    "As soon as you run towards the door that leads deeper inside the building other people notice you and you feel someone tackle you over"
    jump Caught # is that right?
 

label runoutside:
    scene bg coreback3
    "You rush through the door and run as fast as you can. But the man is running after you." 
    "You gain more and more distance and finally he looses track of you. "
    "While calming you breath you think about how to enter the building instead."
    jump inside_building
    
    #e10: man who looks like he goes to the gym in cooking clothes
label askhelp:
    p "Hey, could you please help me with the box, you look like you are stronger than me."
    e10 "Oh yes sure!"
    "You hand him the box"
    p "Thank you. Do you go to the gym?"
    show k1 happy
    e10  "Thanks! Yes, I go almost every day."#flattered expression
    p "Wow, you definitely need to give me work out tips. I have to go now though. See you!"
    e10 "Have a nice one!"

    jump inside_building

label inside_building:
    scene bg main ent
    
    #bg_office_reception
    #TO DO
    "With your disguise intact, you confidently stride through the office building, blending in seamlessly with the bustling crowd. The air is thick with the hum of productivity as employees rush to and from."
    # Checkpoint 1as the Option 1 is correct, if the player chooses 2nd or 3rd option then he will jump to inside_building
    menu:
        "Explore the cubicles":
            jump explore_cubicles
        "Head to the break room":
            jump break_room
        "Check the elevators":
            jump check_elevators

label explore_cubicles:
    scene bg cubicles
    show Me with easeinright
    "Now that you're inside you change back to your regular attire"
    
    scene bg whiskers
    #[Taking a photo from the mobile phone] [BG: Desk with the photo of a dog name whiskers]
    "As you quietly explored the cubicles, your attention was drawn to a desk adorned with a framed picture of an elegant dog, its name proudly displayed beneath the image  Whiskers. The feline's regal demeanor made the picture amusingly out of place in the corporate setting. Intrigued, you decided to capture this curious discovery."

    "After discreetly snapping a photo of Whiskers' portrait, you continued your investigation. Amongst the papers on the desk, you found an official document containing the name and date of birth of an employee."

    "The document provided you with the name Alex Johnson and a birthdate (12/08/1975), leaving you to wonder about the connection between the cat and the employee."

    "Quickly noting down the name and date of birth from the document, you proceeded further."

    define alex_data = InventoryData("Alex Johnson", "Birth: 12/08/1975, potential owner of cat Whiskers")

    $ inventory.add_data(alex_data)

    "{i}The information about Alex Johnson and Whiskers was added to your notebook. {\i}"

    "There your eyes fell upon one famous quote which is unique in the office environment."

    #[Wrting in Journal] [BG: Picture with quote written Here's looking at you, kid – Casablanca]
    #Could you please explain what you mean?

    "A spark of recognition ignited in your mind as you realized the significance of this quote. Hastily, you made a mental connection between the employee's name, the birthdate, and the movie quote."

    "Pulling out your notebook, you meticulously wrote down the details: Alex Johnson, 12/08/1975, Quote: Here's looking at you, kid – Casablanca."

    define alex_data_2 = InventoryData("Alex Johnson", "Birth: 12/08/1975, potential owner of cat Whiskers, Quote: Here's looking at you, kid – Casablanca")

    $ inventory.remove_data(alex_data)
    $ inventory.add_data(alex_data_2)

    "{i}The information was added to your notebook. {\i}"

    "While you're capturing the information, you accidentally knock a pen off the desk, drawing the attention of an observant employee."
    jump interaction_with_employee

label break_room:
    # [BG: Office Canteen with many employees]
    # TO DO
    scene bg office canteen
    "Now that you're inside you change back to your regular attire"


    show Me with easeinright

    "The break room is bustling with activity. Colleagues gather around tables, sharing stories and enjoying a brief respite from their busy day."
    menu:
        "Join a Group of Colleagues Chatting Nearby":
            jump colleagues_chatting_nearby
        "Sit Alone and Observe from a Distance":
            jump observe_from_a_distance

label check_elevators:
    scene bg elevator
    show Me with easeinleft:
        xzoom -1.0
        
    # BG: Elevators
    #TO DO

    menu:
        "Watch a Password Reset Procedure":
            jump password_reset_procedure
        "Interact with Employees Using the Elevator":
            jump employees_using_elevator
        "Examine Posted Notices or Instructions near the Elevators":
            jump instructions_near_the_elevators

label interaction_with_employee:
    scene bg cubicles
    show Me 
    show e4
    # Interaction after knocking off the pen
    menu:
        "Apologize and engage in light conversation":
            jump apologize_and_engage
        "Act confused and ask for help":
            jump act_confused_and_ask_for_help
        "Feign ignorance":
            jump feign_ignorance
        "Try to deflect with humor":
            jump deflect_with_humor

label apologize_and_engage:
    scene bg cubicles
    show Me 
    show e4
    #BG in the cubicles
    # TO DO
    e4 "Hey, is everything alright here? You were looking at that desk pretty intently."


    p "Oh, my apologies! I'm just trying to get my bearings. Everything's so high-tech here, and I'm still struggling with the basics, like those complex password policies."

    e4 "Well, everyone has to follow the IT guidelines. It's for our own security. Are you sure you're in the right area?"

    p "Yes, I'm just overwhelmed by the transition. Back at my last job, I had a simpler system for remembering passwords. Here, it's like you need an encryption key for everything. Do you ever find it a bit much?"

    e4 "I guess it can be a lot at first. But you shouldn't really be discussing password strategies openly. It's a security risk."

    p "Of course, I understand the need for confidentiality. I was just hoping for some generic tips on managing all these different systems. It's a bit daunting, you know?"

    e4 "Well, without going into specifics, I suppose some of us might use familiar things to create a complex password. But that's as much as I can say. You really should be careful about these conversations."

    p "I appreciate the advice. I'll be sure to keep that in mind. Thank you for your help."

    "Some people use familiar things to create a complex password."
    
    
    jump continue_exploring

label act_confused_and_ask_for_help:
    scene bg cubicles
    show Me 
    show e4 
    #BG in the cubicles
    # TO DO
    p "I'm sorry, I got lost in thought. I'm actually trying to find the meeting room. Can you point me in the right direction?"

    e4 "Oh, of course! No problem at all. You'll want to head down this hallway, take the second left, and then it's the third door on your right. You can't miss it; there's a sign that says 'Meeting Room' right outside the door."

    p "Thanks so much! This place is a bit of a maze."
    show e4 smile
    e4 "Tell me about it! Took me a week to stop getting lost. If you need anything else, just let one of us know. Good luck with your meeting!"

    p "I appreciate it. Have a great day!"

    jump continue_exploring


label feign_ignorance:
    scene bg cubicles
    show Me 
    show e4 
    #BG in the cubicles
    # TO DO
    p "Oh, this isn't my desk? I'm so sorry, I thought this was where I was supposed to be for my orientation. Do you know where that is?"

    e4 "No worries at all! It can be confusing around here on your first day. Your orientation is actually happening in the conference room on the first floor. If you take the elevator down, it's right across from the reception area. You'll see a sign marked 'Orientation' outside the door."

    p "Thank you for being so understanding. I'll head down there right away. Hopefully, I haven't missed too much."

    e4 "I'm sure you'll be just fine. They usually start with introductions and some basic company policies, so you should be able to catch up quickly. If you need help finding anything else, just ask anyone here. We're all happy to help."

    p "Thanks again. I'll do that. Have a good day!"

    jump continue_exploring

label deflect_with_humor:
    scene bg cubicles
    show Me 
    show e4 
    #BG in the cubicles
    p "I guess I'm just mesmerized by all the hustle and bustle here. It's like trying to remember a password you just created and forgot two seconds later. Happens to you too, right?"
    show e4 smile

    e4 "Oh, absolutely! It's like my brain decides to do a hard reset the moment I hit 'save'. Just the other day, I spent 20 minutes resetting my password, only to realize I was typing it wrong because I forgot I added an exclamation mark at the end. It's always the special characters that get me."

    p "I know, right? I think our brains weren't designed to hold onto complex passwords mixed with numbers, letters, and symbols. Maybe we should just start using 'password123' and call it a day."

    e4 "Wouldn't that make our IT security team's heads spin! Imagine the chaos. But yeah, I feel you. Keeping track of all these passwords is a full-time job by itself."

    p "Definitely. Well, I better get back to trying to navigate this place. Thanks for the laugh!"

    e4 "Anytime! If you ever need a break from the password madness, you know where to find some sympathy. Good luck finding your way around!"

    jump continue_exploring

label colleagues_chatting_nearby:
    scene bg office canteen

    show Me 
    show e5 with easeinleft
    # [BG: Office Canteen with many employees]
    e5 "Hey, you're new here, right? We were just talking about the team-building event. Did you enjoy it?"


    p "Hey, I am new here! The team-building event was really fun. I got to learn a lot about my new colleagues. How about you guys?"
    show e6 with easeinleft

    e6 "Oh, it was great! I think it's always good to step out of the work routine and get to know each other in a different setting."

    e5 "Absolutely. Plus, it was fun sharing those quirky facts about ourselves. Like, who would've thought I'd be using the year I joined this company as a fun fact?"

    p "That's pretty interesting. Does the year hold a special significance for you?"

    e5 "Well, it was a major turning point in my career, so yeah, it's significant for me. Plus, it's easy to remember, which always helps."

    e6 "I went with something less obvious. I talked about my weird hobby of collecting vintage postcards."

    p "That's really unique, Sam. It must be quite a collection."

    e6 "It is! Anyway, how did you find the password setup here? A bit daunting, isn't it?"

    p "Yeah, it's definitely more complex than my previous job. I'm trying to come up with something strong yet memorable."

    e5 "That's always the challenge. I always suggest mixing personal elements with random characters. Makes it strong and personal."

    e6 "But not too personal, or obvious. Like, don't use your pet's name or anything. Everyone does that."

    p "Right, I was thinking along the lines of something related to my start here. Maybe mixing in the year with other characters."

    e5 "Hmm, it could work, but be careful with using anything too straightforward. The year on its own is a bit risky. You need to throw in some curveballs."

    p "Got it, thanks for the tip. I'll make sure it's not something easily guessable."

    e6 "Yeah, and remember, these conversations about passwords are a bit sensitive. Best to keep the specifics to ourselves."

    p "Of course, I appreciate the advice. I'll come up with something solid and secure."

    e5 "That's the spirit. And hey, welcome to the team! If you need any help, feel free to ask us."

    p "Thanks! I'm sure I'll fit right in."


    "You didn't find much information about the passwords" 
    
    jump inside_building

   
label observe_from_a_distance:
    scene bg office canteen

    show Me with easeinleft:
        xzoom -1.0
    # [BG: Office Canteen with many employees]

    "From your isolated vantage point, you overhear fragmented conversations, catching bits and pieces about office life and daily routines. While you gain a general sense of the company culture, no specific information about password creation or other sensitive topics is gleaned."
    jump inside_building

label password_reset_procedure:
    scene bg elevator2
    show Me with easeinleft:
        xzoom -1.0
    # BG in the elevators
    # TO DO

    "Near the elevators, you notice an IT support staff assisting an employee with a password reset. This situation provides a rare opportunity to understand the company's password policy. As the IT staff member guides the employee through the reset process, you overhear snippets of their conversation."
    
    staff "Remember, your password needs to be strong. It should be something memorable but not obvious to others."
    "The employee nods, considering for a moment, then types something in. You can't see the exact keystrokes, but you notice the employee's eyes momentarily glance at a photo pinned nearby – it's a picture of a mountain."
    e7 "Okay, done. I've used my favorite hiking trail name and added the year I first hiked it, plus an exclamation mark."
    staff "That's a good mix. It's personal but not something everyone would know. Just make sure you remember it without writing it down."
    "The employee leaves, looking satisfied. This interaction gives you a valuable insight into how employees might construct their passwords using personal hobbies or experiences combined with significant dates and special characters."

    jump inside_building

label employees_using_elevator:
    scene bg elevator
    show Me 
    
    # [BG: Elevators]
    #TO DO
    "Spotting an opportunity, you approach an employee who looks like they might be heading to an IT support session."
    show e8 with easeinleft
    p "Hi, I couldn't help overhearing you're heading to IT. I'm new here and still figuring things out. Any advice on managing all these passwords we have to use?"
    e8 "Oh, hi. Honestly, I just follow whatever the IT guidelines say. Can't really go wrong with that, right?"
    p "True, true. I was just wondering if there's a trick to remembering them. I always find myself getting them mixed up."
    e8 "Sorry, I can't really help you there. I just do my best to keep them straight. Maybe IT could give you some tips?"
    
    "The employee gives a polite but dismissive smile and continues on their way, offering no further information."
    jump inside_building


label instructions_near_the_elevators:
    scene bg elevator

    # BG: Some image of instructions near elevator
    #TO DO
    "You carefully read the notices and instructions posted near the elevators. They mostly consist of safety protocols and elevator usage guidelines, offering no clues about password creation or security measures."

    jump inside_building

label continue_exploring:
    scene bg staircase
    show Me
    #BG Office stairs
    #TO DO

    # Checkpoint 2, here the 3rd option is correct and if you choose 1 or 2nd option you continue #further but you will not find out about the room 303 so the player again comes at this option

    "Regardless of your choice, you continue your exploration."
    menu:
        "Investigate Support Staff Contacts" if support_staff_contacts_done:
            jump support_staff_contacts
        "Explore Middle Management Contacts":
            jump middle_contacts
        "Search for a high-ranking employee":
            jump call_mr_johnson

label support_staff_contacts:
    scene bg call
    #TO DO
    #  Scene"[Player with phone dailing and Burt on the other side]" BG: Inside some room
    "Feeling like an undercover agent, you decide to explore the support staff, aiming for the custodian Burt W. Mopbucket, the head of janitorial services. You figure Burt might have some amusing stories about his experiences while cleaning up after everyone."
    "Dialing Burt's number, you brace yourself for a less-than-warm reception."

    p "Hello, Burt? It's Mike from HR. Just doing a quick check-in. Any interesting or amusing things happening during your janitorial adventures?"
    #disgruntled
    burt "Mike from HR? What's this about? I've got a mop in my hand, and I'm not in the mood for chit-chat."

    p "No chit-chat, Burt. Just wondering if you've come across any funny incidents or quirky moments while keeping our workplace spick and span."

    burt "Look, Mike, I'm not here to gossip. I've got a job to do. If you need something cleaned up, submit a request through the proper channels."

    p "Sure thing, Burt. Keep up the excellent work on those floors."

    $ support_staff_contacts_done = True
    
    jump encounter_with_office_cat

label middle_contacts:
    scene bg call
    "With a sly grin, you decide to delve into the world of middle management, hoping to find an unsuspecting hero among the ranks. Scrolling through the directory, you pick Ivy P. Paperwork, the manager of documentation control. Her title might not scream glamour, but you figure she could be the keeper of hidden secrets."

    # TO DO
    #"[Player with phone dailing and Ivy on the other side]" BG: Inside some room

    "You dial Ivy's number and, after a few rings, she picks up."

    p "Hi, Ivy, it's Mike from HR. Just checking in to see if there's anything interesting happening in the documentation world. Any quirky office stories or unique challenges you've faced lately?"


    #Guarded and skeptical
    ivy "Mike from HR? This isn't some kind of survey, is it? I'm pretty busy here."

    p "No survey, Ivy. Just trying to get a feel for the exciting world of middle management. Any funny anecdotes or amusing incidents you'd like to share?"

    ivy "I'm not sure what you're getting at, Mike. We just handle paperwork and try to keep things running smoothly. If you have HR-related questions, you should go through the proper channels."

    p "Got it, Ivy. Just thought I'd lighten the mood with some office tales."

    jump encounter_with_office_cat


label call_mr_johnson:
    scene bg call

    "You find the number of a high-ranking executive, Mr. Johnson, in the directory."
    "You decide to call Mr. Johnson and try to extract information from him."

    #Player with phone dailing and me johnson on the other side BG: Inside some room
    #TO DO

    menu:
        "Introduce yourself as IT support":
            jump introduce_as_IT
        "Pretend to be a colleague":
            jump pretend_to_be_colleague
        "Pretend to be the CEO":
            jump pretend_to_be_CEO
     
    
label introduce_as_IT:

    "You claim to be from IT support, conducting a routine check, and ask him for his computer details."
    p "Hello, Mr. Johnson? This is Alex from IT support. We're conducting a routine check on all executive accounts today. Can I get your computer's model and current operating system version to ensure everything's up to date?"

    mr_johnson "IT support, you say? That's odd; I wasn't notified of any routine checks happening today. Can you tell me exactly what kind of updates you're referring to?"

    p "Oh, it's just standard procedure, sir. We're ensuring that all systems are secure and fully updated to prevent any potential security breaches. It's more of a precautionary measure."

    mr_johnson "I see. But shouldn't these updates be automatic? And usually, for anything regarding executive accounts, there's an email sent out from IT. Can you verify which department you're calling from?"

    p "Yes, of course, updates are typically automatic. However, for high-level executive accounts, we perform manual checks to personalize the security settings. I'm calling from the main IT department. Would you mind providing me with the requested details so we can proceed?"

    mr_johnson "I think I'd be more comfortable verifying this call with our IT department directly before giving out any information. Can I have your extension so I can call you back?"

    p "Actually, Mr. Johnson, I'm currently not at my desk, but I assure you, this won't take long. It's just a formality we need to complete for our records."

    mr_johnson "I'm sorry, but without proper verification, I'm not comfortable disclosing any information over the phone. I'll reach out to our IT department myself and follow up on this. Goodbye."

    #This is the wrong option and you cant go further so go to Checkpoint 2

    jump Caught


label pretend_to_be_CEO:

    p "Hello, Mr. Johnson? This is your CEO. I'm currently reviewing some critical documents for our upcoming board meeting and seem to be having trouble accessing the financial projections. I need to check them from another account. Could you assist me by providing your login credentials so I can verify some details urgently?"

    mr_johnson "I'm sorry, but this is quite unusual. For security reasons, we're advised never to share our login credentials. Could you perhaps specify which documents you need? I can access and share them through a secure channel."

    p "I understand your hesitation, but given the urgency and the sensitive nature of the information, this seemed like the most direct approach. It's just this once, for expediency."

    mr_johnson "I appreciate the urgency, but sharing login details over the phone goes against our company's security policies. I can help in another way or perhaps we can arrange for IT to grant you temporary access?"

    p "I see your point, and I respect your adherence to our security protocols. Let's go with your suggestion and involve IT for the appropriate access. My apologies for the unconventional request."

    mr_johnson "No problem, I'll get in touch with IT right away and ensure they expedite your access. Thank you for understanding the importance of following our security protocols."

#This is the wrong option and you cant go further so go to checkpooint 2

    jump Caught


label pretend_to_be_colleague:
    p "Hello, Mr. Johnson? It's Mike from HR. I hope I'm not catching you at a bad time."

    mr_johnson "Oh, hey Mike! No problem at all. What can I do for you?"

    p "Well, I've been settling into my new role and heard some interesting rumors floating around the office. People are mentioning something about scandalous files on the network. Any truth to that?"

    mr_johnson "Scandalous files? That's an unusual thing to hear about. Where did you get that information, Mike?"

    p "Just some water cooler talk, you know how it goes. I thought I'd check in with someone in the know, like you. Keep it between us, though."

    mr_johnson "Water cooler talk, huh? Seems a bit odd for that to be the topic of casual conversation. Why are you so interested in this, Mike?"

    p "Oh, it's just the usual office grapevine, you know? Curiosity got the better of me. I figured I'd check with someone who has the real scoop."

    mr_johnson "Well, yes, there is a computer in Room 303 with some sensitive information, but it's nothing for everyone to be discussing. Keep it quiet, alright?"

    p "Absolutely, Mr. Johnson. I get it; sensitive stuff. Your secret's safe with me. Anything I should be aware of, or is it all under control?"

    mr_johnson "We're handling it. Just be cautious about spreading rumors, Mike. We don't need unnecessary panic around here."

    p "Of course, Mr. Johnson. I appreciate the heads up. If there's anything I can do to assist or keep things under wraps, you know where to find me."

    mr_johnson "Thanks, Mike. Let's keep it professional around here, alright? I don't want this turning into a bigger issue than it needs to be."

    p "Agreed, Mr. Johnson. I'll be sure to keep things on the down-low. Anything else I should know or any way I can help with the situation?"

    mr_johnson "No, just focus on your work for now. We'll handle this internally. If we need anything from HR, we'll reach out. Thanks for checking in, Mike."

    p "No problem, Mr. Johnson. I'm here if you need anything. Have a good day."

    jump encounter_with_office_cat

label encounter_with_office_cat:

    # Furry Cat Bg: Hallway of the office
    #TO DO
    scene bg office cat
    "As you navigate the halls, you encounter an office cat. It seems to take a liking to you, following you curiously."

    menu:
        "Pet the cat":
            jump pet_the_cat
        "Ignore_the_cat":
            jump Ignore_the_cat

label pet_the_cat:
    scene bg office cat3

    #Bg: some hidden compartemnt
    #TO DO

    "You take a moment to pet the cat, appreciating the unexpected companionship."
    p "Well, aren't you a friendly one? Need a partner in crime, huh?"
    "The cat unexpectedly nudges a wall panel with its head, revealing a hidden compartment."
    scene bg office cat2
    p "Now that's interesting. What secrets are you hiding, my furry friend?"

    "Inside the compartment, you find a set of old keys."

    menu:
        "Take the keys":
            jump take_the_keys
        "Ignore the keys and go to room 303":
            jump room_303


label Ignore_the_cat:

    #This is the wrong option and you cant go further so go to checkpooint 2
    jump Caught

label take_the_keys:

    # Here the player does not know about room 303 if he has selected option 1 and option 2 from label #continue_exploring. 
    "You decide to take the keys, thinking they might come in handy."
    jump room_303

label room_303:
    scene bg room303
    "You enter Room 303, the cat still by your side. The dimly lit room is filled with rows of computers."


    "As you try to access the computer, you realize it's password-protected."

    #default computer_info_collected = False

label desk_choices:
    menu:
        "Unlock the computer":
            jump unlock_the_computer
        "Open the Cupboard with the keys you found":
            jump open_the_cupboard

    #If the player uses option 1 first then the computer will not be unlcoked 
    #Only after exploring the option 2 player will be able to unlock the computer

label unlock_the_computer:
    scene bg computer
    # Computer scene
    #TO DO

    "Frustrated by the password prompt, you decide to take a more direct approach and attempt to unlock the computer."
    
    "Trying a few common passwords that often slip people's minds or are used out of convenience, you input variations of 'password,' '123456,' and 'admin,' but to no avail. "
    
    "The computer remains securely locked, refusing to grant access."

    p "Well, that was worth a shot."

    "Password: whiskers19752926 (This is just until we complete this story part)"

    #Then you look in the INVENTORY and find out about the photo of a dog, a document in which date of #birth is mentioned and the photo you find after opening the cupboard.
    
    # Is the player supposed to try different passwords here?
    label password_2:
        python:
            style.input.color = "#ffffff"
            password_2 = renpy.input("", length=32, screen = "nameInput")
            password_2 = password_2.strip()

    if password_2 == "whiskers19752926":
        jump right
        
    else:
        p "Wrong Password! Would you like to try again?"
        menu:
            "Try again":
                jump password_2
            "Return to choices":
                jump desk_choices
    
    #SO there will be computer screen 
    #The password will be whiskers19752926  first dog name, then date of birth(year) and then the image #found in the background.

    #work with computer info collected?

    jump hidden_camera

label open_the_cupboard:
    scene bg locker

    #After opening the cupboard you find the photo of Mr. johnson along with family and in the #background you can see a number "2926"

    # Will be added to the notebook as soon as we have a visual by the design team

    #$ computer_info_collected = True

    jump unlock_the_computer


label hidden_camera:

    # Checkpoint 3 , after unlock the computer if the player gets caught after this, he can come back #to this option
    #BG: camera inside the room
    #TO DO
    scene bg camera

    "As you delve into the files, you notice a hidden security camera"
    menu:
        "Disable the Camera":
            jump disable_the_camera
        "Evade the Camera's View":
            jump evade_camera_view
        "Create a Distraction":
            jump create_a_distraction

label disable_the_camera:
    "With a sense of urgency, you decide to disable the hidden security camera to avoid leaving any evidence of your covert operation. Stealthily reaching into your pocket, you pull out a small toolkit equipped with electronic gadgets."

    p "Time to go incognito."

    "Carefully, you open the panel concealing the camera's wires, aiming to cut the power source or manipulate its circuits. However, in the process, a tiny alarm is triggered, and a soft electronic beep resonates in the room."
    scene bg cam alarm
    #*Automated System:* "Security breach detected. Security breach detected."
    #TO DO

    "Panicking, you realize that your attempt to disable the camera has backfired. The unexpected alarm attracts attention, and you hear distant footsteps approaching rapidly."

    #This is the wrong option and you cant go further so go to checkpooint 3
    jump Caught


label evade_camera_view:
    show Me with easeinright
    "Choosing a more subtle approach, you decide to evade the camera's view. Carefully studying the room, you identify blind spots and strategically move from cover to cover, using office furniture and potted plants to shield yourself from the camera's lens."

    "Silently, you navigate the room, successfully avoiding detection. As you reach the desired spot without triggering any alarms, a sense of relief washes over you. The camera continues to monitor the room, unaware of your presence."

    jump fumbling_with_the_camera


label create_a_distraction:
    "Thinking quickly, you decide to create a distraction to divert attention away from the camera's view. Your plan is to trigger a minor, but noticeable incident elsewhere in the room to draw the camera's focus."

    p "Let's cause a little diversion."
    "You spot a small stack of papers near a fan. Moving cautiously, you turn the fan to its highest setting, aiming to scatter the papers across the room."
    "The idea is that the fluttering papers will create enough movement to redirect the camera's attention temporarily."
    scene bg fan
    "As you activate the fan, the papers whirl into the air, creating a chaotic flurry."
    "However, this action inadvertently triggers the room's motion sensors, which are linked to the security system."
    
    #Automated System: "Unusual activity detected. Investigating."
    #TO DO

    "The sudden activation of the motion sensors, coupled with the chaotic movement of papers, escalates the situation. Lights begin to flash, and an alarm blares through the room."
    scene bg cam alarm
    "Realizing that the diversion has escalated far beyond your intentions, you hear security personnel being alerted over the building's intercom system."

    #This is the wrong option and you cant go further so go to checkpooint 3
    jump Caught

label fumbling_with_the_camera:
    scene bg room303
    show Me
    show e9 with easeinleft
    e9 "Hey, what are you doing in here?"
    
    menu:
        "Act casual":
            jump act_casual
        "Confront the employee":
            jump confront_the_employee

label act_casual:
    

    "You act casual, pretending to be lost."

    p "Oh, hey there. I was just trying to find the restroom, and I must have taken a wrong turn. Sorry about that!"

    "The employee eyes you skeptically but seems to buy your explanation. He points you in the direction of the restroom, and you proceed as if nothing happened."

    "As you leave the room, you take note of the employee's suspicious gaze but continue to act nonchalant. You casually stroll through the corridors, blending in with the office environment. "

    jump Leaving_building


label confront_the_employee:

    p "Oh, hey there. I'm just doing some maintenance work. Got a call about an issue with the camera in this room."

    e9 "Maintenance? I didn't hear anything about that."

    e9 "I better call security and confirm this. We can't have unauthorized people messing with our cameras."


    "The employee remains suspicious and decides to check with security. Your attempt to confront him raises further red flags."

    "Your attempt has backfired. Security is on their way."

    #This is the wrong option and you cant go further so go to checkpooint 3
    jump Caught

label Leaving_building:
    scene bg cubicles
    "I should get out of here before anyone catches me." #checkpoint4

    menu:

        "Leave building through the kitchen of the canteen":
            jump leavecanteen

        "Leave by yourself through main entrance with a group of people":
            jump leavemain

        "Wait until you don’t see anyone else to leave.":
            jump leavealone

label leavealone:
    scene bg checkpoint2
    show Me with easeinright
    "As you approach the security door, you notice that you would have needed an ID to scan for it to open."

#[Security guard will tap on your shoulder, you turn around]
    scene bg checkpoint3
    show Me 
    show guard1 with easeinleft
    s "Where is your ID card"

    p "I must have lost it, it was right there on my pants"

    menu:

        "Punch him in the face":
            jump punch
        "I must have lost it, it was right there on my pants":
            jump apology
        "Take the ID badge in your inventory" if badge_found:
            jump idcard

label punch:#scene you punching him
    hide Me
    hide guard1
    show punch
    "You punch him in the face and run as fast as you can. But only after three steps one of the security guards pulls you back and holds you tight. "
    
    "You realize that they are too strong and you will not get out of the situation anymore."

label apology:
    show guard1
    show Me 
    s "What's your name, I can look for you in our system."

    menu:

        "I am Ryan Nordberg":
            jump ryan
        "I am Christian Baker":
            jump christian

label ryan:#confused

    s "There is no Ryan Nordberg in our system."

    menu:

        "I am new here at this company, maybe that’s why it is not listed yet":
            jump lie
        "I have to go to an important appointment and you are wasting my time. Please get your manager.":
            jump berude

label lie:

    "The security guard calls his colleague on the phone: “ Hey there is a person, some Ryan Nordberg, he doesn’t have an ID and I can’t find him in our system. What am I supposed to do?"

    s "Alright, I won’t let him leave"

    "He brings you into a small room."
    "As you are waiting for the police you know that you will not be able to continue your mission and that you have to take accountability for your illegal activities."

    #gameover
    jump Caught # like that? #go to checkpoint4

label berude:
    show guard surprised
#[Surprised look]
#TO DO

    s "It’s ok Ryan, you can pass. Next time bring your ID."#friendly

    #outside
    scene bg n42
    show Me with easeinleft:
        xzoom -1.0

    p "That was close. Thank god, I got out of here. I am going to meet Cathy to tell her about everything."

    jump cathymeet

label christian:

#[SG, male, serious look]
# TO DO

    "You see the security guard typing something on his keyboard. "
    s "Alright there we go, Christian Baker. Have a great day!"

#outside
# TO DO
    scene bg n42
    show Me with easeinleft:
        xzoom -1.0
    p "That was close. Thank god, I got out of here. I am going to meet Cathy to tell her about everything."

    jump cathymeet

label leavecanteen:
    scene bg kitchen
    show Me chef
    "You change back into your kitchen clothes and walk into the company's kitchen." #you with kitchen clothes

    "The kitchen is brimming with energy and hectic as chefs and kitchen staff hustle to prepare dishes for the employees. No one really pays attention to you. "
    "You feel safe and almost reach the exit door but suddenly a woman stops you in front of the door."
    show k2 stressed with easeinleft
    k2 "Hey, sorry but can you quickly help out with the dessert. It's so busy right now we can't keep up."

    menu:

        "No sorry, I don't have time right now.":
            jump decline
        "Yes, sure, what do you need help with?":
            jump helped

label decline:
    show Me chef
    show k2 stressed 
    k2 "Ok, that is unfortunate. I will do it myself then"

    "You see that some of the canteen employees starts looking at you skeptical"#skeptic look
    menu:

        "Rush out as fast as you can.":
            jump rushout
        "Act like you are busy with washing some dishes.":
            jump wash

label wash:
    hide Me
    "While washing some dishes you can listen to a conversation of some of the kitchen staff. "
    show k2 happy with easeinleft
    show k1 happy with easeinright:
        xzoom -1.0 
    k2 "This week we had a delivery with boxes full of avocados"

    k3 "Yes, I have heard our company now buys them from TastyFood and gets huge discounts."

    menu: 
        "Stay and continue listening":
            jump listenkitchen

        "Leave the kitchen through the back door":
            jump leavekitchen

label rushout:
    scene bg coreback3
    show Me

    "You ran out of the back door of the canteen kitchen. However the canteen staff noticed you were acting very suspiciously." 

    p "That was close. Thank god, I got out of here. I am going to meet Cathy to tell her about everything."

    jump cathymeet

label helped:
    show Me chef
    show k2 happy 
    k2 "We have to do the salad. Please add all the ingredients to the bowl."

    k2 "Thank you for your help."

    "As you want to leave through the back door, you can overhear two employees chattering."
    show k1 happy with easeinright:
        xzoom -1.0
    k1 "This week we had a delivery with boxes full of avocados”"

    k3 "Yes, I have heard our company now buys them from TastyFood and gets huge discounts."

    menu:

        "Stay and continue listening":
            jump listenkitchen

        "Leave the kitchen through the back door":
            jump leavekitchen

label listenkitchen:
    scene bg kitchen
    show Me chef
    "One of the two employees notices you looking at them."
    show k2 stressed with easeinleft
    k2 "Hey, is there something wrong? Why are you staring at us?"

    menu: 

        "Sorry I didn't mean to stare at you":
            jump apology2

        "Sorry, I couldn’t help. You look so cute.":
            jump flirt2

label apology2:

    "She gives you a weird look but then turns away to continue doing her job. "
    "You are relieved that she didn’t ask you anything and rush out through the back door as fast as you can."
#Outside
    p "Thank god, I got out of here. I am going to meet Cathy to tell her about everything."

    jump cathymeet

label flirt2:
    show k2 angry
    "Person 1[looking mad]: “Are you crazy? I will forward this harrassment to security. Who are you?"

    "You apologize for offending her but now all eyes in the kitchen are on you. You see her calling security on her phone, knowing that you will not get out of this situation anymore."

    jump Caught #goto checkpoint 4

label leavekitchen:
    scene bg coreback3
    "You left the building out of the back door of the kitchen."

    p "Thank god, nobody caught me. I am going to meet Cathy to tell her about everything."

    jump cathymeet

label leavemain:
    scene bg checkpoint2
    show Me with easeinright
    "You see a group of employees walking towards the exit. You run along with them inconspicuously and walk quickly behind one person through the security door."

#Security guard will tap on your shoulder, 
# to do
    
    "When suddenly a security guy taps on your shoulder"
    scene bg checkpoint3
    show Me 
    show guard1
    s "Hey there! Stop!"
    "Oh no, I got caught..."
    show guard wallet
    s "Hey you lost your wallet"
    
    p "Player: Oh thank you Sir! "
    scene bg n42
    show Me with easeinleft:
        xzoom -1.0
    "You rush out of the building" 
    p "Thank god, nobody caught me. I am going to meet Cathy to tell her about everything."

    jump cathymeet

label cathymeet:#meet her in a cafe/bar
    scene bg coffee
    show Me with easeinright
    show cathy with easeinleft
    p "Hey Cathy, I checked out CORE today but I could not find any valid information. I just found this photograph in the trash. Maybe we should give up and move on.."

    c "Hmm, I am sorry.. let me see the photo. "
#[show photo]
#to do
    c "Wait. That’s senator John Smith right there. Why would he be in this picture? "
    p "That’s surprising, I didn’t know that. The other people are the CEOs of CORE."

    c "I have the feeling that something is wrong. Maybe you could find more information about Senator Smith, next."

    p "Okay, I will be in touch!"

    jump start

 