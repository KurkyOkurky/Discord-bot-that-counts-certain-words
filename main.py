import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
variace_nwordu = ["nigger", "negr", "nigga", "nigr", "nygr", "niggr", "nyggr"]

@bot.event
async def on_ready():
    print(("We have logged in as {0.user}".format(bot)))

# načtení counteru
def load_counter():
    with open("counter.json", "r") as f:
        counters = json.load(f)
    return counters

# uložení counteru
def save_counter(counters):
    with open("counter.json", "w") as f:
        json.dump(counters, f)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    users = []
    # Checkne jestli zpráva obsahuje daný slovo
    for n in variace_nwordu:
        if n in message.content.lower():
            counter = load_counter()
            counter["nigger_count"] += 1
            save_counter(counter)
            await message.channel.send("Varianta slova nigger byla napsána " + (str(counter["nigger_count"])) + "krát")
            for user in counter["users"]:
                users.append(user[0])

                # checkne jestli je user v listu
            if str(message.author) not in users:
                counter["users"].append([str(message.author), 1])
                await message.channel.send(1)

            else:
                for idx, user in enumerate(counter["users"]):
                    if user[0] == str(message.author):
                        counter["users"][idx][1] += 1
                        await message.channel.send(
                            str(message.author.mention) + " napsal " + str(counter["users"][idx][1]) + "krát n-word")
            save_counter(counter)

bot.run("MTA3MDA2MTg3NjQyNTI2NTE2Mg.GZ5q6I.SH6WI0Zlyef3g5IDSSCT6-ilIKgVCJwdtKGnD0")
