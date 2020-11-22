import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient


class vein8(commands.Cog, name='leveling'):
    def __init__(self, client):
        self.client= client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id != 757098499836739594:
            return
        if message.author.id == 759784064361299989:
            return
        bot1= 757136905329442859
        bot2=757136943149613076
        music= 768684108770574366
        testing = 757941959796195484
        if message.channel.id == (bot1) or (bot2):
            return
        elif message.channel.id == (music) or (testing):
            return
        author_id= str(message.author.id)

        mongo_url= "mongodb://Abode:vein6969@abode-shard-00-00.hkghi.mongodb.net:27017,abode-shard-00-01.hkghi.mongodb.net:27017,abode-shard-00-02.hkghi.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-l4ozdp-shard-0&authSource=admin&retryWrites=true&w=majority"

        cluster= MongoClient(mongo_url)
        db = cluster['AbodeDB']
        collection= db['Levels']
        user_id = {"_id": author_id}

        if (collection.find_one({"_id": author_id})== None):

            leauge = "Novice scholar"
            user_data= {"_id" : author_id, "points": 1, "Leauge": leauge,"Qi": 0}
            collection.insert_one(user_data)


        else:
            query= {"_id": author_id}
            level = collection.find(query)


            for lvl in level:
                cur_p= lvl['points']
                new_p= cur_p + 1


                cur_q = lvl['Qi']
                new_q = cur_q + 0.25
                Leauge = lvl['Leauge']

                if (new_q % 200) == 0:
                    await ctx.send(f'<:Cuppedfist:757112296094040104> {message.author.mention}, you Qi just got to {new_q}. ')
                if (new_q == 500):
                    await ctx.send(f'<:Cuppedfist:757112296094040104> {message.author.mention}, Congragulations you earned the ``intermediate scholar`` medal.')
                    new_medal1 = 'Intermediate scholar'
                    collection.upate_one({"_id" : author_id}, {"$set":{"Leauge" : new_medal1}})

                elif (new_q == 1500):
                    await ctx.send(f'<:Cuppedfist:757112296094040104> {member.author.mention}, Congragulations you earned the ``Expert scholar`` medal.')
                    new_medal2= 'Expert scholar'
                    collection.upate_one({"_id" : author_id}, {"$set": {"Leauge" : new_medal2}})
                collection.update_one({"_id":author_id}, {"$set":{'points':new_p}})
                collection.update_one({"_id":author_id},  {"$set":{"Qi": new_q}})








def setup (client):
    client.add_cog(vein8(client))
    print("Leveing cog is working.")