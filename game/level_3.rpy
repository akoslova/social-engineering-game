label investigation:
    "Your mission to infiltrate the shadows of the Crimson Group begins now. Armed with nothing but your wits and a powerful determination, you face your first decision. How will you embark on this perilous journey?"

    menu:
        " Visit the Crimson Group's official website."
            jump official_website
        "Search for news articles and reports on the Crimson Group."
            jump news_articles
        "Delve into forums and online discussions about mercenaries."
            jump online_discussion
        "Sift through social media for mentions of the Crimson Group."
            jump social_media

label official_webiste:

    #BG: Laptop Screen Crimson Group Website

    "You navigate to the Crimson Group's website, greeted by their bold slogan: 'In the Shadows, We Forge Your Peace'. "
    "The site is sleek, with a carousel of images showcasing anonymous soldiers in action, underscoring their message of strength and reliability. However, detailed information about their operatives remains elusive."
    menu:
        "Examine their service offerings more closely."
            jump service_offering
        "Look for any mention of specific operations or case studies."
            jump specific_operations
        " Search for contact information or office locations."
            jump office_location

label service_offering:

    #BG: Laptop Screen and Service offering page

    "You delve into the descriptions of their services, ranging from high-risk protection details to strategic military consulting. 
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


label news_articles:

    #BG: Laptop screen and artciles

    "Your search uncovers a mix of investigative reports and opinion pieces. "
    menu:
        "Follow up on the sources quoted in the articles."
            jump sources_quoted
        "Look for any dissenting opinions or exposes."
            jump exposes
        " Check the comment sections for insider insights."
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
        "Engage with users to fish for more information."
            jump more_info
        "Pretend to be interested in hiring to provoke responses."
            jump provoke
        "Search for any leaked information or disgruntled postings."
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
        "Dive deeper into the profiles of these mercenaries."
            jump dive_deeper
        "Gather information on their past missions."
            jump gather_info
        "Look for any personal grievances or vulnerabilities."
            jump personal

label dive_deeper:

    #BG: Mobile Screen with instagram

    "You decide to focus on the personal profiles of Jack Morrison, Patrick Hardman, Marcus Johnson, and Sophia Chen. This approach reveals a treasure trove of information about each mercenary:"

    menu:
        "Examine their social media activity for personal details and professional hints."
            jump personal_details
        "Analyze the content they've liked, shared, or commented on for subtle insights."
            jump analyze
        "Focus on the relationships and connections mentioned in their profiles."
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





