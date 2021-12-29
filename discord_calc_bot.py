import discord
from discord.ext import commands
import asyncio

import random

from math import sqrt, sin, cos, tan
from math import asin as arcsin, acos as arccos, atan as arctan
from math import pi, e, degrees as deg, radians as rad, log


bot = commands.Bot(command_prefix = '#')

@bot.event
async def on_ready():
    print('Ready')

@bot.event
async def on_message(message):
    if message.content.startswith("#help"):
        await message.channel.send(help())

    if message.content.startswith("#calc"):
        try:
            await message.channel.send(evaluate_math(message.content[6:]))
        except:
            await message.channel.send("Check your inputs")
    
        
    if message.content.startswith ("#quadratic"):
        try:
            A, B, C = [int(i) for i in message.content[11:].split(", ")]
            await message.channel.send(quadratic(A, B, C))
        except:
            await message.channel.send("Check your inputs")     

def help():
    return ('To use the simple calculator, type "#calc [question]". \n' +
    '[question] can include\n' + 
    'Operators: +, -, *, /, // (integer division), ' + 
    '** (exponent). \n' +
    'Functions: sin(x), cos(x), tan(x), arcsin(x), arccos(x), ' + 
    'arctan(x), sqrt(x), log(x), abs(x).\n' +
    'Constants: pi, e.\n' +
    'Ambiguities: Trig related functions take in radians as input. Use ' +
    'rad(x) to convert to degrees and deg(x) to convert to radians.\n' +
    'log(x) is the logarithm base-e.\n\n' +
    'To use the quadratic solver, type "#quadratic A, B, C"\n' +
    'Example: "#quadratic 1, -1, -1"')

def evaluate_math(message):
    answer = round(eval(message), 10)
    format_answer = "The answer to " + str(message) + " is " + str(answer)
    return format_answer

def quadratic(a, b, c):
    DISC = b**2 - 4*a*c

    if DISC < 0:
        return "This equation has no roots"
    elif DISC == 0:
        x = round((-b + sqrt(DISC)) / 2*a, 10)
        format_x = "The root is " + str(x)
        return format_x
    else:
        x1 = round((-b + sqrt(DISC)) / 2*a, 10)
        x2 = round((-b - sqrt(DISC)) / 2*a, 10)
        format_x1_x2 = "The roots are " + str(x1) + " and " + str(x2)
        return format_x1_x2


bot.run('YOUR_DISCORD_TOKEN')

input()
