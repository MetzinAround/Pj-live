import discord
import twitch
import config as conf

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
helix = twitch.Helix(conf.twitch_client, conf.twitch_secret)

print(helix.streams())

    

#use Twitch API read the notification that I am live (event emitter), if I am live, post a message on Discord. 