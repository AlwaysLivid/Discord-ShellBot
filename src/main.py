#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: AlwaysLivid
@description: Perform administrative tasks remotely via Discord, without the need of port forwarding and other complicated networking stuff.
'''

print("""
      .__           .__  .__ ___.           __  
  _____|  |__   ____ |  | |  |\_ |__   _____/  |_ 
 /  ___/  |  \_/ __ \|  | |  | | __ \ /  _ \   __\
 \___ \|   Y  \  ___/|  |_|  |_| \_\ (  <_> )  |
/____  >___|  /\___  >____/____/___  /\____/|__|
     \/     \/     \/              \/
         Copyright (C) 2019 AlwaysLivid

=============================================================
======================= DISCLAIMER ==========================
=============================================================
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; read the LICENSE file for details.

This bot was made for personal use and only the bot owner is
permitted to perform any sort of operation.

Never trust untrusted input.

The official documentation does not recommend the use of the
subprocess module without any sort of input sanitization.

https://docs.python.org/3/library/subprocess.html

This bot currently does not support interactive programs that
require additional user input.

=============================================================

""")

import discord
from discord.ext import commands
import subprocess
import logging, random, sys
import config

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - %(asctime)s - %(levelname)s - %(message)s', 
    handlers=[
        logging.FileHandler("{0}/{1}.txt".format(os.path.dirname(os.path.realpath(__file__)), "log")),
        logging.StreamHandler()
    ]
)

try:
    from private import client_secret
    client_secret = private.client_secret
    logging.warning("Using private.py file!")
except ImportError:
	logging.info("The file private.py was not found.")
	logging.warning("Using environment variable instead.")
    client_secret = os.environ['CLIENT_SECRET']

bot = commands.Bot(command_prefix=config.prefix, description=config.description)

async def CogLoader():
    for file in config.extensions:
        try:
            bot.load_extension(file)
        except Exception as e:
            logging.critical("Failed to load {}! ({})".format(file, e))

@bot.event
async def on_ready():
    logging.info("Name: {}".format(bot.user.name))
    logging.info("Name: {}".format(bot.user.discriminator))
    logging.info("ID: {}".format(bot.user.id))
    await CogLoader()
    activity = random.choice(config.statuses)
    await bot.change_presence(activity=discord.Game(name=activity)) 
    if not (os.getenv('CI') == None or os.getenv('CI') == False) or not (os.getenv('CONTINUOUS_INTEGRATION') == None or os.getenv('CONTINUOUS_INTEGRATION') == False):
        logging.critical("CI detected!")
        logging.critical("Everything seems to be fine. Exiting...")
        exit()           
    logging.info("Bot ready!")

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Logging in to Discord!")
    try:
        bot.run(client_secret, reconnect = True)
    except discord.DiscordException as e:
        logging.critical(e)

if __name__ == "__main__":
    main()