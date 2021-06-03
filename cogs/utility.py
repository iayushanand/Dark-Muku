import discord,asyncio,random
from discord import message
from discord.ext import commands
from random import choice, randint




class utility(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.command()
    async def support(self,ctx):
        embed=discord.Embed(title="Support", description="Join **🔗[Dark Muku Support](https://discord.gg/VsPKw3qunU)**,\nA server where you can give feedback to the bot and ask for help or report an issue!", color=0x8000ff)
        embed.add_field(name='Invite Link',value='🔗**[Link](https://bit.ly/33oC2Wm)** to invite this bot in your server.',inline=True)
        embed.set_author(name="Dark Muku Support", icon_url="https://media.discordapp.net/attachments/840423101284089896/840564997204738048/DARK_MUKU.png?width=457&height=457")
        embed.set_footer(text="Thanks for using Dark Muku")
        embed.set_image(url='https://media.discordapp.net/attachments/840423101284089896/840564768527613972/Support_Gif.gif?width=480&height=240')
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["w"])
    async def whois(self,ctx, member: discord.Member = ''):
        if member=='':
            member=ctx.author
        else:
            pass
        
        # Remove unnecessary characters
        hypesquad_class = str(member.public_flags.all()).replace('[<UserFlags.', '').replace('>]', '').replace('_',
                                                                                                         ' ').replace(
        ':', '').title()

        # Remove digits from string
        hypesquad_class = ''.join([i for i in hypesquad_class if not i.isdigit()])

        try:
            status=member.activities[0].name
        except IndexError:
            status='None'
        
        if hypesquad_class == '[]':
            hypesquad_class='None'
        
        
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Thanks for using Dark Muku")

        embed.add_field(name="ID:", value=member.id,inline=True)
        embed.add_field(name="Display Name:", value=member.display_name,inline=True)

        embed.add_field(name="Account Created:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=True)
        embed.add_field(name="Server Joined:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=True)

        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]),inline=True)
        embed.add_field(name="Highest Role:", value=f'{member.top_role.mention}',inline=True)

        embed.add_field(name='Hypesquad',value=f'{hypesquad_class}',inline=True)
        embed.add_field(name='Status',value=f'{status}',inline=True)
        
        await ctx.send(embed=embed)

    format = "%a, %d %b %Y | %H:%M:%S %ZGMT"


    @commands.command(aliases=['av'])
    async def avatar(self,ctx,member:discord.Member=''):
        if member == '':
            member=ctx.message.author

        avatar=member.avatar_url

        memberi=f'{member.name}#{member.discriminator}'

        embed=discord.Embed(title='Avatar',description='',color=0x00000f)
        embed.set_author(name=f'{memberi}',icon_url=f'{avatar}')
        embed.set_image(url=f'{avatar}')
        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)


    @commands.command(aliases=['si'])
    async def servericon(self,ctx):
        icon=str(ctx.guild.icon_url)

        embed=discord.Embed(title='',description='',color=0x123456)
        embed.set_image(url=icon)
        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)
    
    @commands.command(aliases=['cd'])
    async def countdown(self,ctx,seconds:int):
        if seconds == None:
            await ctx.send('<:mukuno:840609577053454366> Please provide seconds')

        elif seconds>60:
            return await ctx.send('Seconds cannot be greater than 60')
        
        await ctx.send(f'Counting Down till **{seconds}s**')
        msg = await ctx.send(f'** **')

        timer = 0
        while timer<seconds:
            await msg.edit(content=f'{seconds-1}')
            await asyncio.sleep(1)
            seconds=seconds-1
        
        await msg.edit(content=f'{ctx.author.mention} Countdown Completed!')
    
    @commands.command(aliases=['info'])
    async def serverinfo(self,ctx):
        membersInServer = ctx.guild.members
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        mc=int(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        def filterOnlyOnlineMembers(member):
            return member.status != discord.Status.offline


        onlineMembersInServer = list(filter(filterOnlyOnlineMembers,membersInServer))

        omc = len(onlineMembersInServer)
        nomc = int(len(onlineMembersInServer))
        

        
        embed = discord.Embed(
            title=" Server Information",
            description=name,
            color=discord.Color.blue()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.set_footer(text='Thanks for using Dark Muku')
        embed.add_field(name='Server Description',value=f'{description}')
        embed.add_field(name='Member Status',value=f'<:Online:841889925510070312> {omc}\n<:Invisible:843396279127506945> {mc-nomc}')


        await ctx.send(embed=embed)
    
    @commands.command(pass_context = True)
    @commands.has_permissions(administrator=True)
    async def nuke(self,ctx,channel:discord.TextChannel=None):
        if channel == None: 
            channel=ctx.channel

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason=f"Has been Nuked! by {ctx.author.name}#{ctx.author.discriminator}")
            await nuke_channel.delete()
            await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
            await new_channel.send("https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")
            await ctx.send("Nuked the Channel sucessfully!")

        else:
            await ctx.send(f"No channel named {channel.name} was found!")
    


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def guildleave(self,ctx):
        def check(msg):
            return msg.channel==ctx.channel and msg.author==ctx.author
        embed=discord.Embed(title='',description='',color=ctx.author.color)
        embed.add_field(name='Confirmation',value='Write \'Y\' for Yes or \'N\' for No.')
        await ctx.send(embed=embed)
        
        try:
            ans = await self.client.wait_for('message',check=check,timeout=15.0)
        except TimeoutError:
            await ctx.send('You didn\'t answer in time :( Please try again')
        
        else:
            if ans.content == 'Y' or ans.content == 'y':
                embed=discord.Embed(title='Last Words!',description='It was a great here, I was so busy with the work that I forgot my retirment is on line ;-;\nIf you faced any problem please join **[Dark Muku Supprt Server](https://discord.gg/VsPKw3qunU)** ')
                embed.set_footer(text='Bot will leave in 5 seconds, feel free to invite it again')
                await ctx.send(embed=embed)
                await asyncio.sleep(5)
                await ctx.guild.leave()
            else:
                await ctx.send(f'Process Cancelled!')
    
    @commands.command()
    async def toss(self,ctx):
        prob = ['Heads','Tails']
        out=f'{random.choice(prob)}'
        dis='None'

        if out == 'Heads':
            dis='<:mukuheads:848067142209634304>'
        elif out == 'Tails':
            dis='<:mukutails:848067144683618344>'
        else:
            pass

        embed=discord.Embed(title='',description='',color=0xffdd00)
        embed.add_field(name=f'{out}',value=f'{dis}',inline=True)
        embed.set_footer(text='Thanks for using Dark Muku')

        await ctx.send(embed=embed)
    

    @commands.command()
    async def rand(self,ctx,num1:int,num2:int):
        guess=f'{randint(num1 , num2)}'

        await ctx.send(f'Random Number between **{num1}** and **{num2}**: **{guess}**')
        
        

          



def setup(client):
    client.add_cog(utility(client))