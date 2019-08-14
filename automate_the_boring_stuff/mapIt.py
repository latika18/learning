#! /usr/bin/python3
#! mapIt.y - Launches a map in browser using an address form the command 
# line or clipboard.

import webbrowser,  sys
import pyperclip

if len(sys.argv) > 1:
	# Get address from command line.
	address = ''.join(sys.argv[1:])

else:
	# Get address from clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.maps.com/maps/place/' + address)
