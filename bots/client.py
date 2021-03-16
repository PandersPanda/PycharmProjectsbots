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

try:
    client.connect((ipAdress, port))
    client.send(botName.encode())
except:
    print("Could not connect to the server, try again")
    exit()

print(botName + " connected to the server \nawaiting message...")

while True:

    try:
        msg = client.recv(2048)
    except:
        break

    if msg.decode() == "Host":
        msg = client.recv(2048)
        print("\nMessage recieved from host: " + msg.decode())
        reply = botName + ": {}".format(bot(msg.decode()))
        print("\nSending " + reply + ", to the server...")
        client.send(reply.encode())
    else:
        print("\n" + msg.decode())

print("Client has been disconnected from the server")
client.close()
