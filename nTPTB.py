from discord.ext import commands
import json
import os
import nltk
from lib2to3.pgen2.tokenize import tokenize
import translators as ts

if os.path.exists(os.getcwd() + "/config.json"):
    with open(".\config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"token": ""}
    with open(os.getcwd() + "/config.json","w+") as f:
        json.dump(configTemplate,f)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


class translator(commands.Cog):
    def __init__(self,bot): 
        self.bot = bot

    @commands.command(name= "test")
    async def test(self,ctx,*,message):
        puncts = nltk.tokenize.wordpunct_tokenize(message)  
        return await ctx.send(puncts)

    @commands.command(name='hello')
    async def test(self,ctx):
        return await ctx.send("Hello, world!")

    @commands.command(name='echo')
    async def echo(self, ctx, *, message):
        return await ctx.send(message)
   
    @commands.command(aliases=['translate', 'tl', 'tr'])
    async def translator(self, ctx, from_language, to_language, *, message):
        translated_message = ts.google(message, str(from_language), str(to_language))
        return await ctx.send(translated_message)

token  = configData["token"]
def setup(bot):
    bot.add_cog(translator(bot))
setup(bot)
bot.run(token)
