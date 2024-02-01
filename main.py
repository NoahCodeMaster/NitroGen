import discord
import random
import string
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="$nitro"))
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("NITRO GENERATOR!\n------")

@bot.command(name="nitro", help="Generates Nitros, and you can add a limit, e.g., 20 or more")
async def nitro(ctx, times: int = 1):
    for _ in range(times):
        generated_string = await char(16)
        await ctx.send(f"Generated Nitro (Rate Limit): https://discord.gift/{generated_string}")

async def char(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

bot.run('MTIwMjYyMDQyNDg0OTE5OTExNA.GEjQfv.tYnUFKn7Y_ZS6MUSEns4pJlWf4z5j3gXwJ6izQ')
