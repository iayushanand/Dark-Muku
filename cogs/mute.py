import discord
from discord.ext import commands
from discord.utils import get


class mute(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self,ctx,member:discord.Member):
        await ctx.message.delete()
        try:
            mrole=get(ctx.guild.roles, name='MUTED')

            await member.add_roles(mrole)
            embed=discord.Embed(title='',decription=f'<:mukuyes:840609577308520519> **{member.name}#{member.discriminator}** was muted')

            embed.set_footer(text='Thanks for using Dark Muku')

            await ctx.send(embed=embed)
        
        except AttributeError:
            
            await ctx.send('<:mukuno:840609577053454366> No role named as \'MUTED\' found')
    

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self,ctx,member:discord.Member):
        await ctx.message.delete()
        try:
            mrole=get(ctx.guild.roles, name='MUTED')

            await member.remove_roles(mrole)
            embed=discord.Embed(title='',description=f'<:mukuyes:840609577308520519> **{member.name}#{member.discriminator}** was unmuted')

            embed.set_footer(text='Thanks for using Dark Muku')
            
            await ctx.send(embed=embed)
        
        except AttributeError:
            await ctx.send('<:mukuno:840609577053454366> No role named as `MUTED` found')



def setup(client):
    client.add_cog(mute(client))