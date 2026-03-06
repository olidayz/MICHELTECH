#!/usr/bin/env python3
"""
News RSS Scraper for MEME MACHINE
Scans French news sources and extracts trending topics
"""
import feedparser
import json
from datetime import datetime
from collections import defaultdict

# French News RSS Sources
RSS_SOURCES = {
    "le_monde": "https://www.lemonde.fr/rss/une.xml",
    "le_figaro": "https://www.lefigaro.fr/rss/une.xml",
    "liberation": "https://www.liberation.fr/rss/une/",
    "bfm": "https://www.bfmtv.com/rss/une/",
    "cnews": "https://www.cnews.fr/rss/une/",
    "valeurs_actuelles": "https://www.valeursactuelles.com/rss.xml",
    "mediapart": "https://www.mediapart.fr/articlesRSS.xml",
    "le_point": "https://www.lepoint.fr/rss/une.xml",
    "lexpress": "https://www.lexpress.fr/rss/une.xml",
    "20minutes": "https://www.20minutes.fr/rss/une.xml",
}

def parse_rss_feed(source_name, url):
    """Parse a single RSS feed"""
    try:
        feed = feedparser.parse(url)
        entries = []
        
        for entry in feed.entries[:15]:  # Top 15 articles
            entries.append({
                "title": entry.get("title", ""),
                "summary": entry.get("summary", "")[:300],
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "source": source_name
            })
        
        return {"source": source_name, "entries": entries, "count": len(entries)}
    except Exception as e:
        return {"source": source_name, "error": str(e), "count": 0}

def scan_all_news():
    """Scan all RSS sources"""
    results = []
    
    print(f"[{datetime.now().isoformat()}] Scanning {len(RSS_SOURCES)} French news sources...")
    
    for source_name, url in RSS_SOURCES.items():
        result = parse_rss_feed(source_name, url)
        results.append(result)
        if "error" in result:
            print(f"  ❌ {source_name}: {result['error']}")
        else:
            print(f"  ✓ {source_name}: {result['count']} articles")
    
    return results

def extract_topics(results):
    """Extract and cluster topics from all news"""
    # Simple keyword extraction
    all_titles = []
    for source in results:
        if "entries" in source:
            for entry in source["entries"]:
                all_titles.append(entry["title"])
    
    # Common French political keywords to filter
    keywords = [
        "Macron", "Le Pen", "Mélenchon", "Attal", "Bayou", "Retailleau",
        "gouvernement", "parlement", "élections", "réforme", "budget",
        "immigration", "sécurité", "économie", "climat", "retraite",
        "Union européenne", "UE", "Russie", "Ukraine", "Gaza",
        "LR", "Renaissance", "LFI", "RN", "PS", "Les Républicains"
    ]
    
    political_articles = []
    for source in results:
        if "entries" in source:
            for entry in source["entries"]:
                title_lower = entry["title"].lower()
                if any(kw.lower() in title_lower for kw in keywords):
                    political_articles.append(entry)
    
    return {
        "total_articles": sum(r.get("count", 0) for r in results),
        "political_articles": len(political_articles),
        "timestamp": datetime.now().isoformat(),
        "sources_scanned": len(RSS_SOURCES),
        "top_political": political_articles[:20]
    }

if __name__ == "__main__":
    results = scan_all_news()
    topics = extract_topics(results)
    
    print(f"\n📊 Summary:")
    print(f"   Total articles: {topics['total_articles']}")
    print(f"   Political articles: {topics['political_articles']}")
    
    # Output JSON for OpenClaw
    print("\n📄 JSON Output:")
    print(json.dumps(topics, ensure_ascii=False, indent=2))
