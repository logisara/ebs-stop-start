import boto3
import botocore
def lambda_handler(event, context):
    envid=['e-jwphshqhdr','e-rzp7zzkmp2']
    client = boto3.client('elasticbeanstalk')
    try:
         for appid in range(len(envid)):
             response = client.terminate_environment(EnvironmentId=str(envid[appid].strip()))
             if response:
                 print('Terminating environment %s' %str(envid[appid]))
             else:
                 print('Failed to Terminate environment %s' %str(envid[appid]))
             
    except Exception as e:
        print(e)
