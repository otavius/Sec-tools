import requests
import threading

domain = "192.168.83.131/mutillidae/"

with open("subdomains.txt") as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []

lock = threading.Lock()

def check_subdomain(subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else: 
        print("[+] Discovered subdomains: ", url)
        with lock:
            discovered_subdomains.append(url)

threads = []
for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain,file=f)