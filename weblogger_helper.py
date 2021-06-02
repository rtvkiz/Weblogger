#!/usr/bin/python3
import sys
import argparse

"""
fetch_logs function iterates through the log file and map the ip
"""


def fetch_logs(filepath, ip_range):
    result = []
    prefix = False
    try:
        if len(ip_range.split('/')) > 1:
            prefix = True
        with open(filepath) as log_file:
            print("Fetching details from the logs..")
            for line in log_file:
                line = line.rstrip()
                ip_val = line.split()[0]
                if prefix:
                    if prefix_check(ip_val, ip_range):
                        result.append(line)
                else:
                    if ip_val == ip_range:
                        result.append(line)
        log_file.close()
        if len(result) == 0:
            print("No record for given address found")
        else:
            count = len(result)
            for i in result:
                print(i)
            print('\n')
            print(" Total " + str(count) + " records found")

    except Exception as e:
        print(e)


"""
verify_ip function verifies the 
input ip from the user
"""


def verify_ip(ip):
    try:
        if len(ip.split('/')) > 1:
            prefix = int(ip.split('/')[1])
            if prefix not in range(1, 33):
                return False
        a, b, c, d = ip.split('/')[0].split('.')
        a, b, c, d = int(a), int(b), int(c), int(d)
        if a and b and c and d not in range(0, 256):
            return False
        return True
    except Exception as e:
        print(e)
        return False


"""
convert_ip_binary function takes ip address 
as an input and convert it to binary
"""


def convert_ip_binary(ip):
    octet_list_int = ip.split(".")
    octet_list_binary = [format(int(i), '08b') for i in octet_list_int]
    binary = ("").join(octet_list_binary)
    return binary


"""
prefix_check function verifies if 
given ip address falls in the ip range
"""


def prefix_check(ip_address, ip):
    [prefix_address, netaddr_size] = ip.split("/")
    netaddr_size = int(netaddr_size)
    prefix_network = get_network_ad(prefix_address, netaddr_size)
    ip_network = get_network_ad(ip_address, netaddr_size)
    return ip_network == prefix_network


"""
get_netword_ad function fetches the network bit
"""


def get_network_ad(address, net_size):
    ip_bin = convert_ip_binary(address)
    network = ip_bin[0:32 - (32 - net_size)]
    return network


"""
The driver function
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', help='Enter ipv4 address')
    parser.add_argument('--path', help='Specify file path if not in the same directory', required=False)
    args = parser.parse_args()
    if args.ip:
        check = verify_ip(args.ip)
    else:
        print("Please enter IP address")
        sys.exit()
    if check:
        print("IP address verified")
        if args.path:
            fetch_logs(args.path, args.ip)
        else:
            fetch_logs('public_access.log.txt', args.ip)
    else:
        print("Please enter valid ip address")
        sys.exit()


if __name__ == '__main__':
    main()