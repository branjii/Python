#!/usr/bin/env python3

#Author: Brandon Vajda
#Date: April 11, 2021


import sys
import os

currentuser = os.popen('whoami')
user = currentuser.read().strip()

if user != 'root':
    print('You must be root')
    print('You are logged in as: ' + user + '\n')
    exit()

print('This script is used to configure the specifed interface file to be DHCP\n')
try:
    path = input('Please enter the full path to the interface file: ')
    f = open(path, 'w')
    interface = input('Name of the interface: ')
    f.write('DEVICE=' + interface + '\n')
    f.write('BOOTPROTO=dhcp\n')
    f.write('IPV6INIT=yes\n')
    f.write('ONBOOT=yes\n')
except IOError:
    print('The file you are trying to access does not exist')
except:
    print('A error has occured. Please try again')
finally:
    f.close()
    exit()
