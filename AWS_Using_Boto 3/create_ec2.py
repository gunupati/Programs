import boto3
from create_vpc import ec2, vpc, public_subnet,securitygroup
# from create_vpc import *
ec2 = boto3.resource('ec2')

# Create a linux instance in the subnet
instances = ec2.create_instances(
 ImageId='ami-0d2692b6acea72ee6',
 InstanceType='t2.micro',
 MaxCount=1,
 MinCount=1,
 NetworkInterfaces=[{
 'SubnetId': public_subnet.id,
 'DeviceIndex': 0,
 'AssociatePublicIpAddress': True,
 'Groups': [securitygroup.group_id]
 }],
 KeyName='ec2-keypair')

