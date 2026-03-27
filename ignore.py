import re

line = "Failed password for invalid user admin from 192.168.1.10"

match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)

print(match)
print(match.group(1))