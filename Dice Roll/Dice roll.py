# Bot token "MTEwMDAyNTIyNDA1MDc2OTk2MQ.GbF7tO.9EIEw6e7GSSujnmawdY-RqyJ9FXrgYkS-77Wss"

import discord, random
from discord.ext import commands

TOKEN = "MTEwMDAyNTIyNDA1MDc2OTk2MQ.GbF7tO.9EIEw6e7GSSujnmawdY-RqyJ9FXrgYkS-77Wss"


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print('bot is ready')


@bot.command(name='roll')
async def roll(ctx):
    print("Debug: Rolling dice.")

    dice_numbers = [1,2,3,4,5,6]
    team_1_roll = random.choice(dice_numbers)
    team_2_roll = random.choice(dice_numbers)
    
    await ctx.channel.send(f"Team 1 rolled, {team_1_roll}")

    await ctx.channel.send(f"Team 2 rolled, {team_2_roll}")
    
    if team_1_roll == team_2_roll:
        await ctx.channel.send("It's a Tie!")
    elif team_1_roll > team_2_roll:
        await ctx.channel.send("Team 1 has Won!")
    else:
        await ctx.channel.send("Team 2 has Won!")


bot.run(TOKEN)
