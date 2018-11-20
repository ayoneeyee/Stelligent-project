# Stelligent-project
Simple rest-api

# Deploy a Python Flask App to AWS Elastic Beanstalk
Flask is a micro framework for Python. This document guides you through the process of creating and deploying a Flask app to AWS Elastic Beanstalk (EB).

Instruction provided in this document are for Unix, they have not been tested on any Window OS.


## Prerequisites
In order to follow this guide, you would need a command line terminal (e.g. bash). Commands are shown in this guide with prompt symbol ($) and name of the current directory, when appropriate.

```bash
~/repos$ command
output
```

### Install Elastic Beanstalk CLI
If you have not installed Elastic Beanstalk CLI then follow the instructions in this section.
1. Run the command to install EB CLI
```bash
~/repos$ pip install awsebcli --upgrade --user
```

some of the command line output have been removed for redabilty, last few lines will look as follow:
```bash
  Running setup.py install for awsebcli ... done
Successfully installed PyYAML-3.13 awsebcli-3.14.6 blessed-1.15.0 botocore-1.12.43 cached-property-1.5.1 cement-2.8.2 certifi-2018.10.15 chardet-3.0.4 colorama-0.3.9 docker-3.5.1 docker-compose-1.21.2 docker-pycreds-0.3.0 dockerpty-0.4.1 docopt-0.6.2 docutils-0.14 idna-2.6 jmespath-0.9.3 jsonschema-2.6.0 pathspec-0.5.5 python-dateutil-2.7.5 requests-2.18.4 semantic-version-2.5.0 six-1.11.0 termcolor-1.1.0 texttable-0.9.1 urllib3-1.22 wcwidth-0.1.7 websocket-client-0.54.0
You are using pip version 10.0.1, however version 18.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```

2. Verify that the EB CLI installed correctly by running
```bash
~/repos$ eb --version
EB CLI 3.14.6 (Python 3.7.0)
```

## Set Up a Python Virtual Environment
Check the python version you have
```bash
~/repos$ python3 -v
Python 3.7.1
```
Navigate to project root directory:
```bash
~/repos$ cd simple-rest-api 
~/repos/simple-rest-api $
```

To create a virtualenv named venv, run the command
```bash
~/repos/simple-rest-api $ python3 -m venv venv
```

Verify venv (a folder named 'venv') is created in the current directory.
```bash
~/repos/simple-rest-api $ ls -l venv
total 8
drwxr-xr-x  12 jana  staff  384 13 Nov 09:35 bin
drwxr-xr-x   2 jana  staff   64 13 Nov 09:35 include
drwxr-xr-x   3 jana  staff   96 13 Nov 09:35 lib
-rw-r--r--   1 jana  staff  114 13 Nov 09:35 pyvenv.cfg
```
venv should have the following: include/ lib/ pyvenv.cfg scripts/

To activate the venv, run the following command
```bash
~/repos/simple-rest-api $ source venv/bin/activate
(venv) ~/repos/simple-rest-api $
```
Note the (venv) in front of the directory name. This indicates that your currently using python in this virtualenv rather than that from system.

Verify python location:
```bash
(venv) ~/repos/simple-rest-api $ which python
/home/repos/simple-rest-api/simple-rest-api/venv/bin/python
```

This shows that a python virtual environment named venv has been created succefully.

## Version Control
Git with [gitflow](https://nvie.com/posts/a-successful-git-branching-model/) branching model is used as version control. For more info about installing git and git flow please refer to the following links:
- https://www.atlassian.com/git/tutorials/install-git
- https://github.com/nvie/gitflow/wiki/Linux 

## Version numbering
This project follows SemVer version numbering schema as described in https://semver.org/. 


## Setup new EB application
Please note that during the following steps, default values may differ on your system. You may choose any value except where indicated.

Setup a new EB application in the default VPC:
```bash
(venv) ~/repos/simple-rest-api $ eb init
```

You will be prompted to select a region you would like to deploy the application. Select region and enter the appropriate number.

```bash
(venv) ~/repos/simple-rest-api $ eb init
Select a default region
1) us-east-1 : US East (N. Virginia)
2) us-west-1 : US West (N. California)
3) us-west-2 : US West (Oregon)
4) eu-west-1 : EU (Ireland)
5) eu-central-1 : EU (Frankfurt)
6) ap-south-1 : Asia Pacific (Mumbai)
7) ap-southeast-1 : Asia Pacific (Singapore)
8) ap-southeast-2 : Asia Pacific (Sydney)
9) ap-northeast-1 : Asia Pacific (Tokyo)
10) ap-northeast-2 : Asia Pacific (Seoul)
11) sa-east-1 : South America (Sao Paulo)
12) cn-north-1 : China (Beijing)
13) cn-northwest-1 : China (Ningxia)
14) us-east-2 : US East (Ohio)
15) ca-central-1 : Canada (Central)
16) eu-west-2 : EU (London)
17) eu-west-3 : EU (Paris)
(default is 3):
```

Next you will be proompted for application name. I usually leave the default application 
name (current directory name), however you can change this as appropriate. 
```bash
(venv) ~/repos/simple-rest-api $ 
Enter Application Name
(default is "mini-rest-api"):
```

Next confirm that your using python by pressing enter:

```bash
(venv) ~/repos/simple-rest-api $ 
It appears you are using Python. Is this correct?
(Y/n):
```

Next you will be prompted for platform version. You MUST select Python 3.6.
```bash
(venv) ~/repos/simple-rest-api $ 
Select a platform version.
1) Python 3.6
2) Python 3.4
3) Python 3.4 (Preconfigured - Docker)
4) Python 2.7
5) Python
(default is 1):
```

Next decline code commit by selecting default value (No)

```bash
(venv) ~/repos/simple-rest-api $ 
Note: Elastic Beanstalk now supports AWS CodeCommit; a fully-managed source control service. To learn more, see Docs: https://aws.amazon.com/codecommit/
Do you wish to continue with CodeCommit? (y/N) (default is n):
```

Next it will ask you to setup ssh, select yes if you want to ssh into the instances, else select no.

```bash
(venv) ~/repos/simple-rest-api $ 
Do you want to set up SSH for your instances?
(Y/n):
```

If you select yes, then you need to enter a keypair name, enter a name e.g. 'simple-api' and press enter
```bash
(venv) ~/repos/simple-rest-api $ 
Type a keypair name.
(Default is aws-eb): simple-api
```

Next you may enter a password, or leave it empty.
```bash
(venv) ~/repos/simple-rest-api $ 
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

At this point, you should have private and public keys to access the instances created in ~/.ssh/ directory. 

## Deploy your application 
Your project directory should now look like this:
```
├── Pipfile
├── Pipfile.lock
├── api
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── core
│   │   ├── __init__.py
│   │   └── errors.py
│   └── simple
│       ├── __init__.py
│       ├── logic.py
│       └── resources.py
├── application.py
├── readme.md
├── requirements.txt
└── .ebignore
└── .gitignore
└── setup.py
└── venv
```
Create a setup of AWS resources required to run your application 
```bash
(venv) ~/repos/simple-rest-api $ eb create
```

When prompted to "Enter Environment Name", press Enter to use the default name.
```bash
(venv) ~/repos/simple-rest-api $ 
Enter Environment Name
(default is mini-rest-api-dev):
```

Then  give a DNS name for EB applications, that have to be unique, so you will need to come up with one for your sample application.
```bash
(venv) ~/repos/simple-rest-api $ 
Enter DNS CNAME prefix
(default is mini-rest-api-dev):
```

Then select a load balancer type, I will leave it as default (classic)
```bash
(venv) ~/repos/simple-rest-api $ 
Select a load balancer type
1) classic
2) application
3) network
(default is 1):
Creating application version archive "app-8263-181113_101128".
Uploading simple-rest-api/app-8263-181113_101128.zip to S3. This may take a while.
Upload Complete.
Environment details for: simple-rest-api-dev
  Application name: simple-rest-api
  Region: us-west-2
  Deployed Version: app-8263-181113_101128
  Environment ID: e-94dkmxzwb7
  Platform: arn:aws:elasticbeanstalk:us-west-2::platform/Python 3.6 running on 64bit Amazon Linux/2.7.5
  Tier: WebServer-Standard-1.0
  CNAME: simple-rest-api-dev.us-west-2.elasticbeanstalk.com
  Updated: 2018-11-13 10:11:35.987000+00:00
Printing Status:
2018-11-13 10:11:34    INFO    createEnvironment is starting.
2018-11-13 10:11:36    INFO    Using elasticbeanstalk-us-west-2-415424352074 as Amazon S3 storage bucket for environment data.
2018-11-13 10:11:57    INFO    Created security group named: sg-030f3a04a200639f1
2018-11-13 10:12:12    INFO    Created load balancer named: awseb-e-9-AWSEBLoa-79VR8T06AZI3
2018-11-13 10:12:12    INFO    Created security group named: awseb-e-94dkmxzwb7-stack-AWSEBSecurityGroup-1ZUFBBO41S2H
2018-11-13 10:12:12    INFO    Created Auto Scaling launch configuration named: awseb-e-94dkmxzwb7-stack-AWSEBAutoScalingLaunchConfiguration-K84SN3L4098Q
2018-11-13 10:13:17    INFO    Created Auto Scaling group named: awseb-e-94dkmxzwb7-stack-AWSEBAutoScalingGroup-1QUVXZ4YB8MM8
2018-11-13 10:13:17    INFO    Waiting for EC2 instances to launch. This may take a few minutes.
2018-11-13 10:13:17    INFO    Created Auto Scaling group policy named: arn:aws:autoscaling:us-west-2:415424352074:scalingPolicy:3b31197a-3059-4a25-b4d0-30773547a9c7:autoScalingGroupName/awseb-e-94dkmxzwb7-stack-AWSEBAutoScalingGroup-1QUVXZ4YB8MM8:policyName/awseb-e-94dkmxzwb7-stack-AWSEBAutoScalingScaleUpPolicy-KDLVEOKX1Y1O
2018-11-13 10:13:17    INFO    Created Auto Scaling group policy named: arn:aws:autoscaling:us-west-2:415424352074:scalingPolicy:748a7a62-cd1f-4d67-beee-8f7fb6ea9d8d:autoScalingGroupName/awseb-e-94dkmxzwb7-stack-AWSEBAutoScalingGroup-1QUVXZ4YB8MM8:policyName/awseb-e-94dkmxzwb7-stack-AWSEBAutoScalingScaleDownPolicy-3JGW3QGM8EHK
2018-11-13 10:13:17    INFO    Created CloudWatch alarm named: awseb-e-94dkmxzwb7-stack-AWSEBCloudwatchAlarmHigh-RYKCV9OEIA9
2018-11-13 10:13:32    INFO    Created CloudWatch alarm named: awseb-e-94dkmxzwb7-stack-AWSEBCloudwatchAlarmLow-B87DP58US0DR
2018-11-13 10:15:11    INFO    Application available at simple-rest-api-dev.us-west-2.elasticbeanstalk.com.
2018-11-13 10:15:11    INFO    Successfully launched environment: simple-rest-api-dev
```

It will take sometime to complete this step.

## Set environment variables
You need to set secret key as an environment variable

```bash
(venv) ~/repos/simple-rest-api $ eb setenv SECRET_KEY=rpDehYpNj9?Pk?c#t+z8=TH=482c*TAc
```

## Tests
Open the url
```bash
(venv) ~/repos/simple-rest-api $ eb open
```
Note this will open base url e.g. http://simple-rest-api-dev.us-west-2.elasticbeanstalk.com since there is nothing at this endpoint/url it will return a page not found error. Base URL will be diffrent for you.

You can test the app by accessing the following URL:
BASE_URL/simple
e.g.
http://simple-rest-api-dev.us-west-2.elasticbeanstalk.com/simple
