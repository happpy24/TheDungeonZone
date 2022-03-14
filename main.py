# import random, time, os, sys, colorama
import random
import time
import os
import sys
import colorama as cr
cr.init(autoreset=True)

# player class
class player:
    def __init__(self):
        self.name = 'playername'
        self.location = 'Room 0'
        self.inventory = ['handcuff', 'dirty bag']
        self.hp = 40

player = player()
name = player.name

 # global variables
isGameRunning = True
scrollspeed = 0.01

yl = ('y', 'yes', 'all right', 'alright', 'very well', 'ofc', 'ofcourse',
    'of course', 'sure', 'certainly', 'absolutely', 'indeed', 'roger', 'aye',
    'aye aye', 'yeah', 'yah', 'yep', 'yup', 'yuppers', 'mhm', 'okay', 'ok',
    'righto', 'yea', 'surely', 'ye', 'yuh', 'ya', 'yarr', 'aight', 'yessir',
    'why not','yee')
nl = ('n', 'no', 'nah', 'nope', 'naw', 'nay', 'noway', 'no way', 'never',
    'nae', 'not at all', 'not really', 'no thanks', 'of course not',
    'negative', 'nope', 'nuh', 'neh', 'nein', 'hell no', 'nonono',
    'forget that', 'nya','nuuu')

# dictionary variables
location = 'location'
title = 'title'
intro = 'intro'
first = 'first'
description = 'description'
extradialogue = 'extradialogue'
exits = 'exits'
event = 'event'
item = 'item'
itemroom = 'itemroom'
N = 'n'
E = 'e'
S = 's'
W = 'w'

# dictionary
locations = {
    "Room 0": {
        title: "The Origin",
        intro: "You are in a dark mossy room. There are four exits on each\nside, from north just came a sound before it turned quiet\nagain. You put the handcuffs and dirty bag in your pocket.\nThey might come in handy after all.",
        first: 0,
        description: "Looks like you are back at the beginning, \nthere are four exits around you.",
        extradialogue: "You start to question if this isn't just a vague\ndream you are in, but once a waterdroplet from the\nmossy ceiling hits your forehead you let that thought go.\nBetter continue moving.",
        exits: "N / E / S / W",
        event: 0,
        item: [],
        itemroom: 0,
        N: "Room 1",
        E: "Room 5",
        S: "Room 8",
        W: "Room 10"
    },
    "Room 1": {
        title: "Small Fella",
        intro: "You notice a weird hairless creature squating on what looks\nlike a lifeless corpse. The creature turns around and locks\neyes with you. The creature jumps from the corpse and lands\ninfront of you.",
        first: 0,
        description: "You enter the room in which you dueled fiercly with an Imp.\nSadly, you could't save the human who fell victim to him.",
        extradialogue: "You poke the Imp and the human to see\nif they were really dead. \n\nYep, they weren't faking it.",
        exits: "N / E / S ",
        event: 1,
        item: [],
        itemroom: 0,
        N: "Room 2",
        E: "Room 3",
        S: "Room 0",
        W: ""
    },
    "Room 2": {
        title: "Nailed It",
        intro: "You enter a nicely lit room, you spot a sledgehammer in\nthe middle of the room, it might come in handy.\n\nThe door to the east is locked, a key is needed to continue.",
        first: 0,
        description: "You find yourself in the room with lots of candles. \nThe massive door looks down at you.",
        extradialogue: "You wished for a wish, and blew out a candle.\n\nPssst... What did you wish for?\nI promise I won't tell anyone.",
        exits: "S",
        event: 0,
        item: ['sledgehammer'],
        itemroom: 1,
        N: "",
        E: "Room 4",
        S: "Room 1",
        W: ""
    },
    "Room 3": {
        title: "3 Heads with an appetite",
        intro: "Well, this is awkward... \nYou entered a big room with chains leading to the necks\nof a huge Cerberus. The dog is sleeping with a bone\nunder its hands. Feeling ballsy?",
        first: 0,
        description: "You enter the room of the sleeping 3 headed beast. It's better\nto think carefully about your next course of action.",
        extradialogue: "You really wanted to pet the dog,\nbut your common sense stopped you.",
        exits: "W",
        event: 0,
        item: [],
        itemroom: 1,
        N: "",
        E: "",
        S: "",
        W: "Room 1"
    },
    "Room 4": {
        title: "The Big Fat Goblin King ",
        intro: f'''A gate drops down behind you, no more way back.\n\n< Goblin King > Who dares entering my room?\n\n< {name} > I have come to defeat you and earn my freedom!\n\n< Goblin King > Very well, your skull will make a\nfine chalice.\n\nYou and the Goblin King both draw out your weapons\nand the final duel began.''',
        first: 0,
        description: "The room is starting to get overflowed with creatures.\n\nIt would be foolish to stay here any longer,\nthere is only one thing left to do; get the hell outta here!",
        extradialogue: "This is no time to do something else than running away!",
        exits: "E",
        event: 1,
        item: [],
        itemroom: 0,
        N: "",
        E: "Exit",
        S: "",
        W: ""
    },
    "Room 5": {
        title: "Sakura Tree",
        intro: f'''You find yourself in some kind of a zen garden. You spot an\nold man laying under a sakura tree\n\n< {name} > Hey! Who are you?\n\nThe old man puts his Kasa hat on, he gets up on his legs and\nwalks over to you. He puts his finger on your forehead and\nstarts humming.\n\n< Sensei > hmmm, you must be {name},Correct?\n\n< {name} > How do you know my name?\n\n< Sensei > I have my ways, what do you seek adventurer?\n\n< {name} > I want to know what I am doing here and how\nto get out of here!\n\n< Sensei > Heh, I know the answers to all of your questions,\nbut first you must fetch me a piece of bread, I cannot think\nso straight without eating a good meal.\n In the meantime,\nI shall rest under my tree.''',
        first: 0,
        description: "You are in the garden of the Sensei.\n\nThe Sensei is still resting under his tree.",
        extradialogue: f'''< {name} > Ever get the feeling that you are not really in\ncharge of your own body? It always feels like someone else\nis pulling the strings on my body and taking full control.\n\n< Sensei > I have heard cases of people losing their\ncontrol of their physical body. Most of the time, it\'s\nthem being crazy. You can try and meditate with me to\ncalm down if you want.\n\n< {name} > Maybe next time, I don't really feel\nlike it right now.''',
        exits: "W",
        event: 0,
        item: [],
        itemroom: 1,
        N: "",
        E: "Room 6",
        S: "",
        W: "Room 0"
    },
    "Room 6": {
        title: "Rusty Cage",
        intro: "You enter a pretty creepy room infested with bugs, there are\ncages everywhere.\n\nOut of the corner of your eye you spot a rusty cage with a\nshiny key inside of it.\n\nThere must be a way to obtain the key.",
        first: 0,
        description: "You walked into the creepy bug infested room filled with\ncages. There is a rusty cage which seems important.",
        extradialogue: "You decided to try and communicate with the bugs.\n\nSuprisingly, bugs cannot comprehend the human language.",
        exits: "W",
        event: 0,
        item: [],
        itemroom: 1,
        N: "",
        E: "",
        S: "Room 7",
        W: "Room 5"
    },
    "Room 7": {
        title: "The Key to succes",
        intro: "You enter the rusty cage, which you smashed with a hammer.",
        first: 0,
        description: "There is nothing in this room left,\nit reminds you of your love life; Empty and depressing...",
        extradialogue: "You hold the bars from the inside of the cage.\nJust for a second, you felt like your criminal uncle.",
        exits: "N",
        event: 0,
        item: ["shiny key"],
        itemroom: 0,
        N: "Room 6",
        E: "",
        S: "",
        W: ""
    },
    "Room 8": {
        title: "50/50: It happens, or it doesn't",
        intro:f'''You spot a big coin.\n\nOut of nowhere,the coin stood up on it side.\n\n< Coin > Ay, pal. Where ya heading?\n\n< {name} > Was that you who just spoke?\n\n< Coin > Oh my, where are my manners? I have not properly\nintroduced my self. You see, friends call me Muntz,\nand I have a crippling gambling addiction.\n\n< {name} > Nice to meet you, Muntz. \n\n< Muntz > By the way, see that door to the east? Rumour has\nit that there is some good loot in that room.\n\n< {name} > Oh, cool. You wont mind me going there, right?\n\n< Muntz > Well you see, this is where my gambling addiction\nneeds to be fullfilled. I need to gamble at least once per\nday! Here, I have an idea: I will do a backflip, you have\nto guess which side I will land, if you win,\nI will let you pass, otherwise you might feel a slight pain.\n\n< {name} > Sounds fair, bring it on!''',
        first: 0,
        description: "You returned back to Munt's room, he smiles at you.",
        extradialogue: "< Muntz > Gambling addiction? Let me tell you a tale, pal.\n\nBack when I still was molten gold, My creator was a drunk\nbastard who was struggling with money. He only had enough\nmolten gold to forge one big coin, which turned out to be\nme. He went to this old hag who lived somewhere in the\noutskirts of his village.\n\nHe challenged her into a coinflip.\n\nIf he won, then she would have to give life to the coin.\nOtherwise she could take his life.\n\nSince I'm alive, you can guess what happened.",
        exits: "N / E",
        event: 1,
        item: [],
        itemroom: 0,
        N: "Room 0",
        E: "Room 9",
        S: "",
        W: ""
    },
    "Room 9": {
        title: "Armory",
        intro: "You enter a pretty beaten up place, It looks like some\ntraining facility. Too bad most of the items were taken,\nexcept for 2 items.",
        first: 0,
        description: "You are in an abandonded training facility.\nUnfortunately most of the good stuff is already taken.",
        extradialogue: "You try to find if there was anything else noteworthy to\npick up. It was kind of desperate to see you rummaging\nthrough. The best thing you found was some chewing gum stuck\nunder a table. Which you immediately put in your mouth.\n\nEw, you weirdo.",
        exits: "W",
        event: 0,
        item: ["dagger","helmet"],
        itemroom: 0,
        N: "",
        E: "",
        S: "",
        W: "Room 8"
    },
    "Room 10": {
        title: "Ooo, a penny!",
        intro: "You find yourself in a...\nwow, this room actually looks harmless.\nThere is nothing really remarkable to say about this one.\n\nYou spot a small penny on the floor.\nIt looks kind of suspicious, but hey, money is money.",
        first: 0,
        description: "You have returned to the not so extaordinary room.\nThis room could've been used for something cooler...",
        extradialogue: "You decided to sing for fun.\n\nIt wasn't the greatest performance, but you felt proud\n\nIn my opinion, it was terrible, but who am I to judge?",
        exits: "N / E / S",
        event: 0,
        item: ['rusty coin'],
        itemroom: 0,
        N: "Room 12",
        E: "Room 0",
        S: "Room 11",
        W: ""
    },
    "Room 11": {
        title: "Calcium Man",
        intro: f'''You enter a pretty fancy dining room. It is fully decorated\nwith golden decorations of what looks like... Skeleton\nstatues?\n\n< ??? > Like what you see?\n\n< {name} > Hey! Who else is in this room?\n\nA noise was heard coming from under the table. A skeleton\npopped his head out of the side of the table. He wore some\ndisco clothing and had a pompadour.\n\n< ??? > Heya, I didn't mean to scare you, sorry if I did.\n\n< {name} > Damn, you almost scared the skeleton out\nof me. Who are you anyway and what are you doing here?\n\n< ??? > *Laughs maniacally* Today is your lucky day, you\nare standing face to face with the most famous underworld\nrockstar. I AM PELVIS PRESLEY, BABY!\n\n< {name} > Sorry, never heard of you.\n\n< Pelvis > Judging by your appearance, no wonder. You are\nstill a lame sack of flesh. Try dying, and you will see\nmy face plastered all over the underworld.\n\nThe skeleton fully gets up on his legs and takes a seat.\nYou notice that his right arm is missing.\n\n< {name} > Hey Pelvis, what ever happened to your right arm?\n\n< Pelvis > One moment I was giving a kickass performance\nin the underworld the very next I found myself in this\ndungeon. I tried finding the exit but walked face first\ninto a 3 headed beast. I barely managed to get out of there.\nBastard took my left arm, and probably used it as a chewing\ntoy.I am not expecting to see my arm any time soon, I would\nbe over\n the moon if I found it.\n\n< {name} > That sounds wild, I will try to help you out.\n\n< Pelvis > Really, you? Thanks, I appreciate it. If you do\nmanage to find it, I will give you something.''',
        first: 0,
        description: "You enter Pelvis' fancy dining room, Pelvis is sitting\non his chair writing something.",
        extradialogue: "Can I vent for a bit? I was supposed to give a performance\ntoday. The skeletons who booked me, canceled last\nminute. It was supposed to take place near this market place in\nthis  dungeon. Oh well, their loss I guess.",
        exits: "N",
        event: 0,
        item: [],
        itemroom: 1,
        N: "Room 10",
        E: "",
        S: "",
        W: ""
    },
    "Room 12": {
        title: "The Legendary Popstar",
        intro: f'''You set foot in this dark room, the floor seems to be \nmade of glass. You notice speakers and smoke generators.\nThe ground begins to shake and a dark silouet slowly rises.\nThe speakers turn and the smoke generators pumped\nout lots of smoke.\n\n< {name} > Where am I? Stay back you creature!\n\n< ??? > HEE, HEE!\n\nThe shadowy figure steps out into the light, you\ncould now barely make out the facial features.\nIt was a male, he had long hair and his nose looked weird.\n\n< ??? > Shamone! Are you Billie Jean?\n\n< {name} > I am not sure who this Billie Jean is,\nshow yourself right now!\n\nThe lights turn on and you can finally see who the man was...\n\nIt was Michael Jackson! He was wearing his signature\nred jacket and black pants.\n\n< MJ > Lets heat up the dancefloor, shall we?\nShow me what you got, if you impress me, I will let\nyou pass by.\n\nThe room was fully covered in smoke\nand Thriller began to play..''',
        first: 0,
        description: "You enter the dance room, the lights seem to be turned off.\n\nMichael Jackson is sitting on the floor and\nis taking a breather.",
        extradialogue: "Wow, phew.\nYou are a natural.\nMy hats off to you.\nY'know, you could've had a great career as a backup dancer.\nToo bad that you won't make it out of here alive.\n\nHEE HEE",
        exits: "N / S",
        event: 1,
        item: [],
        itemroom: 0,
        N: "Room 13",
        E: "",
        S: "Room 10",
        W: ""
    },
    "Room 13": {
        title: "Butch the Butcher",
        intro: f'''You find yourself in some kind of market place,\nthere is only one open shop.\n\nThe shop is called Butch\'s Slaughterhouse.\nYou decide to walk in.\n\n< Butch > What are ya looking for? Animal, goblin\nor even human meat?\n\n< {name} > I am personally not really looking for\nanything, but-\n\n< Butch > What the hell are you doing in a market\nplace then?\n\n< {name} > Jeez, I wanted to ask a question.\n\n< Butch > Yeah, and im trying to turn a damn profit.\nI don\'t talk to freeloaders, come back when you wanna\nbuy some good food.''',
        first: 0,
        description: "You are in Butch's slaughterhouse.\n\nButch doesn't convey any real emotions, he just stares at\nyou, judgingly...",
        extradialogue: "< Butch > You know what? I'll tell you something: If you\nkeep nagging me, you will end up on the menu, got it?\nNow get LOST!",
        exits: "S",
        event: 0,
        item: [],
        itemroom: 1,
        N: "",
        E: "",
        S: "Room 12",
        W: "Room 14"
    },
    "Room 14": {
        title: "The Bone Zone",
        intro: "You enter a pretty epic rave party.\nIt seems only skeletons are present here.",
        first: 0,
        description: "You enter back into the room where some sort of rave party\nis happening. This place is probably some nightclub.\nParty for the dead.",
        extradialogue: "You tap on the shoulder from a skeleton who is dancing.\n\nTheir shoulder falls off.\n\nYou quickly stand a few meters back, and look away\nas if you didn't see or do anything.\n\nThe fool.",
        exits: "E",
        event: 0,
        item: ['bottle of apple juice'],
        itemroom: 0,
        N: "",
        E: "Room 13",
        S: "",
        W: ""
    },
    "Exit": {
        title: "",
        intro: " ",
        first: 1,
        description: " ",
        exits: "",
        event: 0,
        item: []
    }
}

 #                     ___  ____ ____ _ _  _ _ ___ _ ____ _  _ ____ 
#                     |  \ |___ |___ | |\ | |  |  | |  | |\ | [__  
#                     |__/ |___ |    | | \| |  |  | |__| | \| ___]

 # definition for a faster print technique.
def dfast_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)



def delay_print(s):
    global scrollspeed
    for c in s:
        if scrollspeed == 0:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0)
        if scrollspeed == 0.01:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.01)
        if scrollspeed == 0.02:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.02)
        if scrollspeed == 0.03:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.03)



def dramatic_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.3)


# definition for easy access to a 'enter to continue' function
def etc():
    time.sleep(0.1)
    print(f'\n{cr.Fore.WHITE}Press [ENTER] to continue')
    input()


# definition to define the player name.
def choosename():
    # welcome2 name choosing
    sure = 0
    suresure = 'a'
    while sure == 0:
        delay_print('\nWhat is your name, adventurer?\n')
        player.name = input("> ")
        delay_print(f"\nAre you sure '{player.name}' is your name? [y/n]\n")
        suresure = input("> ")
        suresure = suresure.lower()
        if suresure in yl:
            sure = True
        elif suresure in nl:
            delay_print('Alright, make up your mind.')
            time.sleep(1.7)
            os.system("clear")
        else:
            delay_print('I didn\'t quite get that...')
            time.sleep(1.7)
            os.system("clear")

    #roasting of name before game start
    roast()
    print(f'\n{cr.Fore.WHITE}Press [ENTER] to continue, or [s] to skip the intro.\n')
    skip = input('> ')
    if skip.lower() != 's':
        #opening game
        os.system("clear")
        opening()



def roast():
    roast = random.randrange(9)
    if roast == 0:
        dramatic_print(f"\n{player.name}...")
        delay_print(" Weird name, ")
        time.sleep(0.3)
        delay_print("but we'll go with it...\n")
        time.sleep(0.1)
    if roast == 1:
        dramatic_print(f"\n{player.name}...")
        delay_print(" What kind of alcohol were your parents drinking?\n")
        time.sleep(0.1)
    if roast == 2:
        dramatic_print(f"\n{player.name}...")
        delay_print(" I feel sorry for you, ")
        time.sleep(0.3)
        delay_print("well, ")
        time.sleep(0.3)
        delay_print("kind of.\n")
        time.sleep(0.1)
    if roast == 3:
        dramatic_print(f"\n{player.name}...")
        delay_print(" Pretty neat name, ")
        time.sleep(0.3)
        delay_print("I forsee great luck.\n")
        time.sleep(0.1)
    if roast == 4:
        dramatic_print(f"\n{player.name}...")
        delay_print(" That name will strike fear on kittens...\n")
        time.sleep(0.1)
    if roast == 5:
        dramatic_print(f"\n{player.name}...")
        delay_print(" Well, ")
        time.sleep(0.3)
        delay_print("this name will be written down in history books.\n")
        time.sleep(0.1)
    if roast == 6:
        dramatic_print(f"\n{player.name}...")
        delay_print(" You finally might be worthy to beat this.\n")
        time.sleep(0.1)
    if roast == 7:
        dramatic_print(f"\n{player.name}...")
        delay_print(" Yikes, ")
        time.sleep(0.3)
        delay_print("not you!\n")
        time.sleep(0.1)
    if roast == 8:
        dramatic_print(f"\n{player.name}...")
        delay_print(" Wow, ")
        time.sleep(0.3)
        delay_print("even I didn't expect that one...\n")
        time.sleep(0.1)
    if roast == 9:
        dramatic_print(f"\n{player.name}...")
        delay_print(" Shiver me timbers...\n")
        time.sleep(0.1)



def opening():
    print('_' * 60)
    delay_print(
            f'\n    With each breath you took, the smaller the airpocket \n     became. '
        '')
    time.sleep(0.2)
    delay_print( f'''The bag that was placed over your head was \n    obstructing your breathing capabilities. ''')
    time.sleep(0.2)
    delay_print(f'''Suddenly, ''')
    time.sleep(0.2)
    delay_print(f'''the\n''')
    time.sleep(0.2)
    delay_print(f'''  bag was taken off and you were released from your cuffs.\n''')
    time.sleep(0.2)
    delay_print(f'''      You look around and there was no one to be seen.\n''')
    time.sleep(0.2)
    delay_print(f'''      The walls from the room were covered in wet moss.\n''')
    time.sleep(0.2)
    delay_print(f'''    Four exits, ''')
    time.sleep(0.2)
    delay_print(f'''one on each side of the dirty room were \n       visible. ''')
    time.sleep(0.2)
    delay_print(f'''Four possible ways out of this place.\n\n''')
    time.sleep(0.6)
    delay_print(f'''     Suddenly, ''')
    time.sleep(0.2)
    delay_print(f'''what seemed to be a voice, ''')
    time.sleep(0.2)
    delay_print(f'''came from the\n                    room north from you.\n\n''')
    time.sleep(0.4)
    delay_print(f''' >  "{player.name}..."\n\n''')
    time.sleep(0.4)
    delay_print(f'''     You raise your head as the voice tries to lure you\n                    closer. ''')
    time.sleep(0.2)
    delay_print(f'''Is it a trap?\n\n''')
    time.sleep(0.4)
    delay_print(f''' >  "{player.name}..! Please he-"\n\n''')
    time.sleep(0.4)
    delay_print(f'''     The voice get's cut off. ''')
    time.sleep(0.2)
    delay_print(f'''Just the silence, ''')
    time.sleep(0.2)
    delay_print(f'''and the \n      water dripping down the walls and ceiling. ''')
    time.sleep(0.2)
    delay_print(f'''While\n         slowly getting up, ''')
    time.sleep(0.2)
    delay_print(f'''you realize you should\n                   probably start moving.\n\n''')
    time.sleep(0.8)
    delay_print(f'''     Whoever took you here might come back after all...\n''')
    print('_' * 60)
    print('\n')
    etc()



def print_location():
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    delay_print(locations[player.location][title] + '\n\n')

     # check if its the player's first time visiting
    if locations[player.location][first] == 0:
        delay_print(locations[player.location][intro].replace(name, player.name) + '\n')
        locations[player.location][first] = 1
    else:
        delay_print(locations[player.location][description].replace(name, player.name) + '\n')

     # check if there is a fight or other event in the room
    if locations[player.location][event] == 1:
        print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
        etc()
        # trigger fight in room 1
        if locations[player.location] == locations["Room 1"]:
            impfight()
            if player.hp > 0:
                os.system('clear')
                print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
                delay_print('The defeated imp.\n\n')
                delay_print('The imp throbbles backwards and falls to the floor.\nDefeated, just like the maniac defeated whoever went\nthrough this room before you.. Perhaps that was the\nperson who took you here.\n')
        # trigger fight in room 3
        if locations[player.location] == locations["Room 4"]:
            finalfight()
            if player.hp > 0:
                os.system('clear')
                print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
                delay_print('The fallen King\n\n')
                delay_print('As you struck the final blow, the Goblin King fell on his\nbelly, his crown rolling from the top of his head to the\nfloor.\n\nYou finally beat this fat bastard. You decide to sit on\nthe floor,\nand take some heavy breaths. You heard some\nfootsteps approaching from the door you entered.\n\nYou turn around see a hoard of Imps and goblins charging at\nyou! You quickly get on your legs and begin making a run\nfor it.\n\nYou spot the exit to the east.\n')

         # trigger coinflip battle in room 8
        if locations[player.location] == locations["Room 8"]:
            coinflip()
            if player.hp > 0:
                os.system('clear')
                print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
                delay_print('The defeated coin.\n\n')
                delay_print('Muntz steps aside, letting you go to the room east\nfrom here. Already it seems like something shiny\nis in there. Better go investigate.\n')

         # trigger mj in room 12
        if locations[player.location] == locations["Room 12"]:
            danceman()
            if player.hp > 0:
                os.system('clear')
                print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
                delay_print('Satisfied Jackson\n\n')
                delay_print(f'''< MJ > *Claps* you were awesome! I have never seen such a\ndancer in a long time.\n\n< {name} > That means a lot coming from you, sir.\n\n< MJ > In the mean time, I will try to rest a bit,\nit\'s exhausting being dead.\n\nYou can now continue north!\n'''.replace(name, player.name))

        if player.hp > 0:
            delay_print('\nYou can go here: ' + locations[player.location][exits] +'\n')
    else:
        # print all locations the player can go to
        delay_print('\nYou can go here: ' + locations[player.location][exits] +'\n')

     # print items in room
    if len(locations[player.location][item]) >= 1:
        aaaa = 1
        delay_print('There seems to be a \'')
        for x in locations[player.location][item]:
            delay_print(x)
            if len(locations[player.location][item]) > aaaa:
                delay_print("' and a '")
                aaaa += 1
        delay_print('\' on the floor.\n')
    if int(player.hp) > 0:
        print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)



def pickup():
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    if locations[player.location][item] == []:
        delay_print('There aren\'t any items in this room to pick up!\n')
    elif len(player.inventory) == 2:
	    delay_print('Your inventory is full!\n')
    elif len(locations[player.location][item]) == 1:
        delay_print('You picked up a ' + locations[player.location][item][0]+'\n')
        player.inventory.append(locations[player.location][item][0])
        del locations[player.location][item][0]
    else:
        delay_print('Which item do you want to pick up?\n\n')
        print(*locations[player.location][item], sep="\n")
        delay_print('\nType the name of the item you want to pick up\n')
        delay_print('Type [b] to go back.\n\n')
        while True:
            getitem = input('> ')
            if getitem.lower() == 'b':
                print('\n\nYou leave everything in the room\n')
                break
            elif getitem in locations[player.location][item]:
                print(f"\n\nYou picked up a '{getitem.lower()}'.\n")
                player.inventory.append(getitem.lower())
                locations[player.location][item].remove(getitem.lower())
                break
            else:
                print('\n\nPlease choose a valid item to pick up.\n')

    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    etc()



def drop():
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    if player.inventory == []:
        delay_print('You don\'t have any items to drop!\n')
    elif len(player.inventory) == 1:
        delay_print('You dropped a ' + player.inventory[0]+'\n')
        locations[player.location][item].append(player.inventory[0])
        del player.inventory[0]
    else:
        delay_print('Which item do you want to drop?\n\n')
        print(*player.inventory, sep="\n")
        delay_print('\nType the name of the item you want to drop\n')
        delay_print('Type [b] to go back.\n\n')
        while True:
            dropitem = input('> ')
            if dropitem.lower() == 'b':
                print('\n\nYou leave everything in your inventory')
                break
            elif dropitem in player.inventory:
                print(f"\n\nYou dropped up a '{dropitem.lower()}'.\n")
                player.inventory.remove(dropitem.lower())
                locations[player.location][item].append(dropitem.lower())
                break
            else:
                print('\nPlease choose a valid item to drop.\n')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    etc()



def show_inventory():
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    if player.inventory == []:
        delay_print('You don\'t have any items in your inventory!')

    else:
        delay_print('There are the items in your inventory:\n\n')
        print(*player.inventory, sep="\n")
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    etc()



def use_item():
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    if 'bottle of apple juice' in player.inventory:
        player.inventory.remove('bottle of apple juice')
        delay_print('You pop the lid of the bottle of apple juice. A strange odor\ncoming from it. You almost don\'t want to take a sip, but\nyou decide to do it. It sure has a taste, but it\'s extremely\nwatered down.\n\nYour HP increased with 10 ♡!\n')
        player.hp += 10
    elif locations[player.location][itemroom] == 0:
        delay_print('You cannot use any items in this room.\n')
    else:
        if locations[player.location] == locations["Room 2"]:
            if 'shiny key' in player.inventory:
                player.inventory.remove('shiny key')
                locations[player.location][exits] = 'E / S'
                delay_print('You put the shiny key in the one and only keyhole in\nthe room. The door starts vibrating and slowly starts\nlifting. Stones from the ceiling almost falling down\nin the process. You sense that your adventure is almost\ncoming to an end.\n\nThis must be it. The door fully opens, but you already\nspot one more obstacle in your way.\n\nOne final fight. The final fight. Until freedom is yours.\n\nYou can now continue east!\n')
                locations[player.location][itemroom] = 0
            else:
                delay_print("You don't have some sort of 'key' yet!\n")

        if locations[player.location] == locations["Room 3"]:
            if 'hotdog' in player.inventory:
                player.inventory.remove('hotdog')
                player.inventory.append('bone')
                delay_print('You slowly start moving towards the sleeping creature.\nIf it wakes up now, it will be over. You grab the bone\nfrom under his arms and quickly swap it out for the\nhotdog. You stand there, for 2 more seconds, before\nknowing the beast is not going to wake up.\n\nA bone was added to your inventory!\n')
                locations[player.location][itemroom] = 0
            else:
                delay_print("Probably something similar in size,or something to eat\nwill distract him.\n")

        if locations[player.location] == locations["Room 5"]:
            if 'sandwich' in player.inventory:
                player.inventory.remove('sandwich')
                locations[player.location][exits] = 'E / W'
                delay_print(f'''< Sensei > Ah, there we go. Finally some good freakin \'food.\nJust let me, mmm, yeah, ah that tastes amazing!\n\n< {name} > So can you answer my questions?\n\n< Sensei > Certainly, I can think much better now. Okay so,\nbasically you are one of the Overlord\'s victims. He gets\nhis kicks by making these crazy dungeons. He gives tasks to\nhis special soldiers to guard the dungeon the soldier\nguarding this one is called the Goblin King. You must prepare\nwell before challenging him.\n\n< {name} > And why don\'t you leave this dungeon?\n\n< Sensei > Frankly, I like the peacefulness and not being\nbothered by anyone here. I also have got nowhere to go at\nthe surface.I could easily defeat the Goblin King, but\nmeditating here is better.\n\n< {name} > Anything else that I need to know?\n\n< Sensei > Oh, right! There\'s a hidden room behind that\nwaterfall\nto the east. it\'s pretty empty right now…\nHowever, there is a useful item in the room\nbeyond that\nwill help you on your journey. It is locked inside of this\nsturdy cage, If only you had\nsomething to smash the rusty\ncage with, then you might be\nable to grab the item inside.\n\nYou can now continue east!\n'''.replace(name, player.name))
                locations[player.location][itemroom] = 0
            else:
                delay_print("Something to eat is what he needs, it probably shouldn't\nbe fastfood though.\n")

        if locations[player.location] == locations["Room 6"]:
            if 'sledgehammer' in player.inventory:
                locations[player.location][exits] = 'S / W'
                delay_print('You grab the sledgehammer from your backpocket and prepare\nto swing. The wind going through your hair while you stood\nthere, menacingly, with the cage in front of you. You swung\nwith full force to break the bars.\n*KLANK*\n\nYou can now continue south!\n')
                locations[player.location][itemroom] = 0
            else:
                delay_print("There doesn't seem to bee a keyhole, so something to\nbreak it open would the best to use here.\n")

        if locations[player.location] == locations["Room 11"]:
            if 'bone' in player.inventory:
                player.inventory.remove('bone')
                player.inventory.append('sandwich')
                delay_print(f'''You show Pelvis his missing arm, you can see a spark in\nhis empty eye sockets.\n\n< Pelvis > Wow, you actually managed to fetch my arm back!\n\nYou hand the arm over to Pelvis and he attaches it.\nPelvis attaches it smoothly, and flexes his fingers.\n\n< Pelvis > Feels good to have full control! I can finally\nplay the song I was writing, anyways how can I repay you?\n\n< {name} > What can you give me?\n\nPelvis looks around his fancy room.\n\n< Pelvis > Well I cannot give you any of my statues, nor\nthe chairs. I dont think that they will fit in your\npocket. So Im gonna look in the kitchen for some snacks.\n\nYou sit there waiting for Pelvis to return.\n\nPelvis came back with some food.\n\n< Pelvis > Sorry man, this sandwich is what I all got.\nAlive vistors are not that common, if you were dead, we\nwould have had a great feast. So I am gonna add a bonus;\nI will make sure that if I get out of here, you will get\nfront row seatsat my concert, how does that sound?\n\n< {name} > Ehhh, It is better than nothing, but\nthanks for the sandwich.\n'''.replace(name, player.name))
                locations[player.location][itemroom] = 0
            else:
                delay_print("Anything that looks like an ordinary bone could probably\nbe used as arm for Pelvis.\n")

        if locations[player.location] == locations["Room 13"]:
            if 'rusty coin' in player.inventory:
                player.inventory.remove('rusty coin')
                player.inventory.append('hotdog')
                delay_print('*You put a penny on Butch\'s counter*\n\n< Butch > Eh eh eh! Finally showing some money hm? Let me\njust take that lift off of you. I can get ya something\nperfect just for that. Everyone likes hotdogs, you\'re a\nmaniac if ye doesn\'t. Here ya go.\n\nYou wanted to ask him a question, but the hotdog\nalready answered it.\n\nAnd now back off until\nyou find any more of those sweet coins.\n\nA \'hotdog\' was added to your inventory!\n')

            elif 'sledgehammer' in player.inventory:
                locations[player.location][exits] = 'S / W'
                delay_print('You grab the sledgehammer from your backpocket and smash\ninto the wall of the shop,a new room revealing itself.\n\n< Butch > HEY?! What was that all about?!!\nYou are going to pay for that aren\'t you?!\n\nYou can now continue west!\n')
                locations[player.location][itemroom] = 0
            
            else:
                delay_print("You should probably only do business with this guy.\nYou need money to do business, though. Better look on the\nfloor for lost pennies.\n")

    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    etc()



def talk():
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    delay_print(locations[player.location][extradialogue].replace(name, player.name)+'\n')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    etc()



def showmap():
    os.system('clear')
    print(f'{cr.Fore.LIGHTBLACK_EX}_' * 28)
    delay_print('You are here: ' + player.location + '\n')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}┌───┐   ┌───┐   ┌───┐  ┌───┐')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}│ 13│   │ 2 ├───┤ 4 ├──┤ext│')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}└─┬─┘   └─┬─┘   └───┘  └───┘')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}  │       │')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}┌─┴─┐   ┌─┴─┐   ┌───┐')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}│ 12│   │ 1 ├───┤ 3 │')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}└─┬─┘   └─┬─┘   └───┘')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}  │       │')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}┌─┴─┐   ┌─┴─┐   ┌───┐  ┌───┐')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}│ 10├───┤ 0 ├───┤ 5 ├──┤ 6 │')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}└─┬─┘   └─┬─┘   └───┘  └─┬─┘')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}  │       │              │')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}┌─┴─┐   ┌─┴─┐   ┌───┐  ┌─┴─┐')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}│ 11│   │ 8 ├───┤ 9 │  │ 7 │')
    time.sleep(0.05)
    print(f'{cr.Fore.LIGHTBLUE_EX}└───┘   └───┘   └───┘  └───┘')
    time.sleep(0.05)
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 28) + '\n')
    etc()



def options():
    global scrollspeed
    os.system('clear')
    print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
    print('\nWelcome to the options menu.\nWhich option do you want to change?\n')
    print('- [s] Scrollspeed')
    print('- [b] Continue the game')
    optionInp = input('> ')
    optionInp = optionInp.lower()
    if optionInp == 's':
        os.system('clear')
        print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
        print('\nScrollspeed setup')
        print('- [z] Slow')
        print('- [x] Standard')
        print('- [c] Fast')
        print('- [v] Instant')
        print('Choose any of the scrollspeeds listed!')
        scrollspeedInp = input('> ')
        scrollspeedInp = scrollspeedInp.lower()
        if scrollspeedInp == 'z':
            scrollspeed = 0.03
        elif scrollspeedInp == 'x':
            scrollspeed = 0.02
        elif scrollspeedInp == 'c':
            scrollspeed = 0.01
        elif scrollspeedInp == 'v':
            scrollspeed = 0
        else:
            print('I didn\'t quite get that...')
            time.sleep(1.8)
            options()
        os.system('clear')
        print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
        print(' ')
        delay_print('Scrollspeed has been changed')
        print(' ')
        print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
        etc()
        options()
    elif optionInp == 'b':
        os.system('clear')
    else:
        print('I didn\'t quite get that...')
        time.sleep(1.8)
        options()



def helpmenu():
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    print(f'{cr.Fore.LIGHTGREEN_EX}{cr.Style.BRIGHT}                       Controls:')
    time.sleep(0.3)
    print(' ')
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [n]    =  north')
    time.sleep(0.1)
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [e]    =  east')
    time.sleep(0.1)
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [s]    =  south')
    time.sleep(0.1)
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [w]    =  west')
    time.sleep(0.1)
    print(' ')
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [p]    =  pick up')
    time.sleep(0.1)
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [d]    =  drop')
    time.sleep(0.1)
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [i]    =  inventory')
    time.sleep(0.1)
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [u]    =  use (item)')
    time.sleep(0.1)
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [t]    =  talk')
    time.sleep(0.1)
    print(' ')
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [m]    =  show map')
    time.sleep(0.1)
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [o]    =  options')
    time.sleep(0.1)
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [h]    =  help')
    time.sleep(0.1)
    print(' ')
    print(f'{cr.Fore.LIGHTGREEN_EX}                    [q]    =  quit')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    etc()



def quit():
    global isGameRunning
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    delay_print('Are you sure you want to quit?\n')
    delay_print('[1] - Yes, I got something better to do.\n')
    delay_print('[2] - No! I want to finish my adventure!\n')
    delay_print('(You will lose all progress!)\n')
    wannaquit = input('> ')
    if int(wannaquit) == 1:
        print('\nTake care! Thanks for playing!')
        isGameRunning = False
        return isGameRunning
    elif int(wannaquit) == 2:
        print('Good luck on the rest of your adventure.')
        print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
        etc()
    else:
        print("That wasn't a valid option...")
        print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
        etc()



def amogus():
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 30) + '\n')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣶⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⠄⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⣴⡿⠛⠉⠁⠄⠄⠄⠄⠈⢻⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⢸⣿⡅⠄⠄⠄⠄⠄⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣦⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⠛⠃⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠄⠄⠄⠻⣿⣿⣿⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⢸⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⢸⣿⣿⣿⣿⣿⣧⡀⠄⠄⠄⠄⠄⠄⠄⢀⣾⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⢿⣿⣿⣿⣿⣿⣿⡟⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠈⢿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠘⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⢸⣿⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⢀⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⠄⠄⠄⠄⣸⣿⣿⣿⣿⣆⠄⠄⠄⠄⠄⢀⣾⣿⣿⣿⣿⣿⣄⠄⠄⠄⠄⠄⠄')
    print(f'{cr.Fore.RED}⠄⣀⣀⣤⣾⣿⣿⣿⣿⡿⠟⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿⣷⣄⣀⠄⠄⠄')
    print(f'{cr.Fore.RED}⠸⠿⠿⠿⠿⠿⠿⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠛⠿⢿⡿⠿⠿⠿⠃⠄⠄')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 30) + '\n')
    etc()

def impfight():
    global isGameRunning
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    delay_print('Looks like you got into a fight!\n\nIt seems like the creature is going to attack you first.\nBrace for impact!\n')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    etc()
    impHP = 20
    
    while impHP > 0:
        #imp attacking
        os.system('clear')
        print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
        if 'helmet' in player.inventory:
            impAttack = random.randint(0, 3)
        else:
            impAttack = random.randint(0, 5)
        player.hp -= impAttack
        delay_print('- Imp attacks!\n\n')
        time.sleep(0.6)
        if impAttack == 0:
            delay_print('- Miss!\n')
            time.sleep(0.2)
            delay_print('You haven\'t been hit, this time\n')
            delay_print(f"HP: {player.hp} ♡\n")
        else:
            delay_print('- Hit!\n')
            if 'helmet' in player.inventory:
                delay_print('You use your helmet as counter for the attack.\nIt still hurted like hell though.\n\n')
            else:
                delay_print('The imp scratches your skin, and you yell out the pain.\n\n')
            if int(player.hp) > 0:
                delay_print(f"The imp does [{impAttack} ♡] total damage! HP: {player.hp} ♡\n")
            else:
                pass
        print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
        etc()
        
        if player.hp > 0:
            #player attacking
            os.system('clear')
            print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
            delay_print('- Your turn!\n\n')
            time.sleep(0.6)
            if 'dagger' in player.inventory:
                playerAttack = random.randint(6, 10)
            else:
                playerAttack = random.randint(4, 7)
        
            playerHitChance = random.randint(0, 6)      
            if playerHitChance == 0:
                delay_print('- You missed...\n')
                time.sleep(0.2)
                delay_print(f'The imp still has {impHP} HP left..\n')
            else:
                impHP -= playerAttack
                if playerAttack == 10:
                    delay_print('- Critical hit!\n')
                    time.sleep(0.2)
                    delay_print(f'You hit the imp for a total of [{playerAttack} ♡] damage!\n')
                    if impHP > 0:
                        delay_print(f'The imp still has {impHP} HP left..\n')
                else:
                    delay_print('- Hit!\n')
                    time.sleep(0.2)
                    delay_print(f'You hit the imp for a total of [{playerAttack} ♡] damage.\n')
                    if impHP > 0:
                        delay_print(f'The imp still has {impHP} HP left..\n')
            print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
            etc()
        else:
            isGameRunning = False
            impHP = 0
            return isGameRunning
    locations[player.location][event] = 0



def finalfight():
    global isGameRunning
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    delay_print('The Goblin King swings his colossal club to the ground.\nThe sound could be heard echoing in the whole dungeon.\nYou felt impending doom coming your way.\n\n< Goblin King > I pray that you came well equipped.\n')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    etc()
    kingHP = 60
    
    while kingHP > 0:
        #goblin king attacking
        os.system('clear')
        print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
        kingMiss = random.randint(0,7)
        if kingMiss == 0:
            kingAttack = 0
        elif 'helmet' in player.inventory:
            kingAttack = random.randint(2, 6)
        else:
            kingAttack = random.randint(4, 8)
        delay_print('- The Goblin King swings his club!\n\n')
        time.sleep(0.6)
        if kingAttack == 0:
            delay_print('- Miss!\n')
            time.sleep(0.2)
            delay_print('You barely managed to dodge the club.\n')
            delay_print(f"HP: {player.hp} ♡\n")
        else:
            player.hp -= kingAttack
            delay_print('- Hit!\n')
            if 'helmet' in player.inventory:
                delay_print('You use your helmet as defence for the attack.\nIt absorbed some of the damage.\n\n')
            else:
                delay_print('The club smacks you, it left a big bruise.\n\n')
            if int(player.hp) > 0:
                delay_print(f"The Goblin King does [{kingAttack} ♡] total damage! HP: {player.hp} ♡\n")
            else:
                pass
        print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
        etc()
        
        if player.hp > 0:
            #player attacking
            os.system('clear')
            print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
            delay_print('- Your turn!\n\n')
            time.sleep(0.6)
            if 'dagger' in player.inventory:
                playerAttack = random.randint(7, 15)
            else:
                playerAttack = random.randint(4, 7)
        
            playerHitChance = random.randint(0, 7)
            if playerHitChance == 0:
                delay_print('- You missed...\n')
                time.sleep(0.2)
                delay_print(f'The Goblin King still has {kingHP} HP left..\n')
            else:
                kingHP -= playerAttack
                if playerAttack > 14:
                    delay_print('- Critical hit!\n')
                    time.sleep(0.2)
                    delay_print(f'You hit the Goblin King for a total of [{playerAttack} ♡] damage!\n')
                    if kingHP > 0:
                        delay_print(f'The King still has {kingHP} HP left..\n')
                else:
                    delay_print('- Hit!\n')
                    time.sleep(0.2)
                    delay_print(f'You hit the Goblin King for a total of [{playerAttack} ♡] damage.\n')
                    if kingHP > 0:
                        delay_print(f'The Goblin King still has {kingHP} HP left..\n')
            print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
            etc()
        else:
            isGameRunning = False
            kingHP = 0
            return isGameRunning
    locations[player.location][event] = 0




def coinflip():
    os.system('clear')
    notwinning = True
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    delay_print('You got into a coinflip battle!\n\nWin to continue, lose and your HP will be lowered.\n\n')
    delay_print('< Muntz > Feeling lucky already? Heads or Tails.\n')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    while notwinning == True:
        ht = 0
        ht = random.randint(0, 1)
        hort = input('[h] or [t]\n> ')
        os.system('clear')
        print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
        if hort.lower() == 'h':
            delay_print('< You > Heads!\n\n')
            time.sleep(1)
            if ht == 0:
                delay_print('Muntz does a three double backflip and finally lands\non the floor. Muntz looks at you and smiles.\n\n< Muntz > Heads it was! Well done!\n\nYou are finally able to continue.\n')
                print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
                notwinning = False
                locations[player.location][event] = 0
                etc()
            if ht == 1:
                player.hp -= 3
                delay_print(f'Muntz does a three double backflip and finally lands\non the floor. Muntz can\'t look at you yet, and a shiver\ngoes down your spine. Tails. You don\'t know how, but\nsuddenly feel immeasurable pain everywhere in your body,\nalmost getting you on your knees.\n\nYour new HP is {player.hp}.\n\nMuntz gets up. \n\n< Muntz > Well well, I hope that doesn\'t happen again.\nIt\'s much more fun if you win... Try again. I\'m not\nletting you through until you win.\n')
                if player.hp < 0:
                    notwinning = False
                    isGameRunning = False
                    return isGameRunning
        elif hort.lower() == 't':
            delay_print('< You > Tails!\n\n')
            time.sleep(1)
            if ht == 0:
                player.hp -= 3
                delay_print(f'Muntz does a three double backflip and finally lands\non the floor. Muntz looks at you, disappointed, and a shiver\ngoes down your spine. Heads. You don\'t know how, but\nsuddenly feel immeasurable pain everywhere in your body,\nalmost getting you on your knees.\n\nYour new HP is {player.hp}.\n\nMuntz gets up.\n\n< Muntz > Well well, I hope that doesn\'t happen again.\nIt\'s so much more fun if you win... Try again. I\'m not\nletting you through until you win.\n')
                if player.hp < 0:
                    notwinning = False
                    isGameRunning = False
                    return isGameRunning
            if ht == 1:
                delay_print('Muntz does a three double backflip and finally lands\non the floor. Muntz quickly turns around to smile for you.\n\n< Muntz > Tails it was! Well done!\n\nYou are finally able to continue.\n')
                print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
                notwinning = False
                locations[player.location][event] = 0
                etc()
        else:
            print('Choose a valid response!')
            time.sleep(0.9)
        print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')



def danceman():
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    delay_print('Looks like Michael Jackson challenged you to a dance battle!\n\n')
    delay_print('Prepare your moves and try to not mess up!\nDo 3 Epic moves to continue\n')
    locations[player.location][event] = 0
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    etc()
    danceYes = 0
    while danceYes < 3:
        os.system('clear')
        print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')   
        dancetype = random.randint(0,7)
        if dancetype == 0:
            delay_print(f'You accidentally tripped on your shoelaces, ouch!\n\nYou lost 3 HP! - HP: {player.hp} ♡\n')
            player.hp -= 3
        if dancetype == 1:
            delay_print(f'You break your back while trying to break dance.\n\nMichael Jackson giggles at you\n\nYou lost 3 HP! - HP: {player.hp} ♡\n')
            player.hp -= 3
        if dancetype == 2:
            danceYes += 1
            delay_print(f'You gave your best shot at a break dance.\n\nMichael Jackson seems impressed.\nYou nailed {danceYes} moves!\n')
            
        if dancetype == 3:
            danceYes += 1
            delay_print(f'You do a dance that your dance instructor taught you.\n\nMichael Jackson nods at you.\nYou nailed {danceYes} moves!\n')
            
        if dancetype == 4:
            danceYes += 1
            delay_print(f'You get on your belly and perform the worm.\n\nMichael Jackson seems amused.\nYou nailed {danceYes} moves!\n')
            
        if dancetype == 5:
            danceYes += 1
            delay_print(f'You perform a sick backflip.\n\nMichael jackson cheered when you landed!\nYou nailed {danceYes} moves!\n')
        
        if dancetype == 6:
            danceYes += 1
            delay_print(f'You put your legs next to eachother and perform a dab.\n\nMichael Jackson seems confused, but he lets it slide.\nYou nailed {danceYes} moves!\n')
        
        if dancetype == 7:
            delay_print(f'You turn to the side and execute a perfect Moonwalk.\n\nMichael Jackson is overjoyed and faints.\n')
            danceYes = 3
        print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
        etc()



def gameover():
    global isGameRunning, yl, nl
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    print('Ah, you died, somehow.')
    print(f'Ah well, welcome to {cr.Fore.RED}hell{cr.Fore.LIGHTWHITE_EX}, enjoy your stay!')
    print('Thank you for trying, but it seems like you were...')
    print('Not good enough...')
    print('You can always reincarnatie into a new soul!')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')



def ending():
    os.system('clear')
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    delay_print("You walk up the stairs towards the light, the final\nsteps as the only thing in sight. Once you finally\nget to the top, a sunflower field is greeting you.\nBehind you, the dungeon, which exit looks like the\nentrance to some bunker.\n\nYou have no idea where you are, but the sun shining\nover your head comforts you. Time to go home.\n\n")
    time.sleep(1.5)
    print(f"{cr.Fore.LIGHTBLUE_EX}        _____ _            _____          _")
    time.sleep(0.2)
    print(f"{cr.Fore.LIGHTBLUE_EX}       |_   _| |          |  ___|        | |")
    time.sleep(0.2)
    print(f"{cr.Fore.LIGHTBLUE_EX}         | | | |__   ___  | |__ _ __   __| |")
    time.sleep(0.2)
    print(f"{cr.Fore.LIGHTBLUE_EX}         | | | '_ \ / _ \ |  __| '_ \ / _` |")
    time.sleep(0.2)
    print(f"{cr.Fore.LIGHTBLUE_EX}         | | | | | |  __/ | |__| | | | (_| |")
    time.sleep(0.2)
    print(f"{cr.Fore.LIGHTBLUE_EX}         \_/ |_| |_|\___| \____|_| |_|\__,_|\n")
    print((f'{cr.Fore.LIGHTBLACK_EX}_' * 60) + '\n')
    if player.hp >= 25:
        print("You shall pay for what you did to our king.\nEnjoy your freedom while it lasts...")
    if startoroptions == 'speedrunmode':
        endspeedrun = time.time()
        hours, rem = divmod(endspeedrun-startspeedrun, 3600)
        minutes, seconds = divmod(rem, 60)
        time.sleep(1)
        print('Speedrun time:')
        time.sleep(1)
        print("{:0>2}:{:05.2f}".format(int(minutes),seconds))



def move_player(move_action):
    player.location = move_action



def game_loop():
    print_location()
    if player.hp > 0:
        print(f"\nWhat do you want to do?              HP: {player.hp} ♡    [h] = help")
        wdywd = input('> ')
        if wdywd.lower() == 'n':
            if wdywd.capitalize() not in locations[player.location][exits]:
                delay_print("You cannot go that way!")
                etc()
            else:
                move_action = locations[player.location][N]
                move_player(move_action)
        elif wdywd.lower() == 'e':
            if wdywd.capitalize() not in locations[player.location][exits]:
                delay_print("You cannot go that way!")
                etc()
            else:
                move_action = locations[player.location][E]
                move_player(move_action)
        elif wdywd.lower() == 's':
            if wdywd.capitalize() not in locations[player.location][exits]:
                delay_print("You cannot go that way!")
                etc()
            else:
                move_action = locations[player.location][S]
                move_player(move_action)
        elif wdywd.lower() == 'w':
            if wdywd.capitalize() not in locations[player.location][exits]:
                delay_print("You cannot go that way!")
                etc()
            else:
                move_action = locations[player.location][W]
                move_player(move_action)
        elif wdywd.lower() == 'p':
            pickup()
        elif wdywd.lower() == 'd':
            drop()
        elif wdywd.lower() == 'i':
            show_inventory()
        elif wdywd.lower() == 'u':
            use_item()
        elif wdywd.lower() == 't':
            talk()
        elif wdywd.lower() == 'm':
            showmap()
        elif wdywd.lower() == 'o':
            options()
        elif wdywd.lower() == 'h':
            helpmenu()
        elif wdywd.lower() == 'q':
            quit()
        elif wdywd.lower() == 'amogus':
            amogus()
        else:
            delay_print('You can\'t do that! Try something else...')
            etc()
        return isGameRunning


#               ____ ___ ____ ____ ___    ____ ____ ___  ____ 
#               [__   |  |__| |__/  |     |    |  | |  \ |___ 
#               ___]  |  |  | |  \  |     |___ |__| |__/ |___ 

 # welcome1 opening
print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
print(' ')
print(f'{cr.Fore.GREEN}{cr.Style.DIM}                      Welcome to the')
print(' ')
time.sleep(1)
print(f"{cr.Fore.GREEN}      █▀▄ █░█ █▄░█ █▀▀ █▀▀ █▀█ █▄░█   ▀█ █▀█ █▄░█ █▀▀")
time.sleep(0.5)
print(f"{cr.Fore.GREEN}      █▄▀ █▄█ █░▀█ █▄█ ██▄ █▄█ █░▀█   █▄ █▄█ █░▀█ ██▄")
print(' ')
print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
print(' ')
time.sleep(1.2)
print(f'        Legend has it that the people who venture')
print(f'  down this rabbithole never make it back in one piece...')
print(' ')
time.sleep(1.5)
print(f'We, KingLeap and Happy24 wish you good luck making it alive!')
print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
time.sleep(1.2)
print(' ')
print(f'{cr.Fore.LIGHTGREEN_EX}{cr.Style.BRIGHT}                       Controls:')
time.sleep(0.3)
print(' ')
print(f'{cr.Fore.LIGHTGREEN_EX}                    [n]    =  north')
time.sleep(0.1)
print(f'{cr.Fore.LIGHTGREEN_EX}                    [e]    =  east')
time.sleep(0.1)
print(f'{cr.Fore.LIGHTGREEN_EX}                    [s]    =  south')
time.sleep(0.1)
print(f'{cr.Fore.LIGHTGREEN_EX}                    [w]    =  west')
time.sleep(0.1)
print(' ')
print(f'{cr.Fore.LIGHTGREEN_EX}                    [p]    =  pick up')
time.sleep(0.1)
print(f'{cr.Fore.LIGHTGREEN_EX}                    [d]    =  drop')
time.sleep(0.1)
print(f'{cr.Fore.LIGHTGREEN_EX}                    [i]    =  inventory')
time.sleep(0.1)
print(f'{cr.Fore.LIGHTGREEN_EX}                    [u]    =  use (item)')
time.sleep(0.1)
print(f'{cr.Fore.LIGHTGREEN_EX}                    [t]    =  talk')
time.sleep(0.1)
print(' ')
print(f'{cr.Fore.LIGHTGREEN_EX}                    [m]    =  show map')
time.sleep(0.1)
print(f'{cr.Fore.LIGHTGREEN_EX}                    [o]    =  options')
time.sleep(0.1)
print(f'{cr.Fore.LIGHTGREEN_EX}                    [h]    =  help')
time.sleep(0.1)
print(' ')
print(f'{cr.Fore.LIGHTGREEN_EX}                    [q]    =  quit')
print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
time.sleep(1)
print(' ')
print(f'{cr.Fore.WHITE}                Press [ENTER] to continue')
time.sleep(0.1)
print(f'{cr.Fore.WHITE}                [o] to change the options')
startoroptions = input()
os.system("clear")

 # change options before game start
if startoroptions == 'o':
    options()

if startoroptions == 'speedrunmode':
    options()
    startspeedrun = time.time()


choosename()


  #game loop
while isGameRunning == True:
    if locations[player.location] == locations["Exit"]:
        isGameRunning = False
        ending()
    else:
        game_loop()

if int(player.hp) <= 0:
    gameover()