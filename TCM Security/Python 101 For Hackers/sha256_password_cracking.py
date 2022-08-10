#!/usr/bin/env python3
# Project #2 - SHA256 password cracking

# Writing a solution without pwntools because it's broken in both pip *and*
# brew.
#import pwn
import hashlib
import sys


# I wouldn't have implemented user input, added this after watching the video.
if len(sys.argv) != 2:
    print("Invalid arguments!")
    print(f"{sys.argv[0]} <sha256sum>")
    sys.exit()

target_hash = sys.argv[1]
# I worked with a dictionary; added this after watching the video.
password_file = "passwords.txt"

def sha256_cracking():
    with open(password_file, "r") as passwords:
        for password in passwords:
            # If it's not encoded there will be a type error .. and I have no idea
            # why that's the case yet
            hashed_string = hashlib.sha256(password.encode("utf-8"))
            if hashed_string.hexdigest() == target_hash:
                print(f"[+] Found a match: {target_hash} -> {password}")
                exit

sha256_cracking()
