$ renpy.include("inventory.rpy")
$ renpy.include("tutorial_story.rpy")
$ renpy.include("level_1.rpy")

define ph = Character (_("Patric Hardman"), color="#3939f5")

#...

#scene homeoffice/desk

#show player character with phone

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

    sec "thanks for you as well."

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

        "I am calling because my Ex husband forgot again to pay for his son's tutor sessions":
            jump tn_op1
        
        ""

label alexander:

label doctor_dale:

label phising_lvl3:
    "You decide to try your luck by writing a phishing email to all the employees from the Crimson Group."
    "Task: Arrange the email snippets to create an effective phishing email "

    #Minigame Email

label notsuccessful: 
    "Unfortunately, none of the mercenaries fell for your phishing email. Try again. "
label successful: 
    "Transition next day…"
    "Jack Morrison clicked on your link. Now you have access to his computer."



