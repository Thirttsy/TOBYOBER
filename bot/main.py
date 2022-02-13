#TOBY v 1.2
#imports----------------------------------
import discord
import datetime
from discord.ext import commands
import os
import time
import random
import youtube_dl
from youtube_search import YoutubeSearch
from keep_alive import keep_alive
global enablerepeat 
enablerepeat = False

#module imports
import chatlogger


#-----------------------------------------
chatlog_file_read = open("chatlogs.txt", "r")
client = commands.Bot(command_prefix="hey toby, ")
printdate = False
today = datetime.datetime.now()
players = {}
remove_these = "'}]'"
#boot up message
@client.event
async def on_ready():
    print('Logged in as TOBY')

#echo me command
@client.command()
async def rep(ctx, arg):
  await ctx.channel.purge(limit=1)
  await ctx.channel.send(arg)

#handles most text based events
@client.event
async def on_message(message):
    if message.author == client.user:
      return
       
#Commands-----------------------------------------------------------
    """if message.content.startswith('!help'):
       await message.channel.send('List of commands')
       await message.channel.send('!help --------- you already know this one')
       await message.channel.send('!pasta')
       await message.channel.send('!tboy --------- TOBY #1 ENEMY PIC')
       await message.channel.send('!ping --------- pings ryeden')
       await message.channel.send('!bakaorsaka --- what are you?')
       await message.channel.send('!play --------- used for playing music')

    if message.content.startswith('!sus'):
        await message.channel.send('https://www.youtube.com/watch?v=grd-K33tOSM')

    if message.content.startswith('!tboy'):
      await message.channel.send('https://cdn.discordapp.com/attachments/829065426629427250/886509567427625000/tboy.png')"""

#Responses----------------------------------------------------------------
    #he really does tho
    if message.content.startswith('bobby'):
        await message.channel.send('bobby loves among us')
    #bobbypasta
    bobbypasta = [
      'Context?\nPlz',
      'Thats not normal',
      "I don't get it",
      "...",
      'ok "goes invisible"'
    ]

    if message.content.startswith('https://'):
        BPresponse = random.choice(bobbypasta)
        await message.channel.send(BPresponse)
      #  await message.channel.send('Context?')
      #  await message.channel.send('Plz')
    #giraffe
    if message.content.startswith('why do giraffes have long necks'):
        await message.channel.send('because their feet smell!!!')
    #newmodule
    chatlogger.store(message.content, today, printdate)
  

    if message.content != "":
      randints = [1,2,3]
      rand = random.choice(randints)
      if rand == 2 or rand == 3 or rand == 0:
        chatloglines = chatlogger.getlines()
        await message.channel.send(chatloglines[random.randint(0,len(chatloglines))])
        pass


    #-----------
    #talking toby-----------------------------------
    Random_Toby = [
      'im toby',
      'what',
      'really',
      'sup',
      'im not a bot',
      'hey'
    ]

    Random_Pissed_Toby = [
      'its TOBY dumbass',
      'im not TBOY',
      'check your spelling',
      'its TOBY',
      'https://tenor.com/view/napoleon-napoleon-bonaparte-minor-spelling-mistake-i-win-gif-23037131'
    ]

    Random_Yober = [
        'yober',
        'yober?',
        'yober!',
        'yober.'
    ]

    if message.content == 'tboy':
        pissed_response = random.choice(Random_Pissed_Toby)
        await message.channel.send(pissed_response)

    if message.content.startswith('toby') or message.content.startswith('TOBY') or message.content.startswith('Toby'):
        response = random.choice(Random_Toby)
        await message.channel.send(response)

    if message.content.startswith('yober') or message.content.startswith('Yober') or message.content.startswith('YOBER'):
      yober_response = random.choice(Random_Yober)
      #await message.channel.send(yober_response)

    #you're your module
    if message.content.startswith('you\'re') or  message.content.startswith('You\'re'):
        await message.channel.send('https://tenor.com/view/your-youre-spies-in-disguise-your-spies-gif-20405823')
    if message.content.startswith('your') or  message.content.startswith('Your'):
        await message.channel.send('https://tenor.com/view/youre-your-spies-spies-in-disguise-youre-spies-gif-20405819')

    #toby ping-------------------------------------------
    if message.content.startswith('!ping'):
        await message.channel.send('<@685179672702877701>')
        
    #baka or saka
    if message.content.startswith('!bakaorsaka'):
      Baka_Or_Saka = [
        'You are a Bussy Saka',
        'You are a Sussy Baka'
      ]
      BOS = random.choice(Baka_Or_Saka)
      await message.channel.send(BOS)

    #TOBY 1984----------------------------------------
    badwords = [
      'bad',
      'Bad',
      'Toby sucks',
      'toby sucks',
      'fuck toby',
      'Fuck toby',
      'stupid toby',
      'Stupid toby',
      'Toby stupid',
      'toby stupid'
    ]
    if message.content in (badwords):
        await message.channel.send('https://tenor.com/view/1984-skander-big-brother-gif-21303304')
        await message.channel.purge(limit=2)
    #when the imposter is sus finisher
    if message.content.startswith('when'):
        await message.channel.send('when the')
        await message.channel.send('when the imposter is sus')
    await client.process_commands(message)

    if message.author.id == 700770926651899935 and message.content == ('delete 20'):
      await message.channel.send ('ok')
      await message.channel.purge(limit=20)
    
    if message.author.id != 700770926651899935 and message.content == ('delete 20'):
      await message.channel.send('nope, I wont do that for you')
#VC stuff --------------------------------------------------------------
@client.command()
async def download(ctx, inputsearch):
  print("attempting to play music")
  #gets the guild... whatever that is
  guild = ctx.guild

  #searches for music on youtube
  search = inputsearch
  print(search)
  results = YoutubeSearch(search, max_results=1).to_dict()

  print(results)
  ident, thumbnails, title, long_desc, channel, duration, views, publish_time, i_fogor, url_suffix = str(results).split(": ")
  print(url_suffix)
  unmodified_url = 'https://youtube.com' + url_suffix
  print(unmodified_url)
  for character in remove_these:
    url = unmodified_url.replace(character, "")
  print(url)
  song_there = os.path.isfile("song.mp3")
  try:
      if song_there:
          os.remove("song.mp3")
  except PermissionError:
      await ctx.send("Wait for the current playing music to end or use the 'stop' command")
      return
  ydl_opts = {
        'format': 'bestaudio/best',
         'postprocessors': [{
             'key': 'FFmpegExtractAudio',
             'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
  for file in os.listdir("./"):
      if file.endswith(".mp3"):
          os.rename(file, str(inputsearch)+".mp3")

@client.command()
async def play(ctx, inputsong):
  guild = ctx.guild
  #plays the music that was searched
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
  #connects to VC
  await voiceChannel.connect()
  voice_client: discord.VoiceClient = discord.utils.get(client.voice_clients, guild=guild)
  voice_client.play(discord.FFmpegPCMAudio(str(inputsong)+".mp3"), after=None)

#--------------------------------------------------------------------------
#@client.command()
#async def pog(ctx):
#  print('ran')

#--------------------------------------------------------------------------
#gets toby's token
keep_alive()
time.sleep(0.5)
server.server()
client.run(os.getenv('TOKEN'))
