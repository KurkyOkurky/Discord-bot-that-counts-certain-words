import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
word_count = ["Words here"]

@bot.event
async def on_ready():
    print(("We have logged in as {0.user}".format(bot)))

# Loads .json file for saving
def load_counter():
    with open("counter.json", "r") as f:
        counters = json.load(f)
    return counters

# Saves data into .json file
def save_counter(counters):
    with open("counter.json", "w") as f:
        json.dump(counters, f)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    users = []
    # Checks for certain words from list
    for n in variace_nwordu:
        if n in message.content.lower():
            counter = load_counter()
            counter["counter"] += 1
            save_counter(counter)
            await message.channel.send("TEXT " + (str(counter["counter"])) + "TEXT")
            for user in counter["users"]:
                users.append(user[0])

                # Checks if user is in list, if not adds them
            if str(message.author) not in users:
                counter["users"].append([str(message.author), 1])
                await message.channel.send(1)

            else:
                for idx, user in enumerate(counter["users"]):
                    if user[0] == str(message.author):
                        counter["users"][idx][1] += 1
                        await message.channel.send(
                            str(message.author.mention) + " TEXT " + str(counter["users"][idx][1]) + "TEXT")
            save_counter(counter)

bot.run("YOUR TOKEN HERE")
