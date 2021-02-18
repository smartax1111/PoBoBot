import discord
import os
import requests
import json
import random

client = discord.Client()

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response_data = json.loads(response.text)

def get_question():
  randQ = random.randrange(10)
  question = (response_data['results'][randQ]['question'])
  return question
  

@client.event
async def on_ready():
  print("POGGIES, we have logged in as {0.user}".format(client))

@client.event
async def on_message(message): 
  if message.author == client.user: return

  if message.content.startswith("Q"):
    question = get_question()
    await message.channel.send(question)

    async def check(reaction, user):
      return user == message.author and user.content == str((response_data['results'][randQ][correct_answer]))

      try:
        reaction, user = await client.wait_for('message', timeout=60.0, check=check)
      except asyncio.TimeoutError:
        await channel.send(str(response_data['results'][randQ][incorrect_answer]))
      else:
        await channel.send(str(response_data['results'][randQ][correct_answer]))
      

    


client.run(os.getenv("TOKEN"))

