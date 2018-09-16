define m = Character("Tom", color="#00ff00")  # PoV+narrator
define c = Character("Simon", color="#0000ff")  # creator
define h = Character("Mitch",color="#ff00ff")  # helper of creator
define l = Character("Reginald Johnson", color="#ff0000")  # leader of city
define a = Character("ATLAS", color="#ffffff", what_font="pixeldroidMenuRegular.ttf", what_size=36, what_color="#00ff00")  # AI
define todo = Character("TODO:",color="#ff0000",what_color="#ff0000",what_prefix="TODO: ")  # todo items

label start:
    todo "Port prose over from original project!"
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
    $ a.what_args.update({'color':"#00ff00"})
    a "This is AI speaking."
    $ a.what_args.update({'color':"#ff0000"})
    a "This is AI speaking after color change."

    return
