import discord
from discord.ext import commands



class vein10(commands.Cog, name='shop'):
    def __init__(self, client):
        self.client= client




def setup (client):
    client.add_cog(vein10(client))
    print("Shop cog is working.")
