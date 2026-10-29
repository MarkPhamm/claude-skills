"""Download Mark's public Substack posts as plain text, one file per post.

Usage: python3 -I fetch_posts.py <out_dir> [limit]
"""
import json
import pathlib
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser

BASE = "https://markphammm.substack.com/api/v1"
# Substack answers 403 to urllib's default user agent.
HEADERS = {"User-Agent": "Mozilla/5.0"}


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "br", "div", "li", "h1", "h2", "h3", "h4", "pre", "blockquote", "tr"):
            self.out.append("\n")
        if tag in ("h1", "h2", "h3", "h4"):
            self.out.append("#" * int(tag[1]) + " ")
        if tag == "li":
            self.out.append("- ")
        if tag == "img":
            self.out.append("[image]")
        if tag == "code":
            self.out.append("`")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag == "code":
            self.out.append("`")
        if tag in ("p", "h1", "h2", "h3", "h4", "pre", "blockquote"):
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def get(url, tries=4):
    # Substack rate-limits bursts with 429/5xx: back off and retry.
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as err:
            if err.code not in (429, 500, 502, 503, 504) or attempt == tries - 1:
                raise
            time.sleep(2 ** attempt * 2)


def main():
    out = pathlib.Path(sys.argv[1])
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    out.mkdir(parents=True, exist_ok=True)
    archive = get(f"{BASE}/archive?sort=new&limit={limit}")
    for i, post in enumerate(archive):
        data = get(f"{BASE}/posts/{post['slug']}")
        parser = Text()
        parser.feed(data.get("body_html") or "")
        body = re.sub(r"\n{3,}", "\n\n", "".join(parser.out)).strip()
        head = f"TITLE: {data['title']}\nSUBTITLE: {data.get('subtitle') or ''}\nDATE: {data['post_date'][:10]}\n\n"
        (out / f"{i:02d}_{post['slug']}.txt").write_text(head + body)
        print(f"{data['post_date'][:10]}  {data['title']}")
        time.sleep(0.3)


if __name__ == "__main__":
    main()
