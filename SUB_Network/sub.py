# Sample routing table (destination IP, next hop, interface)
routing_table = {
    '192.168.1.0/24': ('192.168.1.1', 'eth0'),
    '10.0.0.0/8': ('10.0.0.1', 'eth1'),
    '0.0.0.0/0': ('192.168.1.254', 'eth2')  # Default route
}

def route_packet(packet):
    destination_ip = packet['destination_ip']
    print(f"Destination IP : {destination_ip}")
    for network, (next_hop, interface) in routing_table.items():
        if destination_ip in network:
            if interface == 'eth0':
                print("Packet forwarded internally to interface eth0.")
            elif interface == 'eth1':
                print("Packet forwarded internally to interface eth1.")
            elif interface == 'eth2':
                print("Packet forwarded externally to next hop:", next_hop)
            return
    
    print("Destination IP not found in routing table. Dropping packet.")

# Example packet
packet = {'destination_ip': '10.1.2.3'}

# Route the packet
print(route_packet(packet))
