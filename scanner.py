

import os

target = input("Enter target IP or website: ")

print("Scanning target:", target)

command = "nmap -sV " + target

result = os.popen(command).read()

print(result)

file = open("scan_report.txt", "w")
file.write(result)
file.close()

print("Scan completed. Report saved in scan_report.txt")


