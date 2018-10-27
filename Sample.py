#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime
import sys

from PostmanAPI import Collections  # if use only collections 
from PostmanAPI import Environments
from PostmanAPI import Mocks
from PostmanAPI import Monitors
from PostmanAPI import Workspaces
from PostmanAPI import User

KEY = '067100f97faf4bc292ac3413bc04b2e0' # add your key to postman access 

def main(argv):

	# collections
	print("Testing collections...")
	coll = Collections(KEY)
	print (coll.get_all())

	# environments
	print("Testing environments...")
	env = Environments(KEY)

	# mocks
	print("Testing mocks...")
	env = Mocks(KEY)

	# monitors
	print("Testing monitors...")
	env = Monitors(KEY)

	# workspaces
	print("Testing workspaces...")
	env = Workspaces(KEY)

	# user
	print("Testing users...")
	env = User(KEY)

if __name__ == "__main__":
    main(sys.argv)
