#!/usr/bin/env python

# <pep8 compliant>

"""
Script for changing cursor shape. Expects new cursor-shape arg ({"block", "ibeam", "underline"})
Example usage: "./gnome-terminal-cursor-shape.py ibeam"
"""

import subprocess
import sys

dconfdump = subprocess.check_output("dconf dump /org/gnome/terminal/legacy/profiles:/", shell=True)
profilestr_array = dconfdump.split('\n\n')

for profilestr in profilestr_array:
	profilestr_keys = profilestr.split('\n')

	profilename = profilestr_keys[0]
	assert profilename[0] == '[' and profilename[len(profilename) - 1] == ']'
	profilename = profilename[1:(len(profilename) - 1)]


	try:
		if sys.argv[1] not in {"block", "ibeam", "underline"}:
			raise ValueError
		subprocess.call("dconf write /org/gnome/terminal/legacy/profiles:/" + profilename + "/cursor-shape \"'" + sys.argv[1] + "'\"", shell=True)
	except IndexError:
		print("Missing cursor-shape argument. Should have argument in {\"block\", \"ibeam\", \"underline\"}.")
	except ValueError:
		print("Invalid cursor-shape value. Should be in {\"block\", \"ibeam\", \"underline\"}.")
