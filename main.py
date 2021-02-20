import discord
import os
import requests
import json
import random
from replit import db
from discord.ext import commands

bot = commands.Bot(command_prefix="$")

client = discord.Client()



response = requests.get("https://opentdb.com/api.php?amount=50&type=boolean")
response_data = json.loads(response.text)
global question_answer


def plus_one(user):
  if user.id in db.keys():
    db[user.id] = db[user.id] + 1
  else:
    db[user.id] = 1

def minus_one(user):
  if user.profile in db.keys():
    db[user.id] = db[user.id] - 1
  else:
    db[user.id] = -1

def answer_not_allowed():
  global question_answer
  question_answer = False

def get_question():
  randQ = random.randrange(50)
  question = (response_data['results'][randQ]['question'])
  
  return question, randQ;
  


@client.event
async def on_ready():
  print("POGGIES, we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  user = message.author
  #keys = db.keys()
  question, randQ = get_question()
  correct_answer = (response_data['results'][randQ]['correct_answer'])
  incorrect_answer = (response_data['results'][randQ]['incorrect_answers'][0])
  
  if user == client.user: 
    return

  

  if message.content.startswith("Q"): 
    print(str(user) + ' has asked for a question')

    global question_answer
    question_answer = True
    
    myEmbed = discord.Embed(title = "Random Question Alpha V0.4", description = str(question) + ' #' + str(randQ), color = 0x00ff00)
    myEmbed.add_field(name = 'Question Bot PoBoBot', value = 'v0.4 now with better messages and console messages', inline = False)
    myEmbed.add_field(name = 'Date Edited:', value = 'February 19th, 2021', inline = False)
    myEmbed.set_footer(text = "Please answer 'True' or 'False'")

    await message.channel.send(embed = myEmbed)


  elif message.content == correct_answer and question_answer == True:
    response = 'That was correct. +1 point rewarded!'
    plus_one(user)
    print(str(user) + ' now has ' + str(db[user.id]) + ' points')
    answer_not_allowed()
    await message.channel.send(response)

  elif message.content == incorrect_answer and question_answer == True:
    response = 'That was incorrect. reduced 1 point :('
    minus_one(user)
    print(str(user) + ' now has ' + str(db[user.id]) + ' points')
    answer_not_allowed()
    await message.channel.send(response)

  elif message.content == '$points':
    print(str(user) + ' has checked their points')
    await message.channel.send(str(user) + ' has ' + str(db[user.id]) + ' points!')

  #elif message.content == '$leaderboard':
    #print('user has checked leaderboard')
    #await message.channel.send(str(keys))


client.run(os.getenv("TOKEN"))




