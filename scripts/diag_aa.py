"""AA HTML yapısı teşhisi — tarih ve related-news selector'ları için."""
import re
import requests
from bs4 import BeautifulSoup

url = "https://www.aa.com.tr/en/europe/gaza-faces-collective-punishment-by-israel-doctors-without-borders/3018693"
r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
soup = BeautifulSoup(r.text, "lxml")

print("=== META tarih adayları ===")
for m in soup.find_all("meta"):
    prop = (m.get("property") or "") + " " + (m.get("name") or "")
    if any(k in prop.lower() for k in ["publish", "date", "time", "created", "modified"]):
        key = m.get("property") or m.get("name")
        val = (m.get("content") or "")[:90]
        print(f"  {key}: {val}")

print()
print("=== TIME tag ===")
for t in soup.find_all("time")[:5]:
    print(f"  datetime={t.get('datetime')} | text={t.get_text(strip=True)[:60]}")

print()
print("=== Schema.org JSON-LD (ilk 400 kar) ===")
for s in soup.find_all("script", type="application/ld+json")[:2]:
    print("  " + s.get_text()[:400])
    print("  ---")

print()
print("=== Article body class arama ===")
body = soup.find("div", class_=re.compile("detay-icerik|article-text|content", re.I))
if body:
    print(f"Body class: {body.get('class')}")
    print()
    print("--- Body içindeki div/section/aside class'ları ---")
    for el in body.find_all(["div", "section", "aside"])[:20]:
        cls = " ".join(el.get("class", []))
        if cls:
            print(f"  {el.name}.{cls[:80]}")
else:
    print("body bulunamadı, alternatif selector'lar:")
    for tag, cls in [("div", "p-detay"), ("article", None), ("main", None)]:
        n = soup.find(tag, class_=re.compile(cls, re.I)) if cls else soup.find(tag)
        print(f"  {tag} (class~{cls}): {'BULUNDU' if n else 'yok'}")

print()
print("=== Tüm body'de 'related/ilgili/haber-listesi/news-list' arama ===")
for el in soup.find_all(class_=re.compile("related|ilgili|haber-listesi|news-list", re.I))[:10]:
    print(f"  {el.name}.{el.get('class')}")

print()
print("=== Article'ın gerçek gövdesi — başlık etrafında ===")
h1 = soup.find("h1")
if h1:
    print(f"H1: {h1.get_text(strip=True)[:80]}")
    parent = h1.parent
    depth = 0
    while parent and depth < 6:
        cls = parent.get("class") if hasattr(parent, "get") else None
        tag_id = parent.get("id") if hasattr(parent, "get") else None
        print(f"  parent[{depth}] {parent.name} class={cls} id={tag_id}")
        parent = parent.parent
        depth += 1

print()
print("=== Sayfadaki 'p' etiketi sayısı ve ilk 5 paragraf ===")
ps = soup.find_all("p")
print(f"Toplam p: {len(ps)}")
for p in ps[:5]:
    txt = p.get_text(strip=True)
    cls = " ".join(p.get("class", []))
    parent_cls = " ".join(p.parent.get("class", [])) if p.parent and hasattr(p.parent, "get") else ""
    print(f"  p.{cls} (parent.{parent_cls[:40]}): {txt[:80]}")

print()
print("=== Gövde paragraflarını tutan parent div'i bul ===")
para_parents: dict[str, int] = {}
for p in ps:
    if p.parent and hasattr(p.parent, "get"):
        cls = " ".join(p.parent.get("class", []))
        if cls:
            para_parents[cls] = para_parents.get(cls, 0) + 1
for cls, n in sorted(para_parents.items(), key=lambda x: -x[1])[:5]:
    print(f"  {n} paragraph -> parent class: {cls}")
