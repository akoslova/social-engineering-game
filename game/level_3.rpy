$ renpy.include("inventory.rpy")
$ renpy.include("tutorial_story.rpy")
$ renpy.include("level_1.rpy")
$ renpy.include("level_2.rpy")

define ph = Character (_("Patric Hardman"), color="#8e0000")
define receptionist2 = Character (_("Receptionist"), color="#8e0000")
define marcus = Character (_("Marcus Johnson"), color="#8e0000")
define hs = Character (_("Hotel Staff"), color="#8e0000")
define sec = Character (_("Secretary"), color="#0000f9")


image wfhcall = "wfhcall.png"
image sec_call = "sec_call.png"
image sec_call2 = "sec_call2.png"
image sec_call3 = "sec_call3.png"
image sec_call4 = "sec_call4.png"
image ph_call4 = "ph_call4.png"

image search1 = "search1.png"
image search2 = "search2.png"
image search3 = "search3.png"
image search4 = "search4.png"
image search5 = "search5.png"
image search6 = "search6.png"
image search7 = "search7.png"
image chat = "chat.png"
image insta = "insta.png"

image bg wfh:
    "bg wfh0"
    pause 0.25
    "bg wfh1"
    pause 0.25
    "bg wfh2"
    pause 0.25
    "bg wfh3"
    pause 0.25
    "bg wfh4"
    pause 0.25
    "bg wfh5"
    pause 0.25
    "bg wfh6"
    pause 0.25
    "bg wfh5"
    pause 0.25
    "bg wfh4"
    pause 0.25
    "bg wfh3"
    pause 0.25
    "bg wfh2"
    pause 0.25
    "bg wfh1"
    pause 0.25
    repeat

image bg wfhphone:
    "bg wfh20"
    pause 0.25
    "bg wfh21"
    pause 0.25
    "bg wfh22"
    pause 0.25
    "bg wfh23"
    pause 0.25
    "bg wfh24"
    pause 0.25
    "bg wfh25"
    pause 0.25
    "bg wfh26"
    pause 0.25
    "bg wfh25"
    pause 0.25
    "bg wfh24"
    pause 0.25
    "bg wfh23"
    pause 0.25
    "bg wfh22"
    pause 0.25
    "bg wfh21"
    pause 0.25
    repeat

label level_3:
    call inventory


label investigation:
    "Your mission to find out about the Crimson Group begins now."
    scene bg wfh

    default website_visited= False
    default news_visited= False
    default online_visited= False

    label invest1:
    menu:
        "Visit the Crimson Group's official website." if not website_visited:
            jump official_website

        "Search for news articles and reports" if not news_visited:
            jump news_articles3

        "Delve into forums and online discussions" if not online_visited:
            jump online_discussion

        "Search through social media":
            jump social_media

label official_website:
    scene bg wfh
    show search1 with dissolve
    #BG: Laptop Screen Crimson Group Website

    "You navigate to the Crimson Group's website, greeted by their bold slogan: 'In the Shadows, We Forge Your Peace'.However, detailed information about their operatives remains elusive."
    menu:
        "Examine their service offerings more closely.":
            jump service_offering
        "Look for any mention of specific operations.":
            jump specific_operations
        " Search for contact information or office locations.":
            jump office_location

label service_offering:
    scene bg wfh
    show search2 with dissolve
    #BG: Laptop Screen and Service offering page

    "You delve into the descriptions of their services, ranging from high-risk protection details to strategic military consulting. "
    "Despite the wealth of information about what they offer, the specifics about who exactly carries out these services remain a secret."

    "This choice doesn't lead to the breakthrough you hoped for."

    $ website_visited = True
    jump invest1

label specific_operations:
    scene bg wfh
    show search3 with dissolve
    #BG: Laptop Screen and Past operations page
    
    "Hoping to find real-world examples of their work, you navigate to a section seemingly dedicated to past operations."
    "Case studies are anonymized, offering no insight into the personnel involved or the exact nature of their missions."
    
    $ website_visited = True
    jump invest1

label office_location:
    scene bg wfh
    show search4 with dissolve
    #BG: Laptop screen and Contact Us page

    "You  look for a more direct way to connect with the Crimson Group, hoping this might lead you to more concrete information. "
    "The 'Contact Us' page presents a generic form for inquiries. There are no direct phone numbers, no names of contact persons, and no specific office locations listed."
    $ website_visited = True
    jump invest1


label news_articles3:
    scene bg wfh
    show search5 with dissolve
    #BG: Laptop screen and artciles

    "Your search uncovers a mix of investigative reports. "
    menu:
        "Follow up on the sources quoted in the articles.":
            jump sources_quoted
        "Look for any opinions or exposes.":
            jump exposes
        " Check the comment sections.":
            jump comment_section


label sources_quoted:
    scene bg wfh
    show search5 with dissolve
    #BG: Laptop screen and articles with sources quoted

    "Eager to find some information, you attempt to track down the sources quoted in various articles. This leads you to a mix of retired military personnel, which is not useful enough"
  
    $ news_visited = True
    jump invest1

label exposes:
    scene bg wfh
    show search5 with dissolve
    #BG: Laptop screen and articles targetting crimson group
    "You find that few poeple who have attempted to shine a light on the darker aspects of the Crimson Group's operations.It appears that any significant dissent is effectively silenced or hidden away from public view."
    "This choice doesn't lead to the breakthrough you hoped for." 

    $ news_visited = True
    jump invest1

label comment_section:
    scene bg wfh
    show search5 with dissolve
    #BG: Laptop screen and comment section of article
    "You go through the comment sections of articles , hoping to find truth left by anonymous persons." 
    "You find that they are largely speculative and often contradictory."
    
    $ news_visited = True
    jump invest1


label online_discussion:
    scene bg wfh
    show search6 with dissolve
    #BG: Laptop screen and forum

    "In the forums, you find threads with rumors. "

    menu:
        "Engage with users to find for more information.":
            jump more_info
        "Pretend to be interested in hiring a mercenary.":
            jump provoke
        "Search for any people who might have hire mercenary in past":
            jump leaked_info


label more_info:
    scene bg wfh
    show chat with dissolve
    #BG: Laptop screen and player chatting

    "You begin to engage with users, hoping to coax out information with some questions. Despite your attempts, no one knew about the Crimson group."
    

    $ online_visited = True
    jump invest1

label provoke:
    scene bg wfh
    show chat with dissolve
    #BG: Laptop screen and player chatting


    "You get an idea, you create a fake identity of someone looking to hire mercenaries for an undisclosed operation.They offer the services of various mercenaries for hire but provide no substantial information about the Crimson Group itself." 


    $ online_visited = True
    jump invest1

label leaked_info:
    scene bg wfh
    show search7 with dissolve
    #BG: Laptop screen and player some posts

    "You search for people who might have hire some mercenaries previously which can provide some information. But you find not find any crucial information." 

   

    $ online_visited = True
    jump invest1


label social_media:
    scene bg wfhphone
    show insta with dissolve
    #BG: Mobile screen and instagram with crimson group page with bio written Your Battles, Our Soldiers

    "Success! You find a secured group with ties to the Crimson Group. Among discussions, you spot their slogan, 'Your Battles, Our Soldiers', alongside some insights into the lives of their mercenaries."


    "You uncover details on key members: Jack Morrison, Patrick Hardman, Marcus Johnson, Sophia Chen "
    define mercenary1_info = InventoryData("Mercenary 1: ","Jack Morrison")
    define mercenary2_info = InventoryData("Mercenary 2: ","Patrick Hardman")
    define mercenary3_info = InventoryData("Mercenary 3: ","Marcus Johnson")
    define mercenary4_info = InventoryData("Mercenary 4: ","Sophia Chen")

    $ inventory.add_data(mercenary1_info)
    $ inventory.add_data(mercenary2_info)
    $ inventory.add_data(mercenary3_info)
    $ inventory.add_data(mercenary4_info)

    "{i} The names of each mercenary was added to your notebook. {\i}"

    #Write above 4 names in Diary

    default gather_visited = False
    default personal_visited = False

    label media2:
        menu:
            "Dive deeper into the profiles":
                jump dive_deeper
            "Gather information on their past missions."if not gather_visited:
                jump gather_info
            "Look for any personal information" if not personal_visited:
                jump personal

label dive_deeper:
    scene bg wfhphone
    show insta 
    #BG: Mobile Screen with instagram

    "You decide to focus on the personal profiles of Jack Morrison, Patrick Hardman, Marcus Johnson, and Sophia Chen."

    default analyze_visited= False
    default focus_visited= False
    label deeper2:
        menu:
            "Examine their social media activity.":
                jump personal_details
            "Analyze the content they've liked, shared, or commented" if not analyze_visited:
                jump analyze
            "Focus on the connections in their profiles." if not focus_visited:
                jump focus


label personal_details:
    scene bg wfhphone
    show insta with dissolve
    #BG: Mobile screen with patrick hardman account on insta
    #one picture of Patrick with his wife and son
    #second picture of Patrick and his son only


    "You come across the account of Patrick Hardman. You find one picture of Patrick Hardman with his family, his wife and his son and second picture of just him and his son."
    "The pictures of Patrick Hardman offer the most emotionally charged storyline. The transition from a family of three to just father and son suggests possibly divorce with his wife."
    "By exploring also the tagged profiles of his ex-wife Tina you find out his sons name is Jason he is around eleven years old and he goes currently to the Lipson - middle school."

    jump phising_lvl3

label analyze:
    scene bg wfhphone
    show insta with dissolve
    #BG: Mobile screen with insta
    "You scroll through the account of each one, but you did not find anything."
    $ analyze_visited = True
    jump deeper2

label focus:
    scene bg wfhphone
    show insta with dissolve
    #BG: Mobile Screen with insta of Crimson group where there is a post of these 4 .
    "You scroll through the account of each one, but you did not find anything."
    $ focus_visited = True
    jump deeper2



label gather_info:
    scene bg wfhphone
    "This choice uncovers specific details about each mercenary:"
    "Jack Morrison: Revealed to be a decorated sniper with numerous confirmed engagements."
    "Patrick Hardman: Identified as an intelligence operative skilled in interrogation and psychological manipulation."
    "Marcus Johnson: Outlined as a tactical leader with a record of high-stakes operations in hostile environments."
    "Sophia Chen: Exposed as a cyber warfare expert with a history of dismantling enemy communications."
    "This information is of no use, you have to try some other option"
    $ gather_visited = True
    jump media2

label personal:
    scene bg wfhphone
    show insta with dissolve
    #BG: Mobile screen with insta of crimson group

    "You try to find some personal information of each mercenary by going through the instagram but you did not find any personal details of mercenaries"
    
    $ personal_visited = True
    jump media2

    
label pretexting:
    scene bg wfhphone
    #scene Homeoffice/Desk
    #show me/player with phone

    "Now you want to know more about Patrick Hardman so you decide to give pretexting a try."
    "With the information gathered from the website and the secondary research about the mercenary Hardman at hand you try calling the office of Crimson. You set up a voice changer and proceed to call your target."

    menu:

        "Try to impersonate the eleven years old son":
            jump jason_hardman
        
        "Try to impersonate the ex-wife of Mr. Hardman":
            jump tina_hardman
        
        "Try pretending to be a close friend of Patric":
            jump alexander
        
        "Try pretending to be the family doctor of Mr. Hardman":
            jump doctor_dale

label jason_hardman:
    scene bg wfh
    show bg wfhcall
    #BG: Player on call
    "Hello ... here is Jason ..."

    menu:

        "I was wondering if you could give me information about my dad Patric Hardman? I had a football game today and he promised to come but did not show up.":
            jump js_op1
        
        "I cant reach my father over his mobile. Is he in at the moment?":
            jump js_op2


label js_op1:
    scene bg wfh
    show bg wfhcall
    
    #BG: Player on call
    menu:

        "He did not answer my message either. Is he ok? Would you give me his number so I can call him?":
            jump js_op1_1
        
        "I was wondering why? Would you give me his number so I can call him?":
            jump js_op1_1


label js_op1_1:

    scene bg wfh
    show bg wfhcall
    show sec_call with dissolve
    #BG: Secretary on call
    Sec "I am afraid I can't do that sweetie. But he is fine I am sure of it! Have a nice day!"

    jump unsuccesful_pretext

label js_op2:
    scene bg wfh
    show bg wfhcall
    show sec_call with dissolve
    #BG: Player on call
    menu:

        "Wait for the response":
            jump js_op2_1
        
        "I know he has a job which involves risks but I did not hear anything from him the last few days":
            jump js_op2_2

label js_op2_1:
    scene bg wfh
    show bg wfhcall
    show sec_call 
    #BG: Secretary and player on call
    sec "Oh Hello Jason, what is the Name of your father?"

    p "Patric, ähm Hardman."

    sec "Ok I see, here in the system that he is not in today."

    p "Where is he?"

    sec "Sorry little man but I can not tell you anything about that. Can you hand your mother the phone please."

    menu:

        "She is doing grocery shopping. But please I mean he wanted to play some video games with me tonight.":
            jump js_op2_1_1
        
        "Ähm not here right now.":
            jump js_op2_1_2
        
        "Finish the call before you get caught":
            jump js_op2_1_3


label js_op2_1_1:
    scene bg wfh
    show bg wfhcall
    show sec_call
    #BG: Secretary and player on call
    sec "… Ok one second. What I can tell you is that he is not in the country at the moment and for next week, so I am afraid he won't make it tonight. I can not tell you more!"

    p "Ok thank you and good day!"

    sec "Thanks for you as well."

label js_op2_1_2:
    scene bg wfh
    show bg wfhcall
    show sec_call
    #BG: Secretary and player on call
    sec "I think its time to finish tis call. Good day!"
    hide sec_call with dissolve
    jump unsuccesful_pretext

label js_op2_1_3:
    scene bg wfhphone

    "You hang up, out of fear getting figured out."

    jump unsuccesful_pretext


label js_op2_2:
    scene bg wfh
    show bg wfhcall
    show sec_call
    #BG: Secretary and player on call
    sec "Dont worry Jason! can I ask you who told you this?"

    menu: 

        "My mom":
            jump js_op2_1_1
        
        "No one":
            jump js_op2_1_2

        "He mentioned it to me":
            jump js_op2_1_1


label tina_hardman:
    scene bg wfh
    show bg wfhcall 
    #BG: Player on call
    "Hello here Is Tina Hardman"

    menu:

        "I am calling because my ex husband forgot again to pay for his son's tutor sessions":
            jump tn_op1
        
        "Can you pretty please help me contacting my ex husband?":
            jump tn_op2

label tn_op1:
    scene bg wfh
    show bg wfhcall
    show sec_call2 with dissolve
    #BG: Secretary and player on call
    p "I am very much annoyed and he is not picking up his phone so can you please help me reach him. This is already the third time this happens and he never is available when I try to call him … I am losing my mind!"

    sec "Hello Mrs Hardman, I am afraid I can't help with that. In the system he is marked as not available. So he is working right now."

    menu:

        "(desperate) It really upsets me..HE ! I am always responsible to deal with HIS shit and then I have to stand there and listen to the tutor, how irresponsible it is of me to let my son walk home alone when it was HIS turn to pick him up!":
            jump tn_op1_1
        
        "(super friendly) Even when I ask you very, very nicely about it? I might bring some cookies as a gesture of gratitude.":
            jump tn_op1_2

label tn_op1_1:
    scene bg wfh
    show bg wfhcall
    show sec_call2
    #BG: Secretary and player on call
    p "I can't deal with it any longer. Give me a contact please or I am losing my mind right now."

    sec "That sounds nasty. A friend of mine went through a similar mess. So she started to take some boxing lessons to let off steam."

    p "Thanks for that advice but I dont see how this helps me in this precarious situation? You see as women we need to stick together to withstand the patriarchy!"

    sec "You are right, Ok listen its (556) 781-4231. Do you have it?"

    p "Yes you're treasure, I will put a picture of him on my punching bag for extra motivation as soon I own one!"

    sec "Haha good idea, I hope you will figure out a solution. Have a nice day!"
    hide sec_call2 with dissolve
    #  Notebook entry Patric Hardman personal phone number  (556) 781-4231

    jump succesful_pretext

label tn_op1_2:
    scene bg wfh
    show bg wfhcall
    show sec_call2
    #BG: Secretary and player on call
    sec "Even if that sounds tempting, I can't help you any further. Have a nice day!"
    hide sec_call2 with dissolve
    jump unsuccesful_pretext

label alexander:
    scene bg wfh
    show bg wfhcall
    show sec_call3 with dissolve
    #BG: Secretary and player on call
    "Hello, here is Alexander, Patric meant I should give him a call when the car he is interested in is finished renovating."
    "I can't reach him on his phone."

    sec "Oh he probably turned it off or something."

    p "Yeah but can you forward my call to him?"

    sec "One moment ... He is not in today!"

    p "Ok so can you give me a contact so I can reach him? He said he wants to know about the car immediately when the process is finished."

    sec " I am not allowed to give out information like that. Sorry!"

    menu:

        "(persuasive) So not even an exception for his best buddy? It's really important to him!":
            jump alx_op1
        
        "(angrily) I swear he will be very angry with you if he misses it!!! If I were you, I'd give in because you don't want to get in trouble, do you?":
            jump alx_op1
    
label alx_op1:
    scene bg wfh
    show bg wfhcall
    show sec_call3
    #BG: Secretary and player on call
    sec "I am afraid I can't do anything for you! I wish a good day bye."
    hide sec_call3 with dissolve
    jump unsuccesful_pretext

label doctor_dale:
    scene bg wfh
    show bg wfhcall
    show sec_call4 with dissolve
    #BG: Secretary and player on call
    p "Hello, here is Doctor Dale, I am trying to reach my patient Mr. Hardman Is he in?
    We got his test results back and It is urgent that he comes back for another examination."

    sec "Hello Mister Dale, I am looking in the system. He is not in! Did you try reaching him on his personal number?"

    menu:

        "No, this is the only contact info we ve got. This must be a mistake or someone forgot to add his phone number.":
            jump doc_op1
        
        "This is quite embarassing but it seems we have made a mistake in his patient records and did not record this vital info.":
            jump doc_op1


label doc_op1:
    scene bg wfh
    show bg wfhcall
    show sec_call4
    #BG: Secretary and player on call
    p "Ok .. normally I would not ask for that but could you be so kindly and give me his phone number? It is quite important that he gets his results asap"

    sec "I am not sure if I am allowed to do that.. don't you have like an emergency contact or something?"

    menu:

        "No sadly you are our last hope to reach him in time. It will stay between us, I promise":
            jump doc_op1_1
        
        "No and we are running out of time his result suggests a serious heart impairment!":
            jump doc_op1_2

label doc_op1_1:
    scene bg wfh
    show bg wfhcall
    show sec_call4
    #BG: Secretary and player on call
    p "I mean he probably is banking on us to deliver him his results in this way immediately thinking we have his contact info stored in the file… So can you make an exception?"

    sec "Ok one Sec: It's here (556) 781-4231. Do you have it?"

    p "Yes! thank you very much that saved us big time! Bye and have a nice day!"

    # Notebook entry Patric Hardman personal phone number  (556) 781-4231
    hide sec_call4 with dissolve
    jump succesful_pretext

label doc_op1_2:
    scene bg wfh
    show bg wfhcall
    show sec_call4
    #BG: Secretary and player on call
    p "I mean he probably is banking on us to deliver him his results in this way immediately thinking we have his contact info stored in the file… So can you make an exception?"

    sec "You are kidding.. I would be shocked if doctors give out strictly private informations about their patients just like this!
    This obviously a prank of some sort! I will report this number to the authorities!"
    hide sec_call4 with dissolve
    "Well that didnt work out!"
    
    jump unsuccesful_pretext

label unsuccesful_pretext:
    scene bg wfhphone
    #BG: Secretary and player on call
    "Unfortunately you were not able to gain the desired information"

    menu:
        "Try again":
            jump pretexting
        
        #"Continue without that information":
        #    jump #Needs to be added

label succesful_pretext:
    scene bg wfhphone
# Number was retrieved can be used for Vishing call
    define patrick_number = InventoryData("Patrick Hardman", "(556) 781-4231")

    $ inventory.add_data(patrick_number)

    "{i} Patric Hardman personal phone number (556) 781-4231 was added to your notebook. {\i}"


    jump vishing


#checkpoint vishing
label vishing:
    scene bg wfh
    show bg wfhcall
    #BG: player on call
    "You decide its time for the next play on Patric Hardman. Your target is to use his phone number and knowledge about him to get him to click on your link which is sent directly per SMS."

    menu:

        "Try calling as principal of Lipson Middel School":
            jump principal
        
        "Pretend calling because of an accident involving his family":
            jump accident
        
        "Pretend calling because Jason was caught stealing":
            jump stealing


label principal:
    scene bg wfh
    show bg wfhcall
    
    #BG: Patrick Hardman and player on call
    p "Sir I call you because your son has picked a fight with his class mate and injured him in the eye. I need you to come by and pick up your son as well as have a talk with me about his behaviour."
    show ph_call with dissolve
    ph "Dam it! And what did the other guy do? My son probably only was defending himself!"

    p "That is definitely possible, however my first concern is for the injured person."
    "I would kindly ask you to fill out a formular to to take responsibility for the injuries to the other boy and to pay for the treatment in cooperation with your insurance company."

    ph "Wait I can not come to your office today. I am ... I am currently on business travel."

    p "Ok I guess we will sent your son home and I await you both on the next workday in my office so we can discuss the consequences. Furthermore I can send you the access link for the formular to your phone."

    ph "No I will not go into advance payment without first getting to know what exactly happened! And that's where it stays!"

    p "... Ok"
    hide ph_call with dissolve
    "You decide to hang up as this play failed to reach your goal."

    jump unsuccesful_vishing



label accident:
    scene bg wfh
    show bg wfhcall
    
    #BG: Patrick Hardman and player on call
    p "Sir I am terribly sorry to inform you that your son and his mother were involved in a car accident and are in critical condition at the moment. We need you to come as soon as possible to the hospital to fill out the paperstuff."
    show ph_call with dissolve
    ph "Fuck! What happened? I can not come by so soon I am in Tropica!"

    p "Ok Sir please calm down"

    ph "Calm down?! Are you kidding me my son is fucking dying and you say calm down?"

    p "They are not dying! We are doing our best!"

    ph "Ok ok I can be there by tomorrow."

    p "Unfortunately we need your information sooner, so we can continue the treatment. Would it be possible for you to fill in your information if we send you a link to the formular?"

    ph "Yeah sure, please do everything in your power to safe my son!"

    p "We will! I sent you the formular."
    hide ph_call with dissolve
    "Shortly after hanging up you get access to Patric's smartphone as he ingnorantly clicked on your link. "
    "You scroll through his messages."

    "When you go through his smartphone messages you see some message from J."
    "Hey! Did everything go well? Excited about the avocado business. Got a good feeling we're gonna make some serious cash with this!! Let's talk soon!"
    #Here ends -> transition level 4
    

label stealing:
    scene bg wfh
    show bg wfhcall
    #BG: Patrick Hardman and player on call
    p "Sir, Your son is in big trouble. We caught him stealing from the bookstore and he even tried to run away from us."
    show ph_call with dissolve
    ph "He did whaaat?"
    
    p "He tried stealing books. Unfortunately, while trying to flee he ran over and injured an old man who was blocking his way. He is in critical condition and hanging on by a thread."
    "The police are on their way and he is totally distraught and begged us to call you."

    ph "My son doesn't like books at all!! What kind of scam is this? If i find you you will regret trying this!"
    hide ph_call with dissolve
    "He did not fell for your tricks and stopped the call immediately after threatening you."

    jump unsuccesful_vishing


label unsuccesful_vishing:
    scene bg wfhphone
    "Your play did not achieve your goal. Try again!"

    #back to checkpoint vishing
label successful_vishing:
    scene bg wfhphone
    #some information we find out

label phising_lvl3:
    scene bg wfh
    "You decide to try your luck by writing a phishing email to all the employees from the Crimson Group."
    "Task: Arrange the email snippets to create an effective phishing email "

    #Minigame Email

label notsuccessful: 
    "Unfortunately, none of the mercenaries fell for your phishing email. Try again. "
label successful: 
    "Transition next day…"
    "Jack Morrison clicked on your link. Now you have access to his computer."
    #BG: 
    "You sit down at your computer, ready to explore."
    menu:
        "Navigate through directories":
            jump explore_file_system
        "Check his email account":
            jump emailaccount

label explore_file_system:
    "As you navigate through the directories, you can only find files that are not useful for you."
    menu:
        "Check his email account":
            jump emailaccount

label emailaccount:

    scene black
    hide screen inv_screen
    call screen emailaccount

screen emailaccount:
    zorder 1
    add "gui/emails/inbox_plain.png"
    imagebutton auto "gui/emails/mail1_%s.png":
        focus_mask True
        action Jump("email1")

    imagebutton auto "gui/emails/mail2_%s.png":
        focus_mask True
        action Jump("email2")

    imagebutton auto "gui/emails/mail3_%s.png":
        focus_mask True
        action Jump("email3")


label email1:
    hide screen inv_screen
    scene black
    call screen emailaccount1

screen emailaccount1:
    zorder 1
    add "gui/emails/mail1.png"
    imagebutton auto "gui/emails/mail1_%s.png":
        focus_mask True
        action Jump("email1")

    imagebutton auto "gui/emails/mail2_%s.png":
        focus_mask True
        action Jump("email2")

    imagebutton auto "gui/emails/mail3_%s.png":
        focus_mask True
        action Jump("email3")

label email2:
    hide screen inv_screen
    scene black
    call screen emailaccount2

screen emailaccount2:
    zorder 1
    add "gui/emails/mail2.png"
    imagebutton auto "gui/emails/mail1_%s.png":
        focus_mask True
        action Jump("email1")

    imagebutton auto "gui/emails/mail2_%s.png":
        focus_mask True
        action Jump("email2")

    imagebutton auto "gui/emails/mail3_%s.png":
        focus_mask True
        action Jump("email3")

        #update journal with information found

label email3:
    hide screen inv_screen
    scene black
    call screen emailaccount3
    "Continue"

screen emailaccount3:
    zorder 1
    add "gui/emails/mail3.png"
    imagebutton auto "gui/emails/mail1_%s.png":
        focus_mask True
        action Jump("email1")

    imagebutton auto "gui/emails/mail2_%s.png":
        focus_mask True
        action Jump("email2")

    imagebutton auto "gui/emails/mail3_%s.png":
        focus_mask True
        action Jump("find_out_more")
        




label find_out_more:#checkpoint x
    show screen inv_screen
    #BG computer background
    menu:
        "Search for hotels in Tropica on the internet":
            jump search_hotels
        "Write an email to Marcus Johnson as Jack Morrison":
            jump write_email

label write_email: 
    "After waiting for two days without a reply from Marcus Johnson, you decide to try something else. "
    jump find_out_more

label search_hotels:
#bg map with three pins --> three hotels with names "Grand Horizon,..."
    "You decide to search on the internet for hotels in the town Tropica."
    "Luckily, you find out that there are only three hotels in the town: Grand Horizon Inn, Hotel Semirani and Hotel Diamond Resorts."
    menu:
        "Try your luck and go to one of the hotels":
            jump hotel_options
        "Call hotels and confidently ask for Marcus Johnson":
            jump call_hotels

label hotel_options:#BG map with 3 hotels?
    "Which hotel would you like to visit?"
    menu:
        "Go to Grand Horizon Inn":
            jump hotel1_fail
        "Go to Hotel Semirani":
            jump hotel2_success
        "Go to Hotel Diamond Resorts":
            jump hotel3_fail

label hotel1_fail:
#BG: Hotel Reception; Character Receptionist male, friendly
    "You go to Grand Horizon Inn"
    receptionist2 "How can we help you?"
    p "I would like to rent a room."
    receptionist2 "Sure, Standard Room or Deluxe Room?"
    menu:
        "Take the Standard Room":
            jump takeroomfail
        "Take the Deluxe Room":
            jump takeroomfail

label hotel3_fail:
#BG: Hotel Reception; Character Receptionist male, friendly
    "You go to Hotel Diamond Resorts."
    receptionist2 "How can we help you?"
    p "I would like to rent a room."
    receptionist2 "Sure, Standard Room or Deluxe Room?"
    menu:
        "Take the Standard Room":
            jump takeroomfail
        "Take the Deluxe Room":
            jump takeroomfail

label takeroomfail:
#BG: Hotel lobby, some people hanging out
    "You sit down in the lobby, pretending to read a newspaper and hope that Marcus Johnson passes by by chance at some point."
    "After you have been waiting for the whole day, you realize that you probably went to the wrong hotel"

    jump search_hotels

    #Go to checkpoint x

label hotel2_success:
#BG: Hotel Reception; Character Receptionist male, friendly
    "You go to Hotel Semirani"
    receptionist2 "How can we help you?"
    p "I would like to rent a room."
    receptionist2 "Sure, Standard Room or Deluxe Room?"
    menu:
        "Take the Standard Room":
            jump takeroom
        "Take the Deluxe Room":
            jump takeroom

label takeroom:#checkpoint r
#BG: In front of your hotel door, a guy entering his room
    "You take your keys and go to your room."
    "Suddenly you observe Marcus Johnson entering his room, which is right next to yours."
    menu:
        "Set up a Wifi Access Point and create a fake login":
            jump setupwifi
        "Knock on Marcus Johnson's door":
            jump knockingjohnson
        "Wait for him to leave his room and break into his room to search for information.":
            jump breakin

label setupwifi:
    "Transition: evening..."
    #BG Laptop screen "0 person logged in"
    "You keep waiting for a couple of hours but no one logs into your fake wifi point."
    #BG Laptop screen "1 person logged in"
    "You are almost ready to give up, when all of a sudden you can see that someone fell for your trap."
    "You find yourself sitting in front of your computer, where you can monitor the victim's online activity."
    "Your heart races as you realize that the victim is Marcus Johnson and you've gained access to his computer. "

    menu:
        "Explore his files":
            jump explorefiles
        "Hack into his facebook account":
            jump facebook
    
        


label explorefiles:
    "The desktop is cluttered with folders and files, but one folder catches your eye - Body Cam Footage."
    "Curious, you open the folder and watch one of the many video files"
    #design: video file possible?
    "Loud and panicked voices can be heard on the video. Lots of people are running around. "
    "In the background you can see lots of trees and plants, probably the rainforest. "
    "Suddenly you hear an aggressive voice that seems to come from the owner of the bodycam. It seems as if a protest is being broken up by force."
    "You decide to save the video footage on you PC as evidence."



    jump pretexting
            





label facebook:
    "You logged into Marcus Johnson's Facebook account. However, all you found were old pictures and private chats with his old school friend."
    "This choice doesn't lead you any further so you decide to explore the files next."

    jump explorefiles


label knockingjohnson:
    "You knock on the hotel room door."
    marcus "Can I help you?"#opens the door

    menu:
        "Pretend to be cleaning staff and tell him you wanted to check if someone is in the room.":
            jump cleaningstaff
        "Try to make friends with him":
            jump makefriends
    
label cleaningstaff:

    p "Good afternoon, sir. I'm here to clean the room. Just wanted to check, if you are here."
    marcus "Yes, I am here as you can see. And I don't want to be disturbed any more, otherwise I'll get the manager. Bye."
    jump takeroom

    #go to checkpoint r

label makefriends:

    p "Hey there! I noticed we're staying on the same floor and thought I'd introduce myself. I'm [name], just trying to make some new friends around here. Maybe we could hang out some time."
    marcus "Look, I'm not really in the mood for making friends. I'm here on business and I don't have time for chitchat."
    p "Oh, I totally get it. Business can be stressful. But sometimes it's good to take a break and unwind, you know? Maybe we could grab a drink later and chat about something other than work?"
    #Marcus's expression darkens
    marcus "I said I'm not interested. Now, if you don't mind, I have work to attend to. Leave me alone."
    p "Alright, no problem. Sorry to bother you."

    "You retreat from the room, feeling a bit embarrassed by the rejection. "
    "It seems Marcus Johnson isn't the friendly type, at least not at the moment. Maybe you should try something else."

    #go to checkpoint m
    jump search_hotels


label breakin:
    "You approach Marcus Johnson's hotel room, feeling a surge of adrenaline as you stand in front of the door. "
    "With a quick glance around to ensure no one's watching, you begin to open the door with force."

    "You step inside his room and start scanning through Marcus's belongings, searching for anything valuable or incriminating."

    "Suddenly, you freeze as you hear footsteps approaching. Before you can react, the door bursts open, and a hotel staff member stands in the doorway"


    hs "What do you think you're doing?! This is a private room!"

    p "I... I was just... I..."

    "Desperately you are trying to think of a credible excuse as you realize the severity of the situation. "
    "You've been caught red-handed, and there's no way to talk your way out of this one."

    hs "That's it. I'm calling security."

    "Before you can protest, the hotel staff member takes out their phone and dials a number." 

    "As you wait for security to arrive , you can't help but regret your reckless decision."

    #go to checkpoint m
    jump search_hotels

label call_hotels:
    #BG phone number keys

    "What hotel do you want to call?"
    menu:
        "Grand Horizon Inn":
            jump hotel1_call
        "Hotel Semirani":
            jump hotel2_call
        "Hotel Diamond Resorts":
            jump hotel3_call


label hotel1_call:#BG dialing
    "You confidently call the hotel and ask for Marcus Johnson."

    receptionist2 "I’m sorry, we don’t have a guest of that name staying here."
    p "I must have confused something then. Thank you!"

    menu:
        "Call a different hotel":
            jump call_hotels
        "Try your luck and go to one of the hotels":
            jump hotel_options

label hotel2_call:#BG dialing

    "You confidently call the hotel and ask for Marcus Johnson."

    receptionist2 "What room number?"
    p "When he told me he would be staying at your hotel, a week ago, he hadn’t checked in and of course even he didn’t know his room number then."
    receptionist2 "Sorry we cannot do that. The safety, security and privacy of our guests is our highest value."

    menu:
        "Call a different hotel":
            jump call_hotels
        "Try your luck and go to one of the hotels":
            jump hotel_options

label hotel3_call:#BG dialing
    "You confidently call the hotel and ask for Marcus Johnson."

    receptionist2 "I’m sorry, we don’t have a guest of that name staying here."
    p "I must have confused something then. Thank you!"

    menu:
        "Call a different hotel":
            jump call_hotels
        "Try your luck and go to one of the hotels":
            jump hotel_options






    



