from telethon import TelegramClient, events, sync
from colorama import Fore, Back, Style
import core.logo as logo


logo.banner()

try:
	api = input('Tg$Api:~# Enter you api:>> ')
	api_hash = input('Tg$Hash:~# Enter you hash:>> ')

	client = TelegramClient('session', api, api_hash)
	client.start()

except:

	print(Fore.RED, 'You fuckin debil')
	raise SystemExit

def sendMes():
	try:
		ms = int(input('Enter num:>> '))
		name = input('Enter target name:>> ')
		mess = input('Enter you massage:>> ')
		for i in range(ms):
			client.send_message(name, mess)

	except KeyboardInterrupt:
		print(Fore.RED, '[-] - Ohh god')
		client.disconnect()


sendMes()