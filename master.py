#!/bin/python

import os
import subprocess

def hello():
  print('Hi NTI300')
  print('This is Grants Python Install Script!')
  
hello()
  
def tree_install():
  print('Installing tree')
  os.system('yum -y install tree')
  
tree_install()

def apache_install():
  print('Installing Apache Web Server')
  os.system('yum -y install httpd')
  
  print('Starting http service')
  os.system('systemctl enable httpd.service')
  
  print('Starting apache server')
  os.system('systemctl start httpd.service')
  
  print('IMPORTANT! Create an inbound security rule to open port 80 on the server')
  
apache_install()

def clone_repo():
  print('installing git')
  os.system('yum -y install git')
  
  print('cloning Grants github repo')
  os.system('git clone https://github.com/grantypantyyy/NTI-300-GG.git')

clone_repo()

def publish_site():
  print('Publishing Website')
  os.system('sudo cp NTI-300-GG/webgrant.html /var/www/html')
  print('adjusting permisions')
  os.system('sudo chmod 644 /var/www/html/webgrant.html')
  os.system('sudo setenforce 0')
  os.system('sudo service httpd restart')
  
publish_site()

def django_install():
    print('Installing Django Web Framework.')
    os.chdir('NTI-300-GG')
    os.system('chmod +x django_install manage.py')
    subprocess.call(['./django_install'])
    os.system('python /opt/django/project1/manage.py runserver 0.0.0.0:8000&')
    
django_install()

def mailx():
    print('Installing mailx')
    os.system('yum -y install mailx')

mailx()

def crontab():
    print('Creating crontab entry for Server Alert emails every 30 minutes.')
    os.system('sudo chmod +x /home/ec2-user/NTI-300-GG/cron2.sh')
    os.system('(crontab -l 2>/dev/null; echo "0,30 * * * * /home/ec2-user/NTI-300-GG/cron2.sh | mail -s \"Server Alert\" grantgrismore@outlook.com") | crontab - ')
    os.system('crontab -l')

crontab()

def update_kernel():
  print('Updating kernal')
  os.system('yum clean all && yum update kernel -y')
  print('Done!')
  print('Verifying dirty cow patch')
  os.system('rpm -q --changelog kernel | grep CVE-2016-5195')
  
update_kernel()

def awscli():
    print('Installing the AWS CLI')
    os.system('pip install -y awscli')

awscli()

def boto3():
    print('Installing Boto3')
    os.system('pip install -y boto3')
    print('Install Script Complete! AWS RHEL Server ready to use.')
  
boto3()
  





















