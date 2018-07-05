'''
Developed with <3, the power of water which is necessary for me to survive and for the sake of doing so.
Designed for 3.6.
@author: AlwaysLivid
'''
print("       .__           .__  .__ ___.           __   ")
print("  _____|  |__   ____ |  | |  |\_ |__   _____/  |_ ")
print(" /  ___/  |  \_/ __ \|  | |  | | __ \ /  _ \   __\ ")
print(" \___ \|   Y  \  ___/|  |_|  |_| \_\ (  <_> )  |  ")
print("/____  >___|  /\___  >____/____/___  /\____/|__|  ")
print("     \/     \/     \/              \/             ")

try:
    import discord
    from discord.ext import commands
    import subprocess
    import logging, random, sys
    import config, private
except (AttributeError, ImportError):
    import time
    print("There was an error with importing some necessary modules.")
    print("Exiting in 5 seconds...")
    time.sleep(5)
    exit()

bot = commands.Bot(command_prefix=config.prefix, description=config.description)

async def CogLoader():
    for file in config.extensions:
        try:
            bot.load_extension(file)
        except Exception as e:
            logging.critical("Failed to load {}! ({})".format(file, e))

@bot.event
async def on_ready():
    logging.info("Bot (almost) ready!")
    logging.info("Name: {}".format(bot.user.name))
    logging.info("Name: {}".format(bot.user.discriminator))
    logging.info("ID: {}".format(bot.user.id))
    await CogLoader()
    activity = random.choice(config.statuses)
    await bot.change_presence(activity=discord.Game(name=activity))            
    logging.info("Bot ready!")

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Logging in to Discord!")
    logging.info("Credentials used: {}".format(private.token))
    bot.run(private.token, reconnect = True)

main()