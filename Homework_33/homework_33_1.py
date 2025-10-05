#запитання 1
#Robots.txt
#Завантажте та збережіть файл robots.txt з веб-сайтів wikipedia, twitter тощо.

import requests

sites = {
    "wikipedia": "https://en.wikipedia.org/robots.txt",
    "x": "https://x.com/robots.txt"
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0 Safari/537.36"
}

for name, url in sites.items():
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        filename = f"{name}_robots.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"[OK] {url} → {filename}")
    except Exception as e:
        print(f"[ERR] {url}: {e}")