#!/usr/bin/python
"""
This script demonstrates how to deploy multiple networks across
either or both availability zones in a K5 region.

Prerequisites:
The following files contain functions or parameters that are used in this program.
 - k5APIsV2.py, library of K5 python functions to simplify API usage
 - k5contract.py, account details
 - k5targetenvironment.py, contains details of the project to use and the list of networks and availability availabilityZones

 If deploying to both availability zones at the same time the 3rd Octect of the IP address will be incremented by 1 for all
 the CIDRs in the list of networks. This is to allow inter AZ network connections between all subnets if necessary. 
 If both AZs had the same CIDRs we could not use the Inter-AZ network connector.

 However, if you do wish to have the same configuration in both AZs simply run the script twice with the respect AZ only each time.

 Execution:
 - Configure k5contract.py with your K5 details
 - Configure k5targetenvironment.py
 - Now simply run the following command from the directory where the files are located
    python k5_environment_create.py

Author: Graham Land
Date: 31/03/17
Twitter: @allthingsclowd
Github: https://github.com/allthingscloud
Blog: https://allthingscloud.eu


"""


from K5APIsV2 import *
from k5contract import *
from k5targetenvironment import *

def increment_cidr(subnet):
    # Note: When deploying to 2 AZs at the same time the 3 octed of the CIDRs
    # in the second AZ will automatically be incremented to allow for future inter AZ connectivity.
    ip, submask = subnet.split('/')
    octets = ip.split('.')
    octets[1] = unicode(int(octets[1]) + 1)
    newSubnet = '.'.join([str(x) for x in octets])
    newCidr = newSubnet + '/' + submask
    return unicode(newCidr)


def k5_environment_create(scopedToken, intCidrList, availabilityZones):

    # loop through availability zones identified in list
    for azIdx, az in enumerate(availabilityZones):
        # create internal networks
        networks = []
        subnets = []

        tempName =  unicode(randomword(5)) + unicode('-') + unicode(az)

        # create a virtual router
        routerName = unicode('router-') + tempName
        routerId = create_router(scopedToken, routerName, az)
        routerId = routerId.json()['router'].get('id')

        # loop through all the networks in the list
        for cidrIdx, cidr in enumerate(intCidrList):
            netName = unicode('net-') + unicode(cidrIdx) + unicode('-') + tempName
            subnetName = unicode('subnet-') + unicode(cidrIdx) + unicode('-') + tempName
            
            # Note: When deploying to 2 AZs at the same time the 3 octed of the CIDRs
            # in the second AZ will automatically be incremented to allow for future inter AZ connectivity.
            if azIdx < 1:
                subnetCidr = cidr 
            else:
                subnet = increment_cidr(subnetCidr)

            # create network
            networkId = create_network(scopedToken, netName, az)
            networkId = networkId.json()['network'].get('id')
            networks.append(networkId)
            
            # create subnet
            subnetId = create_subnet(scopedToken, subnetName, networkId, cidr, az)
            subnetId = subnetId.json()['subnet'].get('id')
            subnets.append(subnetId)

            # connect subnet interface to router
            routerInterface = add_interface_to_router(scopedToken, routerId, subnetId)
    
    return "Complete!"



def main():
    """Summary

    Returns:
        TYPE: Description
    """

    # obtain a k5 project scoped token - user details loaded from k5contract.py file
    scopedK5token = get_scoped_token(userName, password, contractName, projectId, region)

    # deploy the networks identified in the k5targetenvironment.py file
    print k5_environment_create(scopedK5token, networkList, availabilityZones)



if __name__ == "__main__":
    main()
