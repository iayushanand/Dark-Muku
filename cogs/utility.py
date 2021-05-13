import discord
from discord.ext import commands

class utility(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    @commands.command()
    async def support(self,ctx):
        embed=discord.Embed(title="Support", description="Join **🔗[Dark Muku Support](https://discord.gg/VsPKw3qunU)**,\nA server where you can give feedback to the bot and ask for help or report an issue!", color=0x8000ff)
        embed.set_author(name="Dark Muku Support", icon_url="https://media.discordapp.net/attachments/840423101284089896/840564997204738048/DARK_MUKU.png?width=457&height=457")
        embed.set_footer(text="Thanks for using Dark Muku")
        embed.set_image(url='https://media.discordapp.net/attachments/840423101284089896/840564768527613972/Support_Gif.gif?width=480&height=240')
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["w"])
    @commands.has_permissions(manage_messages = True)
    async def whois(self,ctx, member: discord.Member = ''):
        if member=='':
            member=ctx.author
        else:
            pass
    
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        
        # Remove unnecessary characters
        hypesquad_class = str(member.public_flags.all()).replace('[<UserFlags.', '').replace('>]', '').replace('_',
                                                                                                         ' ').replace(
        ':', '').title()

        # Remove digits from string
        hypesquad_class = ''.join([i for i in hypesquad_class if not i.isdigit()])

        status=member.activities[0].name

        roles = [role for role in member.roles]
        embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Thanks for using Dark Muku")

        embed.add_field(name="ID:", value=member.id,inline=True)
        embed.add_field(name="Display Name:", value=member.display_name,inline=True)

        embed.add_field(name="Account Created:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=True)
        embed.add_field(name="Server Joined:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=True)

        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]),inline=True)
        embed.add_field(name="Highest Role:", value=f'{member.top_role.mention}')

        embed.add_field(name='Hypesquad',value=f'{hypesquad_class}')
        embed.add_field(name='Status',value=f'{status}')
        
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

           



def setup(client):
    client.add_cog(utility(client))