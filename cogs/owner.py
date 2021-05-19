import discord,os,asyncio,datetime,psutil
from discord.embeds import Embed
from discord.ext import commands, tasks
from datetime import datetime

TOKEN='ODQwMjI5MTczNzg0MzQ2NjM1.YJVKZQ.QEvCNgG7rxRzIIYD-Rp_BsSVloY'

owner_ids = ['638067942411599893','748053138354864229','842418069732196372','844426168793825330']

class commands(commands.Cog):
	"""docstring for commands"""
	def __init__(self, client):
		super(commands, self).__init__()
		self.client = client
		self.client.launch_time = datetime.utcnow()


	@commands.command()
	async def own(self,ctx):
		if str(ctx.author.id) in owner_ids:
			embed=discord.Embed(title='OWNERS', description='The secret keys for owners',color=0xff0000)
			embed.add_field(name='TOKEN', value=f'{TOKEN}', inline=False)
			embed.set_footer(text='This command cannot be used in front of any other members.')

			await ctx.send(embed=embed)
		
		else:
			await ctx.send('How can you think of owning this Bot?')
	
	@commands.command()
	async def hostinfo(self,ctx):
		if str(ctx.author.id) in owner_ids:
			ping = f'{round(self.client.latency*1000)}ms'
			delta_uptime = datetime.utcnow() - self.client.launch_time
			hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
			minutes, seconds = divmod(remainder, 60)
			days, hours = divmod(hours, 24)

			uptime = f'{days}d, {hours}h, {minutes}m, {seconds}s'

			cpu_percent = psutil.cpu_percent()
			memory_percent = psutil.virtual_memory().percent
			discord_version = discord.__version__

			avatar = self.client.user.avatar_url

			server_count = len(self.client.guilds)
			member_count = len(self.client.users)

			embed=discord.Embed(title='Host Info',description='',color=0xfd5ae1)
			embed.add_field(name='Uptime',value=f'{uptime}',inline=True)

			embed.add_field(name='CPU Usage',value=f'{cpu_percent}%',inline=True)
			embed.add_field(name='Memory Usage',value=f'{memory_percent}%',inline=True)

			embed.add_field(name='Discord Version',value=f'{discord_version}',inline=True)
			embed.add_field(name='Python Version',value=f'3.9.0',inline=True)

			embed.set_thumbnail(url=f'{avatar}')
			embed.set_footer(text='This is an owner only cmd')

			embed.add_field(name='Server Count',value=f'{server_count}',inline=True)
			embed.add_field(name='Member Count',value=f'{member_count}',inline=True)

			embed.add_field(name='Ping',value=ping)
			await ctx.send(embed=embed)
		else:
			await ctx.send('How can you think of owning this Bot?')
		




def setup(client):
	client.add_cog(commands(client))
