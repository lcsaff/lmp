#!/usr/bin/python
# fs monitoring menu

import argparse
import os

version='%(prog)s version : v0.01 '

usage = """
Usage: 
    fs.py [-h] [-o] [-r] [-w] [-v] [-p] [-d]
"""

parser = argparse.ArgumentParser(
    description = "Filesystem monitoring tools",
    formatter_class = argparse.RawDescriptionHelpFormatter,
    epilog = version)

parser.add_argument("-o", "--open", action="store_true",
    help="Print all open syscall")

parser.add_argument("-r", "--read", action="store_true",
    help="Print all read syscall")

parser.add_argument("-w", "--write", action="store_true",
    help="Print all write syscall")

# parser.add_argument("-c", "--create", action="store_true",
#     help="Print all create syscall")

# parser.add_argument("-f", "--fsync", action="store_true",
#     help="Print all fsync syscall")

parser.add_argument("-v", "--vfs_func", action="store_true",
    help="Print all vfs method and counts")

parser.add_argument("-p", "--pcache", action="store_true",
    help="Print failed page cache lookups and hitting accuracy")

parser.add_argument("-d", "--dcache", action="store_true",
    help="Print failed dentry cache lookups and hitting accuracy")

args = parser.parse_args()

if args.open:
    print("Tracing open syscall...")
    os.system("sudo ./tools/open.py")

if args.read:
    print("Tracing read syscall...")
    os.system("sudo ./tools/read.py")
    
if args.write:
    print("Tracing write syscall...")
    os.system("sudo ./tools/write.py")
    
# if args.create:
#     print("Tracing create syscall...")
#     os.system("./tools/create.py")
    
# if args.fsync:
#     print("Tracing fsync syscall...")
#     os.system("./tools/fsync.py")
    
if args.vfs_func:
    print("Tracing vfs functions...")
    os.system("sudo ./tools/vfs.py")
    
if args.pcache:
    print("Tracing page cache stat...")
    os.system("sudo ./tools/pcache.py")

if args.dcache:
    print("Tracing dentry cache stat...")
    os.system("sudo ./tools/dcache.py")
    
else:
    print(usage)
