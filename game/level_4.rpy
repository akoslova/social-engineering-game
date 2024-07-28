$ renpy.include("inventory.rpy")
$ renpy.include("tutorial_story.rpy")

define e1 = Character (_("Employee 1"), color="#8e0000")
define e2 = Character (_("Employee 2"), color="#8e0000")
define jef = Character (_("Jeffrey Miller"), color="#8e0000")
define fake = Character (_("Deep Fake Senator"), color="#8e0000")



# Define the password validation rules
init python:
    def validate_password(rule, password):
        _, check_function = rule
        return check_function(password)

image textboxstatic = "textbox.png"
image bg deepfake = "bg deepfake.jpg"
image bg harddisks = "bg harddisks.jpg"
image bg jefoffice="bg jefoffice.jpg"
image bg tastyfood="bg tastyfood.jpg"
image bg tastyfood2="bg tastyfood2.jpg"
image bg tastyfood3="bg tastyfood3.jpg"
image bg tastyfood4="bg tastyfood4.jpg"
image bg news="bg news.jpg"
image bg blackmail="bg blackmail.jpg"
image bg vacation="bg vacation.jpg"
image bg danger="bg danger.jpg"

image bg cracker:
    "bg cracker1.jpg"
    pause 0.25
    "bg cracker2.jpg"
    pause 0.25
    "bg cracker3.jpg"
    pause 0.25
    "bg cracker4.jpg"
    pause 0.25
    "bg cracker3.jpg"
    pause 0.25
    "bg cracker2.jpg"
    pause 0.25
    "bg cracker1.jpg"
    pause 0.25
    repeat

image bg fireworks:
    "bg fireworks1.jpg"
    pause 0.25
    "bg fireworks2.jpg"
    pause 0.25
    "bg fireworks3.jpg"
    pause 0.25
    "bg fireworks4.jpg"
    pause 0.25
    "bg fireworks5.jpg"
    pause 0.25
    "bg fireworks4.jpg"
    pause 0.25
    "bg fireworks3.jpg"
    pause 0.25
    "bg fireworks2.jpg"
    pause 0.25
    repeat

label level_4:
    call inventory
 
# The game starts here.
label start_level4:
    scene bg coffee
    show Me with easeinright
    show cathy with easeinleft
    "You meet Cathy in a quiet coffee shop. She’s eager to publish the story but agrees that it's best to wait until you have undeniable evidence about the senator's dealings with CORE."
    scene bg wfh with fade
    "Back at your home, you receive an email from TastyFood. They have an important task for you."
    "You think that's not a good idea but decide to go there, knowing it could lead to valuable information."
    scene bg tastyfood with fade 
    show Me with easeinright
    "You arrive at TastyFood and are greeted by the manager, who informs you of a security problem. Your job is to repair the camera."
    scene bg tastyfood2 with fade 
    "As you work on repairing the camera, you overhear a conversation between two employees standing near the break room."

    e1 "Hey, you know those old drives and memory cards they told me to destroy?"

    e2 "Yeah, the ones collecting dust in the storage room. What about them?"

    e1 "I'm thinking of selling them instead. I know a guy who buys old tech. Easy money."

    e2 "Wait, seriously? Isn't that against company policy or something?"

    e1 "Probably, but who’s going to notice? They’re just sitting there, waiting to be tossed out. It’s like free cash lying around."

    e2 "I don't know, man. Sounds risky. What if someone finds out?"

    e1 "Who’s going to find out? The box is labeled 'To be destroyed.' Nobody checks those things. Besides, it’s not like they have a tracking device on them."

    e2 "Still, you’re playing with fire. What if the boss gets wind of it?"

    e1 "Relax, nothing’s going to happen. Just keep this between us. It’s a simple plan. Easy in, easy out."

    e2 "Alright, but if this blows up, I was never here. Deal?"

    e1 "Deal. Now, let’s get back to work before someone actually notices us slacking off."

    menu:
        "Confront Employee directly about the drives and memory cards.":
            jump confront
        "Continue working on the camera while trying to listen for more details.":
            jump continue_working
        "Report this information to the manager immediately.":
            jump tell_manager


label confront:
    scene bg tastyfood3
    show Me with easeinright
    "You decide to confront Jack directly about the drives and memory cards."
    p "Hey, I overheard your conversation. What are you planning to do with those drives and memory cards?"

    e1 "It's none of your business. You better keep your nose out of it."

    "You failed this level. Go back and choose another option."

    jump start_level4

label continue_working:
    scene bg tastyfood2
    "You decide to continue working on the camera while trying to listen for more details."
    "As you work, you hear he mentions a specific location where he plans to stash the drives before selling them. It's the storage room in the back of the building."

    menu:
        "Wait until he leaves and then search the storage room.":
            jump wait
        "Tell the manager what you overheard and suggest checking the storage room.":
            jump tell_manager
        "Follow him discreetly to see where he goes after his shift.":
            jump follow


label wait:
    scene bg harddisks
    "You decide to wait until Jack leaves and then search the storage room."
    "Once Jack is gone, you head to the storage room where you find a box labeled 'To be destroyed.' Inside, there are several old drives and memory cards."

    "You have successfully found the drives and memory cards."

    jump analyze_emails

label tell_manager:
    scene bg tastyfood with fade 
    show Me with easeinright
    "You decide to tell the manager what you overheard and suggest checking the storage room."

    "The manager looks concerned. 'Thank you for letting me know. I'll handle it from here,' he says."

    "You failed this level, you were not suppose to say anything to the manager."

    jump start_level4

label follow:
    scene bg tastyfood4

    "You decide to follow the Employee discreetly to see where he goes after his shift."
    "The employee heads to the storage room, and you watch from a distance as he places the box labeled 'To be destroyed' somewhere."

    menu:
        "Confront him about the box.":
            jump confront
        "Wait until he leaves and then search the storage room.":
            jump wait


label analyze_emails:
    scene bg wfh
    "You find a folder in those drives and inside the folder there are many emails. In emails,you find that 'J' appears to be a key intermediary between CORE and the senator." 
    "The emails contain detailed instructions on financial transfers, land agreements, and political strategies. However, J's true identity remains hidden."
    "One email mentions a rendezvous at a specific luxury hotel during a political fundraiser, attended by several high-profile figures including the senator."

    "You cross-reference this with social media posts, news articles, and hotel booking records. A name frequently appears in connection with these events: 'Jeffrey Miller', the CEO of GreenBanc, a subsidiary of CORE that specializes in environmental projects."

    menu:
        "Investigate Jeffrey Miller's background.":
            jump investigate_miller
        "Search for more emails mentioning 'J'.":
            jump search_J
        "Look into the hotel events and guest lists more thoroughly.":
            jump hotel_events

label investigate_miller:
    scene bg wfh
    "You decide to go deeper into Jeffrey Miller's background. You find that he has a history of involvement in shady business deals and has been spotted frequently with high-profile political figures, including the senator."
    menu:
        "Confront Jeffrey Miller directly at his office.":
            jump confront_jeffrey
        "Set up surveillance on Jeffrey Miller to gather more evidence.":
            jump set_up
        "Look for any financial transactions linking Jeffrey to 'J'.":
            jump financial_transaction


label search_J:
    scene bg wfh
    "You search for more emails mentioning 'J' and did not find any pattern. This is the incorrect choice."
    jump start_level4




label hotel_events:
    scene bg wfh
    "You dig deeper into the hotel events and guest lists. You find that Jeffrey Miller did not attend any key meetings where significant deals were made between CORE and political figures.You failed this level. Go back and choose another option."

    jump start_level4


    

label confront_jeffrey:
    scene bg jefoffice
    "You go to the Jeffrey office and security guard does not let you inside the office.You failed this level. Go back and choose another option."

    jump start_level4

label set_up:
    scene bg jefoffice
    "You try to setup the camera near the office of Jeffrey Miller but security guards sees you.You failed this level. Go back and choose another option."

    jump start_level4


label financial_transaction:
    scene bg wfh
    "By tracing financial transactions, you find that Jeffrey Miller has been moving large sums of money through shell companies, which matches the financial transfers described in the emails from 'J'. You now have a strong suspicion that Jeffrey Miller is 'J'."

    "To confirm your suspicions and extract more information, you decide to use deep fake technology. The plan is to create a video call where Jeffrey Miller believes he is speaking with the senator. The goal is to trick him into revealing his involvement and any additional details about CORE’s operations."

    menu:
        "Collect video and audio samples of the senator.":
            jump collect_samples
        "Create the deep fake video.":
            jump deep_fake
        "Send a convincing email to Jeffrey Miller.":
            jump email_jeffrey


label collect_samples:
    scene bg wfh
    "You need to gather materials to create a convincing deep fake."

    menu:
        "Download public speeches and interviews of the senator.":
            jump download_speeches
        "Record a phone call with the senator.":
            jump record_phone
        "Hire an impersonator to mimic the senator.":
            jump mimic

label deep_fake:
    scene bg wfh
    "Your choice to directly create a deep fake without collecting samples of senator is not a correct option."

    jump start_level4

label email_jeffrey:
    scene bg wfh
    "Your choice to directly email Jeffrey without creating deep fake senator is not a correct option."

    jump start_level4

label record_phone:
    scene bg wfhphone
     
    "You try to find the personal phone number of the Senator but did not find anything. You have failed this level."

    jump start_level4

label mimic:
    scene bg wfh

    "The impersonator did not perfectly mimic the senator's mannerisms, voice, or facial expressions, leading to a less convincing deep fake video."

    jump start_level4

label download_speeches:
    scene bg wfh

    "You collect video and audio samples of the senator from public speeches and interviews."

    menu:
        "Compile the samples into a single video file.":
            jump compile_samples
        "Use the samples to create a deep fake video.":
            jump sample_video
        "Analyze the collected samples for distinctive mannerisms and voice patterns.":
            jump voice_patterns

label voice_patterns:
    scene bg wfh

    "You carefully analyze the collected samples, noting the senator's unique mannerisms and voice patterns."

    menu:
        "Use advanced software to create the deep fake video.":
            jump advanced_software
        "Consult with Cathy on the next steps.":
            jump consult_cathy
        "Continue gathering more samples for accuracy.":
            jump sample_accuracy

label sample_video:
    scene bg wfh
    "The choice to create a deep fake video using samples did not work and hence this is not the correct option."
    jump start_level4

label compile_samples:
    scene bg wfh
    "This option is not correct."

    jump start_level4

label consult_cathy:
    scene bg wfh
    show wfhcall
    "You consult with Cathy and you both decided to create a deep fake video using some advanced software."

    jump advanced_software
label sample_accuracy:
    scene bg wfh
    "You continue your search for gathering more samples and after collecting all the samples you decide to create a deep fake using advanced software."

    jump advanced_software
label advanced_software:
    scene bg wfh
    "Using advanced software, you and Cathy create the deep fake video, fine-tuning every detail to ensure it mimics the senator perfectly."

    "Now, you need to send a convincing email to Jeffrey Miller requesting a private video meeting."
    menu:
        "Send a generic email requesting a meeting.":
            jump generic_email
        "Draft an email using the senator's tone and language.":
            jump draft_email
        "Call Jeffrey Miller directly and request a meeting.":
            jump call_miller

label generic_email:
    scene bg wfh
    "You send a generic email requesting a meeting without any context or urgency."

    jef "This seems odd. Why does the senator want to meet me out of the blue?"

    "Jeffrey ignores the email, and your plan is failed."

    jump start_level4

label call_miller:
    scene bg wfh
    show wfhcall
    "You try calling Jeffrey Miller directly, but he doesn't pick up the phone. This option is not correct."

    jump start_level4

label draft_email:
    scene bg wfh
    "You draft an email using the senator's tone and language, requesting an urgent and private video meeting to discuss sensitive issues about their ongoing operations."

    "The Email - Jeffrey, we need to discuss some pressing matters regarding our project. It’s crucial that we speak privately. Let’s arrange a video call at your earliest convenience. This is highly confidential. – Senator."
    "What will you do next?"
    menu:
        "Wait for Jeffrey Miller to respond.":
            jump wait_respond
        "Follow up with another email if Jeffrey doesn't respond.":
            jump follow_jeffrey
      


label wait_respond:
    scene bg wfh
    "Jeffrey, believing the email to be legitimate, agrees to the meeting."

    jump questions

label follow_jeffrey:
    scene bg wfh
    "Jeffrey gets irritated by this follow-up mail and now will not respond to the previous mail."

    jump start_level4


label questions:
    scene bg wfh
    menu:
        "Prepare questions to ask during the video call.":
            jump prepare_questions
        "Wait for Jeffrey to join the video call.":
            jump wait_jeffrey


label wait_jeffrey:
    scene bg wfh
    "You enter the video call without preparing the question. Jeffrey notice something is wrong and disconnects the call."

    jump start_level4


label prepare_questions:
    scene bg wfh
    "You prepare questions to ensure Jeffrey reveals crucial information."
    scene bg deepfake
    "The video call starts now."
    fake "Jeffrey, I'm beginning to doubt our strategy. Are you sure you haven't left any loose ends that could jeopardize our entire operation?"

    "Jeffrey's expression changes from neutral to angry."

    jef "Leaking information? How dare you accuse me of such a thing! I've made sure every detail is covered. The financial transfers through shell companies are untraceable. GreenBanc is perfectly positioned to channel funds through our environmental projects."

    jef "We've got officials ensuring that any damaging reports are delayed or lost in bureaucracy. The public will never know until it's too late. This partnership with CORE is rock solid, and controlling these rainforest areas will yield massive profits and political influence."

    jef "But why would you bring this up now? What's really going on here, Senator? Are you trying to shift blame? This doesn't sound like you..."

    "Jeffrey's suspicion grows, and he starts to doubt the authenticity of the call."

    "The Deep fake Senator's face remains expressionless for a moment, then suddenly freezes with a big, awkward grin."

    "Beeeeeeep... Connection lost. Please try again later."

    jef "What the...?"

    "The call ends abruptly, leaving Jeffrey confused and staring at his screen."
    "During the call you were able to get access to the senator's PC via remote control."

    jump password_game

# label the_end:
#     python:
#         style.input.color = "#ffffff"
#         the_end = renpy.input("", length=32, screen = "nameInput")
#         the_end = the_end.strip()

    
#         for char in the_end:
#             if char.isupper():
#                 "XYZ"
            
#         "You need to add a Capital Letter!"
#kept here at the start for testing purposes, will be shifted down below later
label password_game:
    scene bg cracker

    "Now that you've got all the information you need, the final step is to secure the evidence from the Senator's PC."
    "As you want to download all relevant data, you can see that his files are password protected."
    "The senator seems to be a fan of riddles, so he didn't make it easy to crack the password"
    "If you are able crack this final code, you will have all the evidence you need to reveal everything."
    "Now is the time to end it all..."

    show textboxstatic:
        yalign 0.96
        xalign 0.5

    # Define the rules for password validation
    $ rules = [
        ("Password must include the reversed form of the user/victim's name (hint: Jeffrey)", lambda pwd: 'yerffej' in pwd.lower()),
        ("Password must contain at least 2 uppercase letters.", lambda pwd: pwd == 'YErffej'),
        ("Password must contain exactly 5 lowercase letters.", lambda pwd: pwd == 'YErffej'),
        ("Password must include a number. Try the result of 50 * (4 + 6) - 100 / 2 (hint: 45_)", lambda pwd: pwd == 'YErffej450'),
        ("Password must contain at least one special character.", lambda pwd: pwd.startswith('YErffej450') and any(c in "!@#$%^&*()-_+=" for c in pwd)),
        ("Password must include the answer to this riddle: What has keys but can't open locks? (hint: a hacker's daily tool)", lambda pwd: pwd.startswith('YErffej450') and any(c in "!@#$%^&*()-_+=" for c in pwd) and 'keyboard' in pwd.lower()),
        ("Password must include the Roman numeral for 99 (answer: X_IX)", lambda pwd: pwd.startswith('YErffej450') and any(c in "!@#$%^&*()-_+=" for c in pwd) and 'keyboard' in pwd.lower() and 'XCIX' in pwd.upper()),
        ("Password has been detected to have a word with the binary 01100011 01100001 01110100", lambda pwd: 'cat' in pwd.lower() and any(c in "!@#$%^&*()-_+=" for c in pwd) and pwd.startswith('YErffej450') and 'keyboard' in pwd.lower() and 'XCIX' in pwd.upper() and 'cat' in pwd.lower())
    ]

    $ password = ""
    $ rule_index = 0

    while rule_index < len(rules):
        $ current_rule = rules[rule_index][0]
        "[current_rule]"

        python:
            style.input.color = "#ffffff"
            password = renpy.input("", default=password, length=32, screen="passcrack")
            password = password.strip()

        # Validate password against the current rule only
        python:
            valid = rules[rule_index][1](password)

        if valid:
            # Check if we're at the last rule
            if rule_index == len(rules) - 1:
                jump ending
            else:
                "Good job! You're closer to cracking it."
                $ rule_index += 1
        else:
            "Wrong password. Please try again."
            "[current_rule]"

    return

label ending:

    "SUCCESS !! You have now successfully reveal that Jeffrey is the one behind of all this."
    "With all the evidence in hand, you face a critical choice."

    menu:
        "Publish the Story":
            jump publish_story
        "Blackmail for Personal Gain":
            jump blackmail
        

label publish_story:
    scene bg news
    "After weeks of gathering evidence, you publish the story together with Cathy, which quickly gained national attention."
    "The criminals are arrested and convicted, bringing long-overdue justice."
    scene bg fireworks
    "You are honored for your bravery in uncovering the truth."

    "People celebrate your bravery with fireworks lighting up the sky, and you're hailed as a hero."

    "You enjoy the spotlight, but life becomes less private. Everyone recognizes you."

    jump start

label blackmail:
    scene bg blackmail
    "Instead of going public, you confront the criminals with evidence."
    "They pay you one million dollars to keep quiet. The public remains unaware."
    scene bg vacation
    "You use the money for a luxurious vacation on a remote island, enjoying life."
    scene bg danger
    "However, your peace is short-lived. The criminals you blackmailed seek revenge, putting your life in danger."

    jump start

