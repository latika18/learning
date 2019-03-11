#! /usr/bin/python3
#! mapIt.y - Launches a map in browser using an address form the command 
# line or clipboard.

import webbrowser,  sys
site = ['https://facebook.com','https://twitter.com','https://linkedin.com']
i = len(site) -1 
while i >= 0:
	webbrowser.open(site[i])
	i -= 1

