import discord
from discord.ext import commands

#made by @sen#0069



client = commands.Bot(command_prefix = '/')


@client.command()
async def say(*args):
    output = ""
    for word in args:
        output += word
        output += ' '
    await client.say(output)
	
	@client.command()
async def say(*args):
    output = ""
    for word in args:
        output += word
        output += ' '
    if user.id = '378254357835284490'    
        await client.say(output)
    else:
        pass                           


client.run('NTE1NjQ2Mzg4NjUxMTYzNjY5.DtoNcg.MbUGs0Ag6dO4lkOoIbblf1ImL0g')