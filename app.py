# imports
import discord
from discord import app_commands
import json

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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@tree.command(name = "test",\
    description = "My first application Command",\
    guild=discord.Object(serverIDs[select]))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=serverIDs[select]))
    print("Ready!")

def run():
    client.run(info['token'])
