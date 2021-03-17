import socket
import os
import _thread
import sys
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) == 2:
    port = int(sys.argv[1])
    print(str(port))
else:
    print("Write the port as an argument for example: 4242")
    sys.exit()

try:
    sock.bind(("localhost", port))
except:
    print("Could not start the server")
    sys.exit()

sock.listen(20)
botsConnected = []  # clients which are always bots
botNames = []
Username = input("Write your username: ")  # This can be changes to your liking

openingLines = ["My dear bots, today I would like to", "Make a great suggestion for the bots", "What wonders will you "
                                                                                               "make the bots do?"]
activities = ["sing", "fight", "kill", "sleep", "chill", "run", "eat", "work", "greet", "joke"]


def multi_threaded_client(connection):
    connected = True
    while connected:
        print("\n" + Username + ": " + random.choice(openingLines) + ": ")
        msg = input()

        if msg.lower() == "-help":
            print("\nHere are a few commands you can use:"
                  "\nactivities: Lists the activities that the bots have unique interactions with"
                  "\nrandom: Choses a random, fun activity"
                  "\nbots: Lists the current connected bots"
                  "\nclose: Closes the server"
                  "\nkick BOTNAME: kicks the chosen bot from the server")
            continue

        if msg.lower() == "close":
            print("Closing server")
            for bot in botsConnected:
                bot.send("disconnect123".encode())
            os._exit(1)

        if msg.lower() == "random":
            msg = random.choice(activities)
            print("Sending " + msg + " to the bots")

        if msg.lower() == "activities":
            print("\nHere are some activities that have unique interactions:")
            for act in activities:
                print(" " + act)
            continue

        if "kick" in msg.lower():
            parsed = msg.split()

            if len(parsed) == 2:
                botKicked = parsed[1]
            else:
                print("The format of the kick-command is kick BOTNAME")
                continue

            if botKicked.lower() in botNames:

                index = botNames.index(botKicked.lower())
                bot = botsConnected[index]
                bot.send("disconnect123".encode())
                remove(bot)

                continue
            else:
                print("Bot: " + botKicked + " is not in the among the connected bots")
                continue

        words = msg.split()
        for word in words:
            if word in activities:
                msg = word

        for bot in botsConnected:
            try:
                bot.send("Host".encode())
                bot.send(msg.encode())
            except:
                remove(bot)

            try:
                reply = bot.recv(2048)
                brodcast(bot, reply)
                time.sleep(0.5)
                print("\n" + reply.decode())
            except:
                break

    connection.close()


def remove(connection):
    if connection in botsConnected:
        index = botsConnected.index(connection)
        del botNames[index]
        botsConnected.remove(connection)
        print("\nBot has been disconnected, number of bots is now " + str(len(botsConnected)))


def brodcast(client, msg):
    for bot in botsConnected:
        try:
            if bot != client:
                bot.send(msg)
        except:
            bot.close()
            remove(bot)


print("/// Welcome to the bot house, the program will start when at least 1 bot is connected ///")
print("/// The bots are: Mario, Gon, Batman, Luffy, Joker and Link ///\n")

while True:
    clientSocket, addr = sock.accept()
    botsConnected.append(clientSocket)

    # Getting the name from the client
    botName = clientSocket.recv(2048).decode()
    botNames.append(botName.lower())

    print("\nBot: " + botName + " with Address: " + str(addr) + " connected")
    print("Number of bots are: " + str(len(botsConnected)))
    print("For more information type -help in the input")

    _thread.start_new_thread(multi_threaded_client, (clientSocket,))
