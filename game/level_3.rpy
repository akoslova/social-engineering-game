$ renpy.include("inventory.rpy")
$ renpy.include("tutorial_story.rpy")
$ renpy.include("level_1.rpy")


define ph = Character (_("Patric Hardman"), color="#3939f5")


label level_3:
    call inventory


label investigation:
    "Your mission to infiltrate the shadows of the Crimson Group begins now. Armed with nothing but your wits and a powerful determination, you face your first decision. How will you embark on this perilous journey?"

    menu:
        "Visit the Crimson Group's official website.":
            jump official_website

        "Search for news articles and reports on the Crimson Group.":
            jump news_articles3

        "Delve into forums and online discussions about mercenaries.":
            jump online_discussion

        "Shift through social media for mentions of the Crimson Group.":
            jump social_media

label official_webiste:

    #BG: Laptop Screen Crimson Group Website

    "You navigate to the Crimson Group's website, greeted by their bold slogan: 'In the Shadows, We Forge Your Peace'. "
    "The site is sleek, with a carousel of images showcasing anonymous soldiers in action, underscoring their message of strength and reliability. However, detailed information about their operatives remains elusive."
    menu:
        "Examine their service offerings more closely.":
            jump service_offering
        "Look for any mention of specific operations or case studies.":
            jump specific_operations
        " Search for contact information or office locations.":
            jump office_location

label service_offering:

    #BG: Laptop Screen and Service offering page

    "You delve into the descriptions of their services, ranging from high-risk protection details to strategic military consulting. "
    "Despite the wealth of information about what they offer, the specifics about who exactly carries out these services remain veiled in secrecy. The descriptions are generic, likely by design, to keep their operatives' identities and backgrounds hidden from public view."
    jump investigation

label specific_operation:

    #BG: Laptop Screen and Past operations page
    
    "Hoping to find real-world examples of their work, you navigate to a section seemingly dedicated to past operations."
    "Case studies are anonymized, offering no insight into the personnel involved or the exact nature of their missions. It's clear that the Crimson Group reveals only what they want the world to know, keeping the true extent of their operations shrouded in mystery."
    jump investigation

label office_location:

    #BG: Laptop screen and Contact Us page

    "You end your exploration by looking for a more direct way to connect with the Crimson Group, hoping this might lead you to more concrete information. "
    "The 'Contact Us' page presents a generic form for inquiries, alongside a nondescript London address and a general email address. There are no direct phone numbers, no names of contact persons, and no specific office locations listed."
    jump investigation


label news_articles3:

    #BG: Laptop screen and artciles

    "Your search uncovers a mix of investigative reports and opinion pieces. "
    menu:
        "Follow up on the sources quoted in the articles.":
            jump sources_quoted
        "Look for any dissenting opinions or exposes.":
            jump exposes
        " Check the comment sections for insider insights.":
            jump comment_section


label sources_quoted:

    #BG: Laptop screen and articles with sources quoted

    "Eager to find concrete information, you attempt to track down the sources quoted in various articles. This leads you to a mix of retired military personnel, defense analysts, and a few journalists who have covered private military companies in the past."
    jump investigation

label exposes:

    #BG: Laptop screen and articles targetting crimson group
    "Convinced that someone must have challenged the public narrative, you search for dissenting opinions and critical exposes. "
    "This endeavor uncovers a few brave souls who have attempted to shine a light on the darker aspects of the Crimson Group's operations.It appears that any significant dissent is effectively silenced or hidden away from public view."

    jump investigation

label comment_section:

    #BG: Laptop screen and comment section of article
    "In a last-ditch effort, you comb through the comment sections of articles and opinion pieces, hoping to find nuggets of truth left by anonymous insiders." 
    "While the comments range from fervent support to vehement criticism of the Crimson Group, they are largely speculative and often contradictory."

    jump investigation


label online_discussion:

    #BG: Laptop screen and forum

    "In the digital back alleys of forums, you find threads interwoven with rumors and awe. "

    menu:
        "Engage with users to fish for more information.":
            jump more_info
        "Pretend to be interested in hiring to provoke responses.":
            jump provoke
        "Search for any leaked information or disgruntled postings.":
            jump leaked_info


label more_info:

    #BG: Laptop screen and player chatting

    "You begin to engage with users, hoping to coax out information with carefully worded questions and expressions of genuine interest. Despite your attempts at subtlety, your inquiries are met with suspicion or vague responses that circle back to public knowledge."
    jump investigation

label provoke:

    #BG: Laptop screen and player chatting


    "Adopting a new strategy, you craft a persona of someone looking to hire mercenaries for an undisclosed but implicitly lucrative operation.They offer the services of various mercenaries for hire but provide no substantial information about the Crimson Group itself." 
    "It seems that your guise has attracted more opportunists than insiders, and no significant leads materialize from these exchanges."
    jump investigation

label leaked_info:

    #BG: Laptop screen and player some posts

    "Your search for leaks or signs of dissent within the ranks leads you to scour countless threads and posts for any shred of dissatisfaction or betrayal." 
    "The few threads that initially seem promising end abruptly, with users disappearing or retracting their statements, suggesting either intimidation or the forum moderators' efficiency in maintaining secrecy."
    jump investigation


label social_media:

    #BG: Mobile screen and instagram with crimson group page with bio written Your Battles, Our Soldiers

    "Success! You find a loosely secured group with ties to the Crimson Group. Among discussions, you spot their slogan, 'Your Battles, Our Soldiers', alongside candid insights into the lives of their mercenaries. This is the break you needed."


    "You uncover details on key members: Jack Morrison, Patrick Hardman, Marcus Johnson, Sophia Chen "

    #Write above 4 names in Diary


    menu:
        "Dive deeper into the profiles of these mercenaries.":
            jump dive_deeper
        "Gather information on their past missions.":
            jump gather_info
        "Look for any personal grievances or vulnerabilities.":
            jump personal

label dive_deeper:

    #BG: Mobile Screen with instagram

    "You decide to focus on the personal profiles of Jack Morrison, Patrick Hardman, Marcus Johnson, and Sophia Chen. This approach reveals a treasure trove of information about each mercenary:"

    menu:
        "Examine their social media activity for personal details and professional hints.":
            jump personal_details
        "Analyze the content they've liked, shared, or commented on for subtle insights.":
            jump analyze
        "Focus on the relationships and connections mentioned in their profiles.":
            jump focus


label personal_details:

    #BG: Mobile screen with patrick hardman account on insta
    #one picture of Patrick with his wife and son
    #second picture of Patrick and his son only


    "You come across with the account of Patrick Hardman.You find one picture of Patrick Hardman with his family, his wife and his son and second picture of just him and his son."
    "The pictures of Patrick Hardman offer the most emotionally charged storyline. The transition from a family of three to just father and son suggests possibly divorce with his wife."

    jump lavel_3

label analyze:

    #BG: Mobile screen with insta
    "You through the account of each one, but you did not find anything."

    jump social_media

label focus:

    #BG: Mobile Screen with insta of Crimson group where there is a post of these 4 .
    "You through the account of each one, but you did not find anything."

    jump social_media



label gather_info:

    "This choice uncovers specific details about each mercenary:"
    "Jack Morrison: Revealed to be a decorated sniper with numerous confirmed engagements."
    "Patrick Hardman: Identified as an intelligence operative skilled in interrogation and psychological manipulation."
    "Marcus Johnson: Outlined as a tactical leader with a record of high-stakes operations in hostile environments."
    "Sophia Chen: Exposed as a cyber warfare expert with a history of dismantling enemy communications."
    "This information is of no use, youo have to try some other option"

    jump social_media

label personal:

    #BG: Mobile screen with insta of crimson group

    "You found nothing in thise option"

    jump social_media
    
label pretexting:

    "As the phishing mail failed to bear any results you decide to give pretexting a try. With the information from the website and the secondary research about the mercenary hardman at hand you try calling the office of Crimson. You set up a voice changer and proceed to call your target."

    menu:

        "Try to impersonate the thirteen years old son":
            jump jason_hardman
        
        "Try to impersonate the ex-wife of Mr. Hardman":
            jump tina_hardman
        
        "Try pretending to be a close friend of Patric":
            jump alexander
        
        "Try pretending to be the family doctor of Mr. Hardman":
            jump doctor_dale

label jason_hardman:

    "Hello ... here is Jason ..."

    menu:

        "I was wondering if you could give me information about my dad Patric Hardman? I had a football game today and he promised to come but did not show up.":
            jump js_op1
        
        "I cant reach my father over his mobile. Is he in at the moment?":
            jump js_op2


label js_op1:

    menu:

        "He did not answer my message either. Is he ok? Would you give me his number so I can call him?":
            jump js_op1_1
        
        "I was wondering why? Would you give me his number so I can call him?":
            jump js_op1_1


label js_op1_1:

    Sec "I am afraid I can't do that sweetie. But he is fine I am sure of it!"


label js_op2:

    menu:

        "Wait for the response":
            jump js_op2_1
        
        "I know he has a job which involves risks but I did not hear anything from him the last few days":
            jump js_op2_2

label js_op2_1:

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

    sec "… Ok one second. What I can tell you is that he is not in the country at the moment and for next week, so I am afraid he won't make it tonight. I can not tell you more!"

    p "Ok thank you and good day!"

    sec "Thanks for you as well."

label js_op2_1_2:

    sec "I think its time to finish tis call. Good day"

label js_op2_1_3:

    "You hang up, out of fear getting figured out."


label js_op2_2:

    sec "Dont worry Jason! can I ask you who told you this?"

    menu: 

        "My mom":
            jump js_op2_1_1
        
        "No one":
            jump js_op2_1_1

        "He mentioned it to me":
            jump js_op2_1_1


label tina_hardman:

    "Hello here Is Tina Hardman"

    menu:

        "I am calling because my ex husband forgot again to pay for his son's tutor sessions":
            jump tn_op1
        
        "Can you pretty please help me contacting my ex husband?":
            jump tn_op2

label tn_op1:

    p "I am very much annoyed and he is not picking up his phone so can you please help me reach him. This is already the third time this happens and he never is available when I try to call him … I am losing my mind!"

    sec "Hello Mrs Hardman, I am afraid I can't help with that. In the system he is marked as not available. So he is working right now."

    menu:

        "(desperate) It really upsets me..HE ! I am always responsible to deal with HIS shit and then I have to stand there and listen to the tutor, how irresponsible it is of me to let my son walk home alone when it was HIS turn to pick him up!":
            jump tn_op1_1
        
        "(super friendly) Even when I ask you very, very nicely about it? I might bring some cookies as a gesture of gratitude.":
            jump tn_op1_2

label tn_op1_1:

    p "I can't deal with it any longer. Give me a contact please or I am losing my mind right now."

    sec "That sounds nasty. A friend of mine went through a similar mess. So she started to take some boxing lessons to let off steam."

    p "Thanks for that advice but I dont see how this helps me in this precarious situation? You see as women we need to stick together to withstand the patriarchy!"

    sec "You are right, Ok listen its (556) 781-4231. Do you have it?"

    p "Yes you're treasure, I will put a picture of him on my punching bag for extra motivation as soon I own one!"

    sec "Haha good idea, I hope you will figure out a solution. Have a nice day!"

    #  Notebook entry Patric Hardman personal phone number  (556) 781-4231

    jump succesful_pretext

label tn_op1_2:

    sec "Even if that sounds tempting, I can't help you any further. Have a nice day!"

label alexander:

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

    sec "I am afraid I can't do anything for you! I wish a good day bye."

label doctor_dale:

    p "Hello, here is Doctor Dale, I am trying to reach my patient Mr. Hardman Is he in?
    We got his test results back and It is urgent that he comes back for another examination."

    sec "Hello Mister Dale, I am looking in the system. He is not in! Did you try reaching him on his personal number?"

    menu:

        "No, this is the only contact info we ve got. This must be a mistake or someone forgot to add his phone number.":
            jump doc_op1
        
        "This is quite embarassing but it seems we have made a mistake in his patient records and did not record this vital info.":
            jump doc_op1


label doc_op1:

    p "Ok .. normally I would not ask for that but could you be so kindly and give me his phone number? It is quite important that he gets his results asap"

    sec "I am not sure if I am allowed to do that.. don't you have like an emergency contact or something?"

    menu:

        "No sadly you are our last hope to reach him in time. It will stay between us, I promise":
            jump doc_op1_1
        
        "No and we are running out of time his result suggests a serious heart impairment!":
            jump doc_op1_2

label doc_op1_1:

    p "I mean he probably is banking on us to deliver him his results in this way immediately thinking we have his contact info stored in the file… So can you make an exception?"

    sec "Ok one Sec: It's here (556) 781-4231. Do you have it?"

    p "Yes! thank you very much that saved us big time! Bye and have a nice day!"

    # Notebook entry Patric Hardman personal phone number  (556) 781-4231

    jump succesful_pretext

label doc_op1_2:

    p "I mean he probably is banking on us to deliver him his results in this way immediately thinking we have his contact info stored in the file… So can you make an exception?"

    sec "You are kidding.. I would be shocked if doctors give out strictly private informations about their patients just like this!
    This obviously a prank of some sort! I will report this number to the authorities!"

    "Well that didnt work out!"
    # Checkpoint



label succesful_pretext:
# Number was retrieved can be used for Vishing call

    


label phising_lvl3:
    "You decide to try your luck by writing a phishing email to all the employees from the Crimson Group."
    "Task: Arrange the email snippets to create an effective phishing email "

    #Minigame Email

label notsuccessful: 
    "Unfortunately, none of the mercenaries fell for your phishing email. Try again. "
label successful: 
    "Transition next day…"
    "Jack Morrison clicked on your link. Now you have access to his computer."
    "You sit down at your computer, ready to explore."
    "As you navigate through directories, you discover a folder labeled 'Partners'."
    menu:
        "Explore the folder":
            jump explore_file_system
        "Check his email account":
            jump emailaccount

label explore_file_system:
    "Inside, you find an advertisement from the Company CORE."



    
#Successful: You found out about Core providing vehicles for the rainforest destruction → Update Journal
    menu:
        "Leave folder and check the email account":
            jump emailaccount


label emailaccount:

    #Todo: Design Email inbox where you only see the subjects
    #From Colleague Marcus Jphnson Subject: Out of Office notice
    #Email from Wife Subject: Need fast reply
    #from company newsletter subject: Exciting News: Successful Deal with CORE for Advanced Tree Technology
    menu:
        "Email1":
            jump email1
        "Email2":
            jump email2
        "Email3":
            jump email3

label find_out_more:#checkpoint x
    
    menu:
        "Search for hotels in Tropica on the internet":
            jump search_hotels
        "Write an email to Marcus Johnson as Jack Morrison":
            jump write_email

label search_hotels:
    "You decide to search on the internet for hotels in the town Tropica."
    "Luckily, you find out that there are only three hotels in the town: Grand Horizon Inn, Hotel Semirani and Hotel Diamond Resorts."
    menu:
        "Try your luck and go to one of the hotels":
            jump hotel_options
        "Call hotels and confidently ask for Marcus Johnson":
            jump call_hotels

label hotel_options:
    "You arrive at the hotel. Which hotel would you like to visit?"
    menu:
        "Go to Grand Horizon Inn":
            jump hotel1_fail
        "Go to Hotel Semirani":
            jump hotel2_success
        "Go to Hotel Diamond Resorts":
            jump hotel3_fail

label hotel1_fail:
    #Todo
    #Go to checkpoint x

label hotel2_success:
    "You go to Hotel 2."
    "Receptionist: How can we help you?"
    "Player: I would like to rent a room."
    "Receptionist: Sure, Standard Room or Deluxe Room?"
    menu:
        "Take the Standard Room":
            jump takeroom
        "Take the Deluxe Room":
            jump takeroom

label takeroom:
    "You take your keys and go to your room."
    "You observe Marcus Johnson entering his room, which is right next to yours."
    menu:
        "Set up a Wifi Access Point and create a fake login":
            jump setupwifi

label setupwifi:
    "Transition: evening..."
    "You keep waiting for a couple of hours but no one logs into your fake wifi point."
    "You are almost ready to give up, when all of a sudden you can see that someone fell for your trap."
    "Now you can monitor the victim's online activity."
    # Todo Mareike

label call_hotels:

    "What hotel do you want to call first?"
    menu:
        "Grand Horizon Inn":
            jump hotel1_call
        "Hotel Semirani":
            jump hotel2_call
        "Hotel Diamond Resorts":
            jump hotel3_call


label hotel1_call:
    "You confidently call the hotel and ask for Marcus Johnson."

    "Hotel 1: 'I’m sorry, we don’t have a guest of that name staying here.'"

label hotel2_call:

    "You confidently call the hotel and ask for Marcus Johnson."

    "Hotel 2: 'What room number?'"
    "Hotel 2: 'When he told me he would be staying at your hotel, a week ago, he hadn’t checked in and of course even he didn’t know his room number then.'"
    "Hotel 2: 'Sorry we cannot do that. The safety, security and privacy of our guests is our highest value.'"

label hotel3_call:
    "You confidently call the hotel and ask for Marcus Johnson."

    "Hotel 3: 'I’m sorry, we don’t have a guest of that name staying here.'"






    



