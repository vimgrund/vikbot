import discord
import json
import requests
import os
from heartbeat import start_heartbeat
from utils import download_pic


def main():
    masterAccounts = os.environ['MASTER_ACCOUNTS'].split(',')
    intents = discord.Intents.default()
    intents.message_content = True
    bot = discord.Client(intents=intents)

    @bot.event
    async def on_message(msg):
        if msg.author == bot.user:
            return
        if not msg.content.startswith("!"):
            return

        author = str(msg.author)
        print(f"new message from {author}: {msg.content}")

        author_name = "#".join(author.split('#')[0:-1])

        if author not in masterAccounts:
            await msg.channel.send(f"Hallo {author_name}, scheint, als wolltest du mich zum Arbeiten animieren... ich höre aber nur auf meine Meister q-:")
            return 

        if msg.content == "!ping":
            await msg.channel.send("pong")
            return

        if msg.content == "!sticker":
            for pic in msg.attachments:
                url = pic.url
                filename = download_pic(url)
                await msg.channel.send(f"Hallo {author_name}, file {filename} gespeichert")
            return

        if msg.content == "!help":
            await msg.channel.send(f"Hallo {author_name}, noch kann ich nicht viel...")
            await msg.channel.send("mit \"!sticker\" kannst du mir ein Bild schicken, dass ich dann erstmal speicher und im nächsten Entwicklungsschritt automatisch auf die Homepage hochlade")
            await msg.channel.send("mit \"!help\" bekommst du genau wieder die gleiche Antwort")
            await msg.channel.send("\"!ping\" beantworte ich mit \"pong\"")
            return

        await msg.channel.send(f"Hallo {author_name}, wie kann ich dienen? \nTippe \"!help\" für eine Beschreibung meiner Fähigkeiten")


    start_heartbeat()
    DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
    bot.run(DISCORD_TOKEN)



if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()