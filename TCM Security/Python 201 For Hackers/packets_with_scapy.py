#!/usr/bin/env python3

from scapy.all import *

ip_layer = IP(dst="247ctf.com")
icmp_layer = ICMP()

# The packet is sent at the IP- and ICMP-layer, the '/' is a combining
# element in this case.
packet = ip_layer / icmp_layer

r = send(packet)

# Prints out all kinds of detail about the sent packet
print(packet.show())
# Show the package in Wireshark, depends on Wireshark being installed on the
# system and within $PATH
wireshark(packet)

# srp will return both hosts that have and have not responded to this
# ARP-scan.
ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.10.0/24"), timeout=3, verbose=False)
for i in ans:
    print(i[1].psrc)
        
# Define common TCP-flags
SYN = 0x02
RST = 0x04
ACK = 0x10

for port in [22, 80, 139, 443, 445, 8080]:
    # Sends a SYN to the destination, from a random port, only return the
    # first response package it gets.
    tcp_connect == sr1(IP(dst="127.0.0.1") / TCP(sport=Randshort(), dport=port, flags="S"), timeout=1, verbose=False)    
    # If there is a response and a TCP-layer
    if tcp_connect and tcp_connect.haslayer(TCP):    
        # .. get the TCP-flags
        response_flags = tcp_connect.getlayer(TCP).flags
        if response_flags == (SYN + ACK):
            snd_rst = send(IP(dst="127.0.0.1") / TCP(sport=RandShort(), dport=port, flags="AR"), verbose=False)            
        elif response_flags == (RST + ACK):
            print(f"{port} is closed")
        else:
            print(f"{port} is closed")

# Import HTTP-functionality for sniffing HTTP-requests
from scapy.layers.http import HTTPRequest

def process(packet):
    if packet.haslayer(HTTPRequest):
        print(packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode())
    
sniff(filter="port 80", prn=process, store=False)

# Scapy is also capable of dealing with packet captures
scapy_cap = rdpcap("error_reporting.pcap")
for packet in scapy_cap:
    if packet.getlayer(ICMP):
        print(packet.load)