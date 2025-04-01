import requests 
import re
from urllib.parse import urlparse, urljoin

# def request(url):
#     try:
#         return requests.get(f"http://{url}")
#     except requests.exceptions.ConnectionError as e:
#         print(f"[-] Error: {e}")

target_url = "http://192.168.83.131/mutillidae/"
target_links = []

def extract_links_from(url):
    response = requests.get(target_url)
    decoded_content = response.content.decode("utf-8")
    return re.findall('(?:href=")(.*?)"', decoded_content)

def crawl(url):
    href_link = extract_links_from(url)
    for link in href_link:
        link = urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)
