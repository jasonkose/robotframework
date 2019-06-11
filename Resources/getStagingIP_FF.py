# this script is used to find edge IP.
# Edge IP of FreeFlow staging network.
# ESSL property, too, will be tested FF staging edge IP.
# that is for log gathering

import dns.resolver
import re


def getStagingIP(hostname):

    edgehostname = hostname + ".edgesuite.net"
    myresolver = dns.resolver.Resolver()
    cnames = myresolver.query(edgehostname, "CNAME")
    cname = str(cnames[0])
    print(cname)
    while True:
        try:
            cnames = myresolver.query(cname,"CNAME")
            cname = str(cnames[0])
            print(cname)
        except:
            break
    if '.akamaiedge.net.' in cname:
        stagingHostname = re.sub('akamaiedge.net.','akamaiedge-staging.net.',cname)
    elif '.akamai.net.' in cname:
        stagingHostname = re.sub('akamai.net.','akamai-staging.net.',cname)

    else:
        stagingHostname = cname
    myanswer = myresolver.query(stagingHostname, "A")
    print('final cname: '+stagingHostname)
    return str(myanswer[0])

def getedgeip(hostname):
    edgehostname = hostname + ".edgekey.net"
    myresolver = dns.resolver.Resolver()
    edgeips = myresolver.query(edgehostname, "A")
    #print(edgeips)
    return edgeips
if __name__ == "__main__":
    hostnames = ["www.naver.com"]
    for hostname in hostnames:
        results = getStagingIP(hostname)
        print(results[0])
        edgeips = getedgeip(hostname)
        for edgeip in edgeips:
            print(edgeip)
