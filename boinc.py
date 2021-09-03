import paramiko
import configparser
import time

# Read config file to get username password and server credentials
client = []
server = [0]*2

config = configparser.ConfigParser()
config.sections()
config.read('boinc.conf')

user = config['Credentials']['user']
pw = config['Credentials']['password']

server[0] = config['IP Address']['ip1']
server[1] = config['IP Address']['ip2']

#SSH connect function
def connect_ssh(server, uname, passw, num):
	client[num].set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client[num].connect(server, username = uname, password = passw)

#function to read results
def send_command(num, command):
	stdin, stdout, stderr = client[num].exec_command(command)
	print(stdout.read().decode('utf-8'))

x = 0
command = 'boinccmd --get_tasks'
for x in range(2):
	print("Connection Started", x)
	client.append([])
	client[x] = paramiko.SSHClient()
	connect_ssh(server[x], user, pw, x)
#	send_command(x, command)

count = 0

while 1:
	#command = 'boinccmd --get_tasks'
	command = 'ls'
	send_command(0, command)
	send_command(1, command)

	time.sleep(60)

	command = 'ls -l'
	send_command(0, command)
	send_command(1, command)
	
	count = count + 1
	print('count = ', count)
	
	time.sleep(60)

print("Connection Finished")