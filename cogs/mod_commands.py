import discord
from discord.ext import commands
from discord import User
import datetime
import typing
import random
from datetime import datetime

color = 0xa100f2
guild = 757098499836739594


class vein(commands.Cog, name="moderation"):
    def __init__(self, Bot):
        self.Bot = Bot
        self.log_channel = self.Bot.get_channel(759583119396700180)

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        if ctx.guild.id != (guild):
            return

        user = ctx.guild.get_member(ctx.author.id)

        me = ctx.guild.get_member(427436602403323905)
        role = ctx.guild.get_role(782624701779673129)
        if ctx.author.id == 427436602403323905:
            return
        if role in user.roles:

            channel = ctx.guild.get_channel(783715160833523722)
            link = ctx.message.jump_url
            embed = discord.Embed(
                color=color, timestamp=datetime.utcnow())
            embed.set_author(name=f"{ctx.author.name}",
                             icon_url=ctx.author.avatar_url)
            embed.add_field(name="Action", value=f'{ctx.message.clean_content[1:]}\n'
                            f'[On here]({link})')
            embed.set_footer(text=f'ID : {ctx.message.id}')

            await channel.send(embed=embed)
        else:
            return

    async def ModLog(self,ctx,commandname =None ,mod= None, target = None, amount :3 =None, Reason =None,
                     channel=None, content = None, jump = None):
        guild = self.Bot.get_guild(self.Bot.guild_id)
        if ctx.guild.id != self.Bot.guild_id:
            return
        log_channel= self.Bot.get_channel(759583119396700180)
        embed = discord.Embed(color = random.choice(self.Bot.color_list),timestamp = datetime.utcnow())
        embed.set_author(name=f"{commandname}",icon_url=ctx.author.avatar_url)
        if mod !=None:
            embed.add_field(name = "Mod", value = f"{mod.display_name} | {mod.mention}")
        if target != None:
            embed.add_field(name = "Target", value = f"{target.display_name} | {target.mention}")

        if amount != None:
            embed.add_field(name= "Amount", value= f'{amount}') 
        if channel!= None:
            embed.add_field(name = "On channel", value=f"{channel}")
        if content!= None:
            embed.add_field(name = "Content", value= f"```css\n{content}```", inline=False)

        if jump != None:
            embed.add_field(name = "Jump", value = f"[Here]({jump})")
        
        if Reason !=None:
            embed.add_field(name= "Reason ", value= f"```css\n{Reason}```", inline=False)
        embed.set_thumbnail(url = guild.icon_url)
        embed.set_footer(icon_url = mod.avatar_url)
        await log_channel.send(embed=embed) 
        return self.ModLog  

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != 757110183800471572:
            return
        msg = message
        await msg.add_reaction("<:check:773959361953267742>")
        await msg.add_reaction("<:xmark:773959363379462184>")
        return

    @commands.command(aliases=['Bot'], hidden=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.guild_only()
    async def abode(self, ctx):

        embed = discord.Embed(color=color)
        embed.set_thumbnail(url=f'{ctx.me.avatar_url}')
        embed.set_author(name="Abode", icon_url=f'{ctx.me.avatar_url}')
        embed.add_field(name="‎‎‎‏‏‎Intro", value=f'**Abode mandator** or abode in short is a discord bot written python (discord.py).\n Abode is created by Vein, as a way to learn python but later on further continued as a fun-command based bot. Vein doesn\'t own any of the api used, so read the footers for the api source.', inline=False)
        embed.add_field(name="Tips", value=f"``.help``  is always there for you :D \n\n"
                        f'Want to earn a custom gif or role? You might earn them by reporting issues on more or the server on our suggestions channel. \n\n'
                        f'``.welcome`` whenever a new user joins. It is a easy way to make them feel welcomed :D \n\n'
                        f'If you can contribute to the server you may bypass some rules and get a higher role. \n\n'

                        f'``.faq`` FAQ are available there, do not leave your mind wander.\n\n'
                        f'Always check the pinned messages or the channel description to learn more about that channel.\n\n'
                        f'By default you don\'t have a cultivator name add it using ``.aliases <your name>.``', inline=False)

        embed.set_footer(
            text=f'Special thanks to Sap on helping me do all these stuffs.')
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(aliases=['frequent_questions'],
                      hidden=True)
    @commands.guild_only()
    async def faq(self, ctx):
        embed = discord.Embed(color=color)
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name="QnA", value=f'**Why is there a logo on every command?** \nBecause why not? <:Scholar2:779239176511946772>\n\n'
                        f'**Can you remove the cooldown on images?** \nNo not anytime soon, maybe in future <:blobspearpeek:775344866246393876>\n\n'
                        f'**Why aren not the image commands not working sometimes?**\nIt\'s due to bad response from the API.')

        embed.timestamp = datetime.utcnow()
        embed.set_footer(
            text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=['purge'], hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=3):
        if amount <= 200:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'**The higher-ups have purged some messages.**', delete_after=10) 
            if ctx.guild.id != self.Bot.guild_id:
                return
            await self.ModLog(ctx = ctx, mod= ctx.author, amount= amount, commandname="Clear", channel=ctx.channel.mention)

        else:
            await ctx.send("Please add a number smaller than 200")

    @commands.command(aliases=['pmuser'], hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def DMuser(self, ctx, user: discord.User, *, msg):
        try:
            await user.send(f'**{ctx.message.author}** has a message for you, \n {msg}')
            await self.ModLog(ctx = ctx, mod= ctx.author, target=user, commandname="Dmuser", channel=ctx.channel.mention
                                , content=msg, jump = ctx.message.jump_url)

        except:
            await ctx.send(f'The user has his/her DMs turned off.')

    @commands.command(aliases=['clearuser'], hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purgeuser(self, ctx, user: discord.Member,
                        num_messages: typing.Optional[int] = 100,
                        ):

        channel = ctx.message.channel
        if ctx.guild.me.top_role < user.top_role:
            return await ctx.send("Admin :(")
        if ctx.message.author.top_role < user.top_role:
            return await ctx.send("You  have lower roles.")

        def check(msg):
            return msg.author.id == user.id

        await ctx.message.delete()
        await channel.purge(limit=num_messages, check=check, before=None)
        await ctx.send(f'**The higher-ups have purged someones messsages.**', delete_after=10)
        await self.ModLog(ctx = ctx, mod= ctx.author, target=user, commandname="Purgeuser", channel=ctx.channel.mention
                            )       

    @commands.command(hidden=True)
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def role(self, ctx, member: discord.Member, *, arg):
        if ctx.guild.me.top_role < member.top_role:
            return await ctx.send("Admin :(")
        if ctx.message.author.top_role < member.top_role:
            return await ctx.send("You  have lower roles.")
        role = discord.utils.get(ctx.guild.roles, name=f"{arg}")

        if role not in member.roles:
            await member.add_roles(role)
            await ctx.send(f"{member} was given role ``{arg}``.")
        else:
            await member.remove_roles(role)
            await ctx.send(f"{member} was removed from the role ``{arg}``.")

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    async def cnick(self, ctx, member: discord.Member, *, arg):
        if ctx.guild.me.top_role < member.top_role:
            return await ctx.send("Admin :(")
        if ctx.message.author.top_role < member.top_role:
            return await ctx.send("You  have lower roles.")
        else:
            await member.edit(nick=arg)
            await ctx.send(f'{member} nickname was changed to {arg} by {ctx.message.author}')

    @commands.command(aliases=['rinfo'], hidden=True)
    @commands.has_permissions(manage_roles=True)
    async def roleinfo(self, ctx, *, rolename):
        allowed = []
        try:
            role = discord.utils.get(ctx.message.guild.roles, name=rolename)
            permissions = role.permissions

            for name, value in permissions:
                if value:
                    name = name.replace('_', ' ').replace(
                        'guild', 'server').title()
                    allowed.append(name)
        except:
            return await ctx.send(f"Couldn't find the role")
        time = role.created_at
        em = discord.Embed(description=f'', color=color, timestamp=time)
        em.set_author(name=f'{rolename}')
        em.set_thumbnail(url=f'{ctx.guild.icon_url}')
        em.add_field(name='__Info__', value=f'**ID :** {str(role.id)} \n'
                                            f'**Color :** {role.color}\n'
                                            f'**Hoisted :** {str(role.hoist)}\n'
                                            f'**Position :** {str(role.position)}\n'
                                            f'**Is mentionable :** {str(role.mentionable)}\n'
                                            f'**Members in role :** {str(len(role.members))}\n')
        em.add_field(name='__Role permissions__',
                     value=f', '.join(allowed), inline=False)
        em.set_footer(text="Role created on")
        await ctx.send(embed=em)

    @commands.command(hidden=True, aliases=['PM'])
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def DM(self, ctx, *, arg):
        await ctx.message.author.send(arg)

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.top_role < member.top_role:
            return await ctx.send("You can't kick someone higher than you.")
        if ctx.me.top_role < member.top_role:
            return await ctx.send("You can't kick a supreme elder can you?")
        if member is None:
            await ctx.send(f'{ctx.message.author.display_name}, Please tag an user whom you want to be kicked from the server.')
        else:
            await member.kick(reason=reason)
            await ctx.send(f'User {member.mention} was kicked from the server for ``{reason}.``')
            await self.ModLog(ctx = ctx, mod= ctx.author, target=member, commandname="Kick", channel=ctx.channel.mention, jump= ctx.message.jump_url
                                , Reason=reason)

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, reason: str = "You were banned from the server for not following the rules."):
        if ctx.author.top_role < member.top_role:
            return await ctx.send("You can't kick someone higher than you.")
        if ctx.me.top_role < member.top_role:
            return await ctx.send("You can't kick a supreme elder can you?")
        if member is not None:
            await ctx.guild.ban(member, reason=reason)
            await ctx.send(f'{member.mention} was banned from the server.')
            await self.ModLog(ctx = ctx, mod= ctx.author, target=member, commandname="Ban", channel=ctx.channel.mention, jump= ctx.message.jump_url
                                , Reason=reason)           
        else:
            await ctx.send("Please specify an user to ban with a reason.")

    '''
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self ,ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        guild = ctx.guild
        if role not in guild.roles:
            perms = discord.Permissions(send_messages=False, speak=False)
            await guild.create_role(name="Muted", permissions=perms)
            await member.add_roles(role)
            await ctx.send(f"{member} was muted.")
        else:
            await member.add_roles(role)
            await ctx.send(f"{member} was muted.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name= "Muted")


        await member.remove_roles(role)
        await ctx.send(f"{member} was unmuted.") '''

    @commands.command(hidden=True, aliases=['cstats'])
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def channelstats(self, ctx):
        channel = ctx.channel
        tmembers = str(len(channel.members))
        nsfw = (ctx.channel.is_nsfw())
        news = (ctx.channel.is_news())
        embed = discord.Embed(color=color)
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name="__Information__", value=f'**Server name: ** {ctx.guild.name} \n'
                        f'**Channel name :** {channel.name}\n'
                        f'**Channel ID : ** {channel.id} \n'
                        f'**Channel type : **{channel.type}\n'
                        f'**Channel category : ** {channel.category}\n'
                        f'**Topic : ** {channel.topic}\n'
                        f'**Channel position :** {channel.position}\n'
                        f'**Created at :** {channel.created_at.strftime("%a, %#d %B %Y, %I:%M %p ")}\n'
                        f'**Slowmode :** {channel.slowmode_delay}\n'
                        f'**Channel Permissions :** {channel.permissions_synced}\n'
                        f'**Channel members :** {tmembers}\n'
                        f'**Is nsfw : ** {nsfw}\n'
                        f'**Is news : ** {news}', inline=False)

        embed.set_author(name="Abode", icon_url=f'{ctx.me.avatar_url}')
        embed.set_footer(
            text=f" Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def complaint(self, ctx, *, arg):
        if ctx.channel.id != (757136905329442859 or 757136943149613076):
            await ctx.send(f'{ctx.author.name}, It\'s good that you have complaints but please use this command on the Bots category.')
            return
        channel = ctx.guild.get_channel(757110183800471572)
        embed = discord.Embed(
            color=ctx.author.color, title=f'{arg}', timestamp=datetime.datetime.utcnow())
        embed.set_author(
            name=f"{ctx.author.name}'s complaint ", icon_url=f'{ctx.author.avatar_url}')
        embed.set_footer(text=f"Submitted on")
        await ctx.message.delete()
        await channel.send(embed=embed)
        await ctx.send(f'{ctx.author.name}, Sent your complaint in <#757110183800471572>.')

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def poll(self, ctx, question, *options: str):
        if len(options) <= 1:
            await ctx.send('Weird you want to make a poll with less than 1 option?')
            return
        if len(options) > 7:
            await ctx.send('Bruh! you can\'t make a poll with more than 7 options.')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['<:check:773959361953267742>',
                         ' <:xmark:773959363379462184>']
        else:
            reactions = ['1️⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣']

        description = []
        for x, option in enumerate(options):
            description += f'\n\n {reactions[x]} {option}'
        embed = discord.Embed(title=question, description=''.join(
            description), color=color, timestamp=datetime.utcnow())
        embed.set_footer(
            text=f'Elder responsible for the poll : {ctx.message.author.name}')
        msg = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await msg.add_reaction(reaction)

        await msg.edit(react_message, embed=embed)

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def slowmode(self, ctx, time):
        self.Bot.log_channel = self.Bot.get_channel(759583119396700180)
        if time == 'remove':
            await ctx.channel.edit(slowmode_delay=0)
            await ctx.send(f'Slowmode removed.')


        else:

            await ctx.channel.edit(slowmode_delay=time)
            await ctx.send(f'{time}s of slowmode was set on the current channel.')

            await self.ModLog(ctx = ctx, mod= ctx.author,commandname="Slowmode", channel=ctx.channel.mention, jump= ctx.message.jump_url
                                , amount=time)
    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def lock(self, ctx):
        hm = discord.utils.get(ctx.guild.roles, name=f'Verified')
        await ctx.channel.set_permissions(hm, send_messages=False, read_messages=True)
        await ctx.send("Channel locked.")

    @commands.command(hidden=True)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx):
        hm = discord.utils.get(ctx.guild.roles, name=f'Verified')
        await ctx.channel.set_permissions(hm, send_messages=True, read_messages=True)
        await ctx.send("Channel unlocked.")

    @commands.command(aliases=[ 'getbotlink'])
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def createbotlink(self, ctx, id_: int):
        await ctx.send(f"https://discord.com/api/oauth2/authorize?client_id={id_}&permissions=0&scope=bot")

def setup(Bot):
    Bot.add_cog(vein(Bot))
    print("Mod cog is working.")
