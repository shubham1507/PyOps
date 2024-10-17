import boto3
import time

# Create an EC2 client using Boto3
ec2_client = boto3.client('ec2', region_name='ap-south-1')

# Replace with your EC2 instance ID
INSTANCE_ID = 'i-****'

def check_ec2_health():
    # Describe the instance's status
    response = ec2_client.describe_instance_status(InstanceIds=[INSTANCE_ID])

    if response['InstanceStatuses']:
        instance_status = response['InstanceStatuses'][0]
        
        instance_state = instance_status['InstanceState']['Name']
        system_status = instance_status['SystemStatus']['Status']
        instance_status_check = instance_status['InstanceStatus']['Status']

        print(f"EC2 Instance State: {instance_state}")
        print(f"System Status: {system_status}")
        print(f"Instance Status: {instance_status_check}")

        if system_status == 'impaired' or instance_status_check == 'impaired':
            print(f"Instance {INSTANCE_ID} is having issues!")
        else:
            print(f"Instance {INSTANCE_ID} is healthy.")
    else:
        print(f"No status available for instance {INSTANCE_ID}. Instance might be stopped.")

# Automate EC2 health check every 30 seconds
while True:
    check_ec2_health()
    time.sleep(30)

'''
(pyops) C:\Users\admin\Desktop\automate_cloud_res>python instance_health_boto.py
EC2 Instance State: running
System Status: ok
Instance Status: ok
Instance i-********** is healthy.

'''
