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
    return


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
