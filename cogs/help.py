import discord,json
from discord.ext import commands





class help_cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        color=ctx.author.color

        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]

        embed=discord.Embed(title='Help Commands',description=f'Use `{pre}help <category>` for more info on that category',color=color)

        embed.add_field(name='Moderation',value='Shows all moderation commands')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command(aliases=['Moderation','mod'])
    async def moderation(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]

        embed=discord.Embed(title='Moderation Commands',description=f'Use `{pre}help <command>` for more info on that command',color=ctx.author.color)

        embed.add_field(name='Commands',value='kick')

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


def setup(bot):
    bot.add_cog(help_cmds(bot))

    