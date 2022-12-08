import boto3
import urllib.request


# Declare the ec2 client
ec2 = boto3.client("ec2", region_name = "ap-southeast-2")

# EC2 describe based on Tag to fetch public IP
res = ec2.describe_instances(
              Filters=[
                {
                'Name': 'tag:Name',
                'Values': [
                        'Webserver',
                 ]
                }])
public_ip = res["Reservations"][0]["Instances"][0]["PublicIpAddress"]
#print(public_ip)
url='http://'+public_ip+'/status'

#Reading body of response
status = urllib.request.urlopen(url).read().decode("utf-8")
#print(status)
if status == 'Okay':
    print('Hello World Webserver is up and running!')
else:
    print('Something Wrong! Seems Webserver is down!')
