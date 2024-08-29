import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')

perm = discord.Intents.default()
perm.message_content = True
perm.members = True
bot = commands.Bot(command_prefix="$", intents=perm)

async def load_cogs():
    for file in os.listdir('commands'):
        if file.endswith('.py'):
            await bot.load_extension(f'commands.{file[:-3]}')

@bot.command()
async def bump(ctx:commands.Context):
    if ctx.author.id == xxxxxx:
        sincs = await bot.tree.sync()
        await ctx.reply(f'{len(sincs)} Comandos sincronizados 🔄')
    else:
        await ctx.reply('Você não pode usar esse comando!')

@bot.event
async def on_ready():
    await load_cogs()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Interstellar 🛰️'))
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

bot.run(token)