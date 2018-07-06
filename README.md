# ShellBot
Perform administrative tasks remotely via Discord, without the need of port forwarding and other complicated networking stuff. This bot was made for experimental/educational purposes.

# Features
You (and only you!) can run commands on your Windows/Mac/Linux workstation by simply ordering the bot to do so.
Just invite the bot to your server and run ```s!exec```!.

# Additional Commands
### **s!cogmgmt**: Add your own cogs.
*Syntax: s!cogmgmt <enable/disable> <cog>*
### **s!reload**: Reload the bot.
### **s!disablebot**: Turn off the bot.

# Additional Notes
If you'd like to give access to the bot to everyone, then just open up *owner.py* using any text editor that doesn't start with v and ends with im, hit *CTRL + F* and finally, delete all the lines that contain the following closure: ```@commands.is_owner()```.

Also, please don't try to run commands such as *python*, *vim*, *rm -rf* or *node* through Discord. This bot was designed with basic commands such as *dir* (Windows), *ls*, *ping* and that sort of simple stuff. You won't be able to enter additional input or interfere with the bot in any way until a return code's returned.

**YOU'RE ON YOUR OWN, RUN THIS BOT AT YOUR OWN RISK, NEVER TRUST UNTRUSTED INPUT.**

# Disclaimer

**THE CODE IS PROVIDED AS IS AND WAS MADE FOR PERSONAL USE AND ONLY. I'M IN NO WAY RESPONSIBLE FOR ANY SORT OF DATA LOSS, HARDWARE DAMAGE, EXPLOSION OF SAID HARDWARE OR ANIMAL-RELATED DEATHS. (Read the license for more details)**
