import requests

data = requests.get("https://raw.githubusercontent.com/notracking/hosts-blocklists/master/dnscrypt-proxy/dnscrypt-proxy.blacklist.txt").text
data = data.split("\n")
host_list = []

def l_create():
    l_count = 0
    for line in data:
        li = line.strip()
        if not li.startswith("#"):
            host_list.append(line.rstrip())
            l_count += 1
    print(str(l_count) + " records recieved")