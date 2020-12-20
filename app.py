from aws_cdk import core
import boto3
client = boto3.client('sts')
region=client.meta.region_name
account_id = client.get_caller_identity()["Account"]
my_env = {'region': region, 'account': account_id}

proj="nicks-cdkdemo-"
from stacks.ec2_stack import EC2Stack

app = core.App()

ec2_stack=EC2Stack(app, proj+"ec2",env=my_env)

app.synth()
