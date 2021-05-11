import discord,os,asyncio
from discord.ext import commands, tasks


TOKEN='ODQwMjI5MTczNzg0MzQ2NjM1.YJVKZQ.QEvCNgG7rxRzIIYD-Rp_BsSVloY'



class commands(commands.Cog):
	"""docstring for commands"""
	def __init__(self, client):
		super(commands, self).__init__()
		self.client = client


	@commands.command()
	@commands.is_owner()
	async def own(self,ctx):
		embed=discord.Embed(title='OWNERS', description='The secret keys for owners',color=0xff0000)
		embed.add_field(name='TOKEN', value=f'{TOKEN}', inline=False)
		embed.set_footer(text='This command cannot be used in front of any other members.')

		await ctx.send(embed=embed)
		

	


def setup(client):
	client.add_cog(commands(client))
