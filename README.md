# auto_smb
a python script using shodan cli to search for authentication disabled SMB and enumerate shares.

# Installation
apt install python3-shodan
apt install smbclient
pip install -r requirements.txt

# Run the script
python3 auto_smb.py

# if you have your own external list, should be formatted as the following:
IP PORT
0.0.0.0 445
0.0.0.0 12345
