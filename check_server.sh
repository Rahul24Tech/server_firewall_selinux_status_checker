#!/bin/bash

# Server details
server='213.181.107.179'
ssh_user='deploy'
ssh_key_path='.ssh/id_rsa'
ssh_cert_path='.ssh/rk-cert.pub'

echo "Checking $server..."

# SSH into the server and run the commands
ssh -p 22 "$ssh_user@$server" -i "$ssh_key_path" -i "$ssh_cert_path" <<EOF
echo "Firewall Status on $server:"
sudo systemctl status firewalld

echo "SELinux Status on $server:"
sestatus
EOF

# Add more checks or commands as needed
