$ renpy.include("inventory.rpy")

define p3 = Character(_("Me"), color="#c8c8ff")
define cathy2 = Character(_("Cathy"), color="#6fd066")
define so = Character (_("Security Officer"), color="#3939f5")
define hc = Character (_("Head Chef"), color="#3939f5")
define s = Character (_("Server"), color="#3939f5")


label level_2:
    "After a brief meeting with the reporter, you're now certain of the politician's identity. With the name and party affiliation of Senator John Smith from Liberty party in hand, your investigation enters its next phase."


    "You start by scouring the internet for any mention of Senator Smith's office location, complemented by a thorough investigation of his Instagram for any inadvertent leaks of his whereabouts."

    menu:
        "Focus on Google, looking for official records or news mentions":
            jump focus_on_google
        "Dive into Instagram, analyzing tagged locations and posts.":
            jump dive_into_insta


label focus_on_google:

    # Here option 3 is correct

    menu:
        "Search for Senator Smith's legislative contributions and voting record.":
            jump voting_record
        "Look up recent news articles for any mention of public appearances or scandals.":
            jump news_articles
        "Investigate the Liberty Party's official website for profiles and press releases mentioning Smith.":
            jump press_releases


label dive_into_insta:

    # Here every option is correct

    menu:
        "Review Senator Smith's official Instagram page for any clues":
            jump review_official_insta
        "Check tagged photos to see if anyone has posted pictures inside or near his office.":
            jump tagged_photos
        "Explore the Instagram stories archive, if available, for past mentions of events or meetings":
            jump stories_archive

label voting_record:

    # BG One picture of computer screen where there is a mention of senator smith community project
    #BG Second picture of computer screen where the Senator Smith of Liberty Party has most votes


    "You discover Senator Smith's active involvement in community service projects, painting him as a dedicated public servant."

    jump focus_on_google

label news_articles:

    #BG Inside computer screen news article of Senator Smith

    "This uncovers a series of positive articles highlighting Smith's efforts in promoting transparency and ethics in politics."

    jump focus_on_google
label press_releases:

    # BG office address of Senator Smith


    "On the Liberty Party's website, you find a detailed biography of Smith, including his office address in the heart of the political district, confirming his standing as a respected member of the party."

    jump senator_office

label review_official_insta:

    # Insta post of many people celebrating where the office address is written top


    "On his official page, you find a post celebrating an anniversary of his office opening, with the address tagged."


    jump senator_office



label tagged_photos:

    # Insta post of senator office

    "A photo tagged by a local business owner showing the exterior of Senator Smith's office, providing its location."

    jump senator_office


label stories_archive:

    # Insta post of some event at the office

    "Stories archive includes a repost from a charity event at his office, confirming the location and showcasing his philanthropic side."


    jump senator_office


label senator_office:

    "You successfully pinpoint the location of Senator Smith's office. The information gathered paints a picture of Senator Smith as a man of integrity and dedication, deeply involved in his community and his duties as a member of the Liberty Party."


    "Following your visit to Senator John Smith's office, you decide it's time to get your hands dirty—literally. The dumpsters located discreetly behind the office building hold the potential to unveil secrets that no digital footprint could reveal. As you approach, you notice two distinct dumpsters: one clearly labeled for paper waste, the other for general refuse. "

    menu:
        "Paper Waste Bin":
            jump paper_waste
        "Other Waste Bin":
            jump other_waste



label paper_waste:

    # Here option 2 is correct

    menu:
        "Look for intact documents, letters, or anything with handwriting.":
            jump intact_documents
        "Search for shredded documents that could be pieced back together.":
            jump shredded_documents
        "Focus on finding envelopes that might contain undiscarded mail or confidential communications.":
            jump finding_envelopes


label other_waste:

    # Here no option is correct option 3 will result in CAUGHT

    menu:
        "Brave the rotten food to look for any discarded personal items that could hold information.":
            jump rotten_food
        "Search for electronic devices or storage media that might have been thrown away.":
            jump electronic_devices
        "Keep an eye out for any unusual items that seem out of place in a typical office waste scenario":
            jump unusual_items

label intact_documents:

    # Emails prinouts
    "Finds a series of personal messages and email printouts that hint at Senator Smith's character and the positive morale among his staff."


label shredded_documents:

    # MINI GAME OF PAPER PUZZLE


    "Uncovers a puzzle challenge where you must reassemble a shredded document."

    jump noisy_cat

label finding_envelopes:

    # some Calenders 

    "Reveals a stack of outdated office calendars and generic event flyers, none of which pertain to Senator Smith's current activities."

label rotten_food:

    # Broken smartphone
    "Leads to the discovery of a broken smartphone."

label electronic_devices:

    # Broken USB drive

    "Uncovers a USB drive among the refuse. However, upon closer inspection, it appears damaged and unlikely to function, rendering its potential contents inaccessible and leaving you with more questions than answers."


label unusual_items:

    # Broken shredder paper

    "Disturbs a hidden mechanical device, which turns out to be an old, malfunctioning paper shredder wedged between bags of paper waste. Its sudden activation creates a brief but loud grinding noise, disrupting the quiet of the evening. This unexpected noise hastens your decision to leave before drawing any further attention."


    jump Caught


label noisy_cat:

    # Cat on the other side of the Bin.
    # Here option 3 is correct

    "As you sift through the papers, the silence of the evening is suddenly broken by a loud noise. Startled, you turn to find a stray cat rummaging through the other side of the dumpster, its eyes reflecting in the dim light. The cat, more curious than frightened, begins to make a ruckus, drawing your attention away from the task at hand."

    menu: 
        "Attempt to gently shoo the cat away, hoping it leaves without causing further commotion.":
            jump shoo_the_cat
        "Ignore the cat and focus on your search, trying to make the most of your time before anyone notices.":
            jump ignore_and_focus
        "Offer some of your snack to the cat, hoping to quiet it down and keep it occupied.":
            jump offer_snack


label shoo_the_cat:

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

    # Here option 1 and option 2 are wrong and leads to caught
    "As you delve deeper into the documents, the cat, undeterred, continues its exploration, causing papers to scatter. Suddenly, the noise escalates as the cat finds something intriguing and dashes out, papers in tow. The commotion attracts attention, and you hear footsteps approaching."

menu:
        "Try to explain your presence as a curious passerby who heard a noise.":
            jump try_and_explain
        " Attempt to hide behind the larger bins, hoping the guard doesn't see you.":
            jump hide_behind_bins
        "Use the moment to escape, taking advantage of the scattered papers as a distraction.":
            jump moment_to_escape


label try_and_explain:

    so "Hey! What are you doing here? This area is off-limits at this time of night."

    p3 "Oh, hi there! I was just passing by and heard this loud noise. It sounded like a cat in distress, so I thought I'd check it out."

    # (raising an eyebrow)
    so "A cat, you say? And you decided to investigate by rummaging through our dumpsters?"

    p3 "Well, I didn't exactly rummage. I was just trying to see if the cat was okay. It seemed scared."

    so "I find that hard to believe. People don't usually wander around private property because they hear a cat. Do you have any ID on you? Why are you really here?"

    # (fumbling for an excuse)
    p3 "I... um, I do have my ID. But honestly, I was just concerned about the cat. Nothing more."

    #(not convinced)
    so "I'm going to have to ask you to stay right here while I call this in. Your story doesn't add up, and you shouldn't be on this property without a valid reason."

    jump Caught


label hide_behind_bins:

    # Player hiding behind the bins 

    "You try to hide behind the bins but the Security Officer notices you. You have been Caught red-handed"

    jump Caught

label moment_to_escape:

    "Provides a narrow escape"

    # He has to repeat this step

    jump noisy_cat

label offer_snack:

    # Cat is eating some food


    "The cat, now intrigued by your offering, calms down and starts eating quietly. This temporary truce allows you to continue your search. "


    jump player_with_phone


label player_with_phone:# [At home, Player with phone]
    "You decide to call Cathy and update her on your findings"
    p3 "Hey Cathy, I found out about a secret meeting at the annual charity event."
    cathy2 "Great! That means we have to be there and collect some evidence for my story!"
    p3 "This will be impossible, I know that they have a guest list, we can’t just show up!"
    cathy2 "I have a plan. As a journalist, I can go there without an invitation because they like it when the press reports on their generous charity event." 
    cathy2 "I will steal some catering clothes and hide them outside for you." 

    jump next_day_2

label next_day_2:

    "You stand outside the event venue, adorned in a chef's uniform stolen from a nearby catering van."
    "Choose a role to blend in seamlessly."

    menu:
        
        "Assume the role of a server, allowing you to move around discreetly.":
            jump server_route

        "Pose as the head chef, giving you more authority and access.":
            jump head_chef_route

label server_route:

    "You confidently slip into the role of a server, blending in with the catering staff bustling around the event location."
    #noch weiter

label head_chef_route:

    #[HEAD CHEF; MAD]
    "Despite your efforts to pose as the head chef, things don't go as smoothly as planned. The real head chef, who was briefly away, returns unexpectedly."

    hc "Excuse me? Who are you, and why are you wearing my uniform?"
    p3 "Oh, my apologies! I'm the new chef brought in for the special menu tonight. They said there would be some changes, and I was told to coordinate directly with you."

    hc "Changes? No one informed me about any changes. What's your name?"
    p3 "Chef Johnson. They rushed me in at the last minute for this event."

    hc "Johnson? I've been the head chef here for years, and I've never heard of you."

    menu:
        "Decide to discuss further with him":
            jump caught_route

        "Tell him you will try to contact the manager to resolve the confusion":
            jump outside_route

label caught_route:

    # go to checkpoint
    p3 "Well, that is unfortunate, but I am the head chef for today."
    hc "Nice try, but I've been running this kitchen for years, and I know all my staff. And you're definitely not the chef approved for this event."

label outside_route:

    #Standing in front of ballroom

    "You rush outside the room and try to calm yourself down. The head chef didn't buy a word you said, and you almost got caught."
    
    menu: 
        "Go inside the ballroom": 
            jump insidefail
        "Check out the building": 
            jump check_out_building #noch machen




label insidefail:

    s "Hey, you! Aren’t you the guy that pretended to be the head chef?"
    s "Don't play innocent! Security!!"
    "They point an accusatory finger in your direction, and the eyes of nearby guests begin to turn toward you."
    "You know that your disguise has been revealed, and you have to face the consequences of your activities..."
    
    # go to checkpoint

label insideserver:

    cathy2 "Did you manage to get in?"
    p3 "Yes, I am a server."
    cathy "Ok meet me inside the ball room."

    "You pick up a tray with delicious food and step into the ball room. "
    "You find yourself in the grand ball room with an assembly of well dressed individuals. "
    "The air is filled with excitement as the most important figures of the company mingle with wealthy potential donors. "
    "Your eyes sweep across the space, searching for Cathy. Dressed in a red dress, she captures your attention. "
    "Adopting the role of a server, you gracefully approach her. In a casual exchange, she selects one of the snacks from your tray and replaces it with an empty plate."
    #   [something peeks out from under the plate → Recorder] Player has to click on it
    "While pretending to be a server, your eyes keenly scan the faces of the gathered guests. "
    "Among the sea of influential figures, you spot the Senator John Smith from your picture."

    #Update inventory-recorder
 


label insideguest:

    cathy2 "Did you manage to get in?"
    p3 "There was a slight complication I am now an official guest"
    cathy2 "Ok meet me at the the dance floor "

    "Dressed in your elegant suit, you enter the ball room. "
    "You find yourself in the grand ball room with an assembly of well dressed individuals. "
    "The air is filled with excitement as the most important figures of the company mingle with wealthy potential donors. "
    "Your eyes scan the surroundings, on the lookout for Cathy. Amidst the crowd, she stands out in a long red dress. "
    "Purposefully, you make your way towards her."
    p3 "May i ask you to a dance?"
    cathy "Sure!"
    "You and Cathy sway to the rhythm of the music, lost in the dance. "
    "Suddenly, she discreetly retrieves a small item from her purse and passes it to you inconspicuously. "
    "Upon closer inspection, you discover it's a compact recorder, swiftly stashing it away in your sleeves."
    #Update inventory-recorder

    "While dancing, your eyes keenly scan the faces of the gathered guests. Among the sea of influential figures, you spot the Senator John Smith from your picture."

    jump start
