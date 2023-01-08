import discord
import json
import requests
import os
from heartbeat import start_heartbeat
from utils import download_pic, ftp_upload


def main():
    masterAccounts = os.environ['VB_MASTER_ACCOUNTS'].split(',')
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

        if msg.content == "!id":
            await msg.channel.send(f"{author} -> {msg.author.id}")
            return

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
                link = ftp_upload(filename, prefix="/vikbot/")
                os.remove(filename)
                await msg.channel.send(f"Hallo {author_name}, file {filename.split('/')[-1]} gespeichert\n{link}")
            return

        if msg.content == "!help":
            await msg.channel.send(f"Hallo {author_name}, noch kann ich nicht viel..."
                                   + "\nmit \"!sticker\" kannst du mir eine Datei schicken, dass ich dann erstmal speicher und im nächsten Entwicklungsschritt automatisch auf die Homepage hochlade"
                                   + "\nmit \"!help\" bekommst du genau wieder die gleiche Antwort"
                                   + "\n\"!ping\" beantworte ich mit \"pong\"")
            return

        await msg.channel.send(f"Hallo {author_name}, wie kann ich dienen? \nTippe \"!help\" für eine Beschreibung meiner Fähigkeiten")



    # start_heartbeat()
    DISCORD_TOKEN = os.environ['VB_DISCORD_TOKEN']
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
