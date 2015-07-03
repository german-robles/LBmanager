LBmanager
=========
This script is a very simple script to manager (UP or Down) nodes from your HAproxy pool.

# Configuration

* First of all you must check that python is installed and python-yaml (pip install pyyaml).
* In one command line you will be able to get down of get up nodes from you haproxy backends.

In the config file (LBmanager.conf) you must define your backends, your server name and socat tunnel

# HAProxy configuration:

In global tag configuration you must add the following:

 stats socket /path/to/haproxysock level admin

# Usage

* In CLI you must run (example)

 python LBmanager.py -b backend1 -n 1 -a disable 

* Help command is supported:

 python LBmanager.py -h

