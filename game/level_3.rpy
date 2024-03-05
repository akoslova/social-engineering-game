$ renpy.include("inventory.rpy")
$ renpy.include("tutorial_story.rpy")
$ renpy.include("level_1.rpy")
<<<<<<< Updated upstream
=======

define ph = Character (_("Patric Hardman"), color="#3939f5")


label investigation:
    "Your mission to infiltrate the shadows of the Crimson Group begins now. Armed with nothing but your wits and a powerful determination, you face your first decision. How will you embark on this perilous journey?"
>>>>>>> Stashed changes

define ph = Character (_("Patric Hardman"), color="#3939f5")

#...

#scene homeoffice/desk

#show player character with phone

label level_3:
    call inventory
    
label pretexting:

    "As the phishing mail failed to bear any results you decide to give pretexting a try. With the information from the website and the secondary research about the mercenary hardman
    at hand you try calling the office of Crimson. You set up a voice changer and proceed to call your target."

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








#scene homeoffice/desk

#show player character with phone

label level_3:
    call inventory
    
label pretexting:

    "As the phishing mail failed to bear any results you decide to give pretexting a try. With the information from the website and the secondary research about the mercenary hardman
    at hand you try calling the office of Crimson. You set up a voice changer and proceed to call your target."

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



