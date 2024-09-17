import pyfiglet
import sys
import socket
from datetime import datetime

ports = [20, 21, 22, 23, 25, 53, 69, 80, 137, 138, 139, 443, 520, 587]

def scan_port(ip, ports):
    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = s.connect_ex((ip, port))
            if result == 0:
                print(f'[ * ] Port {port} is open')
            else:
                print(f'[ * ] Port {port} is closed')
            s.close()
    except KeyboardInterrupt:
        print("Exiting. . . ")
        sys.exit()
    except socket.error:
        print('Host not responding.')
        sys.exit()
    

def main():
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER.PY")
    print(ascii_banner)

    target = input(str('Target IP: '))

    print('_'*50)

    start = datetime.now()

    print(f'Scanning started: {start}')
    print('Scanning target. . .')
    print('_'*50)

    scan_port(target, ports)

    finish = datetime.now()
    print('_'*50)
    print(f'Time elapsed: {finish-start}')

if __name__ == "__main__":
    main()