$ renpy.include("inventory.rpy")
$ renpy.include("tutorial_story.rpy")
$ renpy.include("level_1.rpy")

define inf_sd = " "
define so = Character (_("Security Officer"), color="#0000f9")
define hc = Character (_("Head Chef"), color="#4b0082")
define s = Character (_("Server"), color="#6fd066")
define senator = Character (_("Senator John"), color="#8e0000")

image bg caught="bg caught.jpg"
image bg homelaptop = "bg homelaptop.jpg"
image bg laptopgoogle = "bg laptopgoogle.jpg"
image bg laptopinsta = "bg laptopinsta.jpg"
image bg votingrecord = "bg votingrecord.jpg"
image bg officeaddress = "bg officeaddress.jpg"
image bg celebration = "bg celebration.jpg"
image bg taggedphotos = "bg taggedphotos.jpg"
image bg storiesarchive = "bg storiesarchive.jpg"
image bg senoffice = "bg senoffice.jpg"
image bg waste = "bg waste.jpg"
image bg wastepaper = "bg wastepaper.jpg"
image bg wasteother = "bg wasteother.jpg"
image bg wastecat = "bg wastecat.jpg"
image bg wastecat2 = "bg wastecat2.jpg"
image bg wastecat3 = "bg wastecat3.jpg"
image bg wastehide = "bg wastehide.jpg"
image bg alley = "bg alley.jpg"
image bg charity = "bg charity.jpg"
image bg kitchen2 = "bg kitchen2.jpg"
image bg ballroomdoor = "bg ballroomdoor.jpg"
image bg hallway = "bg hallway.jpg"
image bg hallway2 = "bg hallway2.jpg"
image bg bedroom = "bg bedroom.jpg"

label level_2:
    call inventory
    scene bg homelaptop
    "After a brief meeting with the reporter, you're now certain of the politician's identity. With the name and party affiliation of Senator John Smith from Liberty party in hand, your investigation enters its next phase."


    "You start by scouring the internet for any mention of Senator Smith's office location, complemented by a thorough investigation of his Instagram for any inadvertent leaks of his whereabouts."

    menu:
        "Focus on Google, looking for official records or news mentions":
            jump focus_on_google
        "Dive into Instagram, analyzing tagged locations and posts.":
            jump dive_into_insta

label Caught_Level2:
    scene bg caught
    "You lost the level and need to restart"
    jump level_2

label focus_on_google:
    scene bg laptopgoogle
    #scene Desktop home screen

    # Here option 3 is correct

    menu:
        "Search for Senator Smith's legislative contributions and voting record.":
            jump voting_record
        "Look up recent news articles for any mention of public appearances or scandals.":
            jump news_articles
        "Investigate the Liberty Party's official website for profiles and press releases mentioning Smith.":
            jump press_releases


label dive_into_insta:
    scene bg laptopinsta
    # Here every option is correct

    menu:
        "Review Senator Smith's official Instagram page for any clues":
            jump review_official_insta
        "Check tagged photos to see if anyone has posted pictures inside or near his office.":
            jump tagged_photos
        "Explore the Instagram stories archive, if available, for past mentions of events or meetings":
            jump stories_archive

label voting_record:
    scene bg votingrecord
    # BG One picture of computer screen where there is a mention of senator smith community project
    #BG Second picture of computer screen where the Senator Smith of Liberty Party has most votes


    "You discover Senator Smith's active involvement in community service projects, painting him as a dedicated public servant."

    "This choice doesn't lead to the breakthrough you hoped for."

    jump focus_on_google

label news_articles:
    scene bg votingrecord
    #BG Inside computer screen news article of Senator Smith

    "This uncovers a series of positive articles highlighting Smith's efforts in promoting transparency and ethics in politics."
    "This choice doesn't lead to the breakthrough you hoped for."

    jump focus_on_google
label press_releases:
    scene bg officeaddress
    # BG office address of Senator Smith


    "On the Liberty Party's website, you find a detailed biography of Smith, including his office address in the heart of the political district, confirming his standing as a respected member of the party."

    jump senator_office

label review_official_insta:
    scene bg celebration
    # Insta post of many people celebrating where the office address is written top


    "On his official page, you find a post celebrating an anniversary of his office opening, with the address tagged."


    jump senator_office



label tagged_photos:
    scene bg taggedphotos
    # Insta post of senator office

    "A photo tagged by a local business owner showing the exterior of Senator Smith's office, providing its location."

    jump senator_office


label stories_archive:
    scene bg storiesarchive
    # Insta post of some event at the office

    "Stories archive includes a repost from a charity event at his office, confirming the location and showcasing his philanthropic side."


    jump senator_office


label senator_office:
    scene bg senoffice
    "You successfully pinpoint the location of Senator Smith's office. The information gathered paints a picture of Senator Smith as a man of integrity and dedication, deeply involved in his community and his duties as a member of the Liberty Party."


    "Following your visit to Senator John Smith's office, you decide it's time to get your hands dirty—literally."
    "The dumpsters located discreetly behind the office building hold the potential to unveil secrets that no digital footprint could reveal. As you approach, you notice two distinct dumpsters: one clearly labeled for paper waste, the other for general refuse. "
    scene bg waste
    menu:
        "Paper Waste Bin":
            jump paper_waste
        "Other Waste Bin":
            jump other_waste



label paper_waste:
    scene bg wastepaper
    # Here option 2 is correct
   

    menu:
        "Look for intact documents, letters, or anything with handwriting.":
            jump intact_documents
        "Search for shredded documents that could be pieced back together.":
            jump shredded_documents
        "Focus on finding envelopes that might contain undiscarded mail or confidential communications.":
            jump finding_envelopes


label other_waste:
    scene bg wasteother
    #If player chooses among these option then he 
    menu:
        "Brave the rotten food to look for any discarded personal items that could hold information.":
            jump rotten_food
        "Search for electronic devices or storage media that might have been thrown away.":
            jump electronic_devices
        "Keep an eye out for any unusual items that seem out of place in a typical office waste scenario":
            jump unusual_items

label intact_documents:
    scene bg wastepaper
    # Emails prinouts
    "Finds a series of personal messages and email printouts that hint at Senator Smith's character and the positive morale among his staff."

    "This choice doesn't lead to the breakthrough you hoped for."
    jump paper_waste

label shredded_documents:
    "Try to reassemble the shredded document."
    call screen paper_puzzle

    # MINI GAME OF PAPER PUZZLE
    screen paper_puzzle:
        add "gui/inventory/background.png"
        #image Solid("#474747")
        draggroup:
            drag:
                xpos 0.25
                ypos 0.3
                child "gui/invitation_letter/piece3.png"
                draggable True
                drag_raise True
            drag:
                xpos 0.1
                ypos 0.25
                child "gui/invitation_letter/piece5.png"
                draggable True
                drag_raise True
            drag:
                xpos 0.2
                ypos 0.3
                child "gui/invitation_letter/piece1.png"
                draggable True
                drag_raise True
            drag:
                xpos 0.15
                ypos 0.15
                child "gui/invitation_letter/piece8.png"
                draggable True
                drag_raise True
            drag:
                xpos 0.25
                ypos 0.3
                child "gui/invitation_letter/piece2.png"
                draggable True
                drag_raise True
            drag:
                xpos 0.25
                ypos 0.2
                child "gui/invitation_letter/piece4.png"
                draggable True
                drag_raise True
            drag:
                xpos 0.3
                ypos 0.2
                child "gui/invitation_letter/piece7.png"
                draggable True
                drag_raise True
            drag:
                xpos 0.25
                ypos 0.35
                child "gui/invitation_letter/piece6.png"
                draggable True
                drag_raise True
    
        imagebutton auto "gui/invitation_letter/back_%s.png":
            focus_mask True
            action Jump("save_information")

    label save_information:
        python:
            style.input.color = "#ffffff"
            inf_sd = renpy.input("Type in the information you want to save in your journal", length=100)
            inf_sd = inf_sd.strip()
            save_inf = InventoryData("Information found on shredded document", inf_sd)
            inventory.add_data(save_inf)

    jump noisy_cat

label finding_envelopes:
    scene bg wastepaper
    # some Calenders 

    "Reveals a stack of outdated office calendars and generic event flyers, none of which pertain to Senator Smith's current activities."
    "This choice doesn't lead to the breakthrough you hoped for."
    jump paper_waste

label rotten_food:
    scene bg wasteother
    # Broken smartphone
    "Leads to the discovery of a broken smartphone."
    "This choice doesn't lead to the breakthrough you hoped for."
    "You might find something in paper waste. Go check it."
    jump paper_waste

label electronic_devices:
    scene bg wasteother
    # Broken USB drive

    "Uncovers a USB drive among the refuse. However, upon closer inspection, it appears damaged and unlikely to function, rendering its potential contents inaccessible and leaving you with more questions than answers."
    "This choice doesn't lead to the breakthrough you hoped for."
    "You might find something in paper waste. Go check it."
    jump paper_waste
    

label unusual_items:
    scene bg wasteother
    # Broken shredder paper

    "Revealing a hidden mechanical device, which turns out to be an old, malfunctioning paper shredder wedged between bags of paper waste."
    "Its sudden activation creates a brief but loud grinding noise, disrupting the quiet of the evening. This unexpected noise hastens your decision to leave before drawing any further attention."

    "This choice doesn't lead to the breakthrough you hoped for."
    "You might find something in paper waste. Go check it."
    jump paper_waste



label noisy_cat:
    scene bg wastecat
    # Cat on the other side of the Bin.
    # Here option 3 is correct

    "As you sift through the papers, the silence of the evening is suddenly broken by a loud noise."
    "Startled, you turn to find a stray cat rummaging through the other side of the dumpster, its eyes reflecting in the dim light. The cat, more curious than frightened, begins to make a ruckus, drawing your attention away from the task at hand."

    menu: 
        "Attempt to gently shoo the cat away, hoping it leaves without causing further commotion.":
            jump shoo_the_cat
        "Ignore the cat and focus on your search, trying to make the most of your time before anyone notices.":
            jump ignore_and_focus
        "Offer some of your snack to the cat, hoping to quiet it down and keep it occupied.":
            jump offer_snack


label shoo_the_cat:
    scene bg wastecat3
    # Cat making noise
    # Here option 1 and option 2 are wrong and leads to caught
    "Your attempt to scare the cat off backfires. It leaps out of the dumpster with a loud meow, knocking over a stack of bins in the process. The clamor echoes through the quiet streets, and within minutes, a security guard approaches to investigate the noise."

    menu:
        "Try to explain your presence as a curious passerby who heard a noise.":
            jump try_and_explain
        " Attempt to hide behind the larger bins, hoping the guard doesn't see you.":
            jump hide_behind_bins
        "Use the moment to escape, taking advantage of the scattered papers as a distraction.":
            jump moment_to_escape


label ignore_and_focus:
    scene bg wastecat
    # Here option 1 and option 2 are wrong and leads to caught
    "As you delve deeper into the documents, the cat, undeterred, continues its exploration, causing papers to scatter."
    "Suddenly, the noise escalates as the cat finds something intriguing and dashes out, papers in tow. The commotion attracts attention, and you hear footsteps approaching."

    #jump Caught_Level2

    menu:
        "Try to explain your presence as a curious passerby who heard a noise.":
            jump try_and_explain
        " Attempt to hide behind the larger bins, hoping the guard doesn't see you.":
            jump hide_behind_bins
        "Use the moment to escape, taking advantage of the scattered papers as a distraction.":
            jump moment_to_escape


label try_and_explain:
    scene bg alley
    show Me
    show officer
    #show officer

    so "Hey! What are you doing here? This area is off-limits at this time of night."

    p "Oh, hi there! I was just passing by and heard this loud noise. It sounded like a cat in distress, so I thought I'd check it out."

    # (raising an eyebrow)
    so "A cat, you say? And you decided to investigate by rummaging through our dumpsters?"

    p "Well, I didn't exactly rummage. I was just trying to see if the cat was okay. It seemed scared."

    so "I find that hard to believe. People don't usually wander around private property because they hear a cat. Do you have any ID on you? Why are you really here?"

    # (fumbling for an excuse)
    p "I... um, I do have my ID. But honestly, I was just concerned about the cat. Nothing more."

    #(not convinced)
    so "I'm going to have to ask you to stay right here while I call this in. Your story doesn't add up, and you shouldn't be on this property without a valid reason."

    jump Caught_Level2


label hide_behind_bins:
    scene bg wastehide
    # Player hiding behind the bins 

    "You try to hide behind the bins but the Security Officer notices you. You have been Caught red-handed"

    jump Caught_Level2

label moment_to_escape:
    scene bg alley
    "Provides a narrow escape"

    # He has to repeat this step

    jump player_with_phone

label offer_snack:
    scene bg wastecat2
    # Cat is eating some food


    "The cat, now intrigued by your offering, calms down and starts eating quietly. This temporary truce allows you to continue your search. "


    jump player_with_phone


label player_with_phone:
    scene bg bedroom
    # show [Player with phone]
    "You decide its time to call Cathy and update her on your findings."
    p "Hey Cathy, I found out about a secret meeting at the annual charity event."
    c "Great! That means we have to be there and collect some evidence for my story!"
    p "This will be impossible, I know that they have a guest list, we can’t just show up!"
    c "I have a plan. As a journalist, I can go there without an invitation because they like it when the press reports on their generous charity event." 
    c "I will steal some catering clothes and hide them outside for you." 

    jump next_day_2

    #checkpoint m

label next_day_2:

    #Use map to navigate to the charity event
    scene bg charity
    "You stand outside the event venue, adorned in the chef's uniform stolen from a nearby catering van."
    "Choose a role to blend in seamlessly."

    menu:
        
        "Assume the role of a server, allowing you to move around discreetly.":
            jump server_route

        "Pose as the head chef, giving you more authority and access.":
            jump head_chef_route

label server_route:
    scene bg hallway
    show Me service
    #show you wearing server/kitchen clothes

    "You confidently slip into the role of a server, blending in with the catering staff bustling around the event location."

    "Then you check you phone for new messages."

    jump insideserver
    

label head_chef_route:
    scene bg kitchen2
    show Me chef
    show chef
    # scene kitchen
    #[HEAD CHEF; MAD] you wearing server/kitchen clothes
    "Despite your efforts to pose as the head chef, things don't go as smoothly as planned. The real head chef, who was briefly away, returns unexpectedly."

    hc "Excuse me? Who are you, and why are you wearing my uniform?"
    p "Oh, my apologies! I'm the new chef brought in for the special menu tonight. They said there would be some changes, and I was told to coordinate directly with you."

    hc "Changes? No one informed me about any changes. What's your name?"
    p "Chef Johnson. They rushed me in at the last minute for this event."

    hc "Johnson? I've been the head chef here for years, and I've never heard of you."

    menu:
        "Decide to discuss further with him":
            jump caught_route

        "Tell him you will try to contact the manager to resolve the confusion":
            jump outside_route

label caught_route:
    scene bg kitchen2
    show Me chef
    show chef
    # go to checkpoint m
    p "Well, that is unfortunate, but I am the head chef for today."
    hc "Nice try, but I've been running this kitchen for years, and I know all my staff. And you're definitely not the chef approved for this event."

label outside_route:
    scene bg ballroomdoor
    show Me service
    #Standing in front of ballroom

    "You rush outside the room and try to calm yourself down. The head chef didn't buy a word you said, and you almost got caught."
    
    menu: 
        "Go inside the ballroom": 
            jump insidefail
        "Check out the building": 
            jump check_out_building 


label check_out_building:
#dimly lit corridors
    scene bg hallway
    show Me service

    "You walk through the dimly lit corridors of the building."
    "Suddenly, distant voices begin to echo, gradually growing louder and more distinct. "
    "Instinctively, you press your back against the wall, peering cautiously around the corner. "
    "Just as you begin to contemplate slipping away unnoticed you recognize the unmistakable silhouette of the senator."
    menu: 
        "Hide behind a wall": 
            jump hidewall 
        "Act like you are looking for the bathroom":
            jump actbathroom 
label hidewall:
    scene bg hallway
    show Me service
#hiding space: maybe behind a wall/door, and door of secret meeting visible
    "As the voices gradually grow louder, you hold your breath, fearing discovery. "
    
    scene bg hallway2
    show Me service
    hide Me service with easeinright
    "Then you see three people passing you. Fortunately, they don’t notice you as they disappear into a nearby room. "

    "As they close the door behind them, you are walking towards the door. You can hear voices inside the room."

    menu:
        "Go inside the room as a server and place a tray of food in the room with a recorder hidden underneath the tray.":
            jump insiderecord

        "Listen from outside the room and record it.":
            jump outsiderecord


label actbathroom:
    scene bg hallway
    show Me service
    show senator
    "You try to act casual and as if you are searching for the bathroom. Suddenly three people appear, one of them you recognize as the senator."


#senator evil/mad
    "What are you snooping around for? The ballroom's that way." 
    "Oh I’m just looking for the bathroom, could you please show me where I can find it?"
    "There is no bathroom here. And you shouldn't be hanging around here. This is a restricted area."
    "I'll get security to throw you out!"
#go to checkpoint m



label insidefail:
    scene bg kitchen2
    show Me chef
    show chef4
#other kitchen employee

    s "Hey, you! Aren’t you the guy that pretended to be the head chef?"
    s "Don't play innocent! Security!!"
    #yelling
    "They point an accusatory finger in your direction, and the eyes of nearby guests begin to turn toward you."
    "You know that your disguise has been revealed, and you have to face the consequences of your activities..."
    
    # go to checkpoint m

label insideserver:

#text message bg

    c "Did you manage to get in?"
    p "Yes, I am a server."
    c "Ok meet me inside the ball room."

    #show you with a tray of food
    #scene inside ballroom bg

    "You pick up a tray with delicious food and step into the room. "
    "You find yourself in the grand ball room with an assembly of well dressed individuals. "
    "The air is filled with excitement as the most important figures of the company mingle with wealthy potential donors. "
    "Your eyes sweep across the space, searching for Cathy. Dressed in a red dress, she captures your attention. "
    "Adopting the role of a server, you gracefully approach her. In casual exchange, she selects one of the snacks from your tray and replaces it with an empty plate."
    #   [something peeks out from under the plate → Recorder] Player has to click on it
    #Update inventory-recorder
 
    "While pretending to be a server, your eyes keenly scan the faces of the gathered guests. "
    #senator smith in focus, checking his watch
    "Among the sea of influential figures, you spot the Senator John Smith from your picture."
    "In the midst of the lively chatter, you observe him checking his watch, hinting a sense of urgency."
    "Suddenly you see him getting up and leaving the room."
    menu: 
        "Follow him inconspiciously": 
            jump followsenator 
        "Stay and listen to the speeches":
            jump listenspeeches 

    


label insideguest:

    c "Did you manage to get in?"
    p "There was a slight complication I am now an official guest"
    c "Ok meet me at the the dance floor."

    "Dressed in your elegant suit, you enter the room. "
    "You find yourself in the grand ball room with an assembly of well dressed individuals. "
    "The air is filled with excitement as the most important figures of the company mingle with wealthy potential donors. "
    "Your eyes scan the surroundings, on the lookout for Cathy. Amidst the crowd, she stands out in a long red dress. "
    "Purposefully, you make your way towards her."
    p "May i ask you to a dance?"
    c "Sure!"
    "You and Cathy sway to the rhythm of the music, lost in the dance. "
    "Suddenly, she discreetly retrieves a small item from her purse and passes it to you inconspicuously. "
    "Upon closer inspection, you discover it's a compact recorder, swiftly stashing it away in your sleeves."
    #Update inventory-recorder
#senator smith in focus, checking his watch
    "While dancing, your eyes keenly scan the faces of the gathered guests. Among the sea of influential figures, you spot the Senator John Smith from your picture."
    "In the midst of the lively chatter, you observe him checking his watch, hinting a sense of urgency."
    "Suddenly you see him getting up and leaving the room."
    menu: 
        "Follow him inconspiciously": 
            jump followsenator 
        "Stay and listen to the speeches":
            jump listenspeeches 

label followsenator:
#corridor bg with door visible
    "You follow him carefully. He walks down the corridor and looks around right before he enters into a room and puts up a sign “No disturbing”"

    "As he closes the door behind him, you are walking towards the door. You can hear voices inside the room."

#Options to record can only be seen when ou recieved the recorder from cathy
    menu:
        "Go inside the room as a server and place a tray of food in the room with a recorder hidden underneath the tray.":
            jump insiderecord

        "Listen from outside the room and record it.":
            jump ousiderecord

        "Eavesdrop on the conversation from outside":
            jump outsiderecord2

label insiderecord:
    #scene secret meeting room
    #[Three people 1 female, two male (one of them senator John Smith) staring at you, agressively]
    "You gently knock on the door before entering the room."
    "Person: Hey! What the hell do you think you're doing? This is a private meeting!"
    p "Oh, I'm sorry. I didn't realize there was a private meeting going on. I just wanted to serve some drinks."
    "Person: Well, you can't just barge in like that! We're in the middle of something important."

    p "I honestly didn't know. I wouldn't have come in if I had known there was a meeting."
    "Person: Well, now you know. So, get out and let us finish what we're doing. You can leave the drinks here."
    "You quickly retrieve what you came for, feeling the tension in the room. As you leave, the door closes behind you."

    jump waiting_for

label outsiderecord:

#you in front of door holding ear agianst it


    "You sneak up to the door, catching some hushed voices. "
    "Then you hit the record button, but soon realize that you can barely make out anything from the conversation."
    
    #checkpoint m

label outsiderecord2:

#you in front of door holding ear agianst it


    "You sneak up to the door, catching some hushed voices. "
    "Pressing your ear to the door, you soon realize that you can barely make out anything from the conversation."
    
    #checkpoint m

label listenspeeches:

    "SPEAKER 1: Ladies and gentlemen, in times of challenge, we must unite and strive for progress. Our collective efforts can shape a better world for generations to come."

    "…as you listen to the speeches you completely forget about the secret meeting that takes places at that same time, leaving you unaware of the information that would have completed your mission. The night proceeds, and the secrets remain hidden."

    #checkpoint m


#Checkpoint recorded
label waiting_for:
    

    "You make use of the hiding place you already discovered earlier and watch the door tensely. As the three people leave the room, you wait briefly to avoid a blatant return and then set off to retrieve the recording."


label getrecording:

    "With a cautious push, you enter the room, the weight of the silence weighing on you as you close the door behind you silently."
    "Your hand reaches for the recording, picking it up and tucking it safely into your pocket, the mission nearly accomplished, when the sound of footsteps startles you and the door swings open."

    #scene empty secret meeting room
    #show senator
    senator "Sorry J forgot my lighter in this room…"

    menu:

        "Pick up glasses":
            jump picked_up_glasses

        "Turn around":
            jump turn_around

        "Start running":
            jump running_from


label picked_up_glasses:
    #show player in service clothes

    senator "YOU Again?!"

    p "I am sorry! I was just cleaning up to get your glasses as they are needed in the ballroom. We are running low on unused glasses."

    senator "Hmpf! Did you see my lighter anywhere?"
    
    p "No, I have to go to the kitchen, the staff needs all the help they can get, its like hell right now."

    jump succesful_leaving

label turn_around:

    senator "YOU Again?!"

    p "I was just going to clean up here."

    senator "You know what's funny? You barged into our meeting and now you're back in this room. Somehow I think we should get to the bottom of you."

    senator "So what are you hiding or do you need it beaten out of you? I have the right person to talk to about it and he doesn't ask as nicely as I do. But just keep quiet, actually it's more fun for all of us, you know."

    jump running_from

label running_from:

    "You start running, knocking him aside and running out the door. Suddenly you are stopped, someone grabs you and pushes you against the wall."
    "You try to free yourself, but your arms are caught in a vice-like grip. You have a bad feeling when you see the senator coming towards you, snorting with rage. He points a finger at you"

    senator "You got him? Good, he attacked me! Lets find out what he is doing here!"

    jump caught_from_senator

label caught_from_senator:

    "That's it, you can't talk your way out of this one"
    # jump checkpoint recorded

label succesful_leaving:

    "You do not wait for an answer, but leave as quickly as you can, hoping that the senators will not notice your trembling. 
    You could even swear that your shaking hands make the drinking glasses ring slightly."

    menu: 

        "You decide to get rid of your disguise and plan your next step"

        "Leave the event":
            jump leave_event
        "Mingle with the party guests":
            jump stay_party

label stay_party:

    "You decide to stay a bit longer and look for Cathy. As you find her engrossed in a conversation with a colleague you excuse and pull her onto the dance floor with your hand.
    While you sway to the beat of the music, you tell her about the successful recording and the close encounter with the senator." 

#show cathy red dress
    p "My fingertips are itching to find out what was said on the recording should we get out of here and finally reveal this secret?"

    c "Yeah, let's do that! Can we stop at a fast food restaurant on the way? I get really hungry all the time when I get nervous about things."

    p "Good idea all this fancy snacks, mussels and other stuff is not for me anyway. I prefer a burger and fries to that allways!"

    jump listen_recording

label leave_event:

    "After successfully retrieving the recording, you waste no time in slipping out of the event, the weight of the evidence burning a hole in your pocket. 
    You dial Cathy's number as you hail a cab, arranging to meet her at a discreet location where you can reveal the truth hidden within the recording."  
    
    jump next_day_3

label next_day_3:
# scene meetingspot
# show cathy

    c "Hey, how are you? I am honestly very excited to hear your recording. What you have been doing the last few days is crazy and everything with social.. how was it called?"

    p "Social Engineering. Yeah not the machine or the software itself has the weak point but the human in front of it. Thats the trick!"

    
    "You hand her one of your in ears and play back the recording."

    #Audio recording - with subtitle?

    "You turn your gaze to Cathy as the last words are spoken in the recording."
    
    c "Holy shit who are those guys?"

    p "Your senator, the one you said was suspicious, one of those guys is from CORP and the other one I don't know. I saw his face for a moment, but I can't remember where I saw him before."

    # show cathy worried
    c "So they want to hire the Crimson Group... that's not good, I heard about them, they may have been involved in suppressing riots in Jordan and Russia. 
    I think there was also a colleague who was assaulted by one of their mercenaries while writing about it.
    They are dangerous, you really should not try to go to their base of operations."

    p "Hmm I will think of a way to target them without getting harmed. Are you worried about me?"

    c "Maybe a little bit! I mean we are a good team are we not?"

    #jump level 3

label listen_recording:
# scene Fast food restaurant, Table with food
#show cathy red dress

    "Sitting at the table and diggin in your food the recorder placed in between of you and Cathy"

    c "What you have been doing the last few days.. honestly is impressive and crazy. And everything with social.. how was it called?"

    p "Social Engineering. Yeah not the machine or the software itself has the weak point but the human in front of it. You just need to know which buttons to press!"
 
    "You hand her one of your in-ears and play back the recording."

    #Audio recording - with subtitle?

    "You turn your gaze to Cathy as the last words are spoken in the recording."
    
    c "Holy shit who are those guys?"

    p "Your senator, the one you said was suspicious, one of those guys is from CORP and the other one I don't know. I saw his face for a second, but I can't remember where I saw him before."

    # show cathy worried
    c "So they want to hire the Crimson Group... that's not good, I heard about them, they may have been involved in suppressing riots in Jordan and Russia." 
    c "I think there was also a colleague who was assaulted by one of their mercenaries while writing about it.
        They are dangerous, you really should not try to go to their base of operations."

    p "Hmm I will think of a way to target them without getting harmed. Are you worried about me?"

    c "Maybe a little bit! I mean we are a good team are we not?"

    #jump level 3