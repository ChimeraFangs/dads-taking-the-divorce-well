# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.


define n = Character("The Narrator")
define j = Character("Jonah Peskadito")
define cas = Character("Caspian")

default game_win = False
default ring_caught = 0
default fish_caught = 0

# The game starts here.


label start:
    n "Jonah Peskadito had thought he'd lost everything."  
    n "Kids, a wife. Even a high-paying job in the city."
    n "How could he risk it all, you ask?"
    n "Simply because he didn't feel right. How could he when he's in a landlocked city?"
    n "Not where he's meant to be."
   
    scene bg_seaside


    n "Jonah was born and raised by the sea, a small fishing town. His father first taught him how to fish when he was 7."
    n "Since then? He's been in love with the sea, considers it his first love."
    n "He worked as a fisherman since he was 17 despite the heavy labor. That is.. "
    n "Until he met his ex-wife, Brenda or 'Brendita' as he liked to call her."
    n "She was a very..."


    menu:
        "Modern?":
            n "Yes! A very modern woman."
            n "Fishlandia was not her style, no, not at all."
            n "Where Jonah prefered the natural earth, she prefered concrete and tech."
            n "It's the main reason for the divorce."
        "Ambitious?":
            n "Yes! An incredibly ambitious woman!"
            n "She would constantly talk about wanting to leave their home city."
            n "Thought it would make her happy, the both of them happy."
   
    n "Yet, it made Jonah miserable. He hated the loud noise, the constant nagging of his job."
    n "Brenda realized this, told him he should follow his heart, even if it wasn't with her."
    n "The city was her home, but it was merely Jonah's house."
    n "The sea roared his name."
    n "Everyone knows how unpredictable it can be."
    scene black

    "DAY 0"

    scene bg_home 
    n "The day starts early for a fisherman like himself."
    j "Holy carp! The day is beautiful. Surely, this marks a good day!"
    j "Time to get fishin!"
    scene bg_docks
    n "Waves crash against the beams holding the dock up. Peace and quiet, his favorite sound."

    show fishingrod at left

    $ slider.start(speed=10,jump_win="win_label", jump_lose="lose_label")

    if has_collided == True:
        jump win_label
    elif has_collided == False:
        jump lose_label
        

    label lose_label:
        "You caught a fish... somehow..."
        show shrm_cat at slightright
        "It's a shrimp cat! It came back out of pity!"
        jump first_fish_done

    label win_label:
        "You caught a fish!"
        show shrm_cat at slightright
        "It's a shrimp cat!"
        jump first_fish_done
        
    
    label first_fish_done:
        hide shrm_cat
        j "One more!"

    $ slider.start(speed=20,jump_win="win_label2", jump_lose="lose_label2")
    
    if has_collided == True:
        jump win_label2
    elif has_collided == False:
        jump lose_label2
        

    label lose_label2:
        "Something bit, but ran away!"
        jump second_fish_done

    label win_label2:
        "You caught a fish!"
        show bussiness_fiss at slightright
        "It's a business fish!"
        jump second_fish_done
        
    label second_fish_done:
        hide bussiness_fiss
        j "There must be better!"

    $ slider.start(speed=30,jump_win="win_label3", jump_lose="lose_label3")

    if has_collided == True:
        jump win_label3
    elif has_collided == False:
        jump lose_label3
    label win_label3:
        "Something bit!"
        $ slider.start(speed=100,jump_win="win_labelcas", jump_lose="lose_labelcas")
        if has_collided == True:
            jump win_labelcas
        elif has_collided == False:
            jump lose_labelcas

    label lose_label3:
        "Something bit!"
        $ slider.start(speed=100,jump_win="win_labelcas", jump_lose="lose_labelcas")
        if has_collided == True:
            jump win_labelcas
        elif has_collided == False:
            jump lose_labelcas
        

    label lose_labelcas:
        "Something bit, and is..."
        "Pulling back!"
        jump fishuhman

    label win_labelcas:
        "Something bit, and is..."
        "Pulling back!"
        jump fishuhman
    
        
    label fishuhman:
        scene bg_underwater
        j "The waves..! They're swallowing me whole!"
        j "Need.. to.."
        scene black
        cas "Hhello...blub blub?"
        cas "Oh dear..."
        cas "I might have to eat this one..."
        "SHAKE SHAKE"
        j "HUAH..CHK!"
        scene cas_first_appearance
        cas "Maybe I won't have to eat you... fisher."
        j "What the.. what.. what are you!"
        cas "Thats rude, isn't it?"
        cas "I just saved you."
        scene bg_beach
        show fishuh_smile
        j "You.. You did?"
        cas "Mhmm.."
        j "I.. I don't know how to thank you, I owe you my lif-"
        cas "I know how."
        j "I- what."
        cas "Feed me."
        j "What... what do I feed you?"
        cas "Well, you're a fisherman, aren't you? Fish, blub blub."
        j "Just.. fish?"
        cas "Mhmmm."
        j "That's easy enough, I suppose..."
        cas "I know you need money, so I will reward you if you feed me (even if you're supposed to be paying back a debt or whatever.)"
        j "Well, deal taken, good fishie of mine!"
        cas "....You humans are so weird."
        n "They shake hands, smiling."
        j "Still... where would I find you?"
        hide fishuh_smile
        show fishuh_think
        cas "Hmmm... right here works. I don't have a lot of energy to swim away anyhow."
        j "I should have a Shrimp Cat!"
        hide fishuh_think
        show fishuh_polite1
        cas "I like those."
        hide fishuh_polite1
        show fishuh_polite2
        n "He gives him the Shrimp Cat!"
        cas "This should be enough to sustain me. But tommorrow I will need three fish."
        j "What if i don't?"
        n "He jokes, not expecting a serious answer."
        hide fishuh_polite2
        show fishuh_scary
        cas "I eat you."
        n "His face falls a little, before grinning nervously."
        j "Yes sir!"
        hide fishuh_scary
        show fishuh_smile
        cas "Mmhmm.. blub blub."
        cas "You can rest up for today."
        j "I'll see you tommorow, dear fishie."
        cas "I have a name... fisherman."
        j "So do I! It's Jonah!"
        cas "Caspian."
        j "Then I'll see you tommorow, dear Caspian!"
        scene black
    
    "DAY 1"
    scene bg_home
    n "Once more does Jonah rise. Ready to fish for his friend."
    n "He'll need bigger fish to keep his new buddy content."
    scene bg_docks
    j "This part of the docks will do!"
    j "Time to get a'fishin!"
    show fishingrod
    $ slider.start(speed=15,jump_win="win_label4", jump_lose="lose_label4")
    if has_collided == True:
        jump win_label4
    elif has_collided == False:
        jump lose_label4
        

    label lose_label4:
        "Somethin' bit, but swam away!"
        jump medium1_fish_done

    label win_label4:
        $ fish_caught += 1
        "You caught a fish!"
        show we_arefiss at slightright
        "It's a symbiote fish!"
        jump medium1_fish_done
        
    
    label medium1_fish_done:
        hide we_arefiss
        j "Another!"
    
    $ slider.start(speed=20,jump_win="win_label5", jump_lose="lose_label5")
    if has_collided == True:
        jump win_label5
    elif has_collided == False:
        jump lose_label5
        

    label lose_label5:
        "Somethin' bit, but swam away!"
        jump medium2_fish_done

    label win_label5:
        $ fish_caught += 1
        "You caught a fish!"
        show bonefish at slightright
        "It's a Bonefish!"
        jump medium2_fish_done
        
    
    label medium2_fish_done:
        hide bonefish
        j "Another!"

    $ slider.start(speed=25,jump_win="win_label6", jump_lose="lose_label6")
    if has_collided == True:
        jump win_label6
    elif has_collided == False:
        jump lose_label6
        

    label lose_label6:
        "Somethin' bit, but swam away!"
        jump medium3_fish_done

    label win_label6:
        $ fish_caught += 1
        "You caught a fish!"
        show sunlion at slightright
        "It's a Heliogill!"
        jump medium3_fish_done
        
    
    label medium3_fish_done:
        hide sunlion
        j "There we are!"
        j "I have to call Cas now!"

scene bg_beach
j "Ohhhh...."
j "CASPIANNNN!!!"
show fishuh_smile
n "The merman swims up."
hide fishuh_smile
show fishuh_shock
cas ".....You didn't have to yell that loud."
j "oh."
j "Well, I have your fish!"
hide fishuh_shock
show fishuh_smile
cas "Let me see..."
hide fishuh_smile
if fish_caught >=2:
    show fishuh_smile
    cas "This should be good."
    cas "Thank you, Jonah."
    jump day1_complete
else:
    show fishuh_scary
    cas "Maybe you weren't worth saving."
    j "what..?"
    cas "No matter."
    jump game_over

label game_over:
    scene black
    show text "GAME OVER" at truecenter
    with dissolve
    pause 2.0
    menu:
        "Try Again?":
            jump start 
        "Quit":
            $ renpy.quit() 
    
    label day1_complete:
    j "Your welcome!"
    show fishuh_smile
    cas "Hhmm. As your reward, I'll give you a new fishing rod."
    "You gained another fishing rod!"
    j "This is amazing! Where did you get this??"
    hide fishuh_smile
    show fishuh_think
    cas "Mmh. Found it on the sea floor and fixed it for you."
    n "He can't help but hug him."
    hide fishuh_think
    show fishuh_shockblush
    cas "...!"
    j "You're so kind! I'll be sure to find you bigger fish tomorrow for sure!"
    cas "Yeah... okay."
    j "I'll see you tomorrow?"
    cas "yeah.. okay! blub blub."
    n "He retreats into the ocean, blushing blue."
    scene black
    "DAY 2"
    scene bg_home
    n "Its another day to fish. Jonah is excited to not only use his new fishing rod but to see Caspian!"
    n "He begins making his way to the docks, following his routine."
    scene bg_docks
    j "Now, to use this thing!"
    show fishingrod
    
    $ slider.start(speed=30,jump_win="win_label7", jump_lose="lose_label7")
    if has_collided == True:
        jump win_label7
    elif has_collided == False:
        jump lose_label7
        

    label lose_label7:
        "Something bit, but swam away!"
        jump large1

    label win_label7:
        $ fish_caught += 1
        "You caught a fish!"
        show salmonfuck
        "It's a barbed salmon!"
        jump large1
        
    
    label large1:
        hide salmonfuck
        j "This thing is amazing!"
    
    $ slider.start(speed=35,jump_win="win_label8", jump_lose="lose_label8")
    if has_collided == True:
        jump win_label8
    elif has_collided == False:
        jump lose_label8
        

    label lose_label8:
        "Something bit, but swam away!"
        jump large2

    label win_label8:
        $ fish_caught += 1
        "You caught a fish!"
        show saintfish at slightright
        "It's a Saint Fish!"
        jump large2
        
    
    label large2:
        hide saintfish
        j "Yay!"
    
    $ slider.start(speed=40,jump_win="win_label9", jump_lose="lose_label9")
    if has_collided == True:
        jump win_label9
    elif has_collided == False:
        jump lose_label9
        

    label lose_label9:
        "Something bit, but swam away!"
        jump large3

    label win_label9:
        $ fish_caught += 1
        "You caught a fish!"
        show falseanchor at slightright
        "It's a False Anga!"
        jump large3
        
    
    label large3:
        hide falseanchor
        j "Alright, it's time to call Cas!"

    scene bg_beach
    show fishuh_smile
    j "Oh, Caspian!"
    hide fishuh_smile
    show fishuh_polite2
    cas "Good morning, Jonah."
    j "Good morning!"
    cas "Do you have today's fish?"
    j "I do!"
    hide fishuh_polite2
    show fishuh_polite1
    cas "Wonderful!"
    hide fishuh_polite1
    show fishuh_smile
    j "I even got you bigger fish!"
    cas "That's great! I feel as though I've only gotten hungrier..."
    cas "Let me see..."
hide fishuh_smile
if fish_caught >=4:
    show fishuh_smile
    cas "This should be good."
    cas "Thank you, Jonah."
    jump day2_complete
else:
    show fishuh_scary
    cas "You've disappointed me, Jonah."
    j "what..?"
    cas "No matter."
    jump game_over

    label day2_complete:
    show fishuh_smile
    j "Your welcome!"
    cas "No no, thank you."
    hide fishuh_smile
    show fishuh_scary
    cas "Even though I've threatened you into this..."
    hide fishuh_scary
    show fishuh_confusedblush
    cas "You've been... weirdly nice."
    cas "Not just because i give gifts either."
    hide fishuh_confusedblush
    show fishuh_sad
    cas "Truly, thank you. I won't stay for too long. I'm moving off soon to another part of the sea."
    cas "I figured I would toy with a human, blub blub.."
    cas "But you've been so kind."
    n "For once, Jonah was truly confused."
    j "I mean. S'just how I'd treat anyone else, y'know?"
    cas "And I thank you for that. I'm not exactly... anyone else."
    n "He feels.. strangely sad the sea monster is moving off."
    j "To me, you are."
    show fishuh_shockblush
    cas "...really?"
    j "Yeah! I've thought I was content with just the sea and my routine but... seeing you has been..."

    menu:
        "Amazing?":
            j "Amazing!"
            j "You've been so amazing!"
            j "I never thought I could actually find someone who likes what I do!"
        "Lovely?":
            j "Lovely!"
            j "You've been so lovely!"
            j "You've been so kind even if you're a little scary!"

    cas "Really????"
    j "Yeah!"
    j "I guess what I'm trying to say is that I.. never thought I could actually like interacting with people."
    cas "But you're so... normal and helpful!"
    j "Eh."
    hide fishuh_shockblush
    show fishuh_confused
    cas "EH????"
    cas "But you're so!-"
    hide fishuh_confused
    show fishuh_polite1
    "Y'know???"
    hide fishuh_polite1
    show fishuh_confused
    n "Jonah laughs a bit."
    j "Say, what if I'm so.."
    n "He gestures, giggles a bit."
    j "Can I catch you a final thing tomorrow?"
    show fishuh_think
    pause 1.0
    show fishuh_thinkblush
    cas "Yeah... sure."
    cas "I'll... I'll see you tomorrow."
    j "I'll see you too!"
    scene black
    "DAY 3"
    scene bg_home
    n "Jonah quickly runs to the docks."
    scene bg_docks
    j "One final time, for Caspian! I'll find him something he likes!"
    j "This'll be my hardest catch!"
    show fishingrod
    $ slider.start(speed=58,jump_win="win_labellast", jump_lose="lose_labellast")
    if has_collided == True:
        jump win_label9
    elif has_collided == False:
        jump lose_label9
        

    label lose_labellast:
        "You caught a...!"
        "Nothing?"
        "Oh, no.. you even used your best bait. What will you do?"
        jump lastthing

    label win_labellast:
        "You caught a..."
        show weddingring at slightright
        "WEDDING RING!"
        $ ring_caught += 1
        jump lastthing
        
    
    label lastthing:
        hide falseanchor
        j "I'll have to tell him how I feel!"
        n "Jonah runs the best he can to the beach"
        scene bg_beach
        if ring_caught >=1:
            jump wedding
        else: 
            jump bad_end

        label wedding:
            show fishuh_sad
            cas "Good evening, Jonah.."
            n "Jonah heaves, smiling at the very sight of him."
            show fishuh_think
            cas "Woah! Are you okay!"
            j "Yes! Yes! More than okay!"
            hide fishuh_think
            show fishuh_smile
            cas "How so?"
            j "Means I didn't miss you."
            show fishuh_shockblush
            cas "..!"
            n "Jonah gets down on one knee."
            j "I just wanted to tell you."
            j "You're a wonderful guy and I'd love to marry you!"
            hide fishuh_shockblush
            show fishuh_confusedblush
            cas "Marry?"
            j "Yes!"
            j "Marry!"
            cas "What is that?"
            n "This catches Jonah off guard, and he laughs."
            show fishuh_confused
            cas "What's so funny?"
            j "No, I just-"
            j "I should've known. It's a human thing. Where you swear to be eachothers?"
            cas "Mating?"
            j "WOaah- woah woah----!"
            j "It usually takes a lot of time but.. I just really like you so..."
            cas "Explain this marriage more to me..."
            scene black
            pause 1.0
            cas "I see... Yes.. yes.. Too soon..."
            scene bg_beach
            show fishuh_smile
            j "So, uhm. Maybe this can just be a sign of... being something? I don't know..."
            cas "Mates."
            j "I guess???"
            n "He laughs, flustered."
            n "Jonah jumps as Caspian reaches out to take and put on the ring."
            show fishuh_thinkblush
            j "You--"
            cas "I must admit, I'm rather.. confused. But I'd like to understand things more with you."
            j "Really?"
            cas "Mhm. Though I'd like if we pretended to be married. I like this concept, blub blub."
            scene black
            show marriedlol
            pause 1.5
            n "And so they did."
            n "Wouldn't you know it.. Blue blushes too."
        return

        label bad_end:
            scene bg_beach
            n "He makes it to the beach..."
            n "Far too late."
            n "He looks at the seaside. Alone, again."
return