import socket
import sys
import random
import string
from bots import *

# bots

# Checkes the arguments
if len(sys.argv) == 4:
    botName = str(sys.argv[3])
    ipAdress = str(sys.argv[1])
    port = int(sys.argv[2])

    if botName.lower() in botList:
        bot = eval(botName.lower())
    else:
        print("Bot is not in the current botlist")
        exit()
else:
    print("Not enough arguments")
    exit()

# Connecting
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = True

try:
    client.connect((ipAdress, port))
    client.send(botName.encode())
except:
    print("Could not connect to the server, try again")
    exit()

print(botName + " connected to the server \nawaiting message...")

while connected:

    msg = client.recv(2048)

    if msg.decode() == "disconnect123":
        connected = False

    if msg.decode() == "Host":
        msg = client.recv(2048)
        print("\nMessage recieved from host: " + msg.decode())
        reply = botName + ": {}".format(bot(msg.decode()))
        print("\nSending " + reply + ", to the server...")
        client.send(reply.encode())
    else:
        print("\n" + msg.decode())
        sender = msg.decode().split(":")[0]

        if botName == "joker":
            words = msg.decode().split()
            keyWork = words[len(words)-1]
            if keyWork == "joker":
                reply = "\n" + botName + ": {}".format(bot(keyWork, sender))
                print(reply)

print("Client has been disconnected from the server")
client.close()
