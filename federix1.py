import discord
from discord.utils import get
from discord.ext import commands
from federix2 import songAPI 

bot = commands.Bot(command_prefix='#',help_command=None)

songsInstance = songAPI()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def test(ctx, *, par):
    await ctx.channel.send("You typed {0}".format(par))

@bot.command() 
async def help(ctx):
    emBed = discord.Embed(title="คำสั่งต่างๆ", description="All available bot commands", color=0x002053)
    emBed.add_field(name="#play + url", value="play music", inline=False)
    emBed.add_field(name="#pause", value="pause music", inline=False)
    emBed.add_field(name="#resume", value="resume music", inline=False)
    emBed.add_field(name="#stop", value="stop music", inline=False)
    emBed.add_field(name="#leave", value="bot leave", inline=False)
    emBed.add_field(name="#queueList", value="see queueList", inline=False)
    emBed.set_thumbnail(url='https://lh3.googleusercontent.com/zJ17xXWcMtoVGEmykCcjL7ig73sqwPkuqxNEX6AXQELPZp9NVibQgbov0B62qyVcnPCc=s85?fbclid=IwAR0iqkVJtoCDevZKreg0aXPmdOELTvLoMV7p4Qp1rSyJtgbTx3TdCVGvjrU')
    emBed.set_footer(text='FeDeRiX-Bot', icon_url='https://lh3.googleusercontent.com/zJ17xXWcMtoVGEmykCcjL7ig73sqwPkuqxNEX6AXQELPZp9NVibQgbov0B62qyVcnPCc=s85?fbclid=IwAR0iqkVJtoCDevZKreg0aXPmdOELTvLoMV7p4Qp1rSyJtgbTx3TdCVGvjrU')
    await ctx.channel.send(embed=emBed)

@bot.command() 
async def play(ctx,* ,search: str):
    await songsInstance.play(ctx, search)

@bot.command()
async def stop(ctx):
    await songsInstance.stop(ctx)

@bot.command()
async def pause(ctx):
    await songsInstance.pause(ctx)

@bot.command()
async def resume(ctx):
    await songsInstance.resume(ctx)

@bot.command()
async def leave(ctx):
    await songsInstance.leave(ctx)

@bot.command()
async def queueList(ctx):
    await songsInstance.queueList(ctx)

@bot.command()
async def skip(ctx):
    await songsInstance.skip(ctx)
    
bot.run('yourbottoken')
