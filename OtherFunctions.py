#make sure to remove the other on_guild_channel_create if you use this
@bot.event
async def on_guild_channel_create(channel):
 while True:
  async with aiohttp.ClientSession() as session:
    with open(('YOURFILEDIRECTORYHERE.png'), 'rb') as f:
      img = f.read()
    webhook = await channel.create_webhook(name='Webhook',avatar=img)
    await webhook.send("@everyone")
    await webhook.delete()

