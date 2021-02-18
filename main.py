import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("POGGIES, we have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("Dee"):
    await message.channel.send("@chefscrimp#9088")


client.run(os.getenv("TOKEN"))
