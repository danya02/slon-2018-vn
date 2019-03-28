define m = Character("Tom", color="#00ff00")  # MC
define c = Character("Simon", color="#0000ff")  # creator
define h = Character("Mitch",color="#ff00ff")  # helper of creator
define l = Character("Reginald Johnson", color="#ff0000")  # leader of city
define g = Character("GF (TODO: set name!!)", color="#ff8080")  # MC's GF
define a = Character("ATLAS", color="#ffffff", what_font="pixeldroidMenuRegular.ttf", what_size=36, what_color="#00ff00")  # AI
define todo = Character("TODO:",color="#ff0000",what_color="#ff0000",what_prefix="TODO: ")  # todo items

init python:
    went_to_expo = False
    saw_ai_intro = False
    saw_maze_rooms = [False,False,False,False,False,False,False]
    maze_redcount=0
    maze_greencount=0
    maze_bluecount=0
    maze_yellowcount=0
    maze_magentacount=0
    maze_lightbluecount=0
    maze_blackcount=0
    def ai_say(what, redness=0):
        green=min(1.0, 2-(redness*2))
        green=green*255
        green = int(green)
        green = hex(green)[2:]
        green = '0'+green if len(green)==1 else green
        red=str(hex(int(min(1.0, (redness*2))*255))[2:])
        red = '0'+red if len(red)==1 else red
        a.what_args.update({'color':"#"+red+green+"00"})
        a(str(what))

label start:
    jump introduce_expo
    return

label introduce_expo:
    g "I want you to go to expo!"
    menu:
        "Do I want to go?"
        "Yes.":
            $ went_to_expo = True
            jump expo_start
        "No.":
            jump expo_bypass

label expo_start:
    "We're at the expo."
    g "I want to go to product launch!"
    menu:
        "Want to go to product launch?"
        "Yes.":
            $ saw_ai_intro = True
            jump expo_ai_intro
        "No.":
            jump expo_no_ai_intro

label expo_ai_intro:
    "I agreed to go to the product launch, but I went home before GF."
    jump gf_goes_to_city
label expo_no_ai_intro:
    "I decided not to go to the product launch, and I went home without GF."
    jump gf_goes_to_city

label expo_bypass:
    "I decided to stay at home."
    jump gf_goes_to_city


label gf_goes_to_city:
    g "I'm going to THE CITY!"
    if saw_ai_intro:
        g "You know how interesting it is, you've been at the intro."
    else:
        g "At the expo, there was a product launch, and it turned out to be AI."
        g "And the demos have started recently!"
    menu:
        g "Would you like to go with me?"
        "Yes.":
            jump going_to_city_with_gf
        "No.":
            jump stay_at_home_gf_is_away

label going_to_city_with_gf:
    "And so, we went to THE CITY with GF."
    "Soon, we are attacked by AI."
    jump ai_consumes_withgf
    return

label stay_at_home_gf_is_away:
    "I stay at home while the GF is in the city."
    "I lose contact with her, and the social media looks weird."
    menu:
        "Should I investigate?"
        "Yes.":
            jump investigate_city_or_home
        "No.":
            jump stay_at_home_forever

label investigate_city_or_home:
    menu:
        "How shall I investigate?"
        "Visit the city.":
            jump go_to_city_alone
        "Seek help here.":
            jump stay_home_investigate

label stay_at_home_forever:
    "I wait at home without doing anything."
    "The TV tells me of trouble as I am taken away."
    jump ai_consumes_alone

label go_to_city_alone:
    "I go to THE CITY, where I am attacked by AI. One of the controlled people is my GF."
    jump ai_consumes_versusgf

label stay_home_investigate:
    "I start looking for things that can help me here, and I reach the mayor of THE CITY."
    todo "Port prose over from original project!"
    jump maze_entrance


label maze_entrance:
    "We are in a green room, and a single green corridor is leading out of it."
    "Going through it, we are in a green room, with a light-blue and yellow exit."
    menu:
        "Where should I go?"
        "Light-blue.":
            call maze_lightbluepath
            jump maze_r1
        "Yellow.":
            call maze_yellowpath
            jump maze_r2

label maze_redpath:
    $ maze_redcount+=1
    if maze_redcount==1:
        "We are going along the red path."
        c "Some info about this color."
    elif maze_redcount==2:
        c "Some more info about this color."
    elif maze_redcount==3:
        c "Yet some more info about this color."
    elif maze_redcount==4:
        c "Final info about this color. That's all I know."
    return
label maze_greenpath:
    $ maze_greencount+=1
    if maze_greencount==1:
        "We are going along the green path."
        c "Some info about this color."
    elif maze_greencount==2:
        c "Some more info about this color."
    elif maze_greencount==3:
        c "Yet some more info about this color."
    elif maze_greencount==4:
        c "Final info about this color. That's all I know."
    return

label maze_bluepath:
    $ maze_bluecount+=1
    if maze_bluecount==1:
        "We are going along the blue path."
        c "Some info about this color."
    elif maze_bluecount==2:
        c "Some more info about this color."
    elif maze_bluecount==3:
        c "Yet some more info about this color."
    elif maze_bluecount==4:
        c "Final info about this color. That's all I know."
    return

label maze_magentapath:
    $ maze_magentacount+=1
    if maze_magentacount==1:
        "We are going along the magenta path."
        c "Some info about this color."
    elif maze_magentacount==2:
        c "Some more info about this color."
    elif maze_magentacount==3:
        c "Yet some more info about this color."
    elif maze_magentacount==4:
        c "Final info about this color. That's all I know."
    return

label maze_yellowpath:
    $ maze_yellowcount+=1
    if maze_yellowcount==1:
        "We are going along the yellow path."
        c "Some info about this color."
    elif maze_yellowcount==2:
        c "Some more info about this color."
    elif maze_yellowcount==3:
        c "Yet some more info about this color."
    elif maze_yellowcount==4:
        c "Final info about this color. That's all I know."
    return

label maze_lightbluepath:
    $ maze_lightbluecount+=1
    if maze_lightbluecount==1:
        "We are going along the light-blue path."
    elif maze_lightbluecount==2:
        c "Some more info about this color."
    elif maze_lightbluecount==3:
        c "Yet some more info about this color."
    elif maze_lightbluecount==4:
        c "Final info about this color. That's all I know."
    return

label maze_blackpath:
    $ maze_blackcount+=1
    if maze_blackcount==1:
        "The corridor is very dark."
        "The only thing preventing us from stumbling into walls are the tiny indicator lights here and there on the walls."
        c "It is pitch black. You are likely to be eaten by a grue."
        m "W-what?!"
        c "Oh, just a quote from an old video game, don't worry about it."
        "He doesn't appear to be too bothered..."
    elif maze_blackcount==2:
        m "Hey Simon, why are these corridors so dark?"
        c "What do you mean?"
        c "It's not that dark, you can see the walls all right."
        m "Well, yeah, but all of the other rooms were brightly lit with their own color -- why aren't these?"
        c "Ah well, these are probably just backup channels."
        c "You see, the other corridors and rooms are colored according to their purpose, and these ones might not have a defined purpose yet."
        c "Although..."
        "He looks at a group of indicator lights intently."
        c "Actually no, this is live! This is one of the green corridors!"
        m "So... what does this mean?"
        "Simon is fiddling with his watch."
        c "It means ALTAS has deliberately turned off the lights here!"
        c "That's a huge problem!"
        m "Is ATLAS trying to stop us this way?"
        c "Evidently..."
        c "Ah, nevermind. We can still progress, even with the lights off."
        c "As they say, it's not very effective."
    elif maze_blackcount==3:
        "..."
        "..."
        "..."
        # TODO: add fade to black, fade music to silence
        c "DARK{p=2}DARKER{p=2}YET DARKER{w=3}{nw}"
        c "THE DARKNESS{w=2} KEEPS GROWING{w=3}{nw}"
        c "THE SHADOWS{w=2} CUTTING DEEPER{w=3}{nw}"
        c "PHOTON READINGS{w=2} NEGATIVE{w=3}{nw}"
        c "THIS NEXT EXPERIMENT{p=2}SEEMS VERY{p=2}VERY{p=2}INTERESTING"
        c "..."
        # TODO: add sudden background image, character visual
        c "What do you think?"
        m "What are you talking about?!"
        c "Oh, that's another reference. I thought you knew where this one was from?"
        m "D-don't do that anymore, that's creepy!"
        c "Oh, I'm sorry... I just thought this was getting boring."
        c "Plus, I wouldn't have any other opportunity to use it."
        "Is he actually having fun?!..."

    elif maze_blackcount==4:
        m "Hey, can't we just turn the lights on?"
        m "I'm getting tired of these dark corridors with nothing in them."
        c "I'm sorry, I'm afraid that's impossible."
        c "One of the designers of this maintenance section thought it would be a good idea to make all the lighting in here depend on ATLAS."
        c "The idea was, ATLAS was supposed to agree to be maintained, so the lights would have to be on whenever anyone went here, and otherwise off."
        c "But now that ATLAS is not in an agreeable mood, this is a little bit of a problem."
        c "Not too much problem, mind you; we can still walk around here fine."
        c "But it does mean that we will have to be more persuasive when we meet ATLAS again."
        "I don't like the sound of this..."
    return


label maze_r1:
    "We are in a light-blue room. There are light-blue, blue and black exits."
    menu:
        "Where should I go?"
        "Light-blue.":
            call maze_lightbluepath
            jump maze_entrance
        "Blue.":
            call maze_bluepath
            jump maze_r5
        "Black.":
            call maze_blackpath
            jump maze_r6


label maze_r2:
    "We are in a yellow room. There are yellow, red and green exits."
    menu:
        "Where should I go?"
        "Yellow.":
            call maze_yellowpath
            jump maze_entrance
        "Red.":
            call maze_redpath
            jump maze_r2
        "Green.":
            call maze_greenpath
            jump maze_r6

label maze_r3:
    "We are in a blue room. There is a blue and a red exit."
    menu:
        "Where should I go?"
        "Blue.":
            call maze_bluepath
            jump maze_r5
        "Red.":
            jump maze_redfinal

label maze_r4:
    "We are in a red room. There is a red and a black exit."
    menu:
        "Where should I go?"
        "Red.":
            call maze_redpath
            jump maze_r2
        "Black.":
            call maze_blackpath
            jump maze_r5

label maze_r5:
    "In the middle of the corridor there is a blue room. There are three blue exits marked 'R', 'L' and 'C', as well as a black exit."
    menu:
        "Where should I go?"
        "R.":
            call maze_bluepath
            jump maze_r3
        "L.":
            call maze_bluepath
            jump maze_r1
        "C.":
            jump maze_bluefinal
        "Black.":
            call maze_blackpath
            jump maze_r4

label maze_r6:
    "In the middle of the corridor there is a green room. There are two green exits marked 'R' and 'L' and a black exit."
    menu:
        "Where should I go?"
        "R.":
            jump maze_greenfinal
        "L.":
            call maze_greenpath
            jump maze_r2
        "Black.":
            call maze_blackpath
            jump maze_r1

label maze_redfinal:
    c "I think we are nearing the target."
    jump ai_disabled_by_white_room
label maze_greenfinal:
    c "I think we are nearing the target."
    jump ai_disabled_by_white_room
label maze_bluefinal:
    c "I think we are nearing the target."
    jump ai_disabled_by_white_room

label ai_disabled_by_white_room:
    "We are in a white room."

label ai_consumes_alone:
    "The AI does a thing, and now I can't control myself."
    "{b}Bad Ending.{/b}"
    return

label ai_consumes_withgf:
    "The AI does a thing on me and GF, and now we can't control ourselves."
    "{b}Bad Ending.{/b}"
    return

label ai_consumes_versusgf:
    "The AI does a thing, performed by GF, and now I can't control myself."
    "{b}Bad Ending.{/b}"
    return






label tests:
    
    show simon rigs null
    with dissolve
    "Test!"
    show simon smiling
    with dissolve
    m "This is MC speaking."
    c "This is the creator speaking."
    h "This is the helper speaking."
    l "This is the leader speaking."
    python:
        for i in range(11):
            ai_say('This is AI speaking with redness '+str(i/10.0)+'.',i/10.0)
    g "This is the GF speaking."

    return
