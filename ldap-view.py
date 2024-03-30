#!/usr/bin/python3

from ldap3 import Server, Connection, ALL

"""
This is main.py

Author: Lokesh Kumar
Date: 28 March 2024
"""


server = Server('ldap://localhost:389', get_info=ALL)

# Define LDAP connection
conn = Connection(server, user='cn=Manager,dc=nsm,dc=in', password='master@@321', auto_bind=True)

# Perform LDAP search operation
conn.search('dc=nsm,dc=in', '(objectclass=*)')

# Print search results
print("Search result entries:", len(conn.entries))
print("Search result entries:", conn.entries)

# Close LDAP connection
conn.unbind()


