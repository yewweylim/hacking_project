#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Targeted Interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC Address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw","ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
# change_mac(options.interface, options.new_mac)

ifconfig_results = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_results)

#Use Pythex to create Regex
# mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)
# print(mac_address_search_result.group(0))
