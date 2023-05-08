from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.node import OVSBridge
from mininet.clean import cleanup

import json

class MyTopo(Topo):
    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1' , ip='10.0.0.1')
        h2 = self.addHost( 'h2' , ip='10.0.0.2')
        h3 = self.addHost( 'h3' , ip='10.0.0.3')
        h4 = self.addHost( 'h4' , ip='10.0.0.4')
        h5 = self.addHost( 'h5' , ip='10.0.0.5')

        s1 = self.addSwitch( 's1', cls=OVSBridge)
        s2 = self.addSwitch( 's2', cls=OVSBridge)
        s3 = self.addSwitch( 's3', cls=OVSBridge)

        # Add links
        self.addLink( h1, s1, cls=TCLink,bw=2,delay='15ms')
        self.addLink( h2, s1, cls=TCLink,bw=2,delay='15ms')
        self.addLink( h3, s2, cls=TCLink,bw=2,delay='15ms')
        self.addLink( h4, s3, cls=TCLink,bw=2,delay='15ms')
        self.addLink( h5, s3, cls=TCLink,bw=2,delay='15ms')

        self.addLink( s1, s2, cls=TCLink,bw=2,delay='15ms')
        self.addLink( s2, s3, cls=TCLink,bw=2,delay='15ms')


if __name__ == '__main__':
    cleanup()
    setLogLevel('info')
    topo = MyTopo()
    net = Mininet(topo)
    net.start()
    CLI(net)
    net.stop()