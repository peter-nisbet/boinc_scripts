import paramiko
import configparser

# Read config file to get username password and server credentials
client = []

config = configparser.ConfigParser()
config.sections()
config.read('boinc.conf')

user = config['Credentials']['user']
pw = config['Credentials']['password']

server1 = config['IP Address']['ip1']
server2 = config['IP Address']['ip2']

#SSH connect function
def connect_ssh(server, uname, passw, num):
	client[num].set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client[num].connect(server, username = uname, password = passw)

#function to read results
def read_client(num):
#	stdin, stdout, stderr = client[num].exec_command('boinccmd --get_tasks')
	stdin, stdout, stderr = client[num].exec_command('ls -l')
	print(stdout.read().decode('utf-8'))

x = 0
for x in range(2):
	print("Connection Started", x)
	client.append([])
	client[x] = paramiko.SSHClient()
	connect_ssh(server1, user, pw, x)
	read_client(x)

print("Connection Finished")
