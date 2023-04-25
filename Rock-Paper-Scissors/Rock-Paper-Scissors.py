
import discord, random
from discord.ext import commands

TOKEN = "MTEwMDAyNTIyNDA1MDc2OTk2MQ.GbF7tO.9EIEw6e7GSSujnmawdY-RqyJ9FXrgYkS-77Wss"


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print('bot is ready')

@bot.command(name='play')
async def play(ctx, player_choice):
    player_choice = player_choice.upper()
    print("Debug: Starting game.")

    options = ["ROCK", "PAPER", "SCISSORS"]
    
    if player_choice not in options:
        await ctx.channel.send("Invalid option!")
    else:
        bot_choice = random.choice(options)
        if bot_choice == player_choice:
            await ctx.channel.send(f"It's a TIE... \nBOT has chosen: {bot_choice}     PLAYER chose: {player_choice}")
        elif bot_choice == "ROCK" and player_choice == "SCISSORS":
            await ctx.channel.send(f"Bot Won!... \nBOT has chosen: {bot_choice}   PLAYER chose: {player_choice}")
        elif bot_choice == "PAPER" and player_choice == "ROCK":
            await ctx.channel.send(f"Bot Won!... \nBOT has chosen: {bot_choice}   PLAYER chose: {player_choice}")
        elif bot_choice == "SCISSORS" and player_choice == "PAPER":
            await ctx.channel.send(f"Bot Won!... \nBOT has chosen: {bot_choice}   PLAYER chose: {player_choice}")
        else: 
            await ctx.channel.send(f"Player Won!... \nBOT has chosen: {bot_choice}    PLAYER chose: {player_choice}")
    
bot.run(TOKEN)