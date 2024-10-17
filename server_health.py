import os
import time

# Replace 'ec2-public-ip' with your EC2 instance's public IP address or DNS name
# MAKE SURE ICMP package allowed in inbound rule
EC2_PUBLIC_IP = 'ec2-public-ip'

def check_ec2_status():
    # Ping the EC2 instance, change the '-c' flag to '-n' for Windows
    response = os.system(f"ping -n 1 {EC2_PUBLIC_IP} >nul 2>&1")
    
    if response == 0:
        print(f"EC2 instance {EC2_PUBLIC_IP} is UP")
    else:
        print(f"EC2 instance {EC2_PUBLIC_IP} is DOWN")

# Check EC2 health every 10 seconds
while True:
    check_ec2_status()
    time.sleep(10)
