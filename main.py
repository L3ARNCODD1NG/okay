import discord
import requests
from discord.ext import commands
from discord import file
from discord.utils import get
import os
import json
import urllib.parse
import datetime

client = commands.Bot(command_prefix='?')

@client.command()
@commands.cooldown(3, 300, commands.BucketType.user)
async def totalusers(ctx):
  
   discID = ctx.author.id
   b = requests.get(f"https://lexarmguiv2.online/api/apimain?totalusers")
  
   response = b.text
  
   message = (f"```yaml\nTotal Users : {response}```")
   embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52)
   embedVar.timestamp = datetime.datetime.utcnow()
   embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png") 
   await ctx.channel.send(embed=embedVar)

@client.command()   
async def totalgames(ctx):
  
   discID = ctx.author.id
   b = requests.get(f"https://lexarmguiv2.online/api/apimain?totalgames")
  
   response = b.text
  
   message = (f"```yaml\nTotal Games : {response}```")
   embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52)
   embedVar.timestamp = datetime.datetime.utcnow()
   embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png") 

   await ctx.channel.send(embed=embedVar)
    
@client.command()    
async def lexarv2commands(ctx):
  
   discID = ctx.author.id
   b = requests.get(f"https://lexarmguiv2.online/api/apimain?totalgames")
  
   response = b.text
  
   message = (f"**Commands**\n```yaml\ntotalusers\ntotalgames\nlexarv2info <Lexar Username>\nlexarv2token <Token Here>\nlexarv2features\nlexarv2forgotpass <Lexar Username>```")
   embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52)
   embedVar.timestamp = datetime.datetime.utcnow()
   embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png") 
   await ctx.channel.send(embed=embedVar)

@client.command()    
async def lexarv2info(ctx, username):
  
  discID = ctx.author.id
  
  r = requests.get(f"https://lexarmguiv2.online/api/apimain?lexarinfo={username}")
  response = r.text
  
  if response == 'User Not Found':
       message = (f"```yaml\nUser Not Found```")
       embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52,)
       embedVar.timestamp = datetime.datetime.utcnow()
       embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png") 
       await ctx.channel.send(embed=embedVar)
  else:
      jsoninfo = json.loads(response)
      message = (f"**Site Username** : "+username+"\n**Site ID** : "+jsoninfo["SiteId"]+"\n**Discord** : <@"+jsoninfo["Discord"]+">\n```yaml\nTotal Points : "+str(jsoninfo["TotalPoints"])+"\nTotal Robux : R$ "+str(jsoninfo["TotalRobux"])+"\nTotal Credits : $"+str(jsoninfo["TotalCredits"])+"```")
      embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52)
      embedVar.set_thumbnail(url=jsoninfo["ProfilePic"])
      embedVar.timestamp = datetime.datetime.utcnow()
      embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png")
      await ctx.channel.send(embed=embedVar)

@client.command()    
async def lexarv2token(ctx, token):
  
  discID = ctx.author.id
  
  r = requests.get(f"https://lexarmguiv2.online/api/apimain?tokencheck={token}")
  response = r.text
  
  if response == 'Token Not Found':
       message = (f"```yaml\nToken Not Found```")
       embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52,)
       embedVar.timestamp = datetime.datetime.utcnow()
       embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png")  
       await ctx.channel.send(embed=embedVar)
  elif response == 'No User use this token':
       message = (f"```yaml\nNo User use this token you can register it```\n[**[Register Here]**](https://rbxlexarv2.site/register)")
       embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52,)
       embedVar.timestamp = datetime.datetime.utcnow()
       embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png") 
       await ctx.channel.send(embed=embedVar)
  else:
      jsoninfo = json.loads(response)
      message = (f"This token is taken by **"+str(jsoninfo["Username"])+"**\n **Discord** : <@"+str(jsoninfo["Discord"])+">")
      embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52)
      embedVar.timestamp = datetime.datetime.utcnow()
      embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png") 
      await ctx.channel.send(embed=embedVar)
      
@client.command()    
async def lexarv2features(ctx):
  
  discID = ctx.author.id
  
  message = (f"\n**Feature**\n```yaml\n-Security Checker\n-Account Age Checker\n-Membership Checker\n-7 Webhooks\n-Map Picker\n-Ingame Configuration```\n\n**Login Checker**\n\n```yaml\n-Auto Profit\n-Revenue Checker\n-Security Checker\n-Email Checker\n-Robux Checker\n-Credit Checker\n-Rap Checker\n-Auto Submit Captcha Checker\n-Join Date Checker\n-Cookie Grabber```")
  embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52,)
  embedVar.timestamp = datetime.datetime.utcnow()
  embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png") 
  await ctx.channel.send(embed=embedVar)
  
@client.command()
@commands.cooldown(2, 200, commands.BucketType.user)
async def lexarv2forgotpass(ctx,username):
  
  discID = ctx.author.id
  
  r = requests.get(f"https://lexarmguiv2.online/api/apimain?forgotpass={username}")
  response = r.text
  
  if response == 'Successfully Sent':
       message = (f"```yaml\nSuccessfully sent to your email```")
       embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52,)
       embedVar.timestamp = datetime.datetime.utcnow()
       embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png")  
       await ctx.channel.send(embed=embedVar)
  else:
       message = (f"```yaml\n{response}```")
       embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52,)
       embedVar.timestamp = datetime.datetime.utcnow()
       embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png") 
       await ctx.channel.send(embed=embedVar)
  
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Watching Pornhub ?lexarv2commands'))
    
@client.event
async def on_command_error(ctx, error):
   if isinstance(error, commands.CommandOnCooldown):
        message = (f"```yaml\nCommand Cooldown Try again in {round(error.retry_after, 2)} Seconds```")
        embedVar = discord.Embed(title="Lexar v2 MGUI", description=message, color=0x001f52,)
        embedVar.timestamp = datetime.datetime.utcnow()
        embedVar.set_footer(text='Lexar v2 MGUI',icon_url="https://cdn.discordapp.com/attachments/960931740493447242/986996220583108638/emaxlogo.png")
        await ctx.channel.send(embed=embedVar)
  

client.run(os.environ['token'])
