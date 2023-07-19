import socket
import psutil

def get_ip_address():
    # obtem o ipv4 do computador
    ip_local = socket.gethostbyname(socket.gethostname())
    return ip_local

def get_mac_address():
    # Obtém o endereço MAC do adaptador de rede principal
    mac_address = ''
    for iface in psutil.net_if_addrs().values():
        for addr in iface:
            if addr.family == psutil.AF_LINK:
                mac_address = addr.address
                break
        if mac_address:
            break
    return mac_address

def get_hostname():
    # Obtém o nome do host do computador
    return socket.gethostname()
