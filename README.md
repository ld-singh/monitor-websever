# monitor-websever
## Introduction

The monitor_webserver.py monitors demo Webserver created by https://github.com/ld-singh/terraform-aws-webserver.git

This script fetches IP of the webserver using boto3 python library and then uses http://IP/status to check status of the webserver. 

AWS credentials are required to be set for local environment where the script is run as boto3 function needs to fetch information from AWS account.

 
## Usage

You can test this in two ways:
### 1. Using make
     You can run below command to run this. This will also install dependencies
     
     make monitor
### 2. Running python file directory

     First Install dependencies as follows:
     
     make install-requirements
     or
     pip3 install boto3
     
     
     Now run the script
     
     python3 monitor_webserver.py
   
