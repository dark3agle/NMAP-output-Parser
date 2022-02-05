#Importing the required Libraries

from libnmap.parser import NmapParser 
import os
import sys

# Verify User input 

if len(sys.argv) < 2:
    print("Generates a .txt file containing the open pots summary and the .nmap information\r\n")
    print("USAGE:\t./parsenmap <nmap xml file>\r\n\n")
    sys.exit()

file = sys.argv[1] # Assigning the file input into a variable 

parsed = NmapParser.parse_fromfile(file)

# The Main loop for parsing over teh File

for host in parsed.hosts:
    #print(host[0])
    if host.is_up():
        #ports = host.get_ports
        #if host.ports == " ":
           # print("ports are closed for ", host)
        services = host.services
        if len(services) == 0:
            print(host.address+":Closed")
        else:    
            for service in services:
                if (service.state == "open"):
                    try:
                        print(host.address+":"+str(service.port)+"\t"+(service.service)+"\t"+(service.banner_dict['product']))
                    except:
                        print(host.address+":"+str(service.port)+"\t"+(service.service))

