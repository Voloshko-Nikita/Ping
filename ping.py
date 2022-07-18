from ipaddress import *
import subprocess
import tabulate
def host_ping(ip_list):
    for ip in ip_list:
        with subprocess.Popen(["ping", ip.compressed, '-n', '2'], shell=True, stdout=subprocess.PIPE) as prosess:
            prosess.wait()
            out, _ = prosess.communicate()
            out = out.decode('cp866')
        resp = True if 'мс' in out else False
        if resp:
            print(f'Узел доступен: {ip}')
        else:
            print(f'Узел недоступен: {ip}')
def host_range_ping(start, end):
    if end < start:
        print('Первый должен быть больше!')
    else:
        ips = []
        for i in summarize_address_range(start, end):
            i = ip_address(i)
            ips.append(i)
        host_ping(ips)



def host_range_ping_tab(start, end):
    reacheble = []
    unreacheble = []
    if end < start:
        print('Первый должен быть больше!')
    else:
        ips = []
        for ip in summarize_address_range(start, end):
            with subprocess.Popen(["ping", ip.compressed, '-n', '2'], shell=True, stdout=subprocess.PIPE) as prosess:
                prosess.wait()
                out, _ = prosess.communicate()
                out = out.decode('cp866')
            resp = True if 'мс' in out else False
            if resp:
                reacheble.append(ip)
            else:
                unreacheble.append(ip)

        print(tabulate.tabulate({'Reacheble': reacheble, 'Unreacheble': unreacheble}, headers='keys'))



all_ip = [ip_address('127.0.0.1'), ip_address('8.8.8.8'), ip_address('127.0.0.2'), ip_address('192.168.1.3'), ip_address('192.168.1.4'), ip_address('192.168.1.5'), ip_address('192.168.1.6')]

host_range_ping_tab(ip_address('127.0.0.1'), ip_address('127.0.0.28'))
#host_ping(all_ip)










