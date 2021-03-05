# discordBasicCMDBot

*Basic python discord Bot*

This bot is supposed to be used as an interface to a shell in the machine which is hosting it.
Can be useful as a secondary means to communicate with a machine.

When you execute the _/exit_ command the bot will send back a log file which contains all the commands executed along with the output and timestamp of said command. The bot will be stopped too.

Change the _token.txt_ file with your own token. You can get it from here: [discord developer portal](https://discord.com/developers/applications).

Help prompt:

```
#Help prompt for using cmdBot#

This bot is thought to be an interface for the use of a shell on the machine where it is hosted.

Command prefix: '/'
    Ej: /help,  /cmd <command>

Command list:
    /exit:
        Close the service in the remote machine and send the log back.
    /help:
        Display the help box.
    /clear:
        Clear the last 200 messages in the text channel.
        You can use it multiple times to fully clear the channel.
    /cmd <command>:
        Core command. Type /cmd followed by the command that you want to execute in the remote machine.
        The output of the command will be sent back to the channel.
    /send <file>:
        Send the file selected from the host machine.
    /echo <msg>:
        Return the same message that was sent.

#-------------------------#

Legal note: the developer is not responsible for the fraudulent or malicious use of this bot.
```
