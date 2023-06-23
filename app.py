# imports
import discord
from discord import app_commands
import json

import color

# server IDs
serverIDs = [371696021316829186,869449259139878922]
select = 1

with open('info.json') as json_file:
    info = json.load(json_file)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
intents.message_content = True

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@tree.command(name = "test",\
    description = "My first application Command",\
    guild=discord.Object(serverIDs[select]))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name = "color-box",\
    description = "Makes a box of the color specified",\
    guild=discord.Object(serverIDs[select]))
async def send(interaction, color: str):
    await interaction.response.send_message("You said this color: " + color)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=serverIDs[select]))
    print("Ready!")

def run():
    client.run(info['token'])
