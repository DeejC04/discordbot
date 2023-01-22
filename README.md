# Simple Discord Bot

> **NOTE**: Just to preface, this was just a personal day project of mine. It's far from perfect and needs quite a bit of refinement.

## What does this bot do?  

In its current state, it is very barebones. Its abilities (or should I say, singular ability), are limited to allowing a user to join a designated voice channel, and then have a "personal" channel created for them. The user is then moved into that channel. Once all users leave the channel, it will be deleted.

## Usage

Using this bot is fairly straightforward. First, you are going to want to go to the [Discord Developer Portal](https://discord.com/developers/). You will be promted to sign in, and presented with an "applications" screen. 
![](https://imgur.com/a/XmfY59a)

Click the "New Application" button on the top right and enter a name for this application. It can be whatever. Once typed, accept the terms and conditions and select "Create".

Now, you will be in a screen that looks like this:
![](https://imgur.com/a/bFXDxY4)

Select the "OAuth2" dropdown on the sidebar and select the "URL Generator" option. Check off "bot". Finally, you can grant administrator access to the bot. If you don't want to do that, you *should* be able to get away with just giving it permissions to manage channels and move members.

Once finished, scroll to the bottom of the page and copy the generated URL. Paste that into another tab within your browser, and select the server you'd like to add the bot to. Perfect! You've added the bot.

Navigate to the "Bot" tab on the sidebar now, and click "Reset Token". Once you do, copy that string and paste it somewhere (like a notepad document, at least temporarily).

Scroll down within that same tab, and flip the "Presence Intent", "Server Members Intent", and "Message Content Intent" switches. Make sure to save your changes.

You're now done with the primary setup of the bot. Now comes configuring it to your server! Reference the below section to do so.

## Server Setup

1. Remember that token we generated? We are going to put that into use now.
   - First, clone this repository onto your own PC
   - Then, create a file within the folder called ".env". Within that file, type the following: "DISCORD_TOKEN={token}", and of course replace {token} with whatever token you recieved.
2. Open your text editor or IDE of choice. If you don't have one, you can use something like VSCode. We aren't going to do anything advanced here.
3. Open the Discord bot folder, and open "bot.py" into your text editor/IDE. You may see some errors. This is because there are some required packages; we will get to that.
4. Navigate to line 26. It should look like: `guild = bot.get_guild(1064736630319108156)`. Delete the string of numbers out of the parentheses. 
5. Now, go into Discord.
   - Open your settings, scroll down all the way, and click "Advanced" on the sidebar.
   - Enable Developer Mode
   - Exit your settings, and go to the server you want to add the bot to.
   - At the top left, where the name of your server is, right click. At the bottom of the context menu, you should see "Copy ID". Click this.
6. Paste that ID that you just copied into the now empty parentheses after `bot.get_guild`.
7. Scroll down to line 32 and delete the text inside of the parentheses here too.
8. Open Discord back up.
   - Within your server, create a category in your server called "Create your own channel!". This is case sensitive. 
      - If you'd like to change the name of the category, go to line 29 and replace the text within the quotations with whatever the category name should be. Make sure it's the exact same as the category name within Discord.
   - Next, create a voice channel called "Join to Create a Channel!" or something similar. 
   - Just like before, right click it, and copy its ID.
   - Paste that ID into the parentheses.
9. This step isn't absolutely necessary, but I recommend creating a virtual environment to host this bot from your PC. It's a bit extensive to explain here, but you can Google it. It's very simple and there are tons of resources online.
10. Finally, we will install required packages.
    - Provided you are in the directory of the file, run `pip install -r requirements.txt`.
    - This will install the necessary prerequisites.

### Running the program

Now that the tedious setup is done, how do we run the bot?

Within your terminal (inside of the project directory), type `python3.11 bot.py`. If you don't have 3.11, then just use `python3 bot.py`. 

The bot should now be up and running, feel free to test on your server! Let me know if I missed anything!


## Bugs/Limitations?

While testing, I've definitely experienced a few bugs.

- Likely because of mistakes in my code, there are common `AttributeError`s and `ValueError`s thrown around. I've set these to have exceptions with pass as a parameter. Obviously not the best practice, but it's temporary while I resolve these errors.

