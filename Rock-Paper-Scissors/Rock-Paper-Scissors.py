
import discord, random
from discord.ext import commands

def convert_string_to_emoji(prompt):
    if prompt == "SCISSORS":
        return ":scissors:"
    elif prompt == "ROCK":
        return ":rock:"
    elif prompt == "PAPER":
        return ":newspaper:"
TOKEN = "TOKEN"


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
            await ctx.channel.send(f"BOT has chosen: {convert_string_to_emoji(bot_choice)}     PLAYER chose: {convert_string_to_emoji(player_choice)} \nIt's a TIE...:yawning_face:")
        elif bot_choice == "ROCK" and player_choice == "SCISSORS":
            await ctx.channel.send(f"BOT has chosen: {convert_string_to_emoji(bot_choice)}   PLAYER chose: {convert_string_to_emoji(player_choice)} \nBot Won!:robot:")
        elif bot_choice == "PAPER" and player_choice == "ROCK":
            await ctx.channel.send(f"BOT has chosen: {convert_string_to_emoji(bot_choice)}   PLAYER chose: {convert_string_to_emoji(player_choice)} \nBot Won!:robot:")
        elif bot_choice == "SCISSORS" and player_choice == "PAPER":
            await ctx.channel.send(f"BOT has chosen: {convert_string_to_emoji(bot_choice)}   PLAYER chose: {convert_string_to_emoji(player_choice)} \nBot Won!:robot:")
        else: 
            await ctx.channel.send(f"BOT has chosen: {convert_string_to_emoji(bot_choice)}    PLAYER chose: {convert_string_to_emoji(player_choice)} \n Player Won!:partying_face:")

bot.run(TOKEN)