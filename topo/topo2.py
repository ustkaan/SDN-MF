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
        r7 = self.addSwitch('r7')
        r8 = self.addSwitch('r8')
        r9 = self.addSwitch('r9')
        r10 = self.addSwitch('r10')
        r11 = self.addSwitch('r11')
        r12 = self.addSwitch('r12')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        
        #, use_htb=True
        self.addLink(h1, r8, bw=1000, delay='3ms', loss=2, max_queue_size=100) 
        self.addLink(h1, r1, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(h1, r9, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r1, r2, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r2, r3, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r3, r4, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r9, r10, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r10, r11, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r11, r12, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r12, h2, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r8, r7, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r7, r6, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r6, r5, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r5, h2, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r4, h2, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r7, r2, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r7, r10, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r6, r3, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r6, r11, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r5, r4, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r5, r12, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r8, r1, bw=1000, delay='3ms', loss=2, max_queue_size=100)
        self.addLink(r8, r9, bw=1000, delay='3ms', loss=2, max_queue_size=100)

topos = { 'mytopo': ( lambda: MyTopo() ) }
