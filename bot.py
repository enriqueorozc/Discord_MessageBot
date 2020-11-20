#!/usr/bin/env python3

import discord
import asyncio
import time
import logging
import time
from discord.ext import commands
from discord import User
from discord import VoiceState
from discord import Message
from discord import Client


client = discord.Client()

@client.event
async def on_ready():
    print('Ready to serve a purpose')

@client.event
async def on_voice_state_update(member, before, after):
#Message for User1
    if member.id == UserID:  #Copy and paste Users ID
        if before.channel is None and after.channel is not None:
            if after.channel.id == VoiceChannelID:  #Copy and paste VoiceChannelID
                print("{} joined {}.".format(member.display_name, after.channel))
                channel = client.get_channel(VoiceChannelID)
                await channel.send('Enter Message Here {}'.format(after.channel))


#Message for User2
    if member.id == UserID:  #Copy and paste Users ID
        if before.channel is None and after.channel is not None:
            if after.channel.id == VoiceChannelID:  #Copy and paste VoiceChannelID
                print("{} joined {}.".format(member.display_name, after.channel))
                channel = client.get_channel(VoiceChannelID)
                await channel.send('Enter Message Here {}'.format(after.channel))


#Message for User3
    if member.id == UserID:  #Copy and paste Users ID
        if before.channel is None and after.channel is not None:
            if after.channel.id == VoiceChannelID:  #Copy and paste VoiceChannelID
                print("{} joined {}.".format(member.display_name, after.channel))
                channel = client.get_channel(VoiceChannelID)
                await channel.send('Enter Message Here {}'.format(after.channel))


@client.event
async def on_member_join(member):
    await member.send("Welcome!")


client.run("BOT TOKEN HERE")  #Enter BOT TOKEN
