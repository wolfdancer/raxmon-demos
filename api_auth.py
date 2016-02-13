#!/usr/bin/env python2.7
import getpass
import pyrax
import pyrax.identity
import requests
import json

raxusername = raw_input("Account:")
apikey = getpass.getpass("API Key for <{}>: ".format(raxusername))
pyrax.set_setting("identity_type", "rackspace")
pyrax.set_credentials(raxusername, apikey)
identity = pyrax.identity
print identity.authenticated
print identity.token
print identity.expires

