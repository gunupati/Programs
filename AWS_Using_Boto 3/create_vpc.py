import boto3
ec2 = boto3.resource('ec2')

#create vpc
vpc=ec2.create_vpc(CidrBlock='172.16.0.0/16')
	

#assign a name to our vpc
vpc.create_tags(Tags=[{'Key':"Name",'Value':'my_vpc'}])
vpc.wait_until_available()

# enable public dns hostname so that we can SSH into it later
ec2Client = boto3.client('ec2')
ec2Client.modify_vpc_attribute( VpcId = vpc.id , EnableDnsSupport = { 'Value': True } )
ec2Client.modify_vpc_attribute( VpcId = vpc.id , EnableDnsHostnames = { 'Value': True } )

# create an internet gateway and attach it to VPC
internetgateway = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=internetgateway.id)

# create a route table and a public route
routetable = vpc.create_route_table()
route = routetable.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internetgateway.id)

# create subnet and associate it with route table
private_subnet = ec2.create_subnet(CidrBlock='172.16.1.0/24', VpcId=vpc.id)
private_subnet.create_tags(Tags=[{'Key':"Name",'Value':'private_subnet1'}])
routetable.associate_with_subnet(SubnetId=private_subnet.id)


public_subnet = ec2.create_subnet(CidrBlock='172.16.2.0/24', VpcId=vpc.id)
public_subnet.create_tags(Tags=[{'Key':"Name",'Value':'public_subnet1'}])
routetable.associate_with_subnet(SubnetId=public_subnet.id)


# Create a security group and allow SSH inbound rule through the VPC
securitygroup = ec2.create_security_group(GroupName='SSH-ONLY', Description='only allow SSH traffic', VpcId=vpc.id)
securitygroup.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)


if __name__=='__main__':
    main()

