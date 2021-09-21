import paramiko
import os
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
	#print(stdout.read().decode('utf-8'))
	return  stdout.read().decode('utf-8')

def get_tasks(comp):
	command = 'boinccmd --get_tasks'
	if comp == server[0]:
		print(send_command(0, command))
	elif comp == server[1]: 
		print(send_command(1, command))
	elif comp == 'all':
		print(send_command(0, command))
		print(send_command(1, command))

def update_rosetta(comp):
	command = 'boinccmd --project https://boinc.bakerlab.org/rosetta update'
	if comp == server[0]:
		print(send_command(0, command))
	elif comp == server[1]:
		print(send_command(1, command))
	elif comp == 'all':
		print(send_command(0, command))
		print(send_command(1, command))

def get_hostname(comp):
	command = 'hostname'
	if comp == server[0]:
		print("Server 0, Server name %s, IP: %s", (send_command(0, command), server[0]))
	elif comp == server[1]:
		print("Server 1, Server name %s, IP: %s", (send_command(1, command), server[1]))
	elif comp == 'all':
		print("Server 0, Server name ", send_command(0, command), "IP: ", server[0], " \n")
		print("Server 1, Server name ", send_command(1, command), "IP: ", server[1], " \n")

os.system('clear')

x = 0
command = 'boinccmd --get_tasks'
for x in range(2):
	print("Connection Started", x)
	client.append([])
	client[x] = paramiko.SSHClient()
	connect_ssh(server[x], user, pw, x)

count = 0

while 1:
	print("list of servers. \n")
	get_hostname('all')
	print("List of supported commands: \n u = update server \n g = get task list \n\nRemember to select one of the servers by entering number. \n")

	val = input("Please enter a command. \n")
	
	if val.lower() == 'g':
		val = input("Which server? or type b (back) to return to previous menu. \n")
		while 1:
			if val == '0':
				get_tasks(server[0])
				break
			elif val == '1':
				get_tasks(server[1])
				break
			elif val.lower() == 'a' or val.lower() == 'all':
				get_tasks('all')
				break
			elif val.lower() == 'b' or val.lower() == 'back':
				os.system('clear')
				break
			else:
				print("Invalid server.")
				get_hostname('all')
				val = input("Please enter Server or type b or back to go back.\n")
	elif val.lower() == 'u' or val.lower() == 'update':
		val = input("Which server? or type b (back) to return to previous menu. \n")
		while 1:
			if val == '0':
				update_rosetta(server[0])
				print("Server has been updated.")
				break
			elif val == '1':
				update_rosetta(server[1])
				print("Server has been updated.")
				break
			elif val.lower() == 'a' or val.lower() == 'all':
				update_rosetta('all')
				print("All servers have been updated.")
				break
			elif val.lower() == 'b' or val.lower() == 'back':
				update_rosetta('clear')
				break
			else:
				print("Invalid server.")
				get_hostname('all')
				val = input("Please enter Server or type b or back to go back.\n")
	elif val.lower() == 'q' or val.lower() == 'exit':
		print("Connection Finished")
		quit()
	else:
		os.system('clear')
		print("Command invalid!\n")
