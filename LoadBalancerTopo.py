#! /usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

        net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)

        c1 = net.addController('c1', controller=RemoteController, ip="127.0.0.1", port=6633)

        h1 = net.addHost( 'h1', ip='10.0.0.1' )
        h2 = net.addHost( 'h2', ip='10.0.0.2' )
	h3 = net.addHost( 'Server', ip='10.0.0.3' )
	
        s1 = net.addSwitch( 's1' )
	s2 = net.addSwitch( 's2' )
	s3 = net.addSwitch( 's3' )
        s4 = net.addSwitch( 's4' )

        s1.linkTo( h1 )
        s1.linkTo( h2 )
        s1.linkTo( s2 )
        s1.linkTo( s3 )

        s2.linkTo( s4 )
        s3.linkTo( s4 )
        s4.linkTo( h3 )

        net.build()
        c1.start()
        s1.start([c1])
	s2.start([c1])
	s3.start([c1])
	s4.start([c1])

        CLI( net )
        net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
                   