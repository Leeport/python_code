import sys
import socket
import re
import threading


def prement_host(host):
    host = str.lower(host)
    if "www" not in host:
        if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",host):
            ip = host
        else:
            print("ERROR!!!")
    else:
        try:
            ip = socket.getaddrinfo(host, None)[0][4][0]
        except:
            print("ERROR!!!")
    return ip
def scan_port(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:

        result=s.connect_ex((ip,port))
        if result ==0:
            print('%s open'%(port))
        #else:
        #    print('%s close'%(port))
    except socket.timeout:
        print('%s close'%(port))
    except:
        print('error')
    s.close()




    return ip
if __name__ == "__main__":
    mutex = threading.Lock()
    host = input("input host: ")
    lastport = input("input last port:")
    ip = prement_host(host)
    print(ip)
    for i in range(1,int(lastport)):
        t = threading.Thread(target=scan_port,args=(ip,i))
        t.start()
