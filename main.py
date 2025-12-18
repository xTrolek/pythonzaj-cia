import discord
from discord.ext import commands
from bot_logic import gen_pass
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć')
@bot.command()
async def mis(ctx):
    await ctx.send(f":bear:")
@bot.command()
async def slon(ctx):
    await ctx.send(f":elephant:")
@bot.command()
async def haslo(ctx):
    await ctx.send(gen_pass(10))
@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
@bot.command()
async def joined(ctx, member: discord.Member):
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def losuj(ctx):
    x = random.randint(1,100000)
    await ctx.send(f"🎲 Wylosowana liczba: **{x}**")
@bot.command()
async def blackjack(ctx):
    r = random.randint(1, 3)
    if r==1:
        wynik = ':red_square:'
    elif r==2:
        wynik = ':black_large_square:'
    else:
        wynik = ':green_square:'
    await ctx.send(f"Wylosowałeś: {wynik}")
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency*1000)} ms")



bot.run('TOKEN')
