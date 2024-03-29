#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://docs.api.getpostman.com/

"""

import requests

class Collections:
	def __init__(self, key):
		self.key = key
		self.apiUrl = 'https://api.getpostman.com'

	def get_all(self):
		url = self.apiUrl+'/collections'
		headers ={'X-Api-Key': str(self.key)}
		response = requests.get(url,headers=headers)
		return response.json()

	def get_single(self, collection_uid):
		url = self.apiUrl +'/collections/'+collection_uid
		headers ={'X-Api-Key': str(self.key)}
		response = requests.get(url,headers=headers)
		return response.json()

	def post_create(self, data):
		url = self.apiUrl +'/collections/'
		headers ={'X-Api-Key': str(self.key), 'Content-Type': 'application/json'}
		response = requests.post(url,headers=headers, data=data)
		return response.json()

	def put_update(self, collection_uid, data):
		url = self.apiUrl +'/collections/'+collection_uid
		headers ={'X-Api-Key': str(self.key), 'Content-Type': 'application/json'}
		response = requests.put(url,headers=headers, data=data)

	def del_delete(self, collection_uid):
		url = self.apiUrl +'/collections/'+collection_uid
		headers ={'X-Api-Key': str(self.key), 'Content-Type': 'application/json'}
		response = requests.delete(url,headers=headers)

class Environments:
	def __init__(self, key):
		self.key = key
		self.apiUrl = 'https://api.getpostman.com'

	def get_all(self):
		url = self.apiUrl +'/environments'
		headers ={'X-Api-Key': self.key}
		response = requests.get(url,headers=headers)
		return response.json()

	def get_single(self, environment_uid):
		url = self.apiUrl +'/environments/'+environment_uid
		headers ={'X-Api-Key': str(self.key)}
		response = requests.get(url,headers=headers)
		return response.json()

	def post_create(self, name, urlApi):

		url = self.apiUrl +'/environments/'
		headers ={'X-Api-Key': str(self.key), 'Content-Type': 'application/json'}
		data = '{"environment": { "name": "'+name+'", \
					"values": [ \
						{"key": "apiUrl", "value": "'+urlApi+'"} \
					]\
				}\
				}'
		response = requests.post(url,headers=headers, data=data)

	def put_update(self):
		pass

	def del_delete(self,environments_uid):
		url = self.apiUrl +'/environments/'+environments_uid
		headers ={'X-Api-Key': str(self.key), 'Content-Type': 'application/json'}
		response = requests.delete(url,headers=headers)

class Mocks:
	def __init__(self, key):
		self.key = key
		self.apiUrl = 'https://api.getpostman.com'

	def get_all(self):
		url = self.apiUrl +'/mocks'
		headers ={'X-Api-Key': self.key}
		response = requests.get(url,headers=headers)
		return response.json()

	def get_single(self, mocks_uid):
		url = self.apiUrl +'/mocks/'+mocks_uid
		headers ={'X-Api-Key': str(self.key)}
		response = requests.get(url,headers=headers)
		return response.json()

	def post_create(self, name, urlApi):
		pass

	def put_update(self):
		pass

	def del_delete(self,mocks_uid):
		url = self.apiUrl +'/mocks/'+mocks_uid
		headers ={'X-Api-Key': str(self.key), 'Content-Type': 'application/json'}
		response = requests.delete(url,headers=headers)

class Monitors:
	def __init__(self, key):
		self.key = key
		self.apiUrl = 'https://api.getpostman.com'

	def get_all(self):
		url = self.apiUrl +'/monitors'
		headers ={'X-Api-Key': self.key}
		response = requests.get(url,headers=headers)
		return response.json()

	def get_single(self, monitors_uid):
		url = self.apiUrl +'/monitors/'+monitors_uid
		headers ={'X-Api-Key': str(self.key)}
		response = requests.get(url,headers=headers)
		return response.json()

	def post_create(self, name, urlApi):
		pass

	def put_update(self):
		pass

	def del_delete(self,monitors_uid):
		url = self.apiUrl +'/monitors/'+monitors_uid
		headers ={'X-Api-Key': str(self.key), 'Content-Type': 'application/json'}
		response = requests.delete(url,headers=headers)


class Workspaces:
	def __init__(self, key):
		self.key = key
		self.apiUrl = 'https://api.getpostman.com'

	def get_all(self):
		url = self.apiUrl +'/workspaces'
		headers ={'X-Api-Key': self.key}
		response = requests.get(url,headers=headers)
		return response.json()

	def get_single(self, workspaces_uid):
		url = self.apiUrl +'/workspaces/'+workspaces_uid
		headers ={'X-Api-Key': str(self.key)}
		response = requests.get(url,headers=headers)
		return response.json()

	def post_create(self, name, urlApi):
		pass

	def put_update(self):
		pass

	def del_delete(self,workspaces_uid):
		url = self.apiUrl +'/workspaces/'+workspaces_uid
		headers ={'X-Api-Key': str(self.key), 'Content-Type': 'application/json'}
		response = requests.delete(url,headers=headers)

class User:
	def __init__(self, key):
		self.key = key
		self.apiUrl = 'https://api.getpostman.com'

	def get_api_key_owner(self):
		url = self.apiUrl +'/me'
		headers ={'X-Api-Key': self.key}
		response = requests.get(url,headers=headers)
		return response.json()