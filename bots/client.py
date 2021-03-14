import socket
import sys
import random
import string

#bots

botList = ["anders", "fanni", "maria", "joker", "batman", "luffy", "gon"]

actvities = ["chill", "play", "eat", "sleep", "run", "fight", "kill"]


def joker(a, b = None):
    myDict = {
        "name": "Joker",
        "greet": "I am joker, batman's worst knightmare",
        "run": "Physical labour is not my cup of tea",
        "sleep": "Sleeping is for the weak",
        "kill": "Yes, especially if it involves batman",
        "work": "I haven't worked since I got theese scars",
        "chill": "I will not chill untill I get my revenge",
        "eat": "Well sure! Can't the joker also enjoy a nice meal from time to time?",
        "fight": "No, but I can hire someone else to do it for me",
        "joke": "Knock, knock. Whos there? It's the police m'am! Your son's been hit by a drunk driver. He's dead."
    }
    if a in myDict:
        return myDict[a]

    return "There are other, more importaint things on my mind, hehehe"

def batman(a, b = None):
    myDict = {
        "greet": "I am batman (In a very deep voice)",
        "run": "Yes, I need to be in shape",
        "sleep": "Sleeping is not a priority here",
        "kill": "I would never kill",
        "work": "I work day and night to keep the city safe",
        "eat": "Yes, but not batsoup, that is bad for you",
        "fight": "If its against evil, I will do it!",
        "joke": "I don't know any, ask joker"
    }

    if a in myDict:
        return myDict[a]

    return "Maybe later, as a superhero I don't have much time on my hands"

def luffy(a, b = None):
    myDict = {
        "greet": "I am Luffy, and I am going to be the greatest pyBot king!",
        "run": "Boooooring!",
        "sleep": "ZZZZzzzzz (He is doing it already)",
        "kill": "I'll rather crush the soul of my enemies!",
        "work": "As in working towards being the pirate king? Yes!",
        "eat": "YES! If there is meat!",
        "chill": "Okey, for a little while",
        "fight": "I have been ithcing for a good fight!",
        "sing": "Come onboard and bring along all your hopes and dreeeams",
        "joke": "Have you heard this one! Never mind its too much of a stretch hahaha!"
    }

    if a in myDict:
        return myDict[a]

    return "Sorry, i'd rather {}".format(random.choice(actvities))

def gon(a, b = None):
    myDict = {
        "greet": "I am Gon and one day I will finally find my dad. Can he possibly be here, in the chatroom?",
        "run": "Come on, what are you waiting for!",
        "sleep": "I will practice my nen while I sleep",
        "kill": "No, id rather not",
        "work": "Ahhhh! Even more work?!",
        "eat": "Oh boy! Yes, can't wait. You are paying right?",
        "chill": "Only for a couple minutes, then back to training",
        "fight": "Hihi, I am very strong, just saying",
        "sing": "As you travel far across the globe, starting to awaken as you go",
        "joke": "I know a great one! I just can't seem to remember it"
    }
    if a in myDict:
        return myDict[a]

    return "Hmm, to {} sounds fun!".format(a)

def mario(a, b = None):
    responses = {
        "run": "yahoo!",
        "greet": "It's a mi Mario!",
        "sleep": "*sleeps* (Meanwhile Peach gets kidnapped again)",
        "kill": "Oh yeah! (Mario jumps high up in the air)",
        "work": "Mama mia!",
        "eat": "Ah yes! Mushrooms!",
        "fight": "Hayyya! No, wait thats Link",
        "sing": "Da, da, daratatta (The mario theme starts playing)",
        "joke": "What did the green mushroom say to Luigi? Get a life!"
    }
    if a in responses:
        return responses[a]

    return "Let's a GO!"


#Sjekker argumentene
if(len(sys.argv) == 4):
    botName = str(sys.argv[3])
    ipAdress = str(sys.argv[1])
    port = int(sys.argv[2])
    print(botName)

    if  botName.lower() in botList:
        bot = eval(botName.lower())
    else:
        print("Bot is not in the current botlist")
        exit()
else:
    print("Not enough arguments")
    exit()

#Connecting
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((ipAdress, port))
except:
    print("Could not connect to the server, try again")
    exit()

while True:
    print("\nawaiting message...")
    try:
        msg = client.recv(2048)
    except:
        break

    print("\nMessage recieved: " + msg.decode() + "\n")
    reply = botName + ": {}".format(bot(msg.decode()))
    print("Sending " + reply + " to the server...")
    client.send(reply.encode())

print("Client has been disconnected from the server")
client.close()