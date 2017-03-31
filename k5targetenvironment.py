#!/usr/bin/python

# APPLICATION DETAILS

# K5 target Project
projectId = '7015d1478a4c4bd7b970215d7b0260dd' # k5/openstack demo target project id

# List of required CIDRs
# Note: When deploying to 2 AZs at the same time the 3 octed of the CIDRs
# in the second AZ will automatically be incremented to allow for future inter AZ connectivity.
networkList = ['10.0.1.0/24', '10.0.2.0/24', '10.0.3.0/24']

# List of target Availability Zones
availabilityZones = ['uk-1a','uk-1b']


