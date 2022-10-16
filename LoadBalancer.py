from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr

log = core.getLogger()
s1_dpid=0
s2_dpid=0
s3_dpid=0
s4_dpid=0

def _handle_ConnectionUp (event):
    
      global s1_dpid, s2_dpid, s3_dpid, s4_dpid

      for m in event.connection.features.ports:
            
            #Switch 1
            if m.name == "s1-eth1":
                  
                  #flood ARP packets
                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x806),action=of.ofp_action_output(port=of.OFPP_ALL))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.1",nw_dst="10.0.0.3"),action=of.ofp_action_output(port=3))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.2",nw_dst="10.0.0.3"),action=of.ofp_action_output(port=4))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.3",nw_dst="10.0.0.1"),action=of.ofp_action_output(port=1))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.3",nw_dst="10.0.0.2"),action=of.ofp_action_output(port=2))
                  event.connection.send(msg)

            elif m.name == "s2-eth1":

                  #flood ARP packets
                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x806),action=of.ofp_action_output(port=of.OFPP_ALL))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.1",nw_dst="10.0.0.3"),action=of.ofp_action_output(port=2))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.3",nw_dst="10.0.0.1"),action=of.ofp_action_output(port=1))
                  event.connection.send(msg)

            elif m.name == "s3-eth1":

                  #flood ARP packets
                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x806),action=of.ofp_action_output(port=of.OFPP_ALL))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.2",nw_dst="10.0.0.3"),action=of.ofp_action_output(port=2))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.3",nw_dst="10.0.0.2"),action=of.ofp_action_output(port=1))
                  event.connection.send(msg)

            elif m.name == "s4-eth1":
                  
                  #flood ARP packets
                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x806),action=of.ofp_action_output(port=of.OFPP_ALL))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.1",nw_dst="10.0.0.3"),action=of.ofp_action_output(port=3))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.2",nw_dst="10.0.0.3"),action=of.ofp_action_output(port=3))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.3",nw_dst="10.0.0.1"),action=of.ofp_action_output(port=1))
                  event.connection.send(msg)

                  msg = of.ofp_flow_mod(match=of.ofp_match(dl_type=0x800,nw_src="10.0.0.3",nw_dst="10.0.0.2"),action=of.ofp_action_output(port=2))
                  event.connection.send(msg)



def launch ():
  core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)