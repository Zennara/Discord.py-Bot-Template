# Discord Bot Template with Python 3.x
This is a template for creating a custom [Discord.py](https://discordpy.readthedocs.io/en/stable/api.html) bot on [repl.it](https://www.replit.com). Make sure you read all of the comments as they contain vital information on how to get the bot up and running.

### No Commands.ext
Warning, this does **not** use the Discord Python commands extension. I have never liked using it for my Discord bots, so I did not include it in this template.

### Excessive Comments
I added *a ton* of comments to this so that the viewer might be able to decipher what I put down into this code. It's a compilation of all of the start up stuff I have learned over the years of amaking bots.

### Repl.it Database Support
I also linked repl.it's built-in [database](https://docs.replit.com/hosting/database-faq) because most of my bots use it. By default when the bot joins the server, it will automatically add a key, the `guild id`, with a value of `"prefix": "z/"`. If you want to disable all this, simply delete anything that has to do with `db`.


# How To Set-Up
If you do not want to read the messy comments in the code, here is a step-by-step tutorial on how to set it up below.

## Creating the Bot
- Go to the [Discord Bot Dev Portal](https://discord.com/developers/applications) and sign in.
- From there, go to **applications**
- Create a **New Application**
- Under **General Information**, you can change the bots bio under **description**.
- Click on **Bot**, here you can change the **Username** and **Profile Picture**
- Copy the bot's **Token**
- Ensure you check which **intents** your bot will need. If you don't check them all, make sure you change the **Intents** in the code.

## Adding the Code
- Go to [repl.it](https://www.replit.com) and log-in or create an account
- Go to [this link](https://replit.com/@KeaganLandfried/Discordpy-Bot-Template) and fork the repl. This is the template here.
- Open your repl. Click the left sidebar **lock icon**.
- Create a new secret, name this `TOKEN` with a value of the copied bot token from earlier.
- Overview the code to hopefully understand it.

## Making it Run
- Go to [UptimeRobot](https://www.uptimerobot.com) and sign-in / create an account
- Add a **New Monitor**
- Select the **HTTP(S)** monitor type.
- Enter your link to your repl. You can find it [here](https://cdn.discordapp.com/attachments/929182726203002920/929182736546140201/unknown.png).
- Add a name to easily find it
- Make the **Monitoring Interval** anything less than 60 minutes.

## Inviting the Bot
- Go to your application in the [Discord Bot Dev Portal](https://discord.com/developers/applications)
- Go to **OAuth2**, then **URL Generator**
- Select the checkbox, **bot**.
- Add the permissions your bot will need. If you are just testing, feel free to give it Administrator.
- Copy the link and paste it into your browser to invite the bot.
- Select your server and approve.

### If done correctly, your bot should now run. Test it out by using my built-in `z/ping` commands. The bot should return the message `pong`.
