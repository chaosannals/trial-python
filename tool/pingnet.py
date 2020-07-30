from ipaddress import ip_address, ip_network
from icmplib import ping

for ip in ip_network('192.168.0.0/24'):
    r = ping(str(ip), interval=0.2)
    print('{} => {}'.format(ip, r.is_alive))