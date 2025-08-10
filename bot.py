import os
import discord
from discord.ext import commands

# Get bot token from Render's environment variable
TOKEN = os.getenv("TOKEN")

# Bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def manualsys(ctx):
    message = (
        "Hello, please complete the manual key system with the link below and join the server it leads to, "
        "then show proof of completion and click on the checkpoint 2 channel and complete the second checkpoint: "
        "https://rinku.pro/manual1"
    )
    await ctx.send(message)

# Run the bot
bot.run(TOKEN)
