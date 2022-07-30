from spike import ScanIP
import socket

def resolver(ip):
    try:
        host = socket.gethostbyaddr(ip)
        print(f'{ip} ->> {host[0]}')
    except:
        pass
if __name__ == "__main__":
    s = ScanIP("ir")
    s.scan(resolver)