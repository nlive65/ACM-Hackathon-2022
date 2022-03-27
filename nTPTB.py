from discord.ext import commands
import json
import os
from lib2to3.pgen2.tokenize import tokenize
import translators as translate




if os.path.exists(os.getcwd() + "/config.json"):
    with open(".\config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"token": ""}
    with open(os.getcwd() + "/config.json","w+") as f:
        json.dump(configTemplate,f)


bot = commands.Bot(command_prefix='$', help_command = None)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

async def help(ctx, target_language = 'en'):
    
    return await ctx.send("yay")

class translator(commands.Cog):
    def __init__(self,bot): 
        global langDict
        self.bot = bot
        file = open('countries.txt','r')
        langDict = {}
        f = file.readlines()
        for line in f:
            words = line.split()
            langDict[words[0].lower()] = words[1]
        file.close()
    @commands.command(name = "help")
    async def help(self, ctx, target_language = 'en'):
        return await ctx.send("yay")


    @commands.command(name='hello')
    async def test(self,ctx):
        """ returns hello"""
        return await ctx.send("Hello, world!")

    @commands.command(name='echo')
    async def echo(self, ctx, *, message):
        return await ctx.send(message)
   
    @commands.command(name='translate', aliases = ['tl', 'Tl', 'tL', 'TL'])
    async def translate(self, ctx, from_language, to_language, *, message):
        translated_message = translate.google(message, str(from_language), str(to_language))
        return await ctx.send(translated_message[0])

    @commands.command(name = 'TranslateTTs', aliases = ['tltts'])
    async def translateTTS(self,ctx, from_language, to_language,*, message):
         translated_message = translate.google(message, str(from_language), str(to_language))
         return await ctx.send(translated_message, tts=True)


    @commands.command(name = 'languagGuide', aliases = ['lG', 'lg', 'Lg'])
    async def countryGuide(self, ctx):
        file = open("countries.txt",'r')
        await ctx.send(file.read())
        file.close()

    @commands.command(name = 'languageSearch', aliases = ['ls', 'Ls', 'lS', 'LS'])
    async def languageSearch(self,ctx,*,language):
        return await ctx.send(langDict[language.lower()])
token  = configData["token"]
def setup(bot):
    bot.add_cog(translator(bot))
setup(bot)
bot.run(token)

