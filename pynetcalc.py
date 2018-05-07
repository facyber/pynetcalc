#!/usr/bin/python3

"""Simple terminal IP Subnet Calculator that works for both IPv4 and IPv6 protocols."""

import ipaddress, argparse


#  Function for finding the class of the network address


def addressClass(c):
    """Split the address and store the elements in variable x as a list.

    Compare the first element of the list to the IP address ranges and return a class and it's mask.
    """

    x = c.split('.')
    global mask
    if int(x[0]) in range (8,128):
        mask = 8
        return "A"
    elif int(x[0]) in range(128, 192):
        mask = 16
        return "B"
    elif int(x[0]) in range(192, 224):
        mask = 24
        return "C"
    elif int(x[0]) in range(224, 240):
        return "D"
    else:
        return "E"


# Function for finding the type of the IP address.


def addressType(t):
    if str(t).startswith('169.254'):
        return "APIPA (Automatic Private IP Addressing)"
    elif t.is_loopback:
        return "Loopback"
    elif t.is_link_local:
        return "Link-local"
    elif t.is_private:
        return "Private"
    elif t.is_multicast:
        return "Multicast"
    elif t.is_reserved:
        return "Reserved"
    elif t.is_unspecified:
        return "Unspecified"
    else:
        return "Public"


# Creating the parser and network objects


parser = argparse.ArgumentParser(description="Simple terminal IP Subnet Calculator that works for both IPv4 and IPv6 protocols.")
parser.add_argument("ip_address", help="valid network address/mask")

args = parser.parse_args()
address = args.ip_address

networkAddress = ipaddress.ip_network(address, strict=False)


# Main program


if __name__ == '__main__':
    print("Network Address:", networkAddress)

    if networkAddress.version == 4:
        print("Subnet Mask:", networkAddress.netmask)
        print("Wildcard Mask:", networkAddress.hostmask)
        print("Number of Usable Hosts:", networkAddress.num_addresses - 2)
        print("Usable Host Address Range:", networkAddress[1], "-", networkAddress[-2])
        print("Broadcast Address:", networkAddress.broadcast_address)
        print("Network Class:", addressClass(address))
        print("Address Type:", addressType(networkAddress))
    else:
        interface = ipaddress.IPv6Interface(address)
        ipv6 = interface.ip
        print("Compressed Address:", ipv6.compressed)
        print("Full IPv6 Address:", ipv6.exploded)
        print("Usable Host Address Range:", networkAddress[1], "-", networkAddress[-2])
        print("Address Type:", addressType(networkAddress))