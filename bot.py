import os
import discord
from discord.ext import commands
from aiohttp import web
import asyncio

intents = discord.Intents.default()
intents.message_content = True

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

# Web server handler for uptime monitoring
async def handle(request):
    return web.Response(text="Bot is alive")

app = web.Application()
app.router.add_get("/", handle)

async def start_webserver():
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))  # Use PORT env variable or 8080 default
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"🌐 Webserver running on port {port}")

async def main():
    await start_webserver()           # Start the web server
    await bot.start(os.getenv("TOKEN"))  # Start the Discord bot

asyncio.run(main())
