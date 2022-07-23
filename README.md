<h1 align="center" style="position: relative;">
	<a href="#visit"><img src="./docs/images/icon.png" width="200" height="200"></a><br>
    <strong>RoboBilly</strong>
</h1>

<p align="center">
    "Don't bully me pls"
</p>

<br/>

<p align="center">
    <img alt="Discord" src="https://img.shields.io/discord/750945243305869343?label=Basement&style=flat-square">
    <!-- <img alt="Travis (.com)" src="https://travis-ci.org/github/billydevyt/RoboBilly"> -->
    <!-- <img alt="Python" src=https://img.shields.io/github/pipenv/locked/python-version/billydevyt/RoboBilly> -->
    <img alt="Release" src=https://img.shields.io/github/v/release/billydevyt/RoboBilly?style=flat-square>
    <img alt="Heroku" src="https://img.shields.io/badge/heroku-passing-green?style=flat-square">
    <img alt="License" src="https://img.shields.io/github/license/billydevyt/RoboBilly?style=flat-square">
</p>

<p align="center">
    <a href="#building--running">Building & running</a> •
    <a href="#features">Features</a> •
    <a href="https://github.com/billydevyt/RoboBilly/blob/main/LICENSE">License</a> •
    <a href="https://github.com/billydevyt/RoboBilly/blob/main/.github/CODE_OF_CONDUCT.md">Code of Conduct</a> •
    <a href="#contributing">Contributing</a>
</p>

## Building & running

The bot is written in **Python 3.8**, you can run it via `python bot.py` from command line or just use the `run.bat` file to run it. If you are missing packages make sure to run install mentioned ones in `requirements.txt` prior to building. Also all the files required to Launch to **Heroku** is included.

## Configuration

1. `config.json` is where all of the bot configuration will be placed. The only fields that are essential for running the bot are `Token` and `Prefix`.

```json
{
    "Token": "get it from discord developer portal",
    "Prefix": "[]",
    "mails_channel": "mails",
    "server_name": "server's name here"
}
```

2. give the bot `Administrator` permissions.

3. Run `setup` command in the discord server.(for running this command, the user will need administrator permissions)

## Features
<p>
<img alt="Release" src=https://img.shields.io/github/v/release/billydevyt/RoboBilly?style=flat-square>
</p>


### ⛏ Minecraft 
#### Minecraft Module comes with most of the commands needed to check info of minecraft servers and the players online!
- coord 
- **mc**
    - server info
    - players online
    - player info
### 🔰🔰 Stackoverflow
#### Got a quick question? do a stackoverflow right from discord! 😉
- **stackoverflow**
### **>.<** Weebs
#### Get amazing news and info about anime, thanks to @DriftAsimov 
- **anime**
### 🐈Catify
#### Catify me! ᓇᘏᗢ
- catify
### 🐍 CheatSheet
#### python cheatsheets from https://cheat.sh/python/ 
- cheat
### ♟ Chess
#### Have a chess game right from discord! thanks to @billyeatcookies 
- chess
    - for more info on available commands, check [discord chess!](https://github.com/billyeatcookies/discord-chess)
### 🐙 GithubInfo
#### Got a repository or github user to search up? well you can, right from discord!
- github
### 📝 Latex
#### Render your latex code right from discord! share it quickly!
- latex
### 🎁 Fun!
#### Buncha fun commands to keep the server entertained!
- 8ball
- clap
- cursive
- emojify
- emojify2
- epicgamerrate
- greentext
- hack 
- imagine
- kill
- lemmegoogle
- lenny
- owo
- simprate
- snipe
- uselessweb 
- yasahiroify 
### 👤 User 
#### Rest of the fun commands, with a lot of utilities!
- ascii
    - make ascii arts from discord!
- bing 
- codeblocks 
- dontasktoask 
- git
    - The holy git command set! *git push billy outerspace*
- goodmorning!
- goodnight!
- google 
    - let me google that for you!
- hi 
    - hi!
- info
    - user info
- pastemyst 
- say
    - repeat me! 
- weather
    - billy, hows the weather today!
### 💪🏻 Moderation 
#### Moderation shall be done!
- activity 
- ban 
- kick 
- leaderboard 
- mute 
- myrep 
- purge 
- rep 
- reset 
- slowmode 
- thanks 
- unmute
### 📧 ModMail
#### Modmail service to contact mods easily through bot's dms!
- reply 
- setup
### 📜 Rules
#### Show individual or whole rules as part of moderation, see `rules.json` to set it up!
- rule 
- rules
## ⚙ Misc
- brainfuck
    - billy's brainfuck interpreter! go crazy!
- help
    - the holy help command
### 🤖 Bot
- source
    - bot's repository, means rn where you are, here!
### 🔧 Jishaku
- jishaku
    - management done pog!
### 🛠Owner
- close_http_session
    - close http session used by some of the commands, recommended to use it before killing the bot's process

## Contributing

contributions are accepted. Check out the [Contributing](./.github/CONTRIBUTING.md) for more info.
RoboBilly is [MIT-licensed](./LICENSE.md).

## Visit

Visit us here: https://basement-team.github.io
