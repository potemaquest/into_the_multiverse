import os
import time
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BRIAN_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f"{bot.user} has connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
        )

    members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Members:\n - {members}")


async def on_member_join(member):
    message = f"oh, why hello there {member}, please please, take a seat. Have some slug stew!"


@bot.command(name="brian", help="<use the !brian command to invoke brian>")
async def brian_command(ctx):
    print(ctx.author)
    if ctx.author == bot.user:
        return

    time.sleep(15)

    response = "err, eh, you'll have to speak up there dearie, i'm a little hard of hearing"
    await ctx.send(response)

    # if "happy birthday" in message.content.lower():
    #     await message.channel.send("Oh! why happy birthday my friend! I had no idea, mmmm... very good, yesh.")


@bot.command(name='roll', help='<simulates rolling dice>')
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
                       f"which, ahem, is a total of ehhhhh, ah! {total}")

bot.run(TOKEN)
