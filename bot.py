import discord, os, time, subprocess, re
from discord.ext import commands

bot = commands.Bot(command_prefix='.')
token = 'put ur bot token here'

@bot.command()
async def status(ctx):
    if "Cry.ConsoleApp.exe" in str(os.popen('tasklist').read()):
        await ctx.send('✅ Cry is currently running')
    else:
        await ctx.send('❌ Cry is not currently running')

@bot.command()
async def restart(ctx):
    if "Cry.ConsoleApp.exe" in str(os.popen('tasklist').read()):
        os.system("taskkill /f /im Cry.ConsoleApp.exe")
        p = subprocess.Popen('Cry.ConsoleApp.exe', creationflags=subprocess.CREATE_NEW_CONSOLE)
        await ctx.send('✅ Cry has been restarted and is now running')
    else:
        p = subprocess.Popen('Cry.ConsoleApp.exe', creationflags=subprocess.CREATE_NEW_CONSOLE)
        await ctx.send('❌ Cry was never opened, it is now running')

@bot.command()
async def start(ctx):
    p = subprocess.Popen('Cry.ConsoleApp.exe', creationflags=subprocess.CREATE_NEW_CONSOLE)
    await ctx.send('✅ Cry is now running')

@bot.command()
async def stop(ctx):
    if "Cry.ConsoleApp.exe" in str(os.popen('tasklist').read()):
        os.system("taskkill /f /im Cry.ConsoleApp.exe")
        await ctx.send('✅ Cry was stopped')
    else:
        await ctx.send('❌ Cry was never opened')

bot.run(token)
