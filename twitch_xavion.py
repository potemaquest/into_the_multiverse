import os
import time
import random
import twitchio.client
from twitchio.ext import commands as twitch_commands
from dotenv import load_dotenv

load_dotenv()

twitch_client = twitchio.client.Client()

twitch_bot = twitch_commands.Bot(
    irc_token=os.getenv("TMI_TOKEN"),
    client_id=os.getenv("CLIENT_ID"),
    nick=os.getenv("BOT_NICK"),
    prefix=os.getenv("BOT_PREFIX"),
    initial_channels=[os.getenv("CHANNEL")]
)


@twitch_bot.event
async def event_ready():
    # Called once when the bot goes online.
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = twitch_bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@twitch_bot.event
async def event_message(ctx):
    # Runs every time a message is sent in chat.

    # make sure the bot ignores itself and the streamer
    # if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
    #     return
    await twitch_bot.handle_commands(ctx)


@twitch_bot.command(name="discord")
async def test(ctx):
    await ctx.send("Did you know? Into the Multiverse has a community discord!"
                   " Join us at: https://discord.gg/hjzvcbM5rq")


@twitch_bot.command(name="roll")
async def roll(ctx, number_of_dice, number_of_sides):
    applicable_sides = ["4", "6", "8", "10", "12", "20", "100"]
    if number_of_sides not in applicable_sides:
        await ctx.send("please choose an applicable type of dice")
    else:
        time.sleep(3)
        dice_number = int(number_of_dice)
        sides_number = int(number_of_sides)
        roll = []
        for _ in range(dice_number):
            die = random.choice(range(1, sides_number + 1))
            roll.append(die)

        total = 0
        for dice in roll:
            total = total + int(dice)
        await ctx.send(f"you rolled: \n{roll} \n"
                       f"which is a total of: {total}")

twitch_bot.run()
