import argparse
import ipaddress
import nmap
from datetime import datetime

parse = argparse.ArgumentParser()
parse.add_argument('--host', help="enter the ip/network")
args = parse.parse_args()
nm = nmap.PortScanner()
now = datetime.now()
file_name = now.strftime("%Y%m%d%H%M")+".txt"

def scanHost(host,file):
    result = nm.scan(host,arguments='-sUT -O --top-ports 200')
    print("\t"+nm[host].hostname())
    file.write("\t"+nm[host].hostname()+"\n")
    for proto in ['tcp','udp']:
        for port in result['scan'][host][proto].keys():
            if result['scan'][host][proto][port]['state'] == "open":
                if (port!=2000) and (port!=5060):
                    print("\t{}/{}".format(port,proto))
                    file.write("\t{}/{}\n".format(port,proto))

def main():
    if args.host:
        hosts = args.host.split(",")
        for host in hosts:
            try:
                for i in ipaddress.IPv4Network(host):
                    print("{}".format(i),end='')
                    with open(file_name,'a') as file:
                        file.write(str(i))
                        try:
                            scanHost(str(i),file)
                        except:
                            continue
                    file.close()
            except:
                print("Invalid IP/Network.")
    else:
        print("Usage: python script.py --host 8.8.8.8,1.1.1.0/29")

if __name__ == "__main__":
    main()
