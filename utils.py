import socket
import ipaddress
socket.setdefaulttimeout(1)


def scan_tcp(starting_ip, ending_ip, start, end):
    for ip in range(int(starting_ip), int(ending_ip) + 1):
        for port in range(int(start), int(end) + 1):
            ip_str = str(ipaddress.IPv4Address(ip))

            try:
                target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                target.connect((ip_str, port))
                print('IP:', ip_str, 'Port', port, 'open!')

            except:
                print('IP:', ip_str, 'Port', port, 'closed')

            finally:
                target.close()


def scan_udp(my_string, new_ip, new_port):
    target = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target.sendto(my_string.encode(), (new_ip, int(new_port)))
    try:
        target.recvfrom(1024)
        print("We got a response!")

    except:
        print('No response')

    finally:
        target.close()


def user_tcp(user_ips, user_ports):
    for input_ip in user_ips:
        userIp_toString = str(ipaddress.IPv4Address(input_ip))
        for input_port in user_ports:
            input_port = int(input_port)

            try:
                target = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                target.connect((userIp_toString, input_port))
                print('IP:', userIp_toString, 'Port:', input_port, 'Open')
            except:
                print('IP:', userIp_toString, 'Port:', input_port, 'Closed')
            finally:
                target.close()
