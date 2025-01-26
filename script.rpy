# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kalevi")
define h = Character("Hollo", color="#ee7433")
define m = Character("Martta", color="#ad30df")
define hm = Character("Martta & Hollo", color="#ffffff")

default piipertajaCount = 0
default points = 0

default piipertaja1_visible = True
default piipertaja2_visible = True

default piipertaja3_visible = True
default piipertaja4_visible = True
default piipertaja5_visible = True

default piipertaja6_visible = True
default piipertaja7_visible = True

# The game starts here.

label splashscreen:
    $ renpy.movie_cutscene("lopullinenalku.mpg")
    return

label start:

####### STYLES
    style big_red:
        size 40
        color "#f00"

    style big_white:
        size 40
        color "#ffffff"



####### TRANSFORM
    transform highlight:
        alpha 1.0  # Täysin kirkas
        linear 0.2  # Animoi muutosta 0.2 sekuntia

    transform dim:
        alpha 0.5  # Puoliksi tummennettu
        linear 0.2

    transform button_opacity:
        alpha 0.15  # Normaali tila (läpinäkyvä)

    transform button_visible:
        alpha 1.0  # Hover-tila (täysin näkyvä)

    transform small_button:
        zoom 0.1  # Skaalaa 50 % alkuperäisestä
    


####### SCREENS
    screen found_piipertaja:
        text "Piipertäjä löydetty!" style "big_red":
            xalign 0.5
            yalign 0.25
            textalign 0.5 
        timer 3.5 action [Hide("found_piipertaja")]

    screen count_piipertaja:
        text "Piipertäjiä löydetty: [piipertajaCount]" style "big_red"

    screen bridge:
        text "Piipertäjiä löydetty: [piipertajaCount]" style "big_red"
        if piipertaja1_visible:
            imagebutton:
                xpos 0.6
                ypos 0.55     
                idle "kuplapiip1.png"
                activate_sound ("pii1.mp3")
                # action [Show("found_piipertaja"), IncrementVariable("piipertajaCount"), Return("continueWithPiipertaja"), Hide()]
                # action [IncrementVariable("piipertajaCount"), Return("continueWithPiipertaja"), Hide()]
                action [Show("found_piipertaja"), IncrementVariable("piipertajaCount"), SetVariable("piipertaja1_visible", False)]
                at button_opacity, small_button
        if piipertaja2_visible:
            imagebutton:
                xpos 0.05
                ypos 0.35     
                idle "kuplapiip2.png"
                activate_sound ("mii2.mp3")
                action [Show("found_piipertaja"), IncrementVariable("piipertajaCount"), SetVariable("piipertaja2_visible", False)]
                at button_opacity, small_button
        textbutton "Siirry eteenpäin" style "big_white":
            xpos 0.75 ypos 0.90
            action Return("continueGame")

    screen forestPath:
        text "Piipertäjiä löydetty: [piipertajaCount]" style "big_red"
        if piipertaja3_visible:
            imagebutton:
                xpos 0.75
                ypos 0.40     
                idle "kuplapiip2.png"
                activate_sound ("mii3.mp3")
                # action [Show("found_piipertaja"), IncrementVariable("piipertajaCount"), Return("continueWithPiipertaja"), Hide()]
                # action [IncrementVariable("piipertajaCount"), Return("continueWithPiipertaja"), Hide()]
                action [Show("found_piipertaja"), IncrementVariable("piipertajaCount"), SetVariable("piipertaja3_visible", False)]
                at button_opacity, small_button
        if piipertaja4_visible:
            imagebutton:
                xpos 0.05
                ypos 0.35     
                idle "kuplapiip3.png"
                activate_sound ("pii1.mp3")
                action [Show("found_piipertaja"), IncrementVariable("piipertajaCount"), SetVariable("piipertaja4_visible", False)]
                at button_opacity, small_button
        if piipertaja5_visible:
            imagebutton:
                xpos 0.20
                ypos 0.80     
                idle "kuplapiip1.png"
                activate_sound ("mii2.mp3")
                action [Show("found_piipertaja"), IncrementVariable("piipertajaCount"), SetVariable("piipertaja5_visible", False)]
                at button_opacity, small_button
        textbutton "Siirry eteenpäin" style "big_white":
            xpos 0.75 ypos 0.90
            action Return("continueGame")
        textbutton "Mene taaksepäin" style "big_white":
            xpos 0.05 ypos 0.90
            action Return("goBack")

    screen ruins:
        text "Piipertäjiä löydetty: [piipertajaCount]" style "big_red"
        if piipertaja6_visible:
            imagebutton:
                xpos 0.55
                ypos 0.45     
                idle "kuplapiip1.png"
                activate_sound ("pii1.mp3")
                # action [Show("found_piipertaja"), IncrementVariable("piipertajaCount"), Return("continueWithPiipertaja"), Hide()]
                # action [IncrementVariable("piipertajaCount"), Return("continueWithPiipertaja"), Hide()]
                action [Show("found_piipertaja"), IncrementVariable("piipertajaCount"), SetVariable("piipertaja6_visible", False)]
                at button_opacity, small_button
        if piipertaja7_visible:
            imagebutton:
                xpos 0.21
                ypos 0.74     
                idle "kuplapiip2.png"
                activate_sound ("mii2.mp3")
                action [Show("found_piipertaja"), IncrementVariable("piipertajaCount"), SetVariable("piipertaja7_visible", False)]
                at button_opacity, small_button
        textbutton "Siirry eteenpäin" style "big_white":
            xpos 0.75 ypos 0.90
            action Return("continueGame")
        textbutton "Mene taaksepäin" style "big_white":
            xpos 0.05 ypos 0.90
            action Return("goBack")

    screen ending:
        text "Kansantarinan mukaan jättiläiset Hollo ja Martta rakensivat Hollolan kivikirkon." style "big_white":
            xalign 0.5
            yalign 0.5
            textalign 0.5 

    
####### START
    scene kuva 2

    play music "alkumusa.mp3" loop
    show screen count_piipertaja
    
    k "Karvapiipertäjät ovat tärkeä osa jokapäiväistä elämäämme."
    k "Niiden turkista saa tehtyä lankaa, ne estävät taloja palamasta poroksi ja ne auttavat muissakin arkisissa asioissa."

    scene kuva 3

    k "Mutta yhtenä yönä kammottava jättiläispariskunta Hollo ja Martta varastivat kaikki kylän piipertäjät pistääkseen ne pataan! Oli onni matkassa etteivät he vieneet ihmisiäkin!"
    k "Ehkä juuri siksi olin ainoa joka oli valmis lähtemään pelastamaan piipertäjiä."

    scene kuva 4

    play sound ("piiphata.mp3")
    k "Onneksi jättiläisten säkeissä oli reikiä ja osa piipertäjistä tippui matkan varrelle."
    k "Piipertäjät kuitenkin ovat arkoja otuksia ja ne koittavat vaistomaisesti piiloutua tällaisen koettelemuksen jäljiltä. Ne ovat jopa luoneet ympärilleen suojakuplat."
    k "Jokainen piipertäjä on kylälle elintärkeä, joten minun on löydettävä mahdollisimman moni."
    k "…Ja mielellään ei päätyä piipertäjien seuraksi jättien kitaan."

#### BRIDGE
    scene bg_silta
    play music "silta_bg_musa.mp3" fadeout 1
    show kalevi neutraali
    play sound ("kalevihmmpitka.mp3")

    k "{i}Olen varma että näin ainakin yhden piipertäjän tippuvan jonnekkin näille main, mutta missä se on…?{/i}"

    jump bridge


label bridge:
    scene bg_silta
    play music "silta_bg_musa.mp3" fadeout 1
    hide kalevi_neutraali
    call screen bridge

    $ result = _return
    if result == "continueGame":
        jump forestPath

#### FOREST PATH
label forestPath:
    play music "bg_metsapolku.mp3" fadeout 1
    scene bg_metsapolku
    call screen forestPath

    $ result = _return
    if result == "continueGame":
        jump ruins
    elif result == "goBack":
        jump bridge

#### RUINS
label ruins:
    hide kalevi neutraali
    play music "bg_rauniot.mp3" fadeout 1

    scene bg_rauniot
    call screen ruins

    $ result = _return  

    if result == "continueGame":
        jump cave_entry      
    elif result == "goBack":
        jump forestPath

#### CAVES
label cave_entry:
    scene bg_luolansuu

    play music "luolansuump3.mp3" fadeout 1
    show kalevi neutraali at left

    k "{i}Jos astun jättiläisten luolaan sisään niin sieltä ei ole paluuta ennen kuin asia on selvitetty.{/i}"
    k "{i}Mutta jos aion saada loputkin karvapiipertäjät pelastettua minun on mentävä sinne.{/i}"
    k "{i}Etsinkö metsästä vielä karvapiipertäjiä vai astunko sisälle luolaan?{/i}"

    menu:
        "Mene luolaan":
            jump caves

        "Palaa takaisin":
            jump ruins

label caves:
    scene bg_luoladark

    play music "luola1.mp3" fadeout 1
    queue music "luola2.mp3" loop
    show kalevi yllatys at left, dim
    show hollo neutraali at right, highlight
    play sound ("hollonauru1.mp3")

    h "Ihmisrontio uskaltautuu luolaamme."

    show martta neutraali at center, highlight
    show hollo neutraali at right, dim
    play sound ("marttanauru.mp3")

    m "Hyvä ajoitus, pata olikin jo tulilla. Saamme hitusen tuhdimman aterian."

    show martta neutraali at center, dim
    show kalevi yllatys at left, highlight 

    k "{i}En tahdo tulla syödyksi! Mitä ihmettä minun pitäisi sanoa?{/i}"
    play sound ("kaleviahaa.mp3")
    k "Älkää minua syökö! Olen pahan makuinen!"

    show martta neutraali at center, highlight 
    show kalevi yllatys at left, dim
    play sound ("marttaahaa2.mp3")

    m "Jaa miltä sinä maistut?"

    show martta neutraali at center, dim 
    show kalevi yllatys at left, highlight
    play sound ("kalevihahaa.mp3")

    menu:
        "Happamalta":
            k "Maistun happamalta."
            jump hapan

        "Suolaiselta":
            k "Maistun suolaiselta."
            jump suolainen

        "Makealta":
            k "Maistun makealta."
            jump makea

    label hapan:
        $ points += 1

        show hollo eh at right, highlight
        show kalevi yllatys at left, dim
        play sound ("holloorina1.mp3")
        h "Kuinka happamalta?"

        show kalevi tuskahymy at left, highlight
        show hollo eh at right, dim
        k "Hyvin happamalta"

        show kalevi tuskahymy at left, dim
        show hollo eh at right, highlight
        play sound ("hollotuhahdus.mp3")
        h "Mistä tiedät?"
        jump taste_choice_done

    label suolainen:
        $ points += 2

        show hollo virne at right, highlight
        show kalevi yllatys at left, dim
        play sound ("holloorina4.mp3")
        h "Ihmiset ovat elämäni suola."

        show hollo virne at right, dim
        show martta tsk at center, highlight
        play sound ("marttaahaa2.mp3")
        m "Sinun pitäisi kyllä vähentää suolan kulutusta."
        jump taste_choice_done

    label makea:
        show kalevi yllatys at left, dim
        show martta hymy at center, highlight
        play sound ("marttaahaa2.mp3")
        m "Olet siis täydellinen jälkiruoka."
        jump taste_choice_done

label taste_choice_done:

    show kalevi puhe at left, highlight
    show hollo eh at right, dim
    show martta neutraali at center, dim
    play sound ("kalevihahaa.mp3")
    k "Oottakaas eka yksi pieni juttu! Teidän ei kannata syödä piipertäjiäkään!"

    show kalevi puhe at left, dim
    show martta hymy at center, highlight
    play sound ("marttanauru.mp3")
    m "Miksei muka? Äläkä kehtaa väittää niiden maistuvan pahalta. Me tiedetään kuule kokemuksesta niiden olevan hyviä."

    show martta hymy at center, dim
    show hollo virne at right, highlight
    play sound ("hollonauru2.mp3")
    h "Ne poksahtelevat mukavasti suussa."

    show hollo virne at right, dim
    show kalevi neutraali at left, highlight

    menu:
        "Ne on myrkytetty!":
            $ points += 1
            jump myrkytetty

        "Ne eivät ole tarpeeksi ruokaisia.":
            jump ruokaisa

        "Ne ovat taika-karvapiipertäjiä.":
            $ points += 1
            jump taika

label myrkytetty:
        show martta eh at center, highlight
        show kalevi neutraali at left, dim
        play sound ("marttaaah.mp3")
        m "Myrkytetty?"
        m "Miten? Juotitko niille myrkkyä?"
        play sound ("marttaaah.mp3")
        m "Sinä sairas, sairas, ihminen. Edes me emme tekisi mitään sellaista."

        show martta eh at center, dim
        show hollo pah at right, highlight
        play sound ("hollotuhahdus.mp3")
        h "Kuulostaa keksityltä jutulta. Sitä paitsi kaikkihan tietävät ettei näin pieni määrä myrkkyä riitä kaatamaan isoa jättiläistä."
        jump dont_eat_done

label ruokaisa:
        show kalevi neutraali at left, dim
        show hollo pah at right, highlight
        play sound ("holloorina5.mp3")
        h "…Tuo pitää kyllä paikkaansa. Sattuisitko sattumoisin tietämään mistä löytyisi jotain täyttävämpää?"
        jump ruokaisa_extra

label taika:
        show kalevi neutraali at left, dim
        show martta eh at center, highlight
        play sound ("marttaahaa2.mp3")
        m "Joten niiden syöminen antaa taikavoimia?"

        show hollo eh at right, highlight
        show martta eh at center, dim
        play sound ("holloorina2.mp3")
        h "Vai ovatko ne itse maagisia?"

        show hollo eh at right, dim
        show martta eh at center, highlight
        play sound ("marttaaah.mp3")
        m "Vai onko niiden karvat se maaginen osa? ‘Taika-karva’ piipertäjiä."
        jump dont_eat_done

label ruokaisa_extra:

    show kalevi neutraali at left, highlight
    show hollo pah at right, dim

    menu:
        "Kyllä":
            $ points += 2

            show hollo eh at right, highlight
            show kalevi neutraali at left, dim
            play sound ("hollotuhahdus.mp3")
            h "…"

            show hollo eh at right, dim
            show martta tsk at center, highlight
            play sound ("martta1.mp3")
            m "…"

            show hollo eh at right, highlight
            show martta eh at center, highlight
            play sound ("yhteinen2.mp3")
            hm "Missä?!"
            jump dont_eat_done

        "Ei":
            show kalevi neutraali at left, dim
            show hollo viha at right, highlight
            play sound ("holloorina4.mp3")
            h "Ei? Miten niin ei?"

            show hollo viha at right, dim
            show martta hymy at center, highlight
            play sound ("marttanauru.mp3")
            m "Hehehee, ihminen unohti että hän itse olisi mukavan ruokaisa."
            jump dont_eat_done

label dont_eat_done:
    if points == 0:
        jump bad_ending
    elif 1 <= points <= 3:
        jump ok_ending
    elif points == 4 and piipertajaCount == 7:
        jump perfect_ending
    elif points == 4:
        jump happy_ending


label bad_ending:
    show martta tsk at center, highlight
    show kalevi neutraali at left, dim
    show hollo neutraali at right, dim
    play sound ("martta1.mp3")
    m "Pata kyllä alkaa olemaan jo melkoisen täynnä."

    show martta tsk at center, dim
    show hollo virne at right, highlight
    play sound ("hollonauru2.mp3")
    h "Älä huoli, Marttaseni, raa’at ihmiset ovat aivan yhtä hyviä kuin keitetyt."

    show hollo virne at right, dim
    show kalevi kauhu at left, highlight
    play sound ("kaleviahaa.mp3")
    k "Hei! Kauemmas siitä! Älä-!"

    stop music
    play music "bg_badend.mp3" loop

    scene kuva 5
    window hide
    pause

    jump game_ending

label ok_ending:
    show martta neutraali at center, dim
    show kalevi neutraali at left, dim
    show hollo neutraali at right, highlight
    play sound ("hollotuhahdus.mp3")
    h "Olet hassu pikku ihminen, juoksepas siitä nyt pois ennen kuin kyllästymme papatukseesi."

    show kalevi puhe at left, highlight
    show hollo neutraali at right, dim
    play sound ("kalevihmmlyhyt.mp3")
    k "Mutta karvapiipertäjät-"

    show kalevi puhe at left, dim
    show martta virne at center, highlight
    play sound ("marttanauru.mp3")
    m "Asetetaanpa asiat näin: joko voit pitää henkiriepusi tai voit leikkiä sankaria. Kumpaa arvostat enemmän?"

    show kalevi ajatus at left, highlight
    show martta virne at center, dim
    k "…"

    stop music
    play music "bg_okend.mp3" loop

    scene kuva 6
    window hide
    pause

    jump game_ending

label happy_ending:
    show martta neutraali at center, dim
    show kalevi puhe at left, highlight
    show hollo neutraali at right, dim
    play sound ("kalevihmmlyhyt.mp3")
    k "No, miten on? Vapautatteko karvapiipertäjät?"

    show kalevi puhe at left, dim
    show martta virne at center, highlight
    play sound ("marttanauru.mp3")
    m "Mikä kummallinen otus, kehtaakin väittää meille vastaan. En tiedä onko se rohkeutta vai tyhmyyttä."

    show kalevi hymy at left, highlight
    show martta virne at center, dim
    play sound ("kaleviahaa.mp3")
    k "Olisi parempi jos kyläläisten kiusaamisen sijasta tekisitte kanssamme yhteistyötä. Te olette isoja ja vahvoja, kun taas meillä on enemmän kuin tarpeeksi ruokaa."

    show kalevi hymy at left, dim
    show martta neutraali at center, highlight
    play sound ("marttaaah.mp3")
    m "Hah, hupsu ihminen, täynnä hupsuja ajatuksia. Olisi sääli kiusata sinua tämän enempää."

    show martta neutraali at center, dim
    show hollo pah at right, highlight
    play sound ("holloorina2.mp3")
    h "Ota vaan piipertäjät mukaasi ja lähde. Äläkä kuvittelekkaan että olemme näin armollisia tulevaisuudessa."

    stop music
    play music "bg_happyend.mp3" loop
    play sound ("voitto.mp3")
    "Sait säkillisen piipertäjiä."

    scene kuva 7
    window hide
    pause

    jump game_ending


label perfect_ending:

    show martta neutraali at center, dim
    show kalevi puhe at left, highlight
    show hollo neutraali at right, dim
    play sound ("kalevihmmlyhyt.mp3")
    k "No, miten on? Vapautatteko karvapiipertäjät?"

    show kalevi puhe at left, dim
    show martta virne at center, highlight
    play sound ("marttaahaa2.mp3")
    m "Mikä kummallinen otus, kehtaakin väittää meille vastaan. En tiedä onko se rohkeutta vai tyhmyyttä."

    show kalevi hymy at left, highlight
    show martta virne at center, dim
    play sound ("kaleviahaa.mp3")
    k "Olisi parempi jos kyläläisten kiusaamisen sijasta tekisitte kanssamme yhteistyötä. Te olette isoja ja vahvoja, kun taas meillä on enemmän kuin tarpeeksi ruokaa."

    show kalevi hymy at left, dim
    show hollo viha at right, highlight
    play sound ("holloorina2.mp3")
    h "Yhteistyötä ihmisten kanssa?!"

    show hollo viha at right, dim
    show martta eh at center, highlight
    play sound ("marttaaah.mp3")
    m "Ennenkuulumatonta!"

    show hollo eh at right, highlight
    show martta eh at center, dim
    play sound ("hollotuhahdus.mp3")
    h "Mutta toisaalta…"

    show hollo eh at right, dim
    show martta hymy at center, highlight
    play sound ("marttanauru.mp3")
    m "Niin… Se voisi olla hyvä diili. Ei tarvitsisi jatkuvasti olla kuuntelemassa ihmisten kirkumista."

    show hollo virne at right, highlight
    show martta hymy at center, dim
    play sound ("hollonauru2.mp3")
    h "Hyvä on, ihminen, tehdään kaupat."

    stop music
    play music "bg_happyend.mp3" loop

    scene kuva 8
    window hide
    pause

    jump game_ending

    

# This ends the game.
label game_ending:

    window show
    scene black
    hide screen count_piipertaja
    show screen ending
    window show
    ""

    $ renpy.movie_cutscene("kredut.mpg")

    return
