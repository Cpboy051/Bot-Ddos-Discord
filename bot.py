import discord
import os, sys
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.event
async def on_ready():
    activity = discord.Game(name="By Xalbador", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")


@bot.command()
async def ddos(ctx, ip: str = None, port: int = None):
    if ip is None:
        await ctx.send('Input ip')
    elif port is None:
        await ctx.send('Input port')
    else:
        await ctx.send(f'Attack to {ip} {port}')
        os.system(f'python ddos.py {ip} {port}')

bot.run("token")