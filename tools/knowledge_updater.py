# -*- coding: utf-8 -*-
"""
knowledge_updater.py — self-improving crawl pipeline for Skill #164
(Productivity Coach (Pomodoro/GTD), cluster: lifestyle-personal).

Pattern (per CLAUDE.md):
  1. crawl4ai -> fetch latest papers/standards from domain sources
  2. WebSearch -> latest news/reports from authoritative domain sources
  3. Parse -> title, authors, date, DOI/URL, abstract, key findings
  4. Score -> rank by recency + domain-keyword relevance
  5. Append -> add scored entries to SECOND-KNOWLEDGE-BRAIN.md (date-stamped)
  6. Deduplicate -> skip entries already present (DOI/URL hash)

Recommended schedule: weekly cron.
Graceful degradation: if crawl4ai / network is unavailable, log and exit 0
so the skill keeps working off the existing knowledge base.
"""
import os, re, sys, json, hashlib, datetime

ARXIV_CATEGORIES = []
WEB_SOURCES = ['https://hbr.org', 'https://jamesclear.com', 'https://todoist.com/productivity-methods', 'https://www.calnewport.com']
SEARCH_QUERIES = ['productivity methods research', 'deep work focus evidence', 'time management GTD pomodoro', 'procrastination behavioral science']

BRAIN = os.path.join(os.path.dirname(__file__), "..", "SECOND-KNOWLEDGE-BRAIN.md")
RELEVANCE_KEYWORDS = [w for query in SEARCH_QUERIES for w in query.split()]


def _hash(url: str) -> str:
    return hashlib.sha256((url or "").encode("utf-8")).hexdigest()[:16]


def _existing_hashes(text: str):
    return set(re.findall(r"<!--hash:([0-9a-f]{16})-->", text))


def relevance_score(title: str, abstract: str) -> float:
    blob = (title + " " + abstract).lower()
    hits = sum(1 for k in RELEVANCE_KEYWORDS if k.lower() in blob)
    return hits / max(1, len(RELEVANCE_KEYWORDS))


def fetch_entries():
    """Return list of dicts: title, authors, year, venue, url, abstract.
    Uses crawl4ai when available; otherwise returns [] (graceful degradation)."""
    entries = []
    try:
        from crawl4ai import WebCrawler  # type: ignore
        crawler = WebCrawler(); crawler.warmup()
        for cat in ARXIV_CATEGORIES:
            url = f"https://arxiv.org/list/{cat}/recent"
            try:
                res = crawler.run(url=url)
                entries.extend(_parse_arxiv(getattr(res, "markdown", "") or "", url))
            except Exception as e:
                print(f"[warn] arxiv {cat}: {e}")
        for src in WEB_SOURCES:
            try:
                res = crawler.run(url=src)
                md = getattr(res, "markdown", "") or ""
                if md.strip():
                    entries.append({"title": f"Update scan: {src}", "authors": "-",
                                     "year": str(datetime.date.today().year), "venue": src,
                                     "url": src, "abstract": md[:600]})
            except Exception as e:
                print(f"[warn] source {src}: {e}")
    except Exception as e:
        print(f"[info] crawl4ai unavailable ({e}); skipping live crawl (graceful degradation).")
    return entries


def _parse_arxiv(markdown: str, base_url: str):
    out = []
    for m in re.finditer(r"(arXiv:\d{4}\.\d{4,5})", markdown):
        aid = m.group(1).split(":")[1]
        out.append({"title": f"ArXiv {aid}", "authors": "-",
                     "year": str(datetime.date.today().year), "venue": "arXiv",
                     "url": f"https://arxiv.org/abs/{aid}", "abstract": ""})
    return out


def append_entries(entries):
    if not os.path.exists(BRAIN):
        print(f"[error] knowledge brain not found: {BRAIN}"); return 0
    with open(BRAIN, "r", encoding="utf-8") as f:
        text = f.read()
    seen = _existing_hashes(text)
    scored = sorted(entries, key=lambda e: relevance_score(e["title"], e.get("abstract", "")), reverse=True)
    today = datetime.date.today().isoformat()
    added, lines = 0, []
    for e in scored:
        h = _hash(e["url"])
        if h in seen or not e["url"]:
            continue
        rel = relevance_score(e["title"], e.get("abstract", ""))
        if rel <= 0:
            continue
        lines.append(f"- {today} — **{e['title']}** ({e['venue']}, {e['year']}) "
                     f"[{e['url']}] relevance={rel:.2f} <!--hash:{h}-->")
        seen.add(h); added += 1
    if added:
        with open(BRAIN, "a", encoding="utf-8") as f:
            f.write(f"\n### Auto-crawl {today}\n" + "\n".join(lines) + "\n")
    print(f"[ok] appended {added} new entries to SECOND-KNOWLEDGE-BRAIN.md")
    return added


def main():
    print(f"[run] knowledge_updater for skill #164 (productivity-coach)")
    entries = fetch_entries()
    n = append_entries(entries)
    if n == 0:
        print("[info] no new entries this run (network/dedup/relevance).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
