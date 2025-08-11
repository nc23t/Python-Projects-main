import socket
import ipaddress
from utils import scan_tcp, scan_udp, user_tcp
socket.setdefaulttimeout(1)


while True:
    try:
        answer = input('Would you like to scan for TCP or UDP?:')
    except:
        print('Invalid Input')

    if (answer.lower() == 'tcp'):
        range_user = input('1 for range of IPs, 2 for however much you want:')
        if (range_user == '1'):
            while True:
                try:
                    IPs = input("Enter your starting IP:")
                    ipaddress.IPv4Address(IPs)
                    break
                except ipaddress.AddressValueError:
                    print('Not a valid IPv4 Address')

            while True:
                try:
                    IPe = input("Enter your ending IP address:")
                    ipaddress.IPv4Address(IPe)
                    break
                except ipaddress.AddressValueError:
                    print('Not a valid IPv4 Address')

            while True:
                try:
                    start = int(
                        input('Enter your starting number for your range of ports:'))
                    break
                except ValueError:
                    print("Not a valid port value")
            while True:
                try:
                    end = int(
                        input('Enter your ending number for your range of ports:'))
                    break
                except ValueError:
                    print('Not a valid port value')

            starting_ip = ipaddress.IPv4Address(IPs)
            ending_ip = ipaddress.IPv4Address(IPe)
            scan_tcp(starting_ip, ending_ip, start, end)

        elif (range_user == '2'):
            while True:
                try:
                    user_ips = input(
                        'Seperate each IPv4 Address with a comma, when finished press enter:').split(",")
                    for ips in user_ips:
                        iterateIp = str(ipaddress.IPv4Address(ips))
                    ipaddress.IPv4Address(iterateIp)
                    break
                except ipaddress.AddressValueError:
                    print('Not a valid IPv4 Address')
            while True:
                try:
                    user_ports = input(
                        'Seperate each Port with a comma, when finished press enter:').split(",")
                    for ports in user_ports:
                        checkPorts = int(ports)
                    break
                except ValueError:
                    print('Not a valid port value')
            user_tcp(user_ips, user_ports)

    elif (answer.lower() == 'udp'):
        my_string = str('My Test eh')
        while True:
            try:
                new_ip = str(input('Enter your IP:'))
                ipaddress.IPv4Address(new_ip)
                break
            except ipaddress.AddressValueError:
                print("Not a valid IPv4 Address")

        while True:
            try:
                new_port = int(input('Enter your port number:'))
                break
            except ValueError:
                print("Not a valid port value")
        scan_udp(my_string, new_ip, new_port)
    else:
        print('Invalid input')
