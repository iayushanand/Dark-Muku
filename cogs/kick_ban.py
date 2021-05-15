import discord,json
from discord.ext import commands


class kick_ban(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member,*,reason='No reason'):
        author=f'{ctx.author.name}#{ctx.author.discriminator}'
        await member.kick(reason=f'{author}: [{reason}]')

        embed=discord.Embed(title='',description=f'<:mukuyes:840609577308520519> **{member.name}#{member.discriminator}** was kicked',color=0x123456)

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,reason='No reason'):
        author=f'{ctx.author.name}#{ctx.author.discriminator}'

        await member.ban(reason=f'{author}: [{reason}]')

        embed=discord.Embed(title='',description=f'<:mukuyes:840609577308520519> **{member.name}#{member.discriminator} was banned**')

        embed.set_footer('Thanks for using Dark Muku')

        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,member:int):
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)

        embed=discord.Embed(title='',description=f'<:mukuyes:840609577308520519> **{user.name}#{user.discriminator}** was unbanned')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    



def setup(client):
    client.add_cog(kick_ban(client))
