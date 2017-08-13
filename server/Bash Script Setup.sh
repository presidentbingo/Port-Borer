apt update
apt -y upgrade
echo | echo | echo | echo | echo | echo y | adduser forward --shell /bin/true --no-create-home --disabled-password -q
echo "If you would like to set a password, run \"passwd forward\""
echo pass | echo pass | passwd forward
grep -q "GatewayPorts" /etc/ssh/sshd_config && echo 'It looks like GatewayPorts was already defined in /etc/ssh/sshd_config. Please set this to yes if it isnt already.' || echo "GatewayPorts yes" >> /etc/ssh/sshd_config
echo "I am restarting the SSH service to apply my changes. Im sorry if this disconnected you."
service ssh restart