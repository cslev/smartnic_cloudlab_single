"""Bluefield2 - This topology uses one single Bluefield2 enabled hosts @ Clemson.
It is not directly connected to any other node. It's mostly for doing basic experiments with Bluefield without actually transferring any packet
"""

#
# NOTE: This code was machine converted. An actual human would not
#       write code like this!
#

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
#rspec = pg.Request()


#### ---------------------------- TOPOLOGY -------------------------------------
# Node bf1
node = request.RawPC('bf2')
node.hardware_type = 'r7525'
node.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD'
bs1 = node.Blockstore("bs1", "/mydata")
bs1.size = "50GB"


#### ------------------------- CONFIGURE NODE ---------------------------------
node.addService(pg.Execute(shell="bash", command="/local/repository/smartnic_bootstrap.sh"))

# Print the generated rspec
pc.printRequestRSpec(request)
