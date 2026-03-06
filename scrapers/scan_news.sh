#!/bin/bash
# MEME MACHINE - News RSS Scan
# Runs every 6 hours to keep up with French news

cd /home/oli/.openclaw/workspace/meme-machine/scrapers

# Run the scraper
OUTPUT=$(python3 news_rss.py 2>&1)

# Check if successful
if echo "$OUTPUT" | grep -q "total_articles"; then
    echo "✅ News scan complete"
    # Extract the JSON part and save
    echo "$OUTPUT" | grep -A1000 "^({" > /tmp/news_scan_latest.json
    echo "News scan results saved"
else
    echo "❌ News scan failed"
    echo "$OUTPUT"
fi
