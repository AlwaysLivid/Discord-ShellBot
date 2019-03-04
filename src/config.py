#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: AlwaysLivid
@description: Perform administrative tasks remotely via Discord, without the need of port forwarding and other complicated networking stuff.
'''

if __name__ != "__main__":
    # Bot Configuration
    prefix = "s!"
    description = "Remotely administrate machines without being an expert in networking!"
    extensions = ['owner']
    statuses = ['with the subprocess module.', 'with a random TTY terminal.', 'with an insecure eval() function.']
    shell = True
    # Color Configuration
    neutral_green = 0x98fb98 # Basic functions, such as the ping command. 
    admin_color = 0x00ff00 # Administrative operations.
    success_green = 0x0000ff # Successful operations.
    failure_red = 0xff00000 # Failed operations.
