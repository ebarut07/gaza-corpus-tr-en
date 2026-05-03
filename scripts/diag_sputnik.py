"""Sputnik erişim teşhisi — DNS, TCP, HTTP düzeylerinde."""
import socket
import sys
from urllib.parse import urlparse

import requests

UA_DEFAULT = "GazzeKorpus-Academic/1.0 (test)"
UA_CHROME = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

CANDIDATES = [
    # Ana erişim noktaları
    ("https://sputnikglobe.com/",                      "EN ana sayfa (mevcut domain)"),
    ("https://sputnikglobe.com/20231007/",             "EN günlük arşiv 7 Ekim 2023"),
    ("https://sputnikglobe.com/en/",                   "EN /en/ alt yolu"),
    ("https://sputniknews.com/",                       "Eski EN domain (sputniknews.com)"),
    ("https://sputniknews.com/20231007/",              "Eski EN domain günlük arşiv"),
    ("https://sputnikinternational.com/",              "Sputnik International (eski)"),
    ("https://sputnikafrica.info/",                    "Afrika servisi"),
    ("https://sputnikafrica.media/",                   "Afrika media"),
    ("https://sputnik-georgia.com/",                   "Sputnik Georgia (Kafkas)"),
    ("https://sputnikglobe.com/export/rss2/archive/",  "RSS feed dene"),
    # TR mirror — kontrol grubu
    ("https://anlatilaninotesi.com.tr/",               "TR mirror (kontrol)"),
    ("https://anlatilaninotesi.com.tr/20231007/",      "TR mirror günlük arşiv"),
]


def dns_check(host: str) -> str:
    try:
        addr = socket.gethostbyname(host)
        return f"OK -> {addr}"
    except socket.gaierror as e:
        return f"FAIL: {e}"


def tcp_check(host: str, port: int = 443, timeout: float = 8.0) -> str:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return "OK"
    except socket.timeout:
        return "TIMEOUT (ISP/IP düzeyi blok şüphesi)"
    except ConnectionRefusedError as e:
        return f"REFUSED: {e}"
    except OSError as e:
        return f"OSError: {e}"


def http_check(url: str, ua: str, timeout: float = 12.0) -> str:
    try:
        r = requests.get(url, headers={"User-Agent": ua}, timeout=timeout, allow_redirects=True)
        loc = r.url if r.url != url else ""
        loc_str = f"  redirect->{loc}" if loc else ""
        return f"HTTP {r.status_code} ({len(r.content)} bytes){loc_str}"
    except requests.exceptions.SSLError as e:
        return f"SSL ERROR: {type(e).__name__}"
    except requests.exceptions.ConnectTimeout:
        return "ConnectTimeout"
    except requests.exceptions.ReadTimeout:
        return "ReadTimeout"
    except requests.exceptions.ConnectionError as e:
        return f"ConnectionError: {type(e).__name__}"
    except Exception as e:
        return f"{type(e).__name__}: {e}"


def main() -> int:
    print("=" * 78)
    print("SPUTNIK ERİŞİM TEŞHİSİ")
    print("=" * 78)

    hosts_seen: set[str] = set()
    for url, label in CANDIDATES:
        host = urlparse(url).hostname or "?"
        print(f"\n[{label}]")
        print(f"  URL : {url}")

        if host not in hosts_seen:
            hosts_seen.add(host)
            print(f"  DNS : {dns_check(host)}")
            print(f"  TCP : {tcp_check(host)}")

        print(f"  HTTP-default-UA: {http_check(url, UA_DEFAULT)}")
        print(f"  HTTP-Chrome-UA : {http_check(url, UA_CHROME)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
