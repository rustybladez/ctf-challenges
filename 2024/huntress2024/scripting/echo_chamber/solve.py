#!/usr/bin/env python3

from scapy.all import *

src_ip = '127.0.0.1'
packet = rdpcap('echo_chamber.pcap')
data = b''

for pkt in packet[1:]:
    if pkt[IP].src == src_ip and pkt[ICMP].type == 8:
        data += pkt[Raw].load[16:32]

with open('output', 'wb') as w:
    w.write(data)
