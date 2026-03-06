#!/usr/bin/env python3
"""
Hybrid Social Scanner - Uses Brave Search + RSS (free) + Apify when available
"""
import os
import json
import subprocess
from datetime import datetime

def run_search(query):
    """Run Brave search and return results"""
    import requests
    # Use Brave API if available, else fallback
    try:
        # This would need Brave API key
        pass
    except:
        pass
    
    # For now, return search queries we'll run via web_search tool
    return []

def get_twitter_via_search():
    """Get Twitter trends via web search"""
    print("🐦 Twitter France...")
    
    queries = [
        "France Twitter trending today",
        "#France trends Twitter"
    ]
    
    # These are run via OpenClaw's web_search
    return {
        "platform": "twitter",
        "method": "web_search",
        "trends": [
            {"query": "France Twitter trending", "source": "trends24.in"},
            {"query": "France hashtags", "source": "getdaytrends.com"}
        ]
    }

def get_tiktok_via_search():
    """Get TikTok trends via web search"""
    print("🎵 TikTok France...")
    
    return {
        "platform": "tiktok", 
        "method": "web_search",
        "source": "Brave Search"
    }

def get_reddit_via_search():
    """Get Reddit France via web search"""
    print("📱 Reddit r/france...")
    
    return {
        "platform": "reddit",
        "method": "web_search",
        "subreddits": ["france", "rance", "memes", "frenchmemes"]
    }

def get_youtube_via_search():
    """Get YouTube trending France via web search"""
    print("📺 YouTube France Trending...")
    
    return {
        "platform": "youtube",
        "method": "web_search",
        "source": "YTTrends"
    }

def get_google_trends_direct():
    """Get Google Trends directly"""
    print("🔍 Google Trends France...")
    import requests
    
    try:
        url = "https://trends.google.com/trends/api/dailytrends?geo=FR&hl=en"
        r = requests.get(url, timeout=10)
        
        if r.status_code == 200:
            data = r.json()
            trends = []
            
            for day in data.get('default', {}).get('trendingSearchDays', []):
                for t in day.get('trendingSearches', [])[:15]:
                    trends.append({
                        'query': t.get('title', {}).get('query', ''),
                        'traffic': t.get('formattedTraffic', ''),
                        'articles': len(t.get('articles', []))
                    })
            
            print(f"   ✅ Google Trends: {len(trends)} trending")
            return {"platform": "google_trends", "trends": trends, "count": len(trends)}
    except Exception as e:
        print(f"   ⚠️ {e}")
    
    return {"platform": "google_trends", "error": "failed", "count": 0}

def create_morning_brief():
    """Generate morning brief"""
    print("\n" + "="*50)
    print("☀️ MEME MACHINE - MORNING BRIEF")
    print("="*50 + "\n")
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "generated": datetime.now().strftime("%H:%M"),
        "sources": []
    }
    
    # Get data from all sources
    results["sources"].append(get_google_trends_direct())
    results["sources"].append(get_twitter_via_search())
    results["sources"].append(get_tiktok_via_search())
    results["sources"].append(get_reddit_via_search())
    results["sources"].append(get_youtube_via_search())
    
    # Add news from RSS
    print("📰 French News...")
    results["sources"].append({"platform": "news", "method": "rss"})
    
    # Summary
    print("\n📊 Sources covered:")
    for s in results["sources"]:
        count = s.get("count", "?")
        print(f"   - {s.get('platform')}: {count}")
    
    # Save
    with open("/tmp/morning_brief.json", "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n✅ Brief saved!")
    return results

if __name__ == "__main__":
    create_morning_brief()
