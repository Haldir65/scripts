import ipaddress

ip_array = []
for ip in ipaddress.IPv4Network('192.168.1.0/24'):
    print(ip)
    ip_array.append(ip)

with open('listfile.txt', 'w') as filehandle:
    for listitem in ip_array:
        filehandle.write('%s\n' % listitem)