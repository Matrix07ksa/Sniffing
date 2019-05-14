# -*- coding: utf-8 -*-
from scapy.all import *
from optparse import *
import time 
from termcolor import colored
class Sniffing():
	def __init__(self):
		try :		
			use = OptionParser("""
		_____
	   /    /|_ ___________________________________________
	  /    // /|                                          /|
	 (====|/ //   Hejab Zaeri......            _QP_      / |
	  (=====|https://github.com/Matrix07ksa   (  ' )    / .|
	 (====|/                                   \__/    / /||
	/_________________________________________________/ / ||
	|  _____________________________________________  ||  ||
	| ||                                            | ||
	| ||                                            | ||
	| |                                             | |  
-i --intrface                  info_ip Command Terminal = ifconfig - eth0 - wlan0
-p --protocol                  snif_p  Protcol snifing = icmp,tcp,udp * 
-f --filter                    snif_f  Protcol snifing = icmp,tcp,udp * Infromatsion PRO+
-t --count                     Count Time snifing Packet = 1-10
-s --save                      Save Packet *.pcap
							   """)
			
			use.add_option("-i","--intrface",dest="intrface",help="Write Your Intrface Network Manger")
			use.add_option("-p","--protocol",dest="protcol",help="Write Your Protcol-Network :Example:icmp")
			use.add_option("-t","--count",dest="time",help="Write Your Time Snifing",default=5)
			use.add_option("-s","--save",dest="Save",help="Write Your Save Snifing Packet.txt",default="PacketSnifing.pcap")
			use.add_option("-f","--filter",dest="filt",help="Write Your Protcol-Network Infromatsion PRO+:Example:icmp")
			(options,args) = use.parse_args()
			if options.intrface  == None :
				print(use.usage)
				exit(0)
			elif options.filt !=None  :
				f = sniff(iface=options.intrface,count=10,filter=options.filt)
				File_Pcap= wrpcap(options.Save, f)
				for z in f:
					print(z.show())
					
			else:
				
				FT = True
				while FT:		
					global s
					s = sniff(iface=options.intrface,count=int(options.time),filter=options.protcol)
					File_Pcap= wrpcap(options.Save, s)
					print(colored("............................(Packet)..............................\n","red"))
					print(colored(".....................({})...........................\n".format(time.ctime()),"red"))
					print(colored(s.show(),"blue"))
					s = str(s).split("Sniffed")[1]
					print(colored("Snifing %s"%s,"red"))
				
						
		except KeyboardInterrupt:
			pass
		except AttributeError:
			pass
		except OSError:
			raise Exception("Failed to create network")
			print("Intrface Network Divice")
		except ImportError:
			print("Please Install (scapy) or (optparse) or (termcolor)")
if __name__ == '__main__':
	Sniffing()
			
