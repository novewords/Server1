import requests
import concurrent.futures
import random
from bs4 import BeautifulSoup
import socket

DOMAINS = ["https://httpbin.org/ip", "https://fast.com",
           "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt",
           "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt"]


def check_proxy(proxy):
    try:
        parsed_proxy = proxy.split('://')[1]
        ip, port = parsed_proxy.split(':')
        port = int(port)

        with socket.create_connection((ip, port), timeout=1.25):
            return proxy
    except:
        pass
    return None


def find_working_proxy(proxies):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(check_proxy, proxy): proxy for proxy in proxies}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                for future_to_cancel in futures:
                    if future_to_cancel != future and not future_to_cancel.done():
                        future_to_cancel.cancel()
                return result
    return None

def get_proxies_from_url(url, prefix):
    response = requests.get(url)
    return [f"{prefix}://{x.decode()}" if not x.decode().startswith(prefix) else x.decode() for x in response.iter_lines()]

def GH():
    urls = [
        "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"
    ]
    proxies = get_proxies_from_url(random.choice(urls), "socks5")
    random.shuffle(proxies)
    return find_working_proxy(proxies[:20])

def GH2():
    urls = [
        "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt",
        "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/socks4_proxies.txt"
    ]
    proxies = get_proxies_from_url(random.choice(urls), "socks4")
    random.shuffle(proxies)
    return find_working_proxy(proxies[:15])

def HMN():
    proxies = []
    url = "https://hidemyname.io/en/proxy-list/?maxtime=1200&type=5#list"
    response = requests.get(url, headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "t=384101693",
        "Priority": "u=0, i",
        "Referer": "https://hidemyname.io/en/proxy-list/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": '"Android"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Sec-Gpc": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36"
    })

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        tbody = soup.find('tbody')
        if tbody:
            proxies = [
                f"socks5://{cols[0].text.strip()}:{cols[1].text.strip()}"
                for row in tbody.find_all('tr')
                for cols in [row.find_all('td')]
                if len(cols) >= 2
            ]
            random.shuffle(proxies)
            return find_working_proxy(proxies[:15])
    return None

def WorkingProxy():
    funcs = [HMN, GH, GH2]
    for i in range(2):
        proxy = random.choice(funcs)()
        if proxy:
            return proxy
    return None

