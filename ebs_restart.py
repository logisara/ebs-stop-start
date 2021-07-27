import boto3
import botocore
def lambda_handler(event, context):
    envid=['e-jwphshqhdr']
    client = boto3.client('elasticbeanstalk')
    try:
         for appid in range(len(envid)):
             response = client.rebuild_environment(EnvironmentId=str(envid[appid].strip()))
             if response:
                 print('Restore environment %s' %str(envid[appid]))
             else:
                 print('Failed to Restore environment %s' %str(envid[appid]))

    except Exception as e:
        print(e)
