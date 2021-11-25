#!/usr/bin/env python3

# author: Brandon Vajda
#date: March 30, 2021

#


import sys
import os

currentuser = os.popen('whoami')
user = currentuser.read().strip()

if user != 'root':
    print('You must be root')
    print('You are logged in as: ' + user + "\n")
    exit()

print('This script is used to configure network interface config files.\n----------------------------------------------------------------')

try:
    flag = True
    while flag == True:
        interface = input('Name of interface: ')
        if len(interface) == 0:
            print('Inavlid. Please enter an interface name.')
            flag = True
        else:
            flag = False
    f = open('/etc/sysconfig/network-scripts/ifcfg-' + interface, 'w')

    f.write('DEVICE=' + interface + '\n')
    mac = input('MAC address: ')
    f.write('HWADDR=' + mac + '\n')
    boot = input('Boot interface automatically? (y|n): ')
    if boot == "y":
        boot='yes'
        f.write('ONBOOT=' + boot +'\n')
    elif boot == "n":
        boot='no'
        f.write('ONBOOT=' + boot + '\n')
    else:
        print('Invalid Selection. Please enter "y" or "n".')
        exit()
    choice = input('Enter the number for your choice\n1.)Allow DHCP to configure IP addressing\n2.)Manually configure IP addressing (Static)\n> ')
    if choice == "2":
        choice = 'static'
        f.write('BOOTPROTO=' + choice + '\n')
        ipaddr = input('Enter IP address: ')
        f.write('IPADDR=' + ipaddr + '\n')
        prefix = input('Enter network prefix (/__): ')
        f.write('PREFIX=' + prefix + '\n')
        gateway = input('Enter the default gateway address: ')
        f.write('GATEWAY=' + gateway + '\n')
        dns = input('Enter the primary DNS: ')
        f.write('DNS1=' + dns + '\n')
        f.write('IPV6INIT=no' + '\n')
        f.close()
    elif choice == "1":
        choice = "dhcp"
        f.write('BOOTPROTO=' + choice + '\n')
        f.write('IPV6INIT=yes' + '\n')
        f.close()
    else:
        print('Invalid Selection. Please enter the number 1 or 2.')
        

   
except FileNotFoundError:
    print('The interface configuration file does not exist')
    exit()
except:
    print('A error has occured. Please try again.')
    exit()
finally:
    f.close()
    exit()
