#Discord.py Bot Template, by Zennara#8377
#This template is a compilation of code to make it easier to design your own Discord.py Bot
#I made this for my own use, but don't care who uses it, but please credit me if someone asks :)

#imports
import discord #api
import os #for virtual environment secrets on replit
import keep_alive #this keeps our bot alive from the keep_alive.py file
import asyncio #not needed unless creating loop tasks etc (you'll run into it)
import json #to write db to a json file
import requests #to check discord api for limits/bans
from replit import db #database storage

#api limit checker
#rate limits occur when you access the api too much. You can view Discord.py's api below. There it will tell you whether an action will access the api.
#https://discordpy.readthedocs.io/en/stable/api.html
r = requests.head(url="https://discord.com/api/v1")
try:
  print(f"You are being Rate Limited : {int(r.headers['Retry-After']) / 60} minutes left")
except:
  print("No rate limit")

#declare client
intents = discord.Intents.all() #declare what Intents you use, these will be checked in the Discord dev portal
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("\nYOUR_BOT_NAME Ready.\n")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with some code."))

@client.event
async def on_message(message):
  #check for bots
  if message.author.bot:
    return

  #convert the message to all lowercase
  messagecontent = message.content.lower()

  #this will clear the database if something is broken, WARNING: will delete all entries
  if messagecontent == "z/clear":
    #my database entries are seperates by server id for each key. this works MOST of the time unless you have a large amount of data
    db[str(message.guild.id)] = {"prefix": "z/"}

  #get prefix
  prefix = db[str(message.guild.id)]["prefix"]

  #this is to dump your databse into database.json. Change this to FALSE to stop this.
  DUMP = True
  if DUMP:
    data2 = {}
    count = 0
    for key in db.keys():
      data2[str(key)] = db[str(key)]
      count += 1

    with open("database.json", 'w') as f:
      json.dump(str(data2), f)

  #write your commands below!
  #example command:
    if messagecontent == prefix+"ping":
      await message.channel.send("pong")

@client.event
async def on_guild_join(guild):
  db[str(guild.id)] = {"prefix": "i/"} #for database support


keep_alive.keep_alive() 
#keep the bot running after the window closes, use UptimeRobot to ping the website at least every <60min. to prevent the website from going to sleep, turning off the bot

#run bot
#Add a secret environment variable named TOKEN in replit (lock icon on left sidebar)
client.run(os.environ.get("TOKEN"))