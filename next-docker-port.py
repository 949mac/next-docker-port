#!/usr/bin/python3

# sudo cp next-docker-port.py /usr/local/bin/next-docker-port
# next-docker-port sudo chmod +x /usr/local/bin/next-docker-port

import subprocess
import os
import sys
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("portStart", help="If looking for range 9000+, simply enter 9")
args = parser.parse_args()


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def get_docker_ports(containing):
    portsFound = []
    cmd = 'docker container ls --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" -a | grep "0:' + args.portStart + '"'
    so = os.popen(cmd).read()
    print(so)

    regex = r"0\:([0-9]+)"
    matches = re.finditer(regex, so, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            portsFound.append(int(match.group(groupNum)))

    portsFound.sort()
    current_port_num = 0
    found = False
    for i in range(len(portsFound)):
        print(portsFound[i])
        if (i == 0):
            current_port_num = portsFound[0]
        else:
            current_port_num += 1
            if (current_port_num != portsFound[i]):
                found = True
                break

    if (found == False) :
        current_port_num += 1

    print('👉 ', current_port_num)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_docker_ports('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
