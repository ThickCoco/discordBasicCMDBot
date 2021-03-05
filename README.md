# discordBasicCMDBot

__Basic python discord Bot__

This bot is suppose to be use as an interface to a shell in the machine which is hosting it.
Can be usefull as a secondary mean to comunnicate witch a machine.

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
		You can use it multiples times to full clear the channel.
	/cmd <command>: 
		Core command. Type /cmd followed by the command that you want to execute in the remote machine.
		The output of the command will be send back to the channel.
	/send <file>: 
		Send the file selected from the host machine.
	/echo <msg>: 
		Return the same message that was sent.

#-------------------------#

Legal note: the developer is not responsible for the fraudulent or malicious use of this bot.
```

