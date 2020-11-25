#imports
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import requests

load_dotenv()
token = os.getenv("TOKEN")

#sets our bots target name
client = commands.Bot(command_prefix= '!')

#Disable Help Command
client.remove_command('help')

#Boot event
@client.event
async def on_ready():

    #Confirms login to the bot in the console
    print('We have logged in as {0.user}'.format(client))

    #Counter variable
    guild_count = 0

    #Loops through each server or guild that this bot is in.
    for guild in client.guilds:
            #Prints the id and name of each guild or server this bot is in.
            print(f"- {guild.id} (name: {guild.name}, Member Number: {guild.member_count})")

            #Adds to guild count
            guild_count = guild_count + 1

    #Tells the console how many guilds/ server the bot is in
    print('{0.user} is in '.format(client) + str(guild_count) + " guilds.")


#Ping command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    print(f'Pong! {round(client.latency * 1000)}ms')
    
@client.event
async def on_message(message):
    check = requests.get(f"https://www.purgomalum.com/service/containsprofanity?text=${message.content}")
    check_ = check.text
    
    if check_ == 'true':
        response = requests.get("https://insult.mattbas.org/api/insult")
        await message.channel.send(response.text)

#Runs the entire bot on the token below
client.run(token)
