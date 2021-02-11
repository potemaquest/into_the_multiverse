import os
import discord
from discord.ext import commands as discord_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("XAVION_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

discord_bot = discord_commands.Bot(command_prefix="!")


@discord_bot.event
async def on_ready():
    guild = discord.utils.get(discord_bot.guilds, name=GUILD)

    print(
        f"{discord_bot.user} has connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
        )

    members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Members:\n - {members}")


@discord_bot.command(name="streamup", help="")
async def streamup_command(ctx):
    print(ctx.author)
    if ctx.author == discord_bot.user:
        return

    response = "@everyone it appears that the stream is running. The Evil Bottoms are at it again, folks! \n" \
               "https://www.twitch.tv/into_the_multiverse"
    await ctx.send(response)


discord_bot.run(TOKEN)
