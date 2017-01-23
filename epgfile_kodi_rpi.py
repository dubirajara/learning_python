import urllib.request
import os, sys
import pysftp
import paramiko


url = 'http://xxxxxx.info'
epgfile = '/Users/root/Downloads/tv.xmltv'
host = '192.168.1.41'
user = 'root'
password = 'openelec'
port = 22
command = 'reboot'

urllib.request.urlretrieve(url, epgfile)

print("EPG descargado")


def con_sftp():
	try:
		print('\nConectando por sftp con la Raspberry PI...')
		sftp = pysftp.Connection(host, username=user, password=password)
		sftp.chdir('tvshows')
		sftp.put(epgfile, preserve_mtime=True)
		sftp.close()
		print('\nArquivo subido al servidor con exito')

	except:
		print('\nNo se ha podido conectar por sftp con la Raspberry Pi')
	

def reboot():
	try:
		print('\nReiniciando la Raspberry PI...')
		conecta = paramiko.Transport((host, port))
		conecta.connect(username=user, password=password)
		canal = conecta.open_session()
		canal.exec_command(command)
	
		print('\nRaspberry PI ha sido correctamente reiniciada\n')

	except:
		print('\nNo se ha podido reiniciar la Raspberry Pi\n')


con_sftp()
reboot()
