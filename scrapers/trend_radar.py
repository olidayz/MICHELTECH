#!/usr/bin/env python3
"""
TREND RADAR - Auto-flag rising topics from topics_bible
Runs with scanner, flags topics that are trending
"""
import json
import requests
from datetime import datetime

# Load topics bible
TOPICS_FILE = "/home/oli/.openclaw/workspace/meme-machine/topics_bible.json"

RSS_SOURCES = {
    "lemonde": "https://www.lemonde.fr/rss/une.xml",
    "figaro": "https://www.lefigaro.fr/rss/une.xml",
    "bfmtv": "https://www.bfmtv.com/rss/une/",
    "cnews": "https://www.cnews.fr/rss/une",
    "liberation": "https://www.liberation.fr/rss/une/",
}

def fetch_rss(url):
    try:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        return resp.text
    except:
        return None

def parse_rss_items(xml_text):
    import xml.etree.ElementTree as ET
    items = []
    try:
        if "<rss" in xml_text:
            root = ET.fromstring(xml_text)
            for item in root.findall(".//item"):
                title = item.find("title")
                desc = item.find("description")
                items.append({
                    "title": title.text if title is not None else "",
                    "description": desc.text[:200] if desc is not None and desc.text else ""
                })
    except:
        pass
    return items

def check_topics(topics, all_text):
    """Check which topics are mentioned in the news"""
    found = []
    all_lower = all_text.lower()
    
    for topic in topics.get("topics", []):
        topic_name = topic.get("name", "")
        keywords = topic.get("keywords", [])
        score = topic.get("virality_score", 5)
        
        # Count keyword matches
        matches = 0
        for kw in keywords:
            if kw.lower() in all_lower:
                matches += 1
        
        if matches >= 2:  # At least 2 keywords found
            found.append({
                "topic": topic_name,
                "score": score,
                "matches": matches,
                "angles": topic.get("angles", [])[:3]  # Top 3 angles
            })
    
    # Sort by score
    found.sort(key=lambda x: (-x["score"], -x["matches"]))
    return found

def run_radar():
    print("📡 TREND RADAR - Scanning...")
    
    # Load topics
    with open(TOPICS_FILE) as f:
        topics = json.load(f)
    
    all_text = ""
    article_count = 0
    
    # Fetch all sources
    for source, url in RSS_SOURCES.items():
        xml = fetch_rss(url)
        if xml:
            items = parse_rss_items(xml)
            for item in items:
                all_text += item.get("title", "") + " " + item.get("description", "")
                article_count += 1
    
    # Check for trending topics
    trending = check_topics(topics, all_text)
    
    print(f"\n📊 Found {len(trending)} trending topics from {article_count} articles\n")
    
    # Output
    if trending:
        print("🔥 TRENDING NOW:")
        for i, t in enumerate(trending[:5], 1):
            print(f"  {i}. {t['topic']} (score: {t['score']}/10, {t['matches']} keywords)")
        
        print("\n💡 ANGLES TO USE:")
        for t in trending[:3]:
            print(f"  • {t['topic']}: {t['angles'][0] if t['angles'] else 'N/A'}")
        
        # Save to file
        output = {
            "timestamp": datetime.now().isoformat(),
            "radar": "active",
            "trending": trending[:5],
            "total_articles": article_count
        }
        
        with open("/tmp/trend_radar.json", "w") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Saved to /tmp/trend_radar.json")
    else:
        print("📭 No trending topics found")
        
        # Save empty
        output = {
            "timestamp": datetime.now().isoformat(),
            "radar": "quiet",
            "trending": [],
            "total_articles": article_count
        }
        with open("/tmp/trend_radar.json", "w") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
    
    return output

if __name__ == "__main__":
    run_radar()
