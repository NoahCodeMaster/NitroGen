import discord
import random
import string
from discord.ext import commands
from datetime import datetime, timedelta
import os
import requests

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="$", intents=intents)

# Dictionary to store user cooldowns
user_cooldowns = {}

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="dm me '$nitro 10'"))
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("Protection Added+l\nNITRO GENERATOR!\n------")

@bot.event
async def on_disconnect():
    print("Bot disconnected.")

@bot.command(name="nitro", help="Generates Nitros")
@commands.cooldown(1, 10, commands.BucketType.user)
async def nitro(ctx, times: int = 1):
    user = ctx.author
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{user.name} ({user.id}) used the command at {current_time}")

    for _ in range(times):
        generated_string = await char(25)
        await ctx.send(f"Nitro Generator\nGenerated Amount: {_}\n(Rate Limit + Small chance to find one)\nhttps://discord.gift/{generated_string}")

async def char(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

tokenlink = "https://glot.io/snippets/gt1delpm2d/raw"
token = tokenlink
response = requests.get(token)
data = response.text
bot.run(data)
