import requests 
import threading

lock = threading.Lock()


def request(url):
    try:
        return requests.get(f"http://{url}")
    except requests.exceptions.ConnectionError as e:
        print(f"[-] Error: {e}")


target_url = "192.168.83.131/mutillidae/"

# subdomains

# with open(sub_file, "r") as file:
#     for line in file:
#         word = line.strip()
#         test_url = f"{word}.{target_url}"
#         reponse = request(test_url)
#         if reponse:
#             print(f"[+] Discoverd subdomain -> {test_url}")

# directories 
with open("common.txt", "r") as file:
    for line in file:
        word = line.strip()
        test_url = f"{target_url}/{word}"
        rep = request(test_url)
        if rep:
            print(f"[+] Dicovered URL -> {test_url}")

# discovered_subdomains = []
# directory = []



