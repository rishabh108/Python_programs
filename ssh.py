import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('raspberry.lan', username='shaurya', password='terralogic')

stdin, stdout, stderr = client.exec_command('ls -l')

for line in stdout:
    print line.strip('\n')

client.close()
