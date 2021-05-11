import discord
from discord.ext import commands


class kick_ban(commands.Cogs):
    def __init__(self,client):
        self.client=client
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member,*,reason='No reason'):
        author=f'{ctx.author.name}#{ctx.author.discriminator}'
        await member.kick(reason=f'{author}: [{reason}]')

        embed=discord.Embed(title='',description=f'<:mukuyes:840609577308520519> **{member.name}',color=0x000001)
        embed=discord.Embed(title='',description=f'<:mukuyes:840609577308520519> **{member.name}#{member.discriminator}** was kicked',color=0x123456)

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def kick(Self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]

        embed=discord.Embed(title='Kick',description='Kicks a member from server',color=ctx.author.color)

        embed.add_field('**Syntax**',value=f'{pre}kick `<member>` [reason]')

        embed.add_field('**Perms**',value='Kick Members')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,reason='No reason'):
        author=f'{ctx.author.name}#{ctx.author.discriminator}'

        await member.ban(reason=f'{author}: [{reason}]')
    

def setup(client):
    client.add_cog(kick_ban(client))
