from ipaddress import ip_address, ip_network
from icmplib import multiping
from time import time

ips = [str(ip) for ip in ip_network('192.168.0.0/24')]

start = time()
result = multiping(ips)
end = time()

for r in result:
   print('{} => {}'.format(r.address, r.is_alive))
print('{}s'.format(end - start))