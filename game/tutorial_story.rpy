$ renpy.include("inventory.rpy")

# Declare characters used by this game.
define r = Character(_("Receptionist"), color="#c8ffc8")
define t = Character(_("Toni"), color ="#ffffff")
define p = Character(_("Me"), color="#c8c8ff")
define c = Character(_("Cathy"), color="#000000")
image bg reception="reception.png"
image bg office="bg office.jpeg"
image Receptionist="receptionist.png"
image Toni="tony.png"
image Toni smile="tony_smile.png"
image Toni wave="tony_wave.png"
image Me="playermale.png"
label tutorial:

    call inventory

    # scene bg entryhall 

    scene bg reception
    show Receptionist 
    show Me 
    r "Good morning. Are you new here? What’s your name?"

    #Name Input

    p "Yes, it’s my first day here."

    r "Nice to meet you ___! I will call Toni to tell you that you are here. He will do the onboarding with you."

    scene bg office

    show Toni
    show Me 

    t "Hey there, welcome to the team!"
    t "I am Toni. Today, on your first day at work, I'm going to help you get settled into the company and get to grips with everything."

    #menu: 

    p "Thank you. Nice to meet you!"
    hide Toni
    show Toni smile
    t "If you not already aware: Tasty Food Co. is a global leader in agriculture and nutrition. We utilize the power and provisions of nature to create ingredients and solutions that generate safe, healthy, and sustainable nutrition for people around the world."

    t "Your new job role is pretty awesome. You're our go-to person for keeping our computer systems super secure. Think of it as being a detective for our computers. You're on the lookout for any weak spots that could be trouble."
    
    t "We're thrilled to have you on board, making sure our company's network is strong and ready for anything. Ready to dive into it? Let's do this!" 

    t "To help you understand what your job involves, here's a little exercise for you. Write a phishing email to our colleague Frank from the department."

    p "Sounds good, can you give me more information about Frank?"

    t "Frank is married, has two children and a cat named Lucy. In his free time, he enjoys cycling and hiking. That’s all I personally know."

    p "Great Thanks"

    t "Here on the page you will also find your tasks afterwards" #Highlight Notebook Icon

    #Notebook Action 

    scene bg office
    show Toni wave
    show Me 

    t "Here is your work laptop, everything is already set up for you. I now have to leave you for today. I will be in an important conference for the rest of the day. See you tomorrow!"

    p "All right then I'll get started. See you!"

    scene laptop email
    #Phishing Mail just as text or visuell?

    scene laptop top secret

    #clicking on screen

    "When I remeber correctly then most common used passwords are 123456, password and qwerty. I could just try them out"

    
    menu:

        "Lets try 123456":

            jump wrong

        "Maybe password.":

            jump wrong

        "Could be qwerty":

            jump right

label wrong:

    "Wrong Password! I should try an alternative"

    #Go back to menu?

label right:

    "That worked! Ok what is this?"

    #Show PDF Top Secret Document

    
    menu:

        "Download File and save on a USB drive":
            jump evidence

        "Print out the file":
            jump evidence

        "Close the application and try forgetting about its not your business":
            jump no_evidence

        #Choice has impact later ... remember choice??


label evidence:

    #transition Black

    "5 PM Closing Time… My First Day at Work is finished and I leave the place hasty, to get to the appointment with my friend Cathy in time."

    "I'm just glad I'm meeting Cathy tonight and hopefully with her help I can make a plan of what to do. I think I might be in trouble …"

    scene bg coffee

    "As I am walking towards the bar/café I can not get this information out of my head, is there something illegal going on at my new working place. I feel really terrible because of (choice1-3). taking a document with me/not securing any evidence"
    # fill in the chosen choice

    show friend Cathy

    c "Hey I hope you had a nice first day at work. You look a bit stressed. Did everything go well?"

    p "No not at all I mean at first it went well. Toni was showing me around, but then I discovered some alarming information. Some parts were even blacked out. And then I chose to make a copy of it. I mean what should I do?"

    c "Ok, slow down I think you did the right thing there"

    c "Maybe you're on to something big. Can I have a look at your evidence/notes? I might be able to write a story about it. What do you think?"

    p "Surely this will not be easy?"

    c "Hm, I might need more Information. I will contact you on that matter! Do you have my new number already If not maybe you should write it in your Notebook"

    #Notebook interaction

    #Transition/Finish scene in Coffee shop

label no_evidence:

    #transition Black

    "5 PM Closing Time… My First Day at Work is finished and I leave the place hasty, to get to the appointment with my friend Cathy in time."

    "I'm just glad I'm meeting Cathy tonight and hopefully with her help I can make a plan of what to do. I think I might be in trouble …"

    scene bg coffee

    "As I am walking towards the bar/café I can not get this information out of my head, is there something illegal going on at my new working place. I feel really terrible because of (choice1-3). taking a document with me/not securing any evidence"
    # fill in the chosen choice

    show friend Cathy

    c "Hey I hope you had a nice first day at work. You look a bit stressed. Did everything go well?"

    p "No not at all I mean at first it went well. Toni was showing me around, but then I discovered some alarming information. Some parts were even blacked out. And then I tried forgetting about it because i dont want to get in trouble. I mean what should I have done?"

    c " Ok slow down, Without ayn evidence... Wait are you trying to make a fool out of me?"

    p "No, really not, I swear on our friendship"

    #menu

    c "Can you remember something? What was mentioned or something else?"

    "I remember reading about Forest clearance and Farmer strikes"
        
    "I think there was the mentioning of avocados"

    "I read the word classified"

    "I remember something about having a surprise birthday party for the head of the department"

    # solution to not use label

    c "Maybe you're on to something big. Can I have a look at your evidence/notes? I might be able to write a story about it. What do you think?"

    p "Surely this will not be easy?"

    c "Hm, I might need more Information. I will contact you on that matter! Do you have my new number already If not maybe you should write it in your Notebook"

    #Notebook interaction

    #Transition/Finish scene in Coffee shop

label next_day:

    scene bg phone_message

    "Hey, I found out by using your given information that … company might be involved as well. Do you think you could get information from them? Their Building is in (Address) I marked it on this Map. I wish you luck and keep me updated!"

    #Notebook Map is introduced