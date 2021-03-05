#!/usr/bin/env python3


import subprocess
import os
import discord
import signal
import sys
from datetime import datetime
from discord.ext import commands


#--------------------------------------------------------------------------#


client = commands.Bot(command_prefix="/")
client.remove_command('help')


#--------------------------------------------------------------------------#


#El proceso de eliminar el LOG esta comentado para no perder el log cuando
#cierre de mala manera el programa
async def signal_handler(sig, frame):
	log.close()
	#subprocess.run(["shred", "-f", "-u", "cmdBotLog.txt"])

	sys.exit(0)


#--------------------------------------------------------------------------#
#                                 COMANDOS                                 #
#--------------------------------------------------------------------------#


@client.event
async def on_ready():
	log.write("Inicio de sesion!\n")
	log.write("Fecha: " + str(datetime.now())  + "\n\n\n")


@client.command()
async def exit(ctx):
	log.write("Comando: /exit\n")
	log.write("Fin de sesion!\n")
	log.write("Fecha: " + str(datetime.now())  + "\n")

	log.close()

	await ctx.send(file=discord.File("cmdBotLog.txt"))
	subprocess.run(["shred", "-f", "-u", "cmdBotLog.txt"])

	os._exit(0)


@client.command()
async def help(ctx):
	log.write("Commando: /help\n")
	log.write("Fecha: " + str(datetime.now())  + "\n\n\n")

	lines = open("helpBot.txt", "r").read()
	await ctx.channel.send(lines)


@client.command()
async def clear(ctx):
	try:
		messages = await ctx.channel.history(limit=200).flatten()
		for x in messages:
			await x.delete()
		await ctx.channel.send("Ya puedes mandar!")
	except Exception as e:
		await ctx.channel.send("Error: " + str(e))


@client.command()
async def cmd(ctx, *args):
	log.write("Comando: /cmd\n")
	log.write("Fecha: " + str(datetime.now()) + "\n")

	command = ""
	for x in args:
		command += x + " "
	command.rstrip()

	try:
		log.write("Comando: " + str(command) + "\n\nOutput:\n")

		output = subprocess.run(command, capture_output=True, shell=True)
		stdout = output.stdout.decode()

		if stdout == "":
			msg = "Comando ejecutado con exito (No output)"
			await ctx.channel.send(msg)
			log.write(msg)

		else:
			print("[LOG]")
			print(stdout)
			if len(stdout) >= 2000:
				count = 0
				messages = stdout.split("\n")
				msgSend = ""
				for msg in messages:
					if count == 5:
						await ctx.channel.send(msgSend)
						count = 0
						msgSend = ""

					if count == 0:
						msgSend += msg
					else:
						msgSend += "\n" + msg
					count += 1

				if msg != "":
					await ctx.channel.send(msgSend)

			else:
				await ctx.channel.send(stdout)
			log.write(stdout)

	except Exception as e:
		msg = "Error: " + str(e)
		await ctx.channel.send(msg)
		log.write(msg + "\n")

	log.write("\n\n")


@client.command()
async def send(ctx, arg):
	log.write("Commando: /send\n")
	log.write("Fecha: " + str(datetime.now()) + "\n")

	try:
		await ctx.send(file=discord.File(arg))
		log.write("Fichero " + arg  + " mandado con exito\n")
	except Exception as e:
		msg = "Error: " + str(e)
		await ctx.channel.send(msg)
		log.write("Error al abrir el fichero: " + arg + "\n")
		log.write(msg + "\n")

	log.write("\n\n")



@client.command()
async def echo(ctx, *args):
	log.write("Comando: /echo\n")
	log.write("Fecha: " + str(datetime.now()) + "\n")
	log.write("Mensaje a lanzar de vuelta:\n\"")

	msg = ""
	for x in args:
		msg += x + " "
	msg = msg.rstrip()

	await ctx.channel.send(msg)
	log.write(msg + "\"\n\n")


#--------------------------------------------------------------------------#


signal.signal(signal.SIGINT, signal_handler)

global log
log = open("cmdBotLog.txt", "+w")

TOKEN = open("token.txt", "r").readline()
client.run(TOKEN)























#
