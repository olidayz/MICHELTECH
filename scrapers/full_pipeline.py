#!/usr/bin/env python3
"""
MEME MACHINE - Full Pipeline
Scan → Score → Opportunity → Brief
"""
import sys
import json
import subprocess
from datetime import datetime

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
    return result.stdout

def main():
    print("\n" + "="*60)
    print("🚀 MEME MACHINE - FULL PIPELINE")
    print("="*60)
    print(f"\n⏰ {datetime.now().strftime('%H:%M:%S')}")
    
    # Step 1: Scan news
    print("\n📰 STEP 1: Scanning French News...")
    scan_output = run_command("python3 /home/oli/.openclaw/workspace/meme-machine/scrapers/news_rss.py 2>&1")
    
    # Extract JSON
    try:
        start = scan_output.find('{')
        if start > -1:
            news_data = json.loads(scan_output[start:])
            print(f"   ✓ {news_data.get('total_articles', 0)} articles scanned")
            print(f"   ✓ {news_data.get('political_articles', 0)} political")
    except:
        print("   ⚠️ Scan failed, using samples")
        news_data = {}
    
    # Step 2: Generate opportunities
    print("\n🎯 STEP 2: Scoring Opportunities...")
    
    # Prepare topics
    topics = news_data.get("top_political", [])[:20]
    
    if topics:
        # Save for viral engine
        with open("/tmp/scan_topics.json", "w") as f:
            json.dump({"sources": [{"type": "news", "data": {"top_political": topics}}]}, f)
        
        # Run viral engine
        viral_output = run_command("python3 /home/oli/.openclaw/workspace/meme-machine/scrapers/viral_engine.py 2>&1")
    else:
        print("   ⚠️ No topics, running demo mode")
        viral_output = run_command("python3 /home/oli/.openclaw/workspace/meme-machine/scrapers/viral_engine.py 2>&1")
    
    # Step 3: Read results
    print("\n📋 STEP 3: Generating Brief...")
    try:
        with open("/tmp/viral_opportunities.json", "r") as f:
            results = json.load(f)
    except:
        results = {"opportunities": []}
    
    # Step 4: Format output
    brief = f"""
📊 **MEME MACHINE - DAILY BRIEF**
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ {datetime.now().strftime('%H:%M')} | {len(results.get('opportunities', []))} opportunities

"""
    
    for i, opp in enumerate(results.get("opportunities", [])[:5], 1):
        brief += f"""
**{i}. {opp['topic']}**
📈 Score: {opp['virality_score']}/100
🏷️ {', '.join([p['name'] for p in opp.get('pillars', [])])}
🎭 {opp.get('humor_mechanic', 'juxtaposition')}
🎬 {opp['combos'][0]['character']} × {opp['combos'][0]['world']}
💡 {opp.get('why_viral', '')}

"""
    
    brief += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💾 Saved: /tmp/viral_opportunities.json
"""
    
    print(brief)
    
    # Save full brief
    with open("/tmp/meme_brief.txt", "w") as f:
        f.write(brief)
    
    print("\n✅ Pipeline complete!")
    return brief

if __name__ == "__main__":
    main()
