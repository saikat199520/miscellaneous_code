import boto3

region = 'sa-east-1' 
instances = ['i-0de1f263f859317b8'] 


ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):

    response = ec2.describe_instances(InstanceIds=instances)

    for reservation in response['Reservations']:
        
        for instance in reservation['Instances']:

            state = instance['State']['Name']
            instance_id = instance['InstanceId']
            
            if state == 'running':

                print(f"Instance {instance_id} is running. Stopping now...")
                ec2.stop_instances(InstanceIds=[instance_id])
                
            else:
                
                print(f"Instance {instance_id} is in '{state}' state. Skipping stop.")
