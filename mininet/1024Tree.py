# 1024 tree topo from mininet examples with modifications
#!/usr/bin/env python
from mininet.node import RemoteController
from mininet.clean import cleanup
from mininet.log import setLogLevel

"""
Create a 1024-host network, and run the CLI on it.
If this fails because of kernel limits, you may have
to adjust them, e.g. by adding entries to /etc/sysctl.conf
and running sysctl -p. Check util/sysctl_addon.
"""

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSSwitch
from mininet.topolib import TreeNet
from mininet.examples.treeping64 import HostV4

if __name__ == '__main__':
    cleanup()
    setLogLevel('info')
    c1 = RemoteController( 'cx', ip='127.0.0.1', port=6653)
    network = TreeNet( depth=3, fanout=6, host=HostV4, controller=c1,
                       switch=OVSSwitch, waitConnected=True)
    network.start()
    CLI(network)
    network.stop()
