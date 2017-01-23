import os, sys
import paramiko


host = '192.168.1.41'
user = 'root'
password = 'openelec'
port = 22
command = 'poweroff'


def poweroff():
	try:
		print('\napagando la Raspberry PI...')
		conecta = paramiko.Transport((host, port))
		conecta.connect(username=user, password=password)
		canal = conecta.open_session()
		canal.exec_command(command)
	
		print('\nRaspberry PI ha sido correctamente apagada\n')

	except:
		print('\nNo se ha podido apagar la Raspberry Pi\n')


if __name__ == "__main__":
	poweroff()