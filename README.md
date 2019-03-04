[![Build Status](https://travis-ci.org/alwayslivid/ShellBot.svg?branch=master)](https://travis-ci.org/alwayslivid/ShellBot)

# ShellBot

Perform administrative tasks remotely via Discord, without the need of port forwarding and other complicated networking stuff. This bot was made for personal use.

## Requirements

* Python 3.5.3+
* [discord.py (rewrite)](https://github.com/Rapptz/discord.py/tree/rewrite)

## Setup

* Create a new bot account [here.](https://discordapp.com/developers)
* Obtain your client secret.
* Make a new Python file (*.py*) and enter *client_secret = "<CLIENT SECRET>"*.
* Alternatively, add the client secret to an environment variable with the key *"CLIENT_SECRET"*.

## Usage

* s!cogmgmt: Add your own cogs.
* *Syntax: s!cogmgmt <enable/disable> <cog>*
* s!reload: Reload the bot.
* s!disablebot: Turn off the bot.

### Disclaimer

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; read the LICENSE file for details.

This bot was made for personal use and only the bot owner is
permitted to perform any sort of operation.

Never trust untrusted input.

The official documentation does not recommend the use of the
subprocess module without any sort of input sanitization.

This bot currently does not support interactive programs that
require additional user input.

https://docs.python.org/3/library/subprocess.html