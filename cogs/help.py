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

        embed.add_field(name='Music',value='Shows all music commands')

        embed.add_field(name='Utility',value='Shows all utility commands')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command(aliases=['Moderation','mod'])
    async def moderation(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]

        embed=discord.Embed(title='Moderation Commands',description=f'Use `{pre}help <command>` for more info on that command',color=ctx.author.color)

        embed.add_field(name='Commands',value='`kick`  `ban`  `giverole`  `purge`  `removerole`  `nick`  `setprefix`  `slowmode`   `nuke`')

        await ctx.send(embed=embed)

    @help.command(aliases=['Music','song'])
    async def music(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]

        embed=discord.Embed(title='Music Commands',description=f'Use `{pre}help <command>` for more info on that command',color=ctx.author.color)

        embed.add_field(name='Commands',value='`connect`  `play`  `pause`  `resume`  `stop`  `queue`  `leave`  `now_playing`  `skip`  `volume`')

        await ctx.send(embed=embed)

    @help.command(aliases=['utility','Commands'])
    async def commands(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]

        embed=discord.Embed(title='Normal Commands',description=f'Use `{pre}help <command>` for more info on that command',color=ctx.author.color)

        embed.add_field(name='Commands',value='`avatar`  `countdown`  `servericon`  `serverinfo`  `whois`  `support`  `ping`  `reminder`')

        await ctx.send(embed=embed)

    @help.command()
    async def ban(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Ban',description='Bans a member from the server',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}ban `<member>` [reason]')
        embed.add_field(name='**Perms**',value='Ban Members')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)   

    @help.command()
    async def kick(Self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]

        embed=discord.Embed(title='Kick',description='Kicks a member from server',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}kick `<member>` [reason]')

        embed.add_field(name='**Perms**',value='Kick Members')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def giverole(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Give Role',description='Gives a role to the member',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}giverole `@user_mention` `@role_mention`')
        embed.add_field(name='**Perms**',value='Manage roles')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed) 

    @help.command()
    async def removerole(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Remove Role',description='Removes a role from the member',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}removerole `@user_mention` `@role_mention`')
        embed.add_field(name='**Perms**',value='Manage roles')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def purge(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Purge',description='Deletes the specified amount of messages',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}purge `<number of messages>`')
        embed.add_field(name='**Perms**',value='Manage messages')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def whois(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Who Is',description='Gives some basic info about a user',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}whois `@user_mention`')
        embed.add_field(name='**Perms**',value='No perms needed')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def bug(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Bug',description='Reports bot bugs',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}bug')
        embed.add_field(name='**Perms**',value='No perms needed')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def nick(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Nick',description='Changes the nickname of fthe member',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}nick `@user_mention` `<new nickname>`')
        embed.add_field(name='**Perms**',value='Manage nicknames')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def serverinfo(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Server Info',description='Shows some basic info about the server',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}serverinfo')
        embed.add_field(name='**Perms**',value='No perms needed')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def ping(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Ping',description='Shows your latency to the bot',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}ping')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def reminder(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Reminder',description='Reminds you about something after the time limit',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}reminder `<Time limit in seconds>` `What to remind>`')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def setprefix(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Set Prefix',description='Changes the bot prefix for the guild',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}setprefix `<New bot prefix>`')
        embed.add_field(name='**Perms**',value='Administrator')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def support(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Support',description='Provides the invite link to the bot\'s support server',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}support')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)
        
    @help.command()
    async def servericon(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Server Icon',description='Display\'s the server icon',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}servericon')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def countdown(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Count Down',description='Starts the countdown for the given time',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}countdown `Number of seconds`')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def avatar(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Avatar',description='Displays the avatar of the specified user',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}avatar')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)
    
    @help.command()
    async def volume(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Volume',description='Reduces/Increases the volume fo the music',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}volume `<Volume number>`')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def stop(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Stop',description='Stops the song which is playing and disconnects',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}stop')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def skip(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Skip',description='Skips the currently playing song and moves to the next song',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}skip')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def resume(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Resume',description='Resumes the song if paused',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}resume')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def queue(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Support',description='Displays the songs that are queued',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}queue')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def play(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Play',description='Plays a specified song',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}play `<Song name>`')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def pause(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Pause',description='Pauses the currently playing song',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}pause')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def now_playing(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Now Playing',description='Shows the currently playing song',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}now_playing')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def leave(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Leave',description='Leaves the voice channel',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}leave')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)

    @help.command()
    async def connect(self,ctx):
        with open('prefixes.json','r') as f:
            prefixes=json.load(f)
        
        pre=prefixes[str(ctx.guild.id)]
        embed=discord.Embed(title='Connect',description='Join\'s the voice channel that you are in',color=ctx.author.color)

        embed.add_field(name='**Syntax**',value=f'{pre}connect')
        embed.add_field(name='**Perms**',value='No perms required')

        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)
    

    


def setup(bot):
    bot.add_cog(help_cmds(bot))

    
