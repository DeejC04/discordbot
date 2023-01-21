# Import necessary packages

import discord, os
from dotenv import load_dotenv

# Assign "TOKEN" constant to API token stored in a .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Assign "bot" variable to the Discord client, assign intents to all for ease of use
bot = discord.Client(intents=discord.Intents.all())
# Bot says that it is ready to use once started up
@bot.event
async def on_ready():
    print(f"{bot.user} is ready for use")

# Get guild ID of every server joined

# Allows user to join designated channel to autocreate their own temp one. Deletes when all users leave the channel
@bot.event

# Primary async function that checks for a status update within the voice chat.
async def on_voice_state_update(member, before, after):
    
    # Assigns "guild" variable to the server ID with the get_guild method. This makes it usable later, since the ID can't be directly referenced
    guild = bot.get_guild(1064736630319108156)

    # Assigns "category" variable to the "Voice Channels" category in Discord. This allows later use too
    category = discord.utils.get(guild.categories, name = "Create your own channel!")

    # Essentially the same functionality as the "guild" variable assignment
    channel = bot.get_channel(1066473345886990447)
    
    newchanname = f"Channel for {member}"

   # Primary program conditionals
    #Checks if the voice status of the channel the user joined is the same as the voice status of the channel variable (the one designated to grant a personal channel)
    if after.channel == channel:
        newchan = await guild.create_voice_channel(newchanname, category=category)
        await member.move_to(newchan)
    
    # Checks if the voice status of the channel the user was in before is different than the channel variable (this means they left a different channel; AKA their personal one)
    try:
        if before.channel.name != newchanname:
            pass
        else:
            try:
                if len(before.channel.members) == 0:
                    await before.channel.delete()
            except (ValueError, AttributeError):
                pass
            else:
                pass
    except (ValueError, AttributeError):
        pass

# Runs the bot, takes the token as input to verify
bot.run(TOKEN)

