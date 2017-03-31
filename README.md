# Multiple Network Deployment Script

This script demonstrates how to deploy multiple networks across
either or both availability zones in a K5 region.

## Prerequisites:
The following files contain functions or parameters that are used in this program.
 - k5APIsV2.py, library of K5 python functions to simplify API usage
 - k5contract.py, account details
 - k5targetenvironment.py, contains details of the project to use and the list of networks and availability availabilityZones

 If deploying to both availability zones at the same time the 3rd Octect of the IP address will be incremented by 1 for all
 the CIDRs in the list of networks. This is to allow inter AZ network connections between all subnets if necessary. 
 If both AZs had the same CIDRs we could not use the Inter-AZ network connector.

 However, if you do wish to have the same configuration in both AZs simply run the script twice with the respect AZ only each time.

 ## Execution:
 - Configure k5contract.py with your K5 details
 - Configure k5targetenvironment.py
 - Now simply run the following command from the directory where the files are located
    python k5_environment_create.py

Author: Graham Land

Date: 31/03/17

Twitter: @allthingsclowd

Github: https://github.com/allthingscloud

Blog: https://allthingscloud.eu


