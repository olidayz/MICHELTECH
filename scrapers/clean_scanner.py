#!/usr/bin/env python3
"""
MEME MACHINE - Clean News Scanner v2
Outputs: Topic, Context, Metrics, Your Call
No spin, no framing - just signal.
"""
import json
import requests
from datetime import datetime
from collections import defaultdict
import xml.etree.ElementTree as ET

RSS_SOURCES = {
    "lemonde": "https://www.lemonde.fr/rss/une.xml",
    "france24": "https://www.france24.com/fr/rss",
    "franceinfo": "https://www.francetvinfo.fr/titres.rss",
    "20minutes": "https://www.20minutes.fr/feeds/rss-une.xml",
    "valeurs_actuelles": "https://www.valeursactuelles.com/feed/",
    "huffpost": "https://www.huffingtonpost.fr/feeds/index.xml",
    "rfi": "https://www.rfi.fr/fr/rss",
    "europe1": "https://www.europe1.fr/rss.xml",
    "ouest_france": "https://www.ouest-france.fr/rss-en-continu.xml",
}

TOPIC_KEYWORDS = {
    "economy": ["économie", "inflation", "croissance", "PIB", "chomage", "emploi", "salaire", "pouvoir d'achat", "retraite", "taxe", "impôt", "budget", "dette", "prix"],
    "security": ["sécurité", "police", "crime", "viol", "meurtre", "vol", "agression", "justice", "prison", "délinquance", "attentat", "terrorisme"],
    "immigration": ["immigration", "migrant", "réfugié", "frontière", "asile", "expulsion", "clandestin", "sans-papiers"],
    "politics": ["gouvernement", "Macron", "Premier ministre", "député", "sénateur", "élection", "parti", "LFI", "LR", "RN", "Renaissance", "Mélenchon", "Le Pen", "Bardella", "Assemblée", "49.3"],
    "culture": ["culture", "identité", "tradition", "laïcité", "religion", "woke"],
    "eu": ["UE", "Bruxelles", "européen", "directive", "souveraineté"],
    "health": ["santé", "hôpital", "médecin", "urgences"],
    "education": ["école", "éducation", "lycée", "université"],
    "housing": ["logement", "loyer", "immobilier"],
    "climate": ["climat", "écologie", "environnement", "inondation", "tempête", "crue"],
    "media": ["médias", "BFMTV", "censure", "journaliste"],
}

def fetch_rss(url):
    try:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        resp.raise_for_status()
        return resp.text
    except:
        return None

def parse_items(xml_text, source):
    items = []
    try:
        root = ET.fromstring(xml_text)
        for item in root.findall(".//item"):
            title = item.find("title")
            desc = item.find("description")
            link = item.find("link")
            if title is not None and title.text:
                items.append({
                    "title": title.text.strip(),
                    "description": (desc.text[:200].strip() if desc is not None and desc.text else ""),
                    "link": (link.text.strip() if link is not None and link.text else ""),
                    "source": source
                })
        # Try Atom entries too
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.findall(".//atom:entry", ns):
            title = entry.find("atom:title", ns)
            summary = entry.find("atom:summary", ns)
            if title is not None and title.text:
                items.append({
                    "title": title.text.strip(),
                    "description": (summary.text[:200].strip() if summary is not None and summary.text else ""),
                    "link": "",
                    "source": source
                })
    except:
        pass
    return items

def detect_topic(text):
    text_lower = text.lower()
    scores = {}
    for topic, keywords in TOPIC_KEYWORDS.items():
        count = sum(1 for kw in keywords if kw.lower() in text_lower)
        if count > 0:
            scores[topic] = count
    if scores:
        return max(scores, key=scores.get)
    return "other"

def find_trending(all_items):
    """Find stories mentioned across multiple sources"""
    # Extract key terms from titles
    from collections import Counter
    
    # Simple word frequency across all titles
    word_freq = Counter()
    for item in all_items:
        words = item["title"].lower().split()
        # Filter short words
        meaningful = [w for w in words if len(w) > 4 and w not in {"cette", "après", "avant", "entre", "selon", "leurs", "notre", "cette", "comme", "aussi", "dans", "pour", "avec", "plus", "tout", "sans", "mais", "encore"}]
        word_freq.update(set(meaningful))  # set() to count once per article
    
    # Find hot words (mentioned in 3+ articles across sources)
    hot_words = {word: count for word, count in word_freq.items() if count >= 3}
    
    return hot_words

def scan():
    print("📡 Scanning 9 French news sources...")
    
    all_items = []
    source_counts = {}
    
    for source, url in RSS_SOURCES.items():
        xml = fetch_rss(url)
        if xml:
            items = parse_items(xml, source)
            source_counts[source] = len(items)
            all_items.extend(items)
    
    print(f"📊 {len(all_items)} articles from {len(source_counts)} sources")
    
    # Find trending keywords
    hot_words = find_trending(all_items)
    
    # Group by topic
    topic_stories = defaultdict(list)
    for item in all_items:
        full_text = item["title"] + " " + item.get("description", "")
        topic = detect_topic(full_text)
        topic_stories[topic].append(item)
    
    # Sort topics by article count
    sorted_topics = sorted(topic_stories.items(), key=lambda x: -len(x[1]))
    
    # Output
    print("\n" + "=" * 60)
    print("📊 MEME MACHINE - NEWS SCAN")
    print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)
    
    # Hot words
    if hot_words:
        top_hot = sorted(hot_words.items(), key=lambda x: -x[1])[:10]
        print(f"\n🔥 HOT WORDS (across {len(source_counts)} sources):")
        for word, count in top_hot:
            print(f"   • {word} ({count} articles)")
    
    # Top stories by topic
    print(f"\n📰 TOP STORIES BY TOPIC:")
    for topic, stories in sorted_topics[:6]:
        sources = set(s["source"] for s in stories)
        print(f"\n   [{topic.upper()}] ({len(stories)} articles, {len(sources)} sources)")
        # Show top 2 headlines per topic
        seen = set()
        shown = 0
        for s in stories:
            title_short = s["title"][:80]
            if title_short not in seen and shown < 2:
                seen.add(title_short)
                print(f"   📌 {s['title'][:100]}")
                print(f"      — {s['source']}")
                shown += 1
    
    print("\n" + "=" * 60)
    
    # Save
    output = {
        "timestamp": datetime.now().isoformat(),
        "total_articles": len(all_items),
        "sources": source_counts,
        "hot_words": dict(sorted(hot_words.items(), key=lambda x: -x[1])[:20]),
        "topics": {t: len(s) for t, s in sorted_topics},
    }
    
    with open("/tmp/meme_scan.json", "w") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Saved to /tmp/meme_scan.json")
    return output

if __name__ == "__main__":
    scan()
