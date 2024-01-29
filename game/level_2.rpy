$ renpy.include("inventory.rpy")

define p3 = Character(_("Me"), color="#c8c8ff")
define cathy2 = Character(_("Cathy"), color="#6fd066")

label level_2:# [At home, Player with phone]
    "You decide to call Cathy and update her on your findings"
    p3 "Hey Cathy, I found out about a secret meeting at the annual charity event."
    cathy2 "Great! That means we have to be there and collect some evidence for my story!"
    p3 "This will be impossible, I know that they have a guest list, we can’t just show up!"
    cathy2 "I have a plan. As a journalist, I can go there without an invitation because they like it when the press reports on their generous charity event." 
    cathy2 "I will steal some catering clothes and hide them outside for you." 


