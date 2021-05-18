import discord,asyncio,json
from discord import message
from discord.ext import commands

class bug(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases=['bug','reportbug'])
    async def bugreport(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]

        if ctx.guild.id == 840262056553086987:
            channel = self.client.get_channel(840505934115373056)

            em=discord.Embed(title='Bug Report',description='Report a bug by writing your issue below. You have 60 seconds',color=0xff0000)
            msg = await ctx.send(embed=em)
        
        else:
           return await ctx.send(f'This command can only be used in support server do `{pre}support` for more info!')
        
        def check(message):
            return message.channel == ctx.channel and message.author == ctx.author
        
        try:
            messages = await self.client.wait_for('message', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('You did not answer in given time')
        else:
            await msg.edit(content='Bug report is now submitted! Thanks',embed=None)
            embed=discord.Embed(title='Woops! A bug Found 🐛',description=f'{messages.content}')
            embed.set_author(name=f'{ctx.author.name}#{ctx.author.discriminator}',icon_url=f'{ctx.author.avatar_url}')
            await channel.send(embed=embed)
        




def setup(client):
    client.add_cog(bug(client))