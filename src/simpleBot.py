import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hallo(ctx):
    await ctx.send('Test123')



DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
bot.run(DISCORD_TOKEN)