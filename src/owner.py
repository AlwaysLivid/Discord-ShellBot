#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: AlwaysLivid
@description: Perform administrative tasks remotely via Discord, without the need of port forwarding and other complicated networking stuff.
'''

if __name__ == "__main__":
    exit()

import subprocess
import logging
import config
import discord
import sys
from discord.ext import commands

class Owner:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='disablebot', hidden=True)
    @commands.is_owner()
    async def disablebot(self, ctx):
        logging.info("disablebot command issued by {}#{} (ID: {}).".format(ctx.author, ctx.author.discriminator, ctx.author.id))
        embed = discord.Embed(title=":wave:", color=0x551a8b, description="Roger that, see ya!")
        embed.set_author(icon_url=ctx.author.avatar_url, name=str(ctx.author))
        logging.critical("Logging out per {}'s request!".format(ctx.author))
        await ctx.send(embed=embed)
        self.bot.logout()
        exit()
    
    '''
    Inspired by the following gist;
    https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
    '''
    
    @commands.command(name='cogmgmt', hidden=True)
    @commands.is_owner()
    async def cogmgmt(self, ctx, load: str, file: str):
        class OperationError(Exception):
            pass

        logging.info("cogmgmt ({} {}) command issued by {} (ID: {}).".format(load, file, ctx.author, ctx.author.id))
        load = load.lower()        
        embed = discord.Embed(title="Cog Management", color=config.admin_color)
        embed.set_author(icon_url=ctx.author.avatar_url, name=str(ctx.author))
        try:
            if load == "enable":
                try:
                    logging.info("Loading {}...".format(file))
                    self.bot.load_extension(file)
                    config.extensions.append(file)
                    embed.add_field(name="Status", value="Operation Succeeded!", inline=False)
                    logging.info("Loaded {}...".format(file))
                    await ctx.send(embed=embed)
                except Exception:
                    logging.critical("FAILED TO LOAD {}".format(file))
                    raise OperationError
            elif load == "disable":
                try:
                    logging.info("Unloading {}...".format(file))
                    if file == __name__:
                        logging.critical("Can't unload {}! (You'd unload the core parts of the bot, you silly goose!)".format(__name__))
                        raise OperationError
                    else:
                        try:
                            self.bot.unload_extension(file)
                            config.extensions.remove(file) # Temporarily removes 'file' from the config.extensions list, just in case the user decides to reload the bot after removing the 'file' cog.
                            embed.add_field(name="Status", value="Operation Succeeded!", inline=False)
                            logging.info("Unloaded {}...".format(file))
                            await ctx.send(embed=embed)
                        except Exception:
                            logging.critical("FAILED TO UNLOAD {}".format(file))
                            raise OperationError
                except Exception:
                    raise OperationError
            else:
                raise OperationError
        except OperationError:
            embed.add_field(name="Status", value="Operation Failed! (Check the console for more info!)", inline=False)
            embed.add_field(name="Syntax", value="`m!manualcogloader <enable/disable> <cogname>`", inline=False)
            await ctx.send(embed=embed)

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload(self, ctx):
        logging.info("Reload command issued by {} (ID: {}).".format(ctx.author, ctx.author.id))
        embed = discord.Embed(title="Reload", color=config.admin_color)
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        try:
            for file in config.extensions:
                self.bot.unload_extension(file)
                logging.critical("Unloaded {}!".format(file))
                self.bot.load_extension(file)
                logging.critical("Reloaded {}!".format(file))
            logging.critical("Reloaded!")
            embed.add_field(name="SUCCESS!", value="Operation Succeeded!", inline=False)
            await ctx.send(embed=embed)
        except:
            embed.add_field(name="FAILURE!", value="Operation Failed!", inline=False)
        
        
    @commands.command(name='exec', description="Execute commands")
    @commands.is_owner()
    async def exec(self, ctx, *, args):
        logging.info("exec ({}) command issued by {} (ID: {}).".format(args, ctx.author, ctx.author.id))
        embed = discord.Embed(title="Execution", color=config.admin_color)
        embed.set_author(icon_url=ctx.author.avatar_url, name=str(ctx.author))
        command = args.split(" ")
        output = subprocess.check_output(command).decode()
        embed.add_field(name = "Input", value = args, inline = False)
        embed.add_field(name = "Output", value = output, inline = False)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Owner(bot))