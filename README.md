
# YATS - Yet Another Telegram Store

**YATS** is a telegram bot made in python that lets you create a simple telegram store that is easily customizable to people close to no coding expirience.

|Dependencies       |Version |
|-------------------|--------|
|Python             |>= 3.12 |
|python-telegram-bot|>= 21.10|
|googletrans        |>= 4.0.2|
|langdetect         |>= 1.0.9|

## Setup
 1. Install dependencies by running `python -m pip install "python-telegram-bot>=21.10"` command.
 
 2. Message [@BotFather](https://telegram.me/BotFather) on Telegram and go through the setup process to obtain your HTTP_API token.

 3. Configure `config.json` file as per the table below.
 
|Config           |Suggested value                      |Description |
|-----------------|-------------------------------------|------------|
|bot_name         | "Bot Name"                          |This isn't necessary, but if you host the bot occasionally, I recommend adding it to prevent bot name display issues in old-instance chats after reloading.|
|bot_token        | "HTTP_API Token"                    |Enter the token you obtained from [@BotFather](https://telegram.me/BotFather)|
|channel_link     | "https://t.me/{your_channel_name}"  |Enter your shop or info channel link here so users can join.|
|operator_ids     | [your_user_id]                      |Enter your user ID here. If you don't know it, run the bot empty and send `/start` your ID will appear on the start screen. This grants you access to the admin panel.|
|operator_username| "telegram handle of yours"          |Don't include `@` in the handle. Users can quick chat with you using the bot button if they encounter issues.|

 4. Run the `start.py` script, and everything else will launch automatically.
 
 5. If you set up `config.json` correctly, you should see the admin panel. Enjoy customizing the bot!

## Legal notice

This bot is provided for lawful and legitimate purposes **only**. I do not encourage, endorse, or support any illegal activities. I do not take responsibility for any misuse, illegal activities, or damages caused by this software. Users assume full responsibility for compliance with laws applicable in their country.
