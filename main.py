# import paramiko
# ssh=paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('server_ip', username='', password='')
# log_file_path='/path/to/logs'
# stdin, stdout, stderr = ssh.exec_command('cat ' + log_file_path)
# logs = stdout.read().decode()
# ssh.close()
# print(logs)
a=1234
b=a%100
print(a)
print(b)