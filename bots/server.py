import socket
import os
import _thread
import sys
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if (len(sys.argv) == 2):
    port = int(sys.argv[1])
    print(str(port))
else:
    print("Not enough arguments, need the port as the parameter")

try:
    sock.bind(("localhost", port))
except:
    print("Could not start the server")
    exit()

sock.listen(20)
botsConnected = []
antallBots = 0
ThreadCount = 0
Username = "Host"

lines = ["My dear bots, today I would like to", "Make a great suggestion for the bots"]
activities = ["sing", "fight", "kill", "sleep", "chill", "run", "eat", "work", "greet"]


def multi_threaded_client(connection):
    while True:
        msg = input("\n" + Username + ": " + random.choice(lines) + ": ")

        if msg.lower() == "-help":
            print("\nHere are a few commands you can use:"
                  "\nactivities: Lists the activities that the bots have unique interactions with"
                  "\nrandom: Choses a random, fun activity"
                  "\nbots: Lists the current connected bots"
                  "\nclose: Closes the server")
            continue

        if msg.lower() == "close":
            print("Closing server")
            os._exit(1)

        if msg.lower() == "random":
            msg = random.choice(activities)
            print("Sending " + msg + " to the bots")

        if msg.lower() == "activities":
            print("\nHere are some activities that have unique interactions:")
            for act in activities:
                print(" " + act)
            continue

        for bot in botsConnected:
            try:
                bot.send(msg.encode())
            except:
                bot.close()

            try:
                data = bot.recv(2048)
                print("\n" + data.decode())
            except:
                remove(bot)
                print("\nBot has been disconnected, number of bots is now " + str(len(botsConnected)))

    connection.close()


def remove(connection):
    if connection in botsConnected:
        botsConnected.remove(connection)


print("/// Welcome to the bot house, the program will start when at least 1 bot is connected ///")
print("/// The bots are: Mario, Gon, Batman, Luffy and Joker ///\n")

while True:

    try:
        clientSocket, addr = sock.accept()
        botsConnected.append(clientSocket)
    except:
        break


    _thread.start_new_thread(multi_threaded_client, (clientSocket,))
    print("\nBot:" + "with Address: " + str(addr) + " connected")
    print("Number of bots are: " + str(len(botsConnected)))
    print("For more information type -help in the input")

print("Closing server!")
sock.close()
