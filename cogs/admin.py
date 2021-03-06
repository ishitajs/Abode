import discord
from discord.ext import commands


color = 0xa100f2
server_invite = 'https://discord.gg/tA4PDtX'


class vein4(commands.Cog, name="Admin"):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != 757109995178557511:
            return
        msg = message
        await msg.add_reaction("<:check:773959361953267742>")
        await msg.add_reaction("<:xmark:773959363379462184>")
        return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ultra_purge_user(self, ctx, *, member: discord.Member):
        channel = ctx.message.channel
        member = member

        def check(msg):
            return msg.author.id == member.id

        await ctx.message.delete()
        await channel.purge(limit=None, check=check,)
        await ctx.send(f'All from {member} have been purged by an admin.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purgemany(self, ctx, amount=100000000):

        await ctx.channel.purge(limit=amount)
        await ctx.send(f'**The higher-ups have purged alot of messages.**', delete_after=10)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'User {member} was unbanned from the server by an Admin.')

    ''' Commands like load unload reload is already defined by jsk.'''

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def intro(self, ctx):
        color = 0xa100f2
        embed = discord.Embed(color=color, title=f'ㅤㅤㅤㅤㅤㅤㅤㅤㅤ{ctx.guild.name}')
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')
        embed.add_field(name='Welcome!', value='Welcome to Abode of Scholars. This may be your first time at the server, I and the staff team thanks you for joining our community server.\n\nPlease read the following sets of information before heading off to the chat section to share us stuffs about your favorite novel. Also be sure to suggest us about the things we can improve on, only then we can grow together :)')
        embed.add_field(name='Introduction!',
                        value=f'Adobe of Scholars is a chat-server based on the combination of various fictional worlds from their respective **Chinese Novels**. \n\n The server allows almost everthing which is within the restrictions of [Discord TOS](https://discord.com/terms). \n\nThe server doesnot have any fixed location, it is a global server which accepts all types of readers. \n\nAbode of Scholars is made for those who are fond of reading various types of chinese webnovels, to interact with each other and also to promote the fantasy genre.', inline=False)
        embed.add_field(name='Aspects!', value=f'➤ Custom bot, The Abode Mandator\n'
                        f'➤ Contribution points-system \n'
                        f'➤ Qi and stats system with alot of unique paths and species.\n'
                        f'➤ Custom roles, commands, and more for members with enough contribution points.\n'
                        f'➤ Helpful community\n'
                        f'➤ Good staff members\n'
                        f'➤ Organized server \n'
                        f'➤ Alot of fantasy talks \n', inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def pointsystem(self, ctx):
        color = 0xa100f2
        embed = discord.Embed(
            color=color, totle=f'ㅤㅤㅤㅤㅤㅤㅤㅤㅤCultivation System')

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def rules(self, ctx):
        color = 0xa100f2
        embed = discord.Embed(color=(color))

        embed.add_field(name='Rules!', value='**1.** Do not be racist, homophobic, or sexist, it can be overlooked if the other party is fine with it.\n\n'
                        '**2.** You are allowed to curse on someone as long as they do not mind. There are no barred curse words. If there are complaints on one\'s behavior then it may result in certain actions taken from the moderators\n\n'
                        '**3.** You should not offend or antagonize other parties. You never know who the other party may be.\n\n'
                        '**4.** Spamming of texts, emojis, images, etc is strictly prohibited, if found out it may result in a permanent ban from the server.\n\n'
                        '**5.** The server does allow anything under the [Discord TOS](https://discord.com/terms) but it doesn\'t means that we won\'t take actions if the situation is necessary.\n\n', inline=False)
        embed.add_field(name='‎‎‎‏‏‎ ‎', value='**6.** Posts related to the information of another party, private messages, or pictures without their permission will be removed. This is a rigorous  policy, may result in a permanent ban.\n\n'
                        '**7.** Moderators have final judgment on everything, if they ask you to stop doing something then stop. Do not complain if you have been kicked or banned from the server.\n\n'
                        '**8.** You are free to debate about anything, just don\'t force your beliefs on others.\n\n'
                        '**9.** There shouldn\'t be any bullying or bad behavior to new members.\n\n'
                        '**10.** There should not be any sharing of graphical or image posts related to violence, gore, and things that are against Discord TOS \n\n'
                        '**11.** All NSFW content under TOS  are allowed, as long as they are NOT in Non-NSFW channels. This includes gifs, profile pictures, status,etc.\n\n'
                        '**12.** Self-advertising on main channels won\'t be tolerated, asking for roles, permissions, custom commands will result in warns from the moderators.', inline=False)
        embed.add_field(name='‎‎‎‏‏‎ ', value='**13.** Altough it\'s not prohibited on using Abode\'s command in chat channels, it\'s wise to not do so.\n\n\n'
                        'Thanks to [Skyfarrow](https://discordapp.com/invite/nWU3qMK) for letting me use and modify his rules.', inline=False)
        emojy = '<:PepeHmm:757202636029034526>'
        embed.set_footer(text=f'Give me a hmm if you read through everything.')
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(f"{emojy}")

        channel = ctx.guild.get_channel(757107343522791494)
        msg1 = await channel.fetch_message(782096359175487488)

        await msg1.edit(embed=embed)

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def roles(self, ctx):
        color = 0xa100f2
        admin = ctx.guild.get_role(757102576230596648)
        admin_mention = admin.name
        selder = ctx.guild.get_role(757440901776932994)
        smention = selder.name
        cmelder = ctx.guild.get_role(757477610493182043)
        cmmention = cmelder.name
        ielder = ctx.guild.get_role(757591178349904063)
        imention = ielder.name
        elder = ctx.guild.get_role(757102603556356149)
        emention2 = elder.name
        emelder = ctx.guild.get_role(757166167793074217)
        emention = emelder.name
        oelder = ctx.guild.get_role(757423566231699456)
        omention = oelder.name

        embed = discord.Embed(
            color=(color), title='‎‎‎‏‏‎ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ__Server Roles!__')
        embed.set_thumbnail(url=f'{ctx.guild.icon_url}')

        embed.add_field(name='‎‎‎‏‏‎ ', value=f'**{admin_mention}** \nClan leader is the highest role in the server, clan leaders handle most of the supervision work, server management, etc all the major things within the server.\n\n'
                        f'**{smention}** \nSupreme elders are the founding  leaders of the server.\n', inline=False)

        embed.add_field(name='‎‎‎‏‏‎ ', value=f'**{cmmention}** \nCore elders are the head moderators also the highest of the staffs.\n\n'
                        f'**{imention}** \nInner elders superivse the lower staffs and also have alot of authority.\n\n'
                        f'**{emention2}** \nElder role can be obtained by users above the 40th level with the recommendation from any of the higher staffs and also through their efforts. \n\n'
                        f'**{emention}** \nEmoji elder doesn\'t have much requirements you just need to have creation skills.\n\n'
                        f'**{omention}** \nMembers with good moderation skills can contact any of the higher members to obatin this role.\n\n'
                        f'```fix\nIf aynone has the same question, The elder roles will only be given to users with certain requirements, they don\'t work the same as chat roles.```', inline=False)
        hinstructor = (ctx.guild.get_role(757787649439432785)).name
        binstructor = (ctx.guild.get_role(757787658645667850)).name
        cinstrucotr = (ctx.guild.get_role(757787658645667850)).name
        adisciple = (ctx.guild.get_role(757584739141157045)).name
        bdisciple = (ctx.guild.get_role(757102633952608359)).name
        cdisciple = (ctx.guild.get_role(757102570874339421)).name
        civilian = (ctx.guild.get_role(757262459072544818)).name

        embed.add_field(name='‎‎‎‏‏‎ㅤ', value=f'**{hinstructor}** \nLevel 61 or higher.\n\n'
                        f'**{binstructor}** \nLevel 51 to 61.\n\n'
                        f'**{cinstrucotr}**\nLevel 41 to 51. \n\n'
                        f'**{adisciple}** \nLevel 31 to 41. \n\n'
                        f'**{bdisciple}** \nLevel 21 to 31. \n\n'
                        f'**{cdisciple}** \nLevel 11 to 21. \n\n'
                        f'**{civilian}** \nLevel 3 to 11. \n\n')
        gelder = ctx.guild.get_role(799664368639148044)
        gmention = gelder.name
        ddisciple = ctx.guild.get_role(757102604873498745)
        ddmention = ddisciple.name
        ma = ctx.guild.get_role(757262605122404422)
        mamention = ma.name
        no1 = ctx.guild.get_role(757788428564824104)
        nomention = no1.name
        embed.add_field(name='ㅤ', value=f'ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**__Respected roles__**\n\n'
                        f'**{gmention}** \n{gmention} is the role given to the server boostersm, as expected they revieve extra perks such as 40% extra leveling speed, exclusive roles, chats, etc.\n\n'
                        f'**{ddmention}** \nRole given to the disciple of any of the supreme elders or the clan leader.\n\n'
                        f'**{nomention}** \nThe one with the highest level will recieve this role. (Admins can\'t have this role.\n\n'
                        f'**{mamention}** \nAristocrats are the founding or the OG members of the server.', inline=False)

        emojy = '<:PepeHmm:757202636029034526>'
        embed.set_footer(text=f'Give me a hmm if you read through everything.')
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(f"{emojy}")

        channel = ctx.guild.get_channel(757464183183769600)
        msg1 = await channel.fetch_message(782095794391613451)

        await msg1.edit(embed=embed)

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def bots(self, ctx):
        color = 0xa100f2
        embed = discord.Embed(
            color=(color), title=f'ㅤㅤㅤㅤㅤㅤㅤㅤBots information!')
        embed.add_field(name='Name', value=f'**[.] Abode**\n\n'
                        
                        f'**[-A] Arcane** \n\n'
                        f'**[!d] Disboard** \n\n'
                        f'**[;] YAGPD** \n\n'
                        f'**[-] Groovy ** \n\n'
                        
                        f'**[*] Carl** \n\n'
                        )

        embed.add_field(name='ㅤㅤㅤㅤInfo', value=f'Everything that a bot does.\n\n'
                        
                        f'Leveling and roles. \n\n'
                        f'Bumping server to disboard.\n\n'
                        f'Reaction roles. \n\n'
                        f'Music and lyrics bot.\n\n'
                        f'Reaction roles. \n\n'
                        )

        embed.add_field(name='Links', value=f'[Invite](http://bitly.com/98K8eH)\n\n'
                                            

                                            f'[Leaderboard](https://arcanebot.xyz/lb/757098499836739594) | [Website](https://www.arcanebot.xyz/)\n\n'
                                            f'[Server](https://discord.gg/eY4mens) | [Disboard](https://disboard.org/)\n\n'
                                            f'[Website](https://yagpdb.xyz/) | [Documentation](https://docs.yagpdb.xyz/)\n\n'
                                            f'[Server](https://groovy.bot/support) | [Commands](https://groovy.bot/commands)\n\n '
                                            f'[Website](https://carl.gg/) | [Server](https://discord.com/invite/DSg744v)\n\n'
                        )

        embed.set_footer(
            text=f"Note these bots may do different things on other servers.")

        x = await ctx.send(embed=embed)
        msg = await ctx.guild.get_channel(ctx.channel.id).fetch_message(781536472112168960)
        await msg.edit(embed=embed)

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def key(self, ctx):
        embed = discord.Embed(color=(color))
        embed.add_field(name='ㅤ', value=f'<:check:773959361953267742> : Vote yes\n\n'
                        f'<:xmark:773959363379462184> : Vote no\n\n'
                        f':green_circle: : Approved\n\n'
                        f':yellow_circle: : Maybe in the future\n\n'
                        f':red_circle: :  Denied', inline=False)

        await ctx.send(embed=embed)
        channel = ctx.guild.get_channel(757110183800471572)
        msg = await channel.fetch_message(779279015089143868)

        print(msg.content)
        await msg.edit(embed=embed)

    '''Supreme Elder role can\'t be earned for chat users unless one of the Supreme Elders is permanently inactive. Clan Leader role is only for those who contributes the most.```'''

    @commands.command(aliases=['pinfo'])
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def pointsinfo(self, ctx):
        embed = discord.Embed(color=(color))
        embed.add_field(name='Overall system', value=f'As you have seen or will see there are quite a few things going on here for eg :- Contribution points, Cultivation QI, Realms, Stats, Medals, etc. Everything shall be explained below.', inline=False)
        embed.add_field(name='Contribution points', value=f'If you are new to our server or discord in general you may wonder what are these contribution points about.\n'
                        f'Contibution points like like in your fav novel are points given to a sect member on completion of certain missions, trials, etc.\n'
                        f' In Abode of Scholars one can earn contribution points from chatting, giving suggestions, complaints or anything that contributes to the server.', inline=False)
        embed.add_field(name='Cultivation Qi', value=f'At this point no one is stranger to Qi, Qi here in this server will be increased ``.25`` for every message you send on ofcourse allowed channels. As you make progress on your Qi your stats along with realm with increase slowly but surely. To be more specific for every ``10`` Qi you get your stats will increase.')
        embed.add_field(
            name='Realm', value=f'Realms are actually take from my [favorite novel](https://lord-xue-ying.fandom.com/wiki/Cultivation_Levels), Relams will take you some time to make improvement on but it won\'t be that hard if you are active enough ;).', inline=False)
        embed.add_field(name='Stats', value=f'Stats are as you know attributes of someone, you can see your stats by ``.stats``. To begin with stats are given in a random order so your luck attribute will play some part in it. As I previously said for every 10Qi one gets, his/her stats will also increase.', inline=False)
        embed.add_field(name='Species, Paths and Medals', value=f'Species are also given at random from a list of bunch of unique and exciting spicies from wuxia genre and same with paths but do keep in mind that your path may help you with some things :)\n As medals are the honourable possesion one can have after reaching a certain realm or amount of Qi, do keep in mind that you can only have one medal at one time for now', inline=False)
        embed.add_field(name='What\'s the purpose?', value=f'Ok so you got a ton of points now what to do with them? There are some things you could do with them, you could buy potions, custom commands, custom roles, custom medals, increase stats, or even change your path, species and alot more ``.shop`` should help you :)')
        await ctx.send(embed=embed)


def setup(Bot):
    Bot.add_cog(vein4(Bot))
    print("Admin cog is wokring.")
