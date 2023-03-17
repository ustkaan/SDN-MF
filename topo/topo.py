#!/usr/bin/env python

from mininet.topo import Topo

class MyTopo( Topo ):

    def build( self ):
        r1 = self.addSwitch('r1')
        r2 = self.addSwitch('r2')
        r3 = self.addSwitch('r3')
        r4 = self.addSwitch('r4')
        r5 = self.addSwitch('r5')
        r6 = self.addSwitch('r6')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        
        #, use_htb=True
        self.addLink(h1, r5, bw=1000, delay='3ms', loss=1, max_queue_size=100)
        self.addLink(r5, r1, bw=1000, delay='3ms', loss=1, max_queue_size=100)
        self.addLink(r5, r2, bw=1000, delay='3ms', loss=1, max_queue_size=100)
        self.addLink(r1, r3, bw=1000, delay='3ms', loss=1, max_queue_size=100)
        self.addLink(r2, r4, bw=1000, delay='3ms', loss=1, max_queue_size=100)
        self.addLink(r3, r6, bw=1000, delay='3ms', loss=1, max_queue_size=100)
        self.addLink(r4, r6, bw=1000, delay='3ms', loss=1, max_queue_size=100)
        self.addLink(r6, h2, bw=1000, delay='3ms', loss=1, max_queue_size=100)
        

topos = { 'mytopo': ( lambda: MyTopo() ) }
