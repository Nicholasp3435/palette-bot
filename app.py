# imports
import discord
from discord import app_commands
import json

from PIL import ImageFont, ImageColor

import color as colour

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
    try:
        colour.default_color_box(color)
        file = discord.File('resources/temp.png', filename="color.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://color.png")
        await interaction.response.send_message(
            file=file,embed=embed,content = "You said this color: " + color)
    except:
        await interaction.response.send_message("Could not find color: " + color)

@tree.command(name = "complement",\
    description = "Displays the color and complementary color inputted",\
    guild=discord.Object(serverIDs[select]))
async def send(interaction, color: str):
    try:
        complement = colour.complement(color)
        colour.default_color_box(color, 1)
        colour.default_color_box(complement, 2)
        colour.im_cat('resources/temp1.png', 'resources/temp2.png').save('resources/temp.png')

        file = discord.File('resources/temp.png', filename="color.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://color.png")
        await interaction.response.send_message(
            file=file,embed=embed)
    except:
        await interaction.response.send_message("Could not find color: " + color)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=serverIDs[select]))
    print("Ready!")

def run():
    client.run(info['token'])
