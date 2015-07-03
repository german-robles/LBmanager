#!/usr/bin/python
# -*- coding: utf-8 *-*

try:
	import optparse
	import yaml
	import os
	import sys

except ImportError:
	print 'To run this script you must install missing modules'
class LBmanager:
	def __init__(self):
		imHere = os.path.dirname(os.path.abspath(__file__))
		with open("%s/LBmanager.conf" % (imHere), 'r') as ymlfile:
			cfg = yaml.load(ymlfile)
		backends = (cfg['backends'])
		parser = optparse.OptionParser()
		parser.add_option('-b', '--backend', dest="backend", action="store",
							help="Define backend to manage. Available backends:%s"% backends)
		parser.add_option('-n', '--node', dest="node", action="store", help="Define numerical node to manage")
		parser.add_option('-a', '--action', dest="action", action="store", help="enable & disable nodes (values allowed disable, enable)")
		options, args = parser.parse_args()
		backend = options.backend
		node = options.node
		action = options.action
		self.LBcontroller(backend, node, action)
	def LBcontroller(self, backend, node, action):
		with open("LBmanager.conf", 'r') as ymlfile:
			cfg = yaml.load(ymlfile)
		server = (cfg['server'])	
		socat = (cfg['socat'])
		os.system('echo "%s server %s/%s%s" | socat stdio %s'% (action, backend, server, node, socat))
controller = LBmanager()