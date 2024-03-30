#!/usr/bin/python3

import subprocess
from ldap3 import Server, Connection, MODIFY_REPLACE, MODIFY_ADD, MODIFY_DELETE

"""
This is main.py

Author: Lokesh Kumar
Date: 28 March 2024
"""

# LDAP server details
ldap_server = 'ldap://localhost' # change according to your environment
ldap_port = 389  # Change to the appropriate port number
ldap_user = 'cn=Manager,dc=nsm,dc=in'  # Change to the appropriate LDAP admin user
ldap_password = 'master@@321'  # Change to the appropriate LDAP admin password
ldap_base_dn = 'dc=nsm,dc=in'  # Change to the appropriate LDAP base DN


# Initialize LDAP connection
server = Server(ldap_server, port=ldap_port)
conn = Connection(server, user=ldap_user, password=ldap_password, auto_bind=True)


# Search LDAP entries
def search_ldap(filter_str):
    conn.search(ldap_base_dn, filter_str)
    entries = conn.entries
    return entries

# Find and delete DN entries
def delete_dn(user_dn):
   # Construct the LDAP search command
    ldapsearch_command = "ldapsearch -x cn={} | grep dn: | cut -d ' ' -f 2".format(user_dn)

    # Execute the command and capture output
    entries_bytes = subprocess.check_output(ldapsearch_command, shell=True)

    # Decode bytes to string and remove any white spaces
    entries = entries_bytes.decode('utf-8').strip()

    # Split the LDAP entries into separate lines
    lines = entries.split('\n')

    # Delete entries
    for line in lines:
        delete_ldap_entry(line)

    return 0   # Return Success
    

# Delete LDAP entry
def delete_ldap_entry(entry_dn):
    conn.delete(entry_dn)


# main 
if __name__ == "__main__":
    # Example search
    search_filter = '(objectClass=person)'
    search_result = search_ldap(search_filter)
    user_dn = delete_dn('cdacadmin01')
    #print(user_dn)
    #splitted_entry = dn_entry_split(user_dn)
    #print()
    #print("Search result:")
    #print(search_result)

    

# Close LDAP connection
conn.unbind()