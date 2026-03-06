#!/usr/bin/env python3
"""
VIRALITY ENGINE - Concept Generator
Takes political topics → generates viral content concepts
"""
import json
import random
from datetime import datetime

# ============================================
# CULTURAL HOOKS DATABASE
# ============================================
CULTURAL_HOOKS = {
    "immigration": {
        "worlds": ["GTA V", "Call of Duty", "Siege", "Battlefield"],
        "anime": ["Attack on Titan", "Vinland Saga", "86"],
        "reason": "Siege/defense = borders"
    },
    "economy": {
        "worlds": ["The Sims 4", "GTA V", "Monopoly"],
        "anime": ["Black Clover", "Spy x Family"],
        "reason": "Money struggles = relatable"
    },
    "politicians": {
        "worlds": ["Dark Souls", "GTA V", "Mario Kart"],
        "anime": ["Death Note", "One Punch Man", "Mob Psycho"],
        "reason": "Power + corruption theme"
    },
    "eu_brussels": {
        "worlds": ["Europa Universalis IV", "Crusader Kings", "Victoria 3"],
        "anime": ["Gate", "Redo of Knight"],
        "reason": "Strategy games = bureaucracy"
    },
    "media": {
        "worlds": ["The Sims 4", "Roblox"],
        "anime": ["Death Note", "Erased"],
        "reason": "Truth vs narrative"
    },
    "tradition": {
        "worlds": ["Skyrim", "Zelda TOTK"],
        "anime": ["Naruto", "Demon Slayer"],
        "reason": "Honor vs modern"
    },
    "youth": {
        "worlds": ["Fortnite", "Roblox", "Valorant", "League of Legends"],
        "anime": ["My Hero Academia", "Jujutsu Kaisen"],
        "reason": "Target demo overlap"
    },
    "rural": {
        "worlds": ["Stardew Valley", "Farming Simulator", "Minecraft"],
        "anime": ["Ghibli films", "K-On"],
        "reason": "Nature vs city"
    }
}

# ============================================
# HOOK TEMPLATES
# ============================================
HOOK_TEMPLATES = [
    "When {politician} tries to explain {topic}",
    "The {reference} of {topic}",
    "{politician} in {world} be like...",
    "What {topic} actually looks like",
    "When you realize {topic} is like {reference}",
    "{politician} {action} in {world} format",
    "The {emotion} of seeing {topic} through {world}",
    "{topic} but make it {style}",
]

# ============================================
# CONCEPT GENERATORS
# ============================================
def generate_concept(topic, angle, target_audience="general"):
    """Generate a viral concept for a topic"""
    
    # Get relevant cultural hooks
    hooks = []
    for key, data in CULTURAL_HOOKS.items():
        if key in topic.lower() or key in angle.lower():
            hooks.append(data)
    
    # Default hooks if no match
    if not hooks:
        hooks = [
            {"worlds": ["GTA V", "Mario Kart", "Fortnite"], "anime": ["One Piece", "Jujutsu Kaisen"]}
        ]
    
    hook = random.choice(hooks)
    world = random.choice(hook["worlds"])
    anime = random.choice(hook["anime"])
    
    # Generate concept parts
    concept = {
        "title": f"When {topic} meets {world}",
        "hook": f"First 3 seconds: {world} aesthetic with political setup",
        "setup": f"Show {topic} through {world} gameplay/visuals",
        "payoff": f"The absurdist political punchline",
        "world": world,
        "anime_reference": anime,
        "why_viral": f"{world} audience + political = cross-pollination"
    }
    
    return concept

def generate_3_concepts(topic, angle):
    """Generate 3 different concepts for the same topic"""
    
    concepts = []
    
    # Concept 1: Gaming focus
    concepts.append({
        "number": 1,
        "style": "Gaming",
        "title": f"Gamer take on: {topic}",
        "hook": f"Video game thumbnail aesthetic, thumbnail says '{topic}'",
        "story": "Plays like a walkthrough/pov, but the 'game' is the political situation",
        "world": "GTA V / Mario Kart / FIFA",
        "why": "Gaming audience + political = new reach"
    })
    
    # Concept 2: Anime focus
    concepts.append({
        "number": 2,
        "style": "Anime",
        "title": f"Anime take on: {topic}",
        "hook": "Anime opening credits style, dramatic music",
        "story": "Characters represent politicians, anime tropes applied to policy debate",
        "world": "Jujutsu Kaisen / Demon Slayer / One Piece",
        "why": "Anime is huge in France, political subtext"
    })
    
    # Concept 3: Meme/文化
    concepts.append({
        "number": 3,
        "style": "Meme",
        "title": f"Reddit/Twitter meme format: {topic}",
        "hook": "Screenshot of 'discussion post' or 'chart' format",
        "story": "Fake data visualization, meme format with political point",
        "world": "Meme format / Deep fried / Wholesome",
        "why": "Native to the platforms, algorithm loves it"
    })
    
    return concepts

# ============================================
# MAIN ENGINE
# ============================================
def generate_viral_concepts(topic, context=""):
    """Main entry point"""
    
    print("\n" + "="*60)
    print("🎯 VIRALITY ENGINE")
    print("="*60)
    print(f"\n📌 TOPIC: {topic}")
    if context:
        print(f"📋 CONTEXT: {context}")
    
    # Analyze topic
    angle = analyze_angle(topic)
    
    print(f"\n🎯 DETECTED ANGLE: {angle}")
    print(f"🎬 CULTURAL HOOKS MATCHED: {len(CULTURAL_HOOKS.get(angle, {}).get('worlds', []))}")
    
    # Generate concepts
    print("\n" + "="*60)
    print("🔥 GENERATING CONCEPTS...")
    print("="*60)
    
    concepts = generate_3_concepts(topic, angle)
    
    for c in concepts:
        print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONCEPT #{c['number']} — {c['style']} STYLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 TITLE: {c['title']}

🎬 THE HOOK (0-3s):
   {c['hook']}

📖 THE STORY (3-60s):
   {c['story']}

🎮 WORLD: {c['world']}

💡 WHY IT WORKS:
   {c['why']}
""")
    
    print("="*60)
    print("✅ Concepts generated!")
    return concepts

def analyze_angle(topic):
    """Detect the political angle"""
    topic_lower = topic.lower()
    
    angles = {
        "immigration": ["immigration", "migrant", "frontière", "asile"],
        "economy": ["économie", "argent", "pouvoir d'achat", "inflation", "taxe"],
        "politicians": ["macron", "gouvernement", "ministre", "député"],
        "eu_brussels": ["europe", "bruxelles", "ue", "brussels"],
        "media": ["médias", "bfmtv", "journaliste", "propagande"],
        "tradition": ["tradition", "culture", "identité", "religion"],
        "youth": ["jeunes", "école", "étudiant", "génération"],
        "rural": ["agriculture", "rural", "paysan", "village"]
    }
    
    for angle, keywords in angles.items():
        if any(kw in topic_lower for kw in keywords):
            return angle
    
    return "general"

# ============================================
# CLI
# ============================================
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        topic = "Pension reform protests"
    
    generate_viral_concepts(topic)
