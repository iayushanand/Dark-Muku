import discord,json,random,datetime,asyncio
from discord.client import Client
from discord.ext import commands,tasks
from random import choice
from datetime import datetime


intents = discord.Intents.all()
intents.members = True
intents.presences = True


def get_prefix(client, message): ##first we define get_prefix
    with open('prefixes.json', 'r') as f: ##we open and read the prefixes.json, assuming it's in the same file
        prefixes = json.load(f) #load the json as prefixes
    return prefixes[str(message.guild.id)] #recieve the prefix for the guild id given



client = commands.Bot(command_prefix = get_prefix,intents=intents)

 #removing help command

client.remove_command('help')


cogs = ['cogs.bug','cogs.giveaway','cogs.help','cogs.kick_ban','cogs.mute','cogs.owner','cogs.utility']
client.launch_time = datetime.utcnow()




###### All error handles ######



@client.event #error handle
async def on_command_error(ctx,error):
	if isinstance(error,commands.MissingPermissions): #error handler for missing perms
		embed=discord.Embed(title=f'<:mukuno:840609577053454366> Missing Perms', description=f'You don\'t have required perms to excute the command', color=0xaeff00)
		embed.set_footer(text=f'Command by {ctx.author.name}')
		await ctx.send(embed=embed,delete_after=4.5)
		await ctx.message.delete()
  
	elif isinstance(error,commands.MissingRequiredArgument): #error handelr for missing args
		embed=discord.Embed(title=f'<:mukuno:840609577053454366> Missing Arguments', description=f'Enter all required Arguments!', color=0xaeff00)
		embed.set_footer(text=f'Command by {ctx.author.name}')
		await ctx.send(embed=embed,delete_after=4.5)
		await ctx.message.delete()

	elif isinstance(error, commands.errors.CommandOnCooldown):  #error handler for cooldowns
		embed=discord.Embed(title=f'<:mukuno:840609577053454366> Cooldown', description='The command **{}** is still on cooldown for {:.2f}sec'.format(ctx.command.name, error.retry_after), color=0xaeff00)
		embed.set_footer(text=f'Command by {ctx.author.name}')
		await ctx.send(embed=embed,delete_after=4.5)
  
	elif isinstance(error, commands.errors.CommandNotFound): #error handler for Commands not found
		embed=discord.Embed(title="<:mukuno:840609577053454366> Command Not Found", description="There is no command like that", color=0xaeff00)
		await ctx.send(embed=embed,delete_after=4.5)
		await ctx.message.delete()



	else:
		embed=discord.Embed(title='<:mukuno:840609577053454366> Terminal Error!',description=f'```{error}```',color=0xaeff00) #terminal errors
		await ctx.send(embed = embed,delete_after=4.5)
		await ctx.message.delete()
		raise error




@client.event
async def on_ready():
  print(f'Logged in as {client.user.name} in {len(client.guilds)} Servers')
  for cog in cogs:
    client.load_extension(cog)
  
  changestatus.start()
  info.start()


########## PREFIX CHANGE ###########
@client.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = '$'#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater

@client.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)




############ COMMANDS ########

@client.command(aliases=['prefixset'])
@commands.has_permissions(administrator=True) #ensure that only administrators can use this command
async def setprefix(ctx, prefix): #command: bl!changeprefix ...
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f: #writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: `{prefix}`') #confirms the prefix it's been changed to



@client.command()
async def ping(ctx):
  embed=discord.Embed(title='Pong!',description=f'Latency: `{round(client.latency*1000)}ms`')
  embed.set_footer(text='Thanks for using Dark Muku')

  await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx,limit=1):
  await ctx.message.delete()

  await ctx.channel.purge(limit=limit)

  await ctx.send(F'**<:mukuyes:840609577308520519> Deleted {limit} message(s)**',delete_after=1.5)





@client.command()
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx,duration):
  await ctx.channel.edit(slowmode_delay=duration)

  await ctx.send(f'The channel is now on **{duration}s** slowmode')




@client.command()
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx,member:discord.Member,*,nickname=''):
  if nickname == '':
    nickname = member.name
  
  else:
    pass
  
  old_nick=member.display_name

  await member.edit(nick=f'{nickname}')

  new_nick=member.display_name

  embed=discord.Embed(title='',description=f'<:mukuyes:840609577308520519> Changed nick from **{old_nick}** to **{new_nick}**')

  embed.set_footer(text='Thanks for using Dark Muku')

  await ctx.send(embed=embed)

def converts(time):
  pos = ["s","m","h","d"]

  time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

  unit = time[-1]

  if unit not in pos:
    return -1
  try:
    val = int(time[:-1])
  except:
    return -2
        
  return val * time_dict[unit]



@client.command()
async def reminder(ctx,time,*,message):
  converted = converts(time)

  member=ctx.message.author

  await ctx.send(f'Sure! I will remind you after **{time}**')

  await asyncio.sleep(converted)

  try:
    await member.send(f'`Hey {member.name}!` You told me to remind about: **{message}**')
        
  except:
    await ctx.send(f'{member.mention} You told me to remind me about: **{message}**! but your dm was off')




@client.command(aliases=['role'])
@commands.has_permissions(manage_roles=True)
async def giverole(ctx,member:discord.Member,role:discord.Role):
  await member.add_roles(role)

  embed=discord.Embed(title='',description=f'<:mukuyes:840609577308520519> **{member.name}#{member.discriminator}** got role **{role}**')

  embed.set_footer(text='Thanks for using Dark Muku')

  await ctx.send(embed=embed)



@client.command(aliases=['rrole'])
@commands.has_permissions(manage_roles=True)
async def removerole(ctx,member:discord.Member,role:discord.Role):
  await member.remove_roles(role)

  embed=discord.Embed(title='',description=f'<:mukuyes:840609577308520519> **{member.name}#{member.discriminator}** removed role **{role}**')

  embed.set_footer(text='Thanks for using Dark Muku')

  await ctx.send(embed=embed)






@client.event
async def on_message(msg):
    try:
        if msg.mentions[0] == client.user:


            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            pre = prefixes[str(msg.guild.id)] 

            await msg.channel.send(f'Prefix: `{pre}`')

    except:
        pass

    await client.process_commands(msg)


@tasks.loop(seconds=60)
async def info():
  channel = client.get_channel(842585362270650378)
  msg = await channel.fetch_message(842634008425005076)
  delta_uptime = datetime.utcnow() - client.launch_time
  hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
  minutes, seconds = divmod(remainder, 60)
  days, hours = divmod(hours, 24)

  uptime = f'{days}d, {hours}h, {minutes}m, {seconds}s'
  server_count = len(client.guilds)
  member_count = len(client.users)
				
  ping = f'{round(client.latency*1000)}ms'

  embed=discord.Embed(title='Bot Info',description='The bot\'s current status',color=0xae00ff)
  embed.add_field(name='Ping',value=ping,inline=True)
  embed.add_field(name='Uptime',value=uptime,inline=True)
  embed.add_field(name='Server Count',value=f'{server_count}',inline=True)
  embed.add_field(name='Member Count(overall)',value=f'{member_count}')
  embed.set_image(url='https://media.discordapp.net/attachments/840423101284089896/842636092813082624/Bot_Status.jpg?width=734&height=367')
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/840423101284089896/840564997204738048/DARK_MUKU.png?width=457&height=457')

  embed.set_footer(text='This info gets updated every minute')

  await msg.edit(content=None,embed=embed)


@tasks.loop(seconds=7)
async def changestatus():
  status=[f'over {len(client.users)} users',f'over {len(client.guilds)} servers','Dark Muku Support','sneaky Cats']



  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=(random.choice(status))))





client.run('ODQwMjI5MTczNzg0MzQ2NjM1.YJVKZQ.QEvCNgG7rxRzIIYD-Rp_BsSVloY')
