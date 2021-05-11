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