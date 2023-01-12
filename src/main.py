import discord
import logging
import os
from utils import *


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
        logging.info(f"new message from {author}: {msg.content}")

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

        if msg.content == "!log":
            with open("../vikbot.log", 'r', encoding='utf-8') as log:
                lines = log.readlines()
                for line in lines:
                    await msg.channel.send("`" + line + "`")
            return

        if msg.content == "!schuh":
            for pic in msg.attachments:
                url = pic.url
                filename = download_pic(url)
                link = ftp_2_upload(filename, prefix="/vikbot/")
                if not link == "¯\\_(ツ)_/¯":
                    os.remove(filename)
                await msg.channel.send(f"Hallo {author_name}, file {filename.split('/')[-1]} gespeichert\n{link}")
            return
        if msg.content == "!sticker":
            for pic in msg.attachments:
                url = pic.url
                filename = download_pic(url)
                link = ftp_1_upload(filename, prefix="/img/stricker/")
                if not link == "¯\\_(ツ)_/¯":
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
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', 
                        filename='../vikbot.log', encoding='utf-8', level=logging.INFO)
    logging.info("nothing to say, just starting my day ¯\_(ツ)_/¯")
    main()
