#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime
import sys

from PostmanAPI import *

KEY = '067100f97faf4bc292ac3413bc04b2e0' # add your key to postman access 

def main(argv):

	# collections
	print("Testing collections...")
	coll = Collections(KEY)
	print (coll.get_all())
	print (coll.get_single("24c9cbfa-a3e0-4623-9139-bbc7e4a7b37c"))
	coll.del_delete("24c9cbfa-a3e0-4623-9139-bbc7e4a7b37c")

	# environments
	print("Testing environments...")
	env = Environments(KEY)
	print (env.get_all())

	# mocks
	print("Testing mocks...")
	mocks = Mocks(KEY)
	print (mocks.get_all())

	# monitors
	print("Testing monitors...")
	monit = Monitors(KEY)
	print (monit.get_all())

	# workspaces
	print("Testing workspaces...")
	works = Workspaces(KEY)
	print (works.get_all())

	# user
	print("Testing users...")
	user = User(KEY)
	print(user.get_api_key_owner())

if __name__ == "__main__":
    main(sys.argv)
