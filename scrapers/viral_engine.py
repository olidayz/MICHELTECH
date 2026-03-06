#!/usr/bin/env python3
"""
MEME MACHINE - Viral Opportunity Engine
Takes scanned topics → scores for virality potential → outputs ranked opportunities
"""
import json
import os
from datetime import datetime
from collections import defaultdict

# Load character bible
CHARACTER_BIBLE_PATH = "/home/oli/.openclaw/workspace/meme-machine/character_bible.json"

def load_characters():
    """Load character bible from file"""
    if os.path.exists(CHARACTER_BIBLE_PATH):
        with open(CHARACTER_BIBLE_PATH, "r") as f:
            return json.load(f)
    return {}

CHARACTERS = load_characters()

# ============================================
# EDITORIAL PILLARS (from spec)
# ============================================
PILLARS = {
    "souverainete": {
        "name": "Souveraineté",
        "position": "France should control its own destiny, not Brussels",
        "emotions": ["Pride", "Frustration"],
        "keywords": ["UE", "Europe", "Bruxelles", "immigration", "frontières", "indépendance"]
    },
    "anti-establishment": {
        "name": "Anti-Establishment", 
        "position": "The political class is disconnected from real people",
        "emotions": ["Mockery", "Anger"],
        "keywords": ["Macron", "gouvernement", "députés", "politique", "élite", "Paris"]
    },
    "cultural": {
        "name": "Identité Culturelle",
        "position": "French culture is worth preserving",
        "emotions": ["Nostalgia", "Defiance"],
        "keywords": ["France", "français", "tradition", "langue"]
    },
    "economie": {
        "name": "Économie Populiste",
        "position": "The system is rigged against working/middle class",
        "emotions": ["Resentment", "Solidarity"],
        "keywords": ["pouvoir d'achat", "inflation", "retraite", "salaire", "chômeurs"]
    },
    "media": {
        "name": "Critique des Médias",
        "position": "Legacy media frames narratives, not reports truth",
        "emotions": ["Skepticism", "Humor"],
        "keywords": ["BFMTV", "Le Monde", "médias", "journalistes", "propagande"]
    }
}

# ============================================
# HUMOR MECHANICS (from spec)
# ============================================
HUMOR_MECHANICS = {
    "juxtaposition": {
        "name": "Juxtaposition",
        "description": "Serious topic + unserious context",
        "weight": 1.0,
        "examples": ["Politician in Animal Crossing", "EU regulation as Minecraft server admin"]
    },
    "recognition": {
        "name": "Recognition", 
        "description": "Specific truth audience feels but can't articulate",
        "weight": 1.2,  # Highest weight - this drives shares
        "examples": ["Specific observation about everyday life", "Things no one says but everyone thinks"]
    },
    "escalation": {
        "name": "Escalation",
        "description": "Starts normal, gets progressively more absurd",
        "weight": 0.9,
        "examples": ["Each beat raises stakes", "3+ beats minimum"]
    },
    "deflation": {
        "name": "Deflation",
        "description": "Build up as grand, then puncture",
        "weight": 0.9,
        "examples": ["Politician speech → mundane reality"]
    }
}

# ============================================
# WORLD LIBRARY (to be expanded)  
# ============================================
WORLDS = {
    # === GAMING ===
    "animal_crossing": {
        "name": "Animal Crossing",
        "category": "Gaming",
        "aesthetic": "Wholesome, pastel, cute",
        "tension": "Dark undertones - villagers have existential crises",
        "format_fit": ["daily life", "conversation", "confession"],
        "french_audience": "Casual, families, nostalgic adults"
    },
    "gta": {
        "name": "GTA V",
        "category": "Gaming",
        "aesthetic": "Open world, satirical, crime",
        "tension": "Heists, chaos, satire of American life",
        "format_fit": ["heist", "rampage", "satire", "chaos"],
        "french_audience": "Young men 18-35, gaming culture"
    },
    "dark_souls": {
        "name": "Dark Souls",
        "category": "Gaming",
        "aesthetic": "Punishing, dark fantasy, difficult",
        "tension": "Endless suffering, impossible odds",
        "format_fit": ["boss fight", "death", "tutorial", "punishing difficulty"],
        "french_audience": "Hardcore gamers, dark fantasy fans"
    },
    "mario_kart": {
        "name": "Mario Kart",
        "category": "Gaming",
        "aesthetic": "Competitive, colorful, chaotic",
        "tension": "Win at all costs, betrayal",
        "format_fit": ["race", "blue shell surprise", "betrayal", " comeback"],
        "french_audience": "Everyone, casual gaming, parties"
    },
    "minecraft": {
        "name": "Minecraft",
        "category": "Gaming",
        "aesthetic": "Blocky, creative, infinite",
        "tension": "Building vs destruction, survival",
        "format_fit": ["building", "creeper explosion", "mining", "redstone"],
        "french_audience": "Huge in France, all ages"
    },
    "sims": {
        "name": "The Sims 4",
        "category": "Gaming",
        "aesthetic": "Domestic, relatable, absurdist",
        "tension": "Life sims go wrong, AI behavior",
        "format_fit": ["daily life", "relationship", "career", "build house"],
        "french_audience": "Casual gamers, especially women"
    },
    "fortnite": {
        "name": "Fortnite",
        "category": "Gaming",
        "aesthetic": "Battle royale, colorful, mainstream",
        "tension": "Last one standing, builds, battles",
        "format_fit": ["battle", "victory dance", "building", "skins"],
        "french_audience": "Gen Z, huge in France"
    },
    "zelda": {
        "name": "Zelda: TOTK",
        "category": "Gaming",
        "aesthetic": "Epic fantasy, adventure, nostalgic",
        "tension": "Save the princess, epic quest",
        "format_fit": ["quest", "dungeon", "boss", "glitching"],
        "french_audience": "Nostalgic adults, gamers"
    },
    "fifa_fc25": {
        "name": "FC 25 (FIFA)",
        "category": "Gaming",
        "aesthetic": "Sports, realistic, competitive",
        "tension": "Win the match, rivalry",
        "format_fit": ["match", "goal", "training", "Ultimate Team"],
        "french_audience": "Huge, especially Ligue 1 fans"
    },
    "roblox": {
        "name": "Roblox",
        "category": "Gaming",
        "aesthetic": "Kids, chaotic, meme-friendly",
        "tension": "Anything can happen",
        "format_fit": ["game", "avatar", "challenge", "obby"],
        "french_audience": "Kids, young teens"
    },
    "genshin": {
        "name": "Genshin Impact",
        "category": "Gaming",
        "aesthetic": "Anime, gacha, fantasy",
        "tension": "Wish for characters, explore",
        "format_fit": ["quest", "gacha", "exploration", "waifu"],
        "french_audience": "Anime fans, mobile gamers"
    },
    "call_of_duty": {
        "name": "Call of Duty",
        "category": "Gaming",
        "aesthetic": "Military, realistic, action",
        "tension": "Combat, warfare",
        "format_fit": ["shooter", "mission", "killstreak", "camper"],
        "french_audience": "Hardcore FPS players"
    },
    "pokemon": {
        "name": "Pokémon",
        "category": "Gaming",
        "aesthetic": "Cute, collectible, nostalgic",
        "tension": "Gotta catch 'em all",
        "format_fit": ["battle", "collection", "evolution", "shiny"],
        "french_audience": "Nostalgic 25-40, kids"
    },
    "mario_odyssey": {
        "name": "Super Mario Odyssey",
        "category": "Gaming",
        "aesthetic": "Colorful, whimsical, travel",
        "tension": "Save Princess Peach",
        "format_fit": ["travel", "transformation", "boss", "collect coins"],
        "french_audience": "Casual, families"
    },
    "elder_scrolls": {
        "name": "Elder Scrolls (Skyrim)",
        "category": "Gaming",
        "aesthetic": "Epic fantasy, open world, dragons",
        "tension": "Dragonborn, epic quests",
        "format_fit": ["quest", "dragon", "magic", "modding"],
        "french_audience": "RPG fans, nostalgic"
    },
    "league_of_legends": {
        "name": "League of Legends",
        "category": "Gaming",
        "aesthetic": "MOBA, competitive, esports",
        "tension": "Ranked, toxicity, esports",
        "format_fit": ["ranked game", "feed", "throw", "nerf", "esports"],
        "french_audience": "Huge esports following"
    },
    "valorant": {
        "name": "Valorant",
        "category": "Gaming",
        "aesthetic": "Tactical FPS, neon, competitive",
        "tension": "Ranked, abilities, clutch",
        "format_fit": ["clutch", "smurf", "agent", "ranked"],
        "french_audience": "Young FPS players"
    },
    "mortal_kombat": {
        "name": "Mortal Kombat",
        "category": "Gaming",
        "aesthetic": "Violent, brutal, gory",
        "tension": "Fatalities, fighting",
        "format_fit": ["fatality", "fight", "brutal", "x-ray"],
        "french_audience": "Fighting game fans"
    },
    
    # === ANIME ===
    "one_piece": {
        "name": "One Piece",
        "category": "Anime",
        "aesthetic": "Pirates, adventure, emotional",
        "tension": "Pirate crews, treasure, nakama",
        "format_fit": ["pirate crew", "fight", "emotional scene", "gear 5"],
        "french_audience": "Massive in France, all ages"
    },
    "jujutsu_kaisen": {
        "name": "Jujutsu Kaisen",
        "category": "Anime",
        "aesthetic": "Dark anime, action, curses",
        "tension": "Curses, exorcism, Gojo",
        "format_fit": ["domain expansion", "cursed energy", "Gojo", "sukuna"],
        "french_audience": "Young anime fans"
    },
    "demon_slayer": {
        "name": "Demon Slayer",
        "category": "Anime",
        "aesthetic": "Beautiful, emotional, action",
        "tension": "Demons, breathing techniques, Tanjiro",
        "format_fit": [" Nichirin", "breathing", "muzan", " Nezuko"],
        "french_audience": "Huge mainstream appeal"
    },
    "naruto": {
        "name": "Naruto",
        "category": "Anime",
        "aesthetic": "Nostalgic, ninja, emotional",
        "tension": "Ninjas, war, peace",
        "format_fit": ["rasengan", "sharingan", "war", " fillers"],
        "french_audience": "Nostalgic 25-35"
    },
    "dragon_ball": {
        "name": "Dragon Ball",
        "category": "Anime",
        "aesthetic": "Iconic, power levels, transformation",
        "tension": "Power levels, transformation, fight",
        "format_fit": ["transform", "kamehameha", "power level", "Goku"],
        "french_audience": "Universally known"
    },
    "attack_on_titan": {
        "name": "Attack on Titan",
        "category": "Anime",
        "aesthetic": "Dark, dystopian, shocking",
        "tension": "Titans, walls, freedom",
        "format_fit": ["titan transformation", "rumbling", "walls", "Eren"],
        "french_audience": "Hardcore anime fans"
    },
    "death_note": {
        "name": "Death Note",
        "category": "Anime",
        "aesthetic": "Psychological, cat-and-mouse",
        "tension": "Mind games, morality, L vs Light",
        "format_fit": ["writing names", "L", " Kira", "trap"],
        "french_audience": "Intellectual anime fans"
    },
    "sailor_moon": {
        "name": "Sailor Moon",
        "category": "Anime",
        "aesthetic": "Magical girl, pastel, nostalgic",
        "tension": "Save the world, love",
        "format_fit": ["transformation", "attack", "healing", "crystals"],
        "french_audience": "Nostalgic women 25-40"
    },
    
    # === SPORTS ===
    "football_ligue1": {
        "name": "Ligue 1 Football",
        "category": "Sports",
        "aesthetic": "Stadium, passion, rivalry",
        "tension": "Matches, transfers, drama",
        "format_fit": ["goal", "celebration", "derby", "transfer"],
        "french_audience": "Massive, all demographics"
    },
    "psg": {
        "name": "PSG",
        "category": "Sports",
        "aesthetic": "Luxury, stars, Qatar",
        "tension": "Champions League, Mbappé, money",
        "format_fit": ["star", "champions league", "money", "Messi"],
        "french_audience": "Huge, love/hate relationship"
    },
    "om": {
        "name": "Olympique de Marseille",
        "category": "Sports",
        "aesthetic": "Passion, Mediterranean, working class",
        "tension": "Victory, Velodrome, passion",
        "format_fit": ["Velodrome", "goal", "Classico", "south"],
        "french_audience": "Cult following"
    },
    "nba": {
        "name": "NBA Basketball",
        "category": "Sports",
        "aesthetic": "American, stars, entertainment",
        "tension": "Games, dunks, drama",
        "format_fit": ["dunk", "game winner", "trade", "LeBron"],
        "french_audience": "Growing, especially youth"
    },
    
    # === FRENCH CULTURE ===
    "marseillais": {
        "name": "Les Marseillais",
        "category": "Reality TV",
        "aesthetic": "Drama, Mediterranean, chaotic",
        "tension": "Fights, relationships, vacation",
        "format_fit": ["fight", "drama", "vacation", "couple"],
        "french_audience": "Young women 15-25"
    },
    "koh_lanta": {
        "name": "Koh-Lanta",
        "category": "Reality TV",
        "aesthetic": "Adventure, survival, strategy",
        "tension": "Elimination, strategies, betrayal",
        "format_fit": ["island", "immunity", "vote", "adventure"],
        "french_audience": "Massive, all ages"
    },
    "the_voice": {
        "name": "The Voice",
        "category": "Reality TV",
        "aesthetic": "Talents, emotions, competition",
        "tension": "Blind audition, battle, finale",
        "format_fit": ["singing", "coach", "battle", "stage"],
        "french_audience": "Mainstream family"
    },
    
    # === FRENCH RAP ===
    "booba": {
        "name": "Booba",
        "category": "Music",
        "aesthetic": "Luxury, gangster, iconic",
        "tension": "Beef, success, legacy",
        "format_fit": ["DUC", "Lunar", "cell", "pistolet"],
        "french_audience": "Huge, all ages"
    },
    "ninho": {
        "name": "Ninho",
        "category": "Music",
        "aesthetic": "Drill, modern, success",
        "tension": "G drill, hits, lifestyle",
        "format_fit": ["drill", "Jefe", "musto", "lifestyle"],
        "french_audience": "Gen Z"
    },
    "sdm": {
        "name": "SDM",
        "category": "Music",
        "aesthetic": "Drill, chaotic, energetic",
        "tension": "Freestyle, features, energy",
        "format_fit": [" freestyle", "drill", "chaos", "energy"],
        "french_audience": "Young"
    },
    "gTA": {
        "name": "GTA (French Rap)",
        "category": "Music",
        "aesthetic": "Drill, street, Paris",
        "tension": "Drill, Paris, street",
        "format_fit": ["drill", "Paris", "13", "freestyle"],
        "french_audience": "Drill fans"
    },
    
    # === STREAMING ===
    "twitch": {
        "name": "Twitch Streaming",
        "category": "Streaming",
        "aesthetic": "Live, interactive, chaotic",
        "tension": "Live reactions, chat, drama",
        "format_fit": ["stream", "chat", "raid", "drama"],
        "french_audience": "Huge, gamers & viewers"
    },
    "youtube_fr": {
        "name": "YouTube France",
        "category": "Streaming",
        "aesthetic": "Vlogs, drama, commentary",
        "tension": "Drama, algorithm, drama",
        "format_fit": ["video", "drama", "collab", "algorithm"],
        "french_audience": "Everyone"
    },
    
    # === MEME CULTURE ===
    "d进行全面": {
        "name": "French Meme Pages",
        "category": "Memes",
        "aesthetic": "Relatable, absurd, niche",
        "tension": "Trends, reposts, neurchi",
        "format_fit": ["relatable", " absur", "neurchi", "repost"],
        "french_audience": "Young internet users"
    },
    " shit": {
        "name": "r/France",
        "category": "Reddit",
        "aesthetic": "Discussion, memes, salty",
        "tension": "Debates, memes, national identity",
        "format_fit": ["thread", "comment", "débat", "mème"],
        "french_audience": "Redditors 18-35"
    },
    
    # === CINEMA ===
    "trans_formers": {
        "name": "Transformers",
        "category": "Cinema",
        "aesthetic": "Action, explosions, Michael Bay",
        "tension": "Robots fighting, explosions",
        "format_fit": ["robots", "explosion", " Megan", " Bayhem"],
        "french_audience": "Action fans"
    },
    "avengers": {
        "name": "Avengers",
        "category": "Cinema",
        "aesthetic": "Superhero, action, franchise",
        "tension": "Saving the world, team-ups",
        "format_fit": ["superhero", "team up", "action", " endgame"],
        "french_audience": "Mainstream"
    },
    
    # === TV SHOWS ===
    "breaking_bad": {
        "name": "Breaking Bad",
        "category": "TV Shows",
        "aesthetic": "Dark, intense, crime",
        "tension": "Meth, power, morality",
        "format_fit": ["chemistry", " Heisenberg", "cook", "break bad"],
        "french_audience": "Prestige TV fans"
    },
    "game_of_thrones": {
        "name": "Game of Thrones",
        "category": "TV Shows",
        "aesthetic": "Fantasy, political, shocking",
        "tension": "Thrones, dragons, betrayal",
        "format_fit": ["throne", "dragon", "betrayal", "winter"],
        "french_audience": "Massive, was cultural event"
    },
    "house_dragon": {
        "name": "House of the Dragon",
        "category": "TV Shows",
        "aesthetic": "Fantasy, Targaryen, dragons",
        "tension": "Succession, civil war, dragons",
        "format_fit": ["dragon", "Targaryen", "succession", "war"],
        "french_audience": "Fantasy fans"
    },
    "squid_game": {
        "name": "Squid Game",
        "category": "TV Shows",
        "aesthetic": "Korean, deadly games, social commentary",
        "tension": "Deadly games, survival, money",
        "format_fit": ["game", "red light", "soldier", "mask"],
        "french_audience": "Mainstream"
    },
    
    # === YOUTUBE / INFLUENCERS ===
    "squeezie": {
        "name": "Squeezie",
        "category": "Influencer",
        "aesthetic": "Gaming YouTuber, funny, relatable",
        "tension": "Gaming, commentary, drama",
        "format_fit": ["gaming", "video", " livestream", "collab"],
        "french_audience": "Young, gamers"
    },
    "mcfly": {
        "name": "McFly & Carlito",
        "category": "Influencer",
        "aesthetic": "Comedy, sketches, wholesome",
        "tension": "Funny videos, chemistry",
        "format_fit": ["sketch", "funny", "wholesome", "drôle"],
        "french_audience": "Young, families"
    },
    "norman": {
        "name": "Norman (Norman Thavaud)",
        "category": "Influencer",
        "aesthetic": "Comedy, cringe, relatable",
        "tension": "Videos, cringe, taboo",
        "format_fit": ["comedy", "cringe", "taboo", "rentre"],
        "french_audience": "Young adults"
    },
    
    # === AESTHETICS / VIRAL TRENDS ===
    "barbie": {
        "name": "Barbie",
        "category": "Movie/Aesthetic",
        "aesthetic": "Pink, meta, pink saturated",
        "tension": "World tour, Ken, existential",
        "format_fit": ["pink", "Ken", "dreamhouse", "meta"],
        "french_audience": "Everyone, pop culture"
    },
    "addams_family": {
        "name": "Addams Family",
        "category": "Movie/Aesthetic",
        "aesthetic": "Gothic, dark comedy, spooky",
        "tension": "Family, creepy, funny",
        "format_fit": ["creepy", "family", "Thing", "Gomez"],
        "french_audience": "Nostalgic families"
    },
    "wednesday": {
        "name": "Wednesday Addams",
        "category": "TV/Aesthetic",
        "aesthetic": "Gothic, dark academia, mysterious",
        "tension": "Outcast, psychic, Nevermore Academy",
        "format_fit": ["dance", "mysterious", "school", "gothic"],
        "french_audience": "Teens, young adults, goth fans"
    },
    
    # === VIRAL MEME CULTURE 2024-2025 ===
    "skibidi_toilet": {
        "name": "Skibidi Toilet",
        "category": "Viral",
        "aesthetic": "Absurd, surreal, Gen Alpha",
        "tension": "Heads in toilets, camera heads, war",
        "format_fit": ["skibidi", "toilet", "camera", "surreal"],
        "french_audience": "Gen Alpha, kids"
    },
    "brainrot": {
        "name": "Brainrot Culture",
        "category": "Viral",
        "aesthetic": "Chaotic, absurd, Gen Z/Alpha",
        "tension": "Nonsensical humor, sigma, gyatt",
        "format_fit": ["sigma", "gyatt", "skibidi", "Ohio"],
        "french_audience": "Gen Z, Gen Alpha"
    },
    "sigma_grindset": {
        "name": "Sigma Grindset",
        "category": "Viral",
        "aesthetic": "Lone wolf, successful, stoic",
        "tension": "Alpha vs Sigma, hustle culture",
        "format_fit": ["grind", "sigma", "lone wolf", "success"],
        "french_audience": "Young men, meme enthusiasts"
    },
    "grimace_shake": {
        "name": "Grimace Shake",
        "category": "Viral",
        "aesthetic": "Purple, McDonald's, cursed",
        "tension": "Drinking, dying, chaotic",
        "format_fit": ["purple", "shake", "McDonald's", "cursed"],
        "french_audience": "Gen Z, meme culture"
    },
    "rizz": {
        "name": "Rizz Culture",
        "category": "Viral",
        "aesthetic": "Charisma, game, confidence",
        "tension": "W rizz, L rizz, Kai Cenat",
        "format_fit": ["rizz", "game", "charisma", "flirting"],
        "french_audience": "Gen Z, stream watchers"
    },
    "kai_cenat": {
        "name": "Kai Cenat",
        "category": "Streamer/Influencer",
        "aesthetic": "Chaotic, funny, high energy",
        "tension": "Reacting, gaming, 7 days",
        "format_fit": ["react", "gaming", "chaos", "collab"],
        "french_audience": "Gen Z, international"
    },
    "ishowspeed": {
        "name": "IShowSpeed",
        "category": "Streamer/Influencer",
        "aesthetic": "Hyperactive, chaotic, global",
        "tension": "China travels, Ronaldo, screaming",
        "format_fit": ["travel", "reaction", "Ronaldo", "chaos"],
        "french_audience": "Gen Z, global audience"
    },
    
    # === MORE ANIME (Current/Seasonal 2024-2025) ===
    "solo_leveling": {
        "name": "Solo Leveling",
        "category": "Anime",
        "aesthetic": "Dark fantasy, leveling, shadow army",
        "tension": "Weakest to strongest, Sung Jinwoo",
        "format_fit": ["level up", "shadow", "dungeon", "monarch"],
        "french_audience": "Huge mainstream appeal, all ages"
    },
    "sakamoto_days": {
        "name": "Sakamoto Days",
        "category": "Anime",
        "aesthetic": "Action comedy, assassins, family",
        "tension": "Retired hitman, protecting family",
        "format_fit": ["assassin", "convenience store", "fight", "family"],
        "french_audience": "Action fans, shonen lovers"
    },
    "dandadan": {
        "name": "Dandadan",
        "category": "Anime",
        "aesthetic": "Supernatural, chaotic, emotional",
        "tension": "Ghosts vs aliens, Okarun, Momo",
        "format_fit": ["ghosts", "aliens", "transformation", "chaos"],
        "french_audience": "Anime fans, Gen Z"
    },
    "frieren": {
        "name": "Frieren: Beyond Journey's End",
        "category": "Anime",
        "aesthetic": "Whimsical, melancholic, fantasy",
        "tension": "Elf lifespan, grief, journey continues",
        "format_fit": ["magic", "journey", "emotional", "elf"],
        "french_audience": "Fantasy fans, emotional stories"
    },
    "chainsaw_man": {
        "name": "Chainsaw Man",
        "category": "Anime",
        "aesthetic": "Dark, gory, unhinged",
        "tension": "Devil hunter, Denji, Makima",
        "format_fit": ["devils", "chainsaw", "gore", "unhinged"],
        "french_audience": "Dark anime fans, Gen Z"
    },
    "spy_x_family": {
        "name": "Spy x Family",
        "category": "Anime",
        "aesthetic": "Wholesome, spy comedy, family",
        "tension": "Spy dad, assassin mom, psychic kid",
        "format_fit": ["spy", "family", "Anya", "wholesome"],
        "french_audience": "Mainstream, families, all ages"
    },
    "my_hero_academia": {
        "name": "My Hero Academia",
        "category": "Anime",
        "aesthetic": "Superhero shonen, action",
        "tension": "Quirks, UA, hero vs villain",
        "format_fit": ["quirks", "hero", "villain", "Deku"],
        "french_audience": "Shonen fans, teens"
    },
    "haikyuu": {
        "name": "Haikyuu!!",
        "category": "Anime",
        "aesthetic": "Sports, volleyball, teamwork",
        "tension": "Underdog, Karasuno, spike",
        "format_fit": ["volleyball", "spike", "team", "match"],
        "french_audience": "Sports fans, wholesome"
    },
    "vinland_saga": {
        "name": "Vinland Saga",
        "category": "Anime",
        "aesthetic": "Vikings, historical, philosophical",
        "tension": "War, revenge, pacifism, Thorfinn",
        "format_fit": ["vikings", "war", "philosophy", "growing"],
        "french_audience": "Mature anime fans, history"
    },
    "blue_lock": {
        "name": "Blue Lock",
        "category": "Anime",
        "aesthetic": "Soccer, ego, competitive",
        "tension": "Survival game, best striker, ego",
        "format_fit": ["soccer", "ego", "competition", "goal"],
        "french_audience": "Sports fans, competitive"
    },
    "oshinoko": {
        "name": "Oshi no Ko",
        "category": "Anime",
        "aesthetic": "Idol industry, dark, mystery",
        "tension": "Reincarnation, idol secrets, revenge",
        "format_fit": ["idol", "stage", "reincarnation", "mystery"],
        "french_audience": "Anime fans, idol culture"
    },
    
    # === TWITCH/STREAMING TRENDS ===
    "just_chatting": {
        "name": "Just Chatting",
        "category": "Streaming",
        "aesthetic": "Casual, conversational, variety",
        "tension": "Reacting, talking, community",
        "format_fit": ["react", "chat", "variety", "podcast"],
        "french_audience": "Huge category, all demographics"
    },
    "geoguessr": {
        "name": "GeoGuessr",
        "category": "Streaming",
        "aesthetic": "Geography, guessing, educational",
        "tension": "Pinpoint location, clues, skill",
        "format_fit": ["guess", "world", "location", "flags"],
        "french_audience": "Strategy fans, educational"
    },
    "reaction_streams": {
        "name": "Reaction Streams",
        "category": "Streaming",
        "aesthetic": "Reacting, commentary, shared experience",
        "tension": "First time watching, overreaction",
        "format_fit": ["react", "first time", "shock", "laugh"],
        "french_audience": "Entertainment seekers"
    },
    "asmr": {
        "name": "ASMR",
        "category": "Streaming",
        "aesthetic": "Relaxing, tingles, whispering",
        "tension": "Calm, sleep aid, triggers",
        "format_fit": ["whisper", "triggers", "relax", "sleep"],
        "french_audience": "Sleep help, relaxation"
    },
    "vtubers": {
        "name": "VTubers",
        "category": "Streaming",
        "aesthetic": "Virtual avatar, anime, interactive",
        "tension": "Avatar vs real, character, community",
        "format_fit": ["avatar", "virtual", "anime", "character"],
        "french_audience": "Anime fans, Japanese culture"
    },
    "mukbang": {
        "name": "Mukbang",
        "category": "Streaming",
        "aesthetic": "Eating, food, ASMR",
        "tension": "Massive food, chewing sounds",
        "format_fit": ["eating", "food", "chewing", "massive"],
        "french_audience": "Food lovers, curious"
    },
    "subathon": {
        "name": "Subathon",
        "category": "Streaming",
        "aesthetic": "Marathon, endurance, community",
        "tension": "Days without sleep, timer extends",
        "format_fit": ["marathon", "timer", "sleep", "record"],
        "french_audience": "Dedicated fans, community"
    },
    "vtuber_fr": {
        "name": "French VTubers",
        "category": "Streaming",
        "aesthetic": "Virtual avatar, French culture, anime",
        "tension": "Character lore, French jokes",
        "format_fit": ["virtual", "anime", "French", "character"],
        "french_audience": "French anime community"
    },
    
    # === FRENCH REALITY TV ===
    "star_academy": {
        "name": "Star Academy",
        "category": "Reality TV",
        "aesthetic": "Singing competition, academy, emotional",
        "tension": "Singing, eliminations, academy life",
        "format_fit": ["singing", "elimination", "stage", "emotion"],
        "french_audience": "Massive mainstream, TF1"
    },
    "lamour_dans_le_pre": {
        "name": "L'Amour est dans le pré",
        "category": "Reality TV",
        "aesthetic": "Farmers, countryside, romance",
        "tension": "Country love, letters, speed dating",
        "format_fit": ["farmer", "countryside", "love", "speed date"],
        "french_audience": "M6 audience, rural France"
    },
    "marie_premier_regard": {
        "name": "Mariés au premier regard",
        "category": "Reality TV",
        "aesthetic": "Married at first sight, science",
        "tension": "Strangers married, will it work?",
        "format_fit": ["wedding", "strangers", "science", "drama"],
        "french_audience": "M6 viewers, relationship drama"
    },
    "pekin_express": {
        "name": "Pékin Express",
        "category": "Reality TV",
        "aesthetic": "Adventure race, hitchhiking, exotic",
        "tension": "Race, no money, challenges",
        "format_fit": ["race", "hitchhike", "exotic", "challenge"],
        "french_audience": "Adventure lovers, travel"
    },
    "danse_avec_les_stars": {
        "name": "Danse avec les Stars",
        "category": "Reality TV",
        "aesthetic": "Dancing, celebrities, sequins",
        "tension": "Learning to dance, competition",
        "format_fit": ["dance", "celebrity", "competition", "sequins"],
        "french_audience": "TF1 mainstream, families"
    },
    "les_cinquante": {
        "name": "Les Cinquante",
        "category": "Reality TV",
        "aesthetic": "Survival, strategy, elimination",
        "tension": "Island survival, alliances, voting",
        "format_fit": ["island", "survival", "vote", "alliance"],
        "french_audience": "W9 audience, reality fans"
    },
    "les_apprentis_aventuriers": {
        "name": "Les Apprentis Aventuriers",
        "category": "Reality TV",
        "aesthetic": "Young adventurers, jungle, drama",
        "tension": "Young people, adventure, conflicts",
        "format_fit": ["jungle", "young", "drama", "adventure"],
        "french_audience": "Young adults, reality fans"
    },
    
    # === FRENCH RAP (More Artists) ===
    "jul": {
        "name": "Jul",
        "category": "Music",
        "aesthetic": "Marseille, prolific, cult following",
        "tension": "Dackor, Marseille, massive output",
        "format_fit": ["Marseille", "dackor", "C'est pas des lol", "prolific"],
        "french_audience": "Massive, working class, Marseille"
    },
    "gazo": {
        "name": "Gazo",
        "category": "Music",
        "aesthetic": "Drill, masked, mysterious",
        "tension": "Drill FR, masked persona, hits",
        "format_fit": ["drill", "mask", "mysterious", "Drippy"],
        "french_audience": "Drill fans, Gen Z"
    },
    "sch": {
        "name": "SCH",
        "category": "Music",
        "aesthetic": "Luxury, Marseille, poetic",
        "tension": "A7, street stories, deep lyrics",
        "format_fit": ["Marseille", "A7", "luxury", "poetic"],
        "french_audience": "Rap connoisseurs, South"
    },
    "plk": {
        "name": "PLK",
        "category": "Music",
        "aesthetic": "Melodic, introspective, Polak",
        "tension": "Polish roots, melodies, success",
        "format_fit": ["Polak", "melodic", "introspective", "hits"],
        "french_audience": "Young rap fans"
    },
    "damso": {
        "name": "Damso",
        "category": "Music",
        "aesthetic": "Poetic, dark, Belgian",
        "tension": "Deep lyrics, controversy, poetry",
        "format_fit": ["poetry", "dark", "Belgian", "controversy"],
        "french_audience": "Intellectual rap fans"
    },
    "tiakola": {
        "name": "Tiakola",
        "category": "Music",
        "aesthetic": "Afrobeat, dance, melodies",
        "tension": "Afro-trap, hits, dance vibes",
        "format_fit": ["afrobeat", "dance", "melodies", "vibe"],
        "french_audience": "Party, dance lovers"
    },
    "werenoi": {
        "name": "WeRenoi",
        "category": "Music",
        "aesthetic": "Drill, street, raw",
        "tension": "Street stories, drill beats",
        "format_fit": ["drill", "street", "raw", "authentic"],
        "french_audience": "Drill fans, authentic rap"
    },
    "gims": {
        "name": "Gims",
        "category": "Music",
        "aesthetic": "Pop rap, mainstream, Congolese",
        "tension": "Massive hits, pop crossover",
        "format_fit": ["pop", "mainstream", "hits", "variety"],
        "french_audience": "Mainstream, all ages"
    },
    "nekfeu": {
        "name": "Nekfeu",
        "category": "Music",
        "aesthetic": "Poetic, jazz rap, introspective",
        "tension": "1995 crew, movies, deep lyrics",
        "format_fit": ["poetry", "jazz", "introspective", "1995"],
        "french_audience": "Old school fans, thinkers"
    },
    "orelsan": {
        "name": "Orelsan",
        "category": "Music",
        "aesthetic": "Storytelling, humor, Normandy",
        "tension": "Clever wordplay, relatable stories",
        "format_fit": ["story", "humor", "wordplay", "relatable"],
        "french_audience": "Massive mainstream appeal"
    },
    
    # === FRENCH REGIONS/CULTURE ===
    "bretagne": {
        "name": "Bretagne",
        "category": "French Culture",
        "aesthetic": "Celtic, sea, traditions",
        "tension": "Breton identity, galette, fest-noz",
        "format_fit": ["galette", "celtic", "sea", "tradition"],
        "french_audience": "Bretons, regional pride"
    },
    "provence": {
        "name": "Provence",
        "category": "French Culture",
        "aesthetic": "Lavender, sun, Mediterranean",
        "tension": "Pastis, pétanque, slow life",
        "format_fit": ["lavender", "pastis", "sun", "Mediterranean"],
        "french_audience": "South lovers, vacation"
    },
    "alsace": {
        "name": "Alsace",
        "category": "French Culture",
        "aesthetic": "Christmas markets, Germany influence",
        "tension": "Choucroute, bilingual, identity",
        "format_fit": ["Christmas", "choucroute", "bilingual", "identity"],
        "french_audience": "Alsatians, Christmas lovers"
    },
    "lyon": {
        "name": "Lyon",
        "category": "French Culture",
        "aesthetic": "Gastronomy, traboules, lights",
        "tension": "Bouchons, cuisine, Festival of Lights",
        "format_fit": ["food", "bouchon", "lights", "gastronomy"],
        "french_audience": "Food lovers, Lyon pride"
    },
    "bordeaux": {
        "name": "Bordeaux",
        "category": "French Culture",
        "aesthetic": "Wine, elegance, 18th century",
        "tension": "Wine culture, river, rugby",
        "format_fit": ["wine", "vineyard", "elegant", "rugby"],
        "french_audience": "Wine lovers, elegant"
    },
    "toulouse": {
        "name": "Toulouse",
        "category": "French Culture",
        "aesthetic": "Pink city, rugby, aerospace",
        "tension": "Cassoulet, rugby, space",
        "format_fit": ["pink", "cassoulet", "rugby", "space"],
        "french_audience": "Southwest, rugby fans"
    },
    "parisian_cafe": {
        "name": "Parisian Café Culture",
        "category": "French Culture",
        "aesthetic": "Terrace, espresso, people watching",
        "tension": "Philosophy, cigarettes, romance",
        "format_fit": ["terrace", "coffee", "philosophy", "romance"],
        "french_audience": "Paris lovers, clichés"
    },
    "montmartre": {
        "name": "Montmartre",
        "category": "French Culture",
        "aesthetic": "Artistic, bohemian, Sacré-Cœur",
        "tension": "Painters, Amélie, village feel",
        "format_fit": ["art", "painter", "Amélie", "village"],
        "french_audience": "Art lovers, tourists, romantics"
    },
    "french_cuisine": {
        "name": "French Cuisine",
        "category": "French Culture",
        "aesthetic": "Gastronomy, Michelin, terroir",
        "tension": "Quality ingredients, technique, pride",
        "format_fit": ["cooking", "chef", "ingredients", "terroir"],
        "french_audience": "Food lovers, national pride"
    },
    "baguette_culture": {
        "name": "Baguette Culture",
        "category": "French Culture",
        "aesthetic": "Daily ritual, bakery, crust",
        "tension": "Best baguette, tradition, UNESCO",
        "format_fit": ["bakery", "crust", "daily", "tradition"],
        "french_audience": "All French people, daily life"
    },
    
    # === TIKTOK TRENDS ===
    "tiktok_dance": {
        "name": "TikTok Dance Trends",
        "category": "TikTok",
        "aesthetic": "Choreography, viral, trending",
        "tension": "Learning dances, going viral",
        "format_fit": ["dance", "viral", "trend", "choreo"],
        "french_audience": "Gen Z, dancers"
    },
    "tiktok_food": {
        "name": "TikTok Food Trends",
        "category": "TikTok",
        "aesthetic": "Viral recipes, satisfying, food",
        "tension": "Trying trends, fails, success",
        "format_fit": ["recipe", "cooking", "viral", "food"],
        "french_audience": "Food lovers, home cooks"
    },
    "tiktok_beauty": {
        "name": "TikTok Beauty Trends",
        "category": "TikTok",
        "aesthetic": "Makeup, skincare, transformation",
        "tension": "Before/after, hacks, products",
        "format_fit": ["makeup", "skincare", "transformation", "glow up"],
        "french_audience": "Beauty enthusiasts, teens"
    },
    "tiktok_fashion": {
        "name": "TikTok Fashion Trends",
        "category": "TikTok",
        "aesthetic": "Outfits, hauls, aesthetics",
        "tension": "Trend cycles, fast fashion, self-expression",
        "format_fit": ["outfit", "haul", "aesthetic", "style"],
        "french_audience": "Fashion lovers, Gen Z"
    },
    "clean_girl": {
        "name": "Clean Girl Aesthetic",
        "category": "TikTok",
        "aesthetic": "Minimalist, slicked back, dewy",
        "tension": "Effortless beauty, wellness",
        "format_fit": ["minimal", "slick back", "dewy", "wellness"],
        "french_audience": "Beauty enthusiasts"
    },
    "mob_wife": {
        "name": "Mob Wife Aesthetic",
        "category": "TikTok",
        "aesthetic": "Glamorous, fur, dramatic",
        "tension": "Sopranos inspired, maximalist",
        "format_fit": ["fur", "glam", "dramatic", "maximalist"],
        "french_audience": "Fashion forward, Gen Z"
    },
    "aura_farming": {
        "name": "Aura Farming",
        "category": "TikTok",
        "aesthetic": "Confidence, sports, energy",
        "tension": "Gaining/losing aura, viral clips",
        "format_fit": ["confidence", "sports", "energy", "viral"],
        "french_audience": "Sports fans, Gen Z"
    },
    "silent_review": {
        "name": "Silent Reviews",
        "category": "TikTok",
        "aesthetic": "No talking, expressions only",
        "tension": "Ratings through gestures, reactions",
        "format_fit": ["silent", "rating", "gestures", "review"],
        "french_audience": "Comedy fans, relatable"
    },
    
    # === MUSIC GENRES ===
    "phonk": {
        "name": "Phonk",
        "category": "Music",
        "aesthetic": "Memphis rap, slowed, drifting",
        "tension": "Cowbell, drifting videos, viral",
        "format_fit": ["cowbell", "drift", "slowed", "bass"],
        "french_audience": "Car culture, internet music"
    },
    "afrobeats": {
        "name": "Afrobeats",
        "category": "Music",
        "aesthetic": "African rhythms, dance, joyful",
        "tension": "Global rise, fusion, dance",
        "format_fit": ["rhythm", "dance", "African", "global"],
        "french_audience": "Diverse, dance lovers"
    },
    "kpop": {
        "name": "K-Pop",
        "category": "Music",
        "aesthetic": "High production, choreography, fandom",
        "tension": "Comebacks, choreography, stans",
        "format_fit": ["comeback", "dance", "choreo", "fandom"],
        "french_audience": "K-pop stans, teens"
    },
    "latin_music": {
        "name": "Latin Music",
        "category": "Music",
        "aesthetic": "Reggaeton, bachata, rhythm",
        "tension": "Global hits, Bad Bunny, dance",
        "format_fit": ["reggaeton", "dance", "rhythm", "summer"],
        "french_audience": "Summer vibes, dance"
    },
    "french_variete": {
        "name": "French Variété",
        "category": "Music",
        "aesthetic": "Classic French songs, chanson",
        "tension": "Nostalgia, classics, timeless",
        "format_fit": ["chanson", "classic", "nostalgic", "timeless"],
        "french_audience": "Older generations, nostalgic"
    },
    "electro_fr": {
        "name": "French Electro",
        "category": "Music",
        "aesthetic": "Daft Punk legacy, Justice, festivals",
        "tension": "French touch, festivals, DJ",
        "format_fit": ["electro", "festival", "DJ", "French touch"],
        "french_audience": "Festival goers, electronic"
    },
    
    # === TV SHOWS (More) ===
    "wednesday_series": {
        "name": "Wednesday (Series)",
        "category": "TV Shows",
        "aesthetic": "Dark academia, gothic, mystery",
        "tension": "Nevermore, mystery, outcast",
        "format_fit": ["dance", "gothic", "mystery", "school"],
        "french_audience": "Teens, Netflix viewers"
    },
    "last_of_us": {
        "name": "The Last of Us",
        "category": "TV Shows",
        "aesthetic": "Post-apocalyptic, emotional, zombies",
        "tension": "Survival, Joel and Ellie, infected",
        "format_fit": ["zombies", "survival", "emotional", "fungus"],
        "french_audience": "Gaming fans, prestige TV"
    },
    "the_bear": {
        "name": "The Bear",
        "category": "TV Shows",
        "aesthetic": "Kitchen drama, anxiety, Chicago",
        "tension": "Restaurant pressure, family trauma",
        "format_fit": ["kitchen", "chef", "pressure", "sandwich"],
        "french_audience": "Food industry, prestige TV"
    },
    "succession": {
        "name": "Succession",
        "category": "TV Shows",
        "aesthetic": "Rich family, media empire, drama",
        "tension": "Power struggle, dysfunctional, wealth",
        "format_fit": ["family", "power", "wealth", "dysfunctional"],
        "french_audience": "Prestige TV fans, business"
    },
    "euphoria": {
        "name": "Euphoria",
        "category": "TV Shows",
        "aesthetic": "Teen drama, drugs, glitter",
        "tension": "Addiction, relationships, identity",
        "format_fit": ["teen", "drugs", "glitter", "drama"],
        "french_audience": "Gen Z, teen drama fans"
    },
    "stranger_things": {
        "name": "Stranger Things",
        "category": "TV Shows",
        "aesthetic": "80s nostalgia, sci-fi, horror",
        "tension": "Upside Down, kids, monsters",
        "format_fit": ["80s", "sci-fi", "kids", "monster"],
        "french_audience": "Nostalgia, sci-fi fans"
    },
    "white_lotus": {
        "name": "The White Lotus",
        "category": "TV Shows",
        "aesthetic": "Satire, luxury, mystery",
        "tension": "Wealthy guests, staff, death",
        "format_fit": ["resort", "wealthy", "satire", "mystery"],
        "french_audience": "Satire fans, HBO viewers"
    },
    
    # === MORE GAMING ===
    "baldurs_gate": {
        "name": "Baldur's Gate 3",
        "category": "Gaming",
        "aesthetic": "D&D, fantasy, choices matter",
        "tension": "Tav, companions, dice rolls",
        "format_fit": ["dice", "companion", "romance", "choice"],
        "french_audience": "RPG fans, D&D"
    },
    "stardew_valley": {
        "name": "Stardew Valley",
        "category": "Gaming",
        "aesthetic": "Cozy farming, pixel art, relationships",
        "tension": "Farm life, villagers, mines",
        "format_fit": ["farm", "crops", "villager", "cozy"],
        "french_audience": "Cozy gamers, relaxing"
    },
    "elden_ring": {
        "name": "Elden Ring",
        "category": "Gaming",
        "aesthetic": "Dark fantasy, FromSoft, open world",
        "tension": "Difficult, exploration, lore",
        "format_fit": ["boss", "difficult", "exploration", "lore"],
        "french_audience": "Hardcore gamers, challenge"
    },
    "hollow_knight": {
        "name": "Hollow Knight",
        "category": "Gaming",
        "aesthetic": "Metroidvania, dark, beautiful",
        "tension": "Exploration, boss fights, lore",
        "format_fit": ["bug", "explore", "boss", "atmospheric"],
        "french_audience": "Indie game fans, challenging"
    },
    "undertale": {
        "name": "Undertale",
        "category": "Gaming",
        "aesthetic": "Pixel art, emotional, choices",
        "tension": "Mercy or fight, Sans, determination",
        "format_fit": ["pixel", "emotional", "sans", "choice"],
        "french_audience": "Indie fans, emotional stories"
    },
    "among_us": {
        "name": "Among Us",
        "category": "Gaming",
        "aesthetic": "Space, betrayal, social deduction",
        "tension": "Imposter, tasks, sus",
        "format_fit": ["imposter", "tasks", "sus", "vote"],
        "french_audience": "Casual, friends gaming"
    },
    "fall_guys": {
        "name": "Fall Guys",
        "category": "Gaming",
        "aesthetic": "Colorful, chaotic, battle royale",
        "tension": "Beans, obstacles, crown",
        "format_fit": ["bean", "obstacle", "crown", "fall"],
        "french_audience": "Casual, party game"
    },
    "subnautica": {
        "name": "Subnautica",
        "category": "Gaming",
        "aesthetic": "Underwater, survival, ocean",
        "tension": "Alien ocean, fear, exploration",
        "format_fit": ["underwater", "survival", "ocean", "fear"],
        "french_audience": "Survival fans, ocean"
    },
    "terraria": {
        "name": "Terraria",
        "category": "Gaming",
        "aesthetic": "2D sandbox, exploration, bosses",
        "tension": "Building, fighting, exploring",
        "format_fit": ["2D", "sandbox", "boss", "explore"],
        "french_audience": "Sandbox fans, building"
    },
    "portal": {
        "name": "Portal",
        "category": "Gaming",
        "aesthetic": "Puzzle, sci-fi, GLaDOS",
        "tension": "Cake is a lie, portals, AI",
        "format_fit": ["puzzle", "portal", "GLaDOS", "cake"],
        "french_audience": "Puzzle fans, humor"
    },
    "csgo": {
        "name": "Counter-Strike",
        "category": "Gaming",
        "aesthetic": "Tactical FPS, competitive, skins",
        "tension": "Bomb, defuse, clutch",
        "format_fit": ["bomb", "defuse", "clutch", "skins"],
        "french_audience": "Competitive FPS, esports"
    },
    "rocket_league": {
        "name": "Rocket League",
        "category": "Gaming",
        "aesthetic": "Cars, soccer, aerial",
        "tension": "Aerials, goals, freestyles",
        "format_fit": ["car", "ball", "aerial", "goal"],
        "french_audience": "Sports, competitive"
    },
    "fnaf": {
        "name": "Five Nights at Freddy's",
        "category": "Gaming",
        "aesthetic": "Horror, animatronics, jumpscare",
        "tension": "Survive nights, animatronics, lore",
        "format_fit": ["animatronic", "jumpscare", "night", "lore"],
        "french_audience": "Horror fans, teens"
    },
    
    # === FRENCH INTERNET CULTURE ===
    "neurchi": {
        "name": "Neurchi (French Meme Culture)",
        "category": "French Internet",
        "aesthetic": "Absurdist, self-referential, French",
        "tension": "Inside jokes, absurd humor, community",
        "format_fit": ["absurd", "self-aware", "French", "community"],
        "french_audience": "Young French internet users"
    },
    "pdp": {
        "name": "PDP (Pas De Problème)",
        "category": "French Internet",
        "aesthetic": "Relatable, French life, humor",
        "tension": "French everyday situations, memes",
        "format_fit": ["relatable", "French", "situation", "meme"],
        "french_audience": "French meme consumers"
    },
    "onestla": {
        "name": "On Est La",
        "category": "French Internet",
        "aesthetic": "French urban culture, rap, viral",
        "tension": "Catchphrases, viral moments",
        "format_fit": ["catchphrase", "viral", "urban", "rap"],
        "french_audience": "Urban French youth"
    },
    "tonton_du_bled": {
        "name": "Tonton du Bled",
        "category": "French Internet",
        "aesthetic": "Maghrebi-French humor, family",
        "tension": "Uncle wisdom, cultural clash",
        "format_fit": ["family", "wisdom", "culture", "humor"],
        "french_audience": "Maghrebi-French community"
    },
    "mamie_layette": {
        "name": "Mamie Layette",
        "category": "French Internet",
        "aesthetic": "Grandma wisdom, cooking, family",
        "tension": "Traditional recipes, family love",
        "format_fit": ["cooking", "grandma", "family", "traditional"],
        "french_audience": "Family oriented, nostalgic"
    },
    
    # === HISTORICAL / PERIOD ===
    "medieval": {
        "name": "Medieval / Knights",
        "category": "Historical",
        "aesthetic": "Knights, castles, chivalry",
        "tension": "Quests, battles, honor",
        "format_fit": ["knight", "castle", "quest", "dragon"],
        "french_audience": "History buffs"
    },
    "french_revolution": {
        "name": "French Revolution",
        "category": "Historical",
        "aesthetic": "Revolution, guillotine, liberty",
        "tension": "Revolution, monarchy, terror",
        "format_fit": ["guillotine", "revolution", "liberté", "marat"],
        "french_audience": "Historical awareness"
    },
    
    # === VIRAL FORMATS ===
    "skibidi": {
        "name": "Skibidi Toilet",
        "category": "Viral",
        "aesthetic": "Absurd, surreal, chaotic",
        "tension": "Head in toilet, surreal",
        "format_fit": ["skibidi", "toilet", "surreal", "absurd"],
        "french_audience": "Kids, Gen Alpha"
    },
    "bird": {
        "name": "Meme Bird",
        "category": "Viral",
        "aesthetic": "抽象, weird, surreal",
        "tension": "Abstract humor",
        "format_fit": ["bird", "weird", "abstract", "mysterious"],
        "french_audience": "Meme communities"
    }
}


# ============================================
# VISUAL STYLES (for image generation) - EXPANDED
# ============================================
STYLES = {
    # === ANIME / MANGA ===
    "anime": {"name": "Anime Style", "keywords": ["anime", "manga style", "Japanese animation"], "description": "Japanese animation visual style"},
    "manga": {"name": "Manga Style", "keywords": ["manga", "comic art", "ink", "pen and ink", "screentone"], "description": "Japanese comic art with ink and screentone"},
    "chibi": {"name": "Chibi", "keywords": ["chibi", "super deformed", "cute anime", "kawaii"], "description": "Super deformed cute anime characters"},
    "ghibli": {"name": "Studio Ghibli", "keywords": ["Ghibli style", "watercolor anime", "whimsical", "Miyazaki"], "description": "Whimsical watercolor anime by Studio Ghibli"},
    "mecha": {"name": "Mecha", "keywords": ["mecha", "giant robot", "mechanical", "Gundam"], "description": "Giant robot and mechanical suit anime"},
    "shonen": {"name": "Shonen", "keywords": ["shonen", "action anime", "spiky hair", "battle"], "description": "Action-oriented anime for young boys"},
    "shojo": {"name": "Shojo", "keywords": ["shojo", "sparkles", "romance anime", "soft", "flowers"], "description": "Romance-oriented anime with soft aesthetics"},
    "seinen": {"name": "Seinen", "keywords": ["seinen", "mature anime", "dark", "realistic"], "description": "Mature anime for adult audiences"},
    "isekai": {"name": "Isekai", "keywords": ["isekai", "another world", "reincarnation", "fantasy"], "description": "Transported to another world genre"},
    "josei": {"name": "Josei", "keywords": ["josei", "adult women", "realistic romance", "slice of life"], "description": "Anime targeting adult women"},
    "90s_anime": {"name": "90s Anime", "keywords": ["90s anime", "retro anime", "cel shading", "VHS"], "description": "Classic 1990s anime visual style"},
    "sakuga": {"name": "Sakuga", "keywords": ["sakuga", "key animation", "fluid motion", "detailed"], "description": "High-quality key animation sequences"},

    # === WESTERN COMICS ===
    "marvel": {"name": "Marvel Comic", "keywords": ["Marvel comic", "comic book", "panel", "superhero"], "description": "Marvel superhero comic book style"},
    "dc": {"name": "DC Comic", "keywords": ["DC comic", "superhero", "dark", "Gotham"], "description": "DC Comics dark superhero style"},
    "indie_comic": {"name": "Indie Comic", "keywords": ["indie comic", "alternative comic", "underground"], "description": "Independent alternative comics"},
    "comic_strip": {"name": "Comic Strip", "keywords": ["comic strip", "funny pages", "newspaper"], "description": "Newspaper comic strip format"},
    "bd": {"name": "Bande Dessinée", "keywords": ["bande dessinée", "BD", "French comic", "European"], "description": "French/European comic book tradition"},
    "graphic_novel": {"name": "Graphic Novel", "keywords": ["graphic novel", "literary comic", "long form"], "description": "Long-form literary comic format"},
    "underground_comix": {"name": "Underground Comix", "keywords": ["underground comix", "R. Crumb", "counterculture"], "description": "Counterculture comics of the 60s-70s"},
    "webcomic": {"name": "Webcomic", "keywords": ["webcomic", "internet comic", "digital comic"], "description": "Comics published on the internet"},

    # === ART MOVEMENTS ===
    "renaissance": {"name": "Renaissance", "keywords": ["renaissance", "da Vinci", "Michelangelo", "classical", "perspective"], "description": "15th-16th century European art revival"},
    "baroque": {"name": "Baroque", "keywords": ["baroque", "dramatic", "chiaroscuro", "ornate", "Caravaggio"], "description": "Dramatic 17th century art with strong contrast"},
    "rococo": {"name": "Rococo", "keywords": ["rococo", "ornate", "pastel", "aristocratic", "French"], "description": "Ornate French aristocratic art style"},
    "neoclassicism": {"name": "Neoclassicism", "keywords": ["neoclassicism", "Greek", "Roman", "heroic", "David"], "description": "Greek and Roman inspired classical art"},
    "romanticism": {"name": "Romanticism", "keywords": ["romanticism", "emotion", "nature", "dramatic", "sublime"], "description": "Emotion-focused 19th century movement"},
    "impressionism": {"name": "Impressionism", "keywords": ["impressionism", "soft brushstrokes", "Monet", "light"], "description": "Capturing light and momentary impressions"},
    "post_impressionism": {"name": "Post-Impressionism", "keywords": ["post-impressionism", "Van Gogh", "Cézanne", "bold"], "description": "Bold colors and expressive forms after Impressionism"},
    "expressionism": {"name": "Expressionism", "keywords": ["expressionism", "distorted", "emotional", "Munch", "vivid"], "description": "Distorted forms expressing inner emotion"},
    "cubism": {"name": "Cubism", "keywords": ["cubism", "geometric", "Picasso", "fragmented", "abstract"], "description": "Objects shown from multiple angles simultaneously"},
    "futurism": {"name": "Futurism", "keywords": ["futurism", "speed", "technology", "movement", "dynamic"], "description": "Celebrating speed and modern technology"},
    "dadaism": {"name": "Dadaism", "keywords": ["dada", "absurd", "anti-art", "collage", "nonsense"], "description": "Anti-art movement embracing absurdity"},
    "constructivism": {"name": "Constructivism", "keywords": ["constructivism", "Soviet", "geometric", "propaganda", "red"], "description": "Soviet-era geometric propaganda art"},
    "art_nouveau": {"name": "Art Nouveau", "keywords": ["Art Nouveau", "organic", "Mucha", "flowing lines", "nature"], "description": "Decorative style with flowing organic lines"},
    "art_deco": {"name": "Art Deco", "keywords": ["Art Deco", "glamour", "1920s", "geometric", "elegant"], "description": "Glamorous geometric style of the 1920s-30s"},
    "bauhaus": {"name": "Bauhaus", "keywords": ["bauhaus", "functional", "geometric", "modernist", "primary colors"], "description": "Functional modernist design movement"},
    "pop_art": {"name": "Pop Art", "keywords": ["Pop Art", "bright colors", "Warhol", "Lichtenstein", "mass media"], "description": "Bold imagery from popular culture"},
    "op_art": {"name": "Op Art", "keywords": ["op art", "optical illusion", "geometric", "movement", "pattern"], "description": "Visual effects creating illusions of movement"},
    "abstract_expressionism": {"name": "Abstract Expressionism", "keywords": ["abstract expressionism", "Pollock", "drip", "gestural"], "description": "Spontaneous automatic painting"},
    "color_field": {"name": "Color Field", "keywords": ["color field", "Rothko", "large canvas", "flat color"], "description": "Large areas of flat color"},
    "pointillism": {"name": "Pointillism", "keywords": ["pointillism", "dots", "Seurat", "divisionism"], "description": "Image composed of small distinct dots"},
    "fauvism": {"name": "Fauvism", "keywords": ["fauvism", "wild color", "Matisse", "bold", "unnatural"], "description": "Wild bold unnatural colors"},
    "surrealism_art": {"name": "Surrealism", "keywords": ["surrealism", "Dali", "dream", "bizarre", "Magritte"], "description": "Dream-like imagery that defies logic"},
    "de_stijl": {"name": "De Stijl", "keywords": ["de stijl", "Mondrian", "primary colors", "grid", "geometric"], "description": "Dutch movement with primary colors and grids"},
    "suprematism": {"name": "Suprematism", "keywords": ["suprematism", "Malevich", "geometric", "abstract", "pure"], "description": "Pure geometric abstraction"},
    "pre_raphaelite": {"name": "Pre-Raphaelite", "keywords": ["pre-raphaelite", "medieval", "detailed", "romantic", "nature"], "description": "Highly detailed romantic medieval-inspired art"},
    "symbolism": {"name": "Symbolism", "keywords": ["symbolism", "mystical", "mythological", "dreamlike"], "description": "Mystical and mythological art movement"},
    "naive_art": {"name": "Naive Art", "keywords": ["naive art", "folk art", "childlike", "Rousseau"], "description": "Childlike untrained artistic style"},
    "outsider_art": {"name": "Outsider Art", "keywords": ["outsider art", "raw", "untrained", "brut"], "description": "Art by self-taught outsiders"},
    "lowbrow": {"name": "Lowbrow / Pop Surrealism", "keywords": ["lowbrow", "pop surrealism", "Kaws", "counterculture"], "description": "Underground pop culture-influenced art"},
    "ukiyo_e": {"name": "Ukiyo-e", "keywords": ["ukiyo-e", "Japanese woodblock", "Hokusai", "waves", "edo"], "description": "Traditional Japanese woodblock printing"},
    "sumi_e": {"name": "Sumi-e", "keywords": ["sumi-e", "ink wash", "Japanese brush", "minimalist"], "description": "Japanese ink wash painting"},
    "chinese_painting": {"name": "Chinese Painting", "keywords": ["Chinese painting", "shan shui", "ink wash", "calligraphy"], "description": "Traditional Chinese landscape and ink painting"},

    # === DIGITAL ART ===
    "digital_painting": {"name": "Digital Painting", "keywords": ["digital painting", "concept art", "tablet"], "description": "Digital medium painting style"},
    "concept_art": {"name": "Concept Art", "keywords": ["concept art", "fantasy art", "game design"], "description": "Conceptual design art for media"},
    "low_poly": {"name": "Low Poly", "keywords": ["low poly", "geometric 3D", "triangulated"], "description": "Simplified geometric 3D style"},
    "pixel_art": {"name": "Pixel Art", "keywords": ["pixel art", "8-bit", "retro gaming", "sprite"], "description": "Grid-based retro gaming art"},
    "vector": {"name": "Vector Art", "keywords": ["vector", "flat design", "minimalist", "scalable"], "description": "Clean scalable digital illustration"},
    "3d_render": {"name": "3D Render", "keywords": ["3D render", "CGI", "octane", "blender"], "description": "Computer-generated 3D imagery"},
    "isometric": {"name": "Isometric", "keywords": ["isometric", "3D perspective", "flat 3D", "diagram"], "description": "Angled 3D perspective without vanishing point"},
    "voxel": {"name": "Voxel Art", "keywords": ["voxel", "3D pixel", "cube", "minecraft style"], "description": "3D volumetric pixel art"},
    "glitch_art": {"name": "Glitch Art", "keywords": ["glitch", "corrupted", "data moshing", "digital error"], "description": "Intentional digital corruption as art"},
    "generative_art": {"name": "Generative Art", "keywords": ["generative", "algorithmic", "code art", "procedural"], "description": "Art created by algorithms and code"},
    "motion_graphics": {"name": "Motion Graphics", "keywords": ["motion graphics", "animated", "kinetic", "typography"], "description": "Animated graphic design"},
    "ui_design": {"name": "UI Design", "keywords": ["UI design", "interface", "app", "clean", "modern"], "description": "User interface design aesthetic"},
    "flat_design": {"name": "Flat Design", "keywords": ["flat design", "2D", "minimal", "solid colors", "no shadow"], "description": "Minimalist 2D design without shadows"},
    "skeuomorphic": {"name": "Skeuomorphic", "keywords": ["skeuomorphic", "realistic", "texture", "old iOS"], "description": "Design mimicking real-world textures"},
    "neomorphism": {"name": "Neomorphism", "keywords": ["neomorphism", "soft UI", "subtle shadow", "modern"], "description": "Soft extruded UI design style"},
    "ascii_art": {"name": "ASCII Art", "keywords": ["ASCII art", "text art", "characters", "terminal"], "description": "Art made from text characters"},

    # === PAINTING STYLES & TECHNIQUES ===
    "oil_painting": {"name": "Oil Painting", "keywords": ["oil painting", "canvas", "rich colors", "classical"], "description": "Traditional oil on canvas painting"},
    "watercolor": {"name": "Watercolor", "keywords": ["watercolor", "soft paint", "transparent", "flowing"], "description": "Water-based paint with soft edges"},
    "acrylic": {"name": "Acrylic", "keywords": ["acrylic painting", "bold colors", "modern", "texture"], "description": "Fast-drying acrylic paint style"},
    "pastel": {"name": "Pastel", "keywords": ["pastel", "soft colors", "chalk", "delicate"], "description": "Soft chalk-like pastel medium"},
    "gouache": {"name": "Gouache", "keywords": ["gouache", "opaque watercolor", "matte", "illustration"], "description": "Opaque water-based paint"},
    "charcoal": {"name": "Charcoal", "keywords": ["charcoal", "sketch", "black and white", "smudge"], "description": "Black carbon drawing medium"},
    "ink_drawing": {"name": "Ink Drawing", "keywords": ["ink", "pen", "crosshatch", "line art", "illustration"], "description": "Pen and ink illustration technique"},
    "graffiti": {"name": "Graffiti", "keywords": ["graffiti", "street art", "spray paint", "urban", "tags"], "description": "Urban spray-painted street art"},
    "street_art": {"name": "Street Art", "keywords": ["street art", "Banksy", "stencil", "mural", "public"], "description": "Public space artistic expression"},
    "impasto": {"name": "Impasto", "keywords": ["impasto", "thick paint", "texture", "3D", "Van Gogh"], "description": "Thick textured paint creating 3D effect"},
    "palette_knife": {"name": "Palette Knife", "keywords": ["palette knife", "thick paint", "texture", "bold strokes"], "description": "Thick paint applied with a knife"},
    "fresco": {"name": "Fresco", "keywords": ["fresco", "Sistine Chapel", "wall painting", "plaster"], "description": "Painting on wet plaster walls"},
    "mosaic": {"name": "Mosaic", "keywords": ["mosaic", "tiles", "Byzantine", "colorful", "fragments"], "description": "Art from small colored pieces"},
    "stained_glass": {"name": "Stained Glass", "keywords": ["stained glass", "cathedral", "light", "colorful", "lead"], "description": "Colored glass window art"},
    "collage": {"name": "Collage", "keywords": ["collage", "mixed media", "cut and paste", "layered"], "description": "Mixed media cut-and-paste art"},
    "woodcut": {"name": "Woodcut", "keywords": ["woodcut", "linocut", "print", "relief", "carved"], "description": "Carved wood block printing"},
    "etching": {"name": "Etching", "keywords": ["etching", "engraving", "metal plate", "fine lines"], "description": "Metal plate engraving printmaking"},
    "screen_print": {"name": "Screen Print", "keywords": ["screen print", "silkscreen", "Warhol", "layers"], "description": "Layered screen printing technique"},
    "monotype": {"name": "Monotype", "keywords": ["monotype", "print", "unique", "pressed"], "description": "One-of-a-kind print technique"},
    "batik": {"name": "Batik", "keywords": ["batik", "wax resist", "fabric", "Indonesian"], "description": "Wax resist fabric dyeing technique"},
    "embroidery_art": {"name": "Embroidery Art", "keywords": ["embroidery", "needle", "thread", "textile", "craft"], "description": "Artistic needlework and textile art"},
    "calligraphy": {"name": "Calligraphy", "keywords": ["calligraphy", "lettering", "brush", "Arabic", "Chinese"], "description": "Artistic handwriting and lettering"},
    "chiaroscuro": {"name": "Chiaroscuro", "keywords": ["chiaroscuro", "light dark", "dramatic", "Caravaggio"], "description": "Strong light and shadow contrast"},
    "trompe_loeil": {"name": "Trompe-l'oeil", "keywords": ["trompe loeil", "illusion", "realistic", "deceive eye", "French"], "description": "Optical illusion of three dimensions"},
    "plein_air": {"name": "Plein Air", "keywords": ["plein air", "outdoor", "landscape", "natural light"], "description": "Painting outdoors in natural light"},
    "sfumato": {"name": "Sfumato", "keywords": ["sfumato", "soft edges", "da Vinci", "smoky", "blend"], "description": "Soft blended edges without lines"},

    # === PHOTOGRAPHY ===
    "portrait": {"name": "Portrait Photo", "keywords": ["portrait photo", "studio", "face", "headshot"], "description": "Studio portrait photography"},
    "documentary": {"name": "Documentary", "keywords": ["documentary", "street photography", "reportage"], "description": "Documentary street photography"},
    "film": {"name": "Film Photo", "keywords": ["film photo", "analog", "vintage", "grain"], "description": "Analog film photography with grain"},
    "cinematic": {"name": "Cinematic", "keywords": ["cinematic", "movie still", "anamorphic", "widescreen"], "description": "Movie-like visual composition"},
    "polaroid": {"name": "Polaroid", "keywords": ["polaroid", "instant photo", "white border", "vintage"], "description": "Instant film photography aesthetic"},
    "disposable_camera": {"name": "Disposable Camera", "keywords": ["disposable camera", "flash", "candid", "party"], "description": "Single-use camera candid aesthetic"},
    "lomography": {"name": "Lomography", "keywords": ["lomography", "lomo", "toy camera", "vignette", "light leak"], "description": "Lo-fi analog toy camera aesthetic"},
    "infrared": {"name": "Infrared", "keywords": ["infrared", "false color", "red trees", "surreal landscape"], "description": "Infrared photography with false colors"},
    "double_exposure": {"name": "Double Exposure", "keywords": ["double exposure", "overlay", "blend", "ghostly"], "description": "Two images overlaid on one frame"},
    "long_exposure": {"name": "Long Exposure", "keywords": ["long exposure", "light trails", "smooth water", "motion blur"], "description": "Extended shutter time photography"},
    "macro": {"name": "Macro Photography", "keywords": ["macro", "close up", "detail", "tiny", "insect"], "description": "Extreme close-up photography"},
    "aerial": {"name": "Aerial / Drone", "keywords": ["aerial", "drone", "bird eye", "top down"], "description": "Overhead drone photography"},
    "noir_photo": {"name": "Film Noir Photo", "keywords": ["film noir", "shadow", "moody", "black white", "detective"], "description": "Dark moody black and white photography"},
    "fashion_photo": {"name": "Fashion Photography", "keywords": ["fashion photo", "editorial", "model", "haute couture"], "description": "High fashion editorial photography"},
    "food_photo": {"name": "Food Photography", "keywords": ["food photo", "plating", "restaurant", "close up food"], "description": "Appetizing food photography"},

    # === AESTHETICS (MASSIVELY EXPANDED - 30+ entries) ===
    "vaporwave": {"name": "Vaporwave", "keywords": ["vaporwave", "nostalgic", "pink cyan", "retro computer", "glitch", "roman bust"], "description": "Nostalgic 80s/90s aesthetic with glitchy graphics"},
    "synthwave": {"name": "Synthwave", "keywords": ["synthwave", "neon", "80s", "retrowave", "grid", "sunset"], "description": "80s-inspired neon lights and futuristic vibes"},
    "cottagecore": {"name": "Cottagecore", "keywords": ["cottagecore", "rustic", "wholesome", "flowers", "vintage dress", "pastoral"], "description": "Romanticized rural life and nature"},
    "dark_academia": {"name": "Dark Academia", "keywords": ["dark academia", "gothic", "books", "tweed", "moody", "library"], "description": "Scholarly aesthetic with dark colors and classical architecture"},
    "light_academia": {"name": "Light Academia", "keywords": ["light academia", "beige", "books", "soft", "classical", "study"], "description": "Lighter scholarly aesthetic with cream tones"},
    "cyberpunk": {"name": "Cyberpunk", "keywords": ["cyberpunk", "neon dystopia", "high tech low life", "rain", "city"], "description": "High-tech dystopian future with neon and urban decay"},
    "steampunk": {"name": "Steampunk", "keywords": ["steampunk", "Victorian", "gears", "brass", "steam"], "description": "Victorian-era steam-powered technology aesthetic"},
    "solarpunk": {"name": "Solarpunk", "keywords": ["solarpunk", "green", "sustainable", "utopia", "solar panels", "nature"], "description": "Optimistic green sustainable future"},
    "dieselpunk": {"name": "Dieselpunk", "keywords": ["dieselpunk", "1940s", "diesel", "war era", "retro futuristic"], "description": "WWII-era diesel technology aesthetic"},
    "atompunk": {"name": "Atompunk", "keywords": ["atompunk", "atomic", "1950s", "nuclear", "space age", "raygun"], "description": "1950s atomic age futuristic aesthetic"},
    "coquette": {"name": "Coquette", "keywords": ["coquette", "feminine", "pink", "bows", "lace", "romantic"], "description": "Hyper-feminine aesthetic with bows and pink"},
    "balletcore": {"name": "Balletcore", "keywords": ["balletcore", "ballet", "pink", "tutu", "elegant", "dance"], "description": "Ballet-inspired soft elegant aesthetic"},
    "goblincore": {"name": "Goblincore", "keywords": ["goblincore", "moss", "mud", "shiny objects", "forest", "mushroom"], "description": "Chaotic nature aesthetic celebrating dirt and trinkets"},
    "fairycore": {"name": "Fairycore", "keywords": ["fairycore", "fairy", "wings", "sparkles", "nature", "magical"], "description": "Enchanted forest aesthetic with fairies"},
    "angelcore": {"name": "Angelcore", "keywords": ["angelcore", "white", "wings", "heavenly", "soft", "divine"], "description": "Heavenly angelic aesthetic with white and gold"},
    "devilcore": {"name": "Devilcore", "keywords": ["devilcore", "red", "dark", "horns", "fire", "hell"], "description": "Dark demonic aesthetic with red and black"},
    "dreamcore": {"name": "Dreamcore", "keywords": ["dreamcore", "liminal", "nostalgic", "surreal", "uncanny"], "description": "Nostalgic dream-like aesthetic with liminal spaces"},
    "weirdcore": {"name": "Weirdcore", "keywords": ["weirdcore", "uncanny", "distorted", "text", "strange", "eerie"], "description": "Disturbing internet aesthetic with distorted imagery"},
    "kidcore": {"name": "Kidcore", "keywords": ["kidcore", "colorful", "childish", "rainbow", "90s toys", "playful"], "description": "Childhood nostalgia with bright colors"},
    "normcore": {"name": "Normcore", "keywords": ["normcore", "normal", "basic", "unassuming", "everyday"], "description": "Embracing normal unpretentious fashion"},
    "gorpcore": {"name": "Gorpcore", "keywords": ["gorpcore", "outdoor", "hiking", "technical", "Patagonia"], "description": "Outdoor gear as everyday fashion"},
    "barbiecore": {"name": "Barbiecore", "keywords": ["barbiecore", "pink", "plastic", "glam", "doll", "hot pink"], "description": "Hyper-pink Barbie doll culture aesthetic"},
    "mermaidcore": {"name": "Mermaidcore", "keywords": ["mermaidcore", "ocean", "shells", "iridescent", "underwater"], "description": "Ocean-inspired aesthetic with shimmer"},
    "royalcore": {"name": "Royalcore", "keywords": ["royalcore", "crown", "palace", "elegant", "royal", "gold"], "description": "Royal palace elegance aesthetic"},
    "regencycore": {"name": "Regencycore", "keywords": ["regencycore", "Bridgerton", "empire waist", "19th century"], "description": "Regency era Bridgerton-inspired aesthetic"},
    "witchcore": {"name": "Witchcore", "keywords": ["witchcore", "witch", "potions", "herbs", "moon", "spell"], "description": "Magical witchcraft aesthetic"},
    "vampirecore": {"name": "Vampirecore", "keywords": ["vampirecore", "vampire", "gothic", "blood", "nocturnal", "cape"], "description": "Vampire-inspired gothic elegance"},
    "medieval_aesthetic": {"name": "Medievalcore", "keywords": ["medievalcore", "knight", "castle", "tapestry", "historical"], "description": "Medieval-inspired aesthetic with castles and knights"},
    "grandmacore": {"name": "Grandmacore", "keywords": ["grandmacore", "cozy", "knitting", "vintage", "warm", "doily"], "description": "Cozy grandmother aesthetic"},
    "corporate_girlie": {"name": "Corporate Girlie", "keywords": ["corporate", "office", "girlboss", "linkedin", "latte"], "description": "Work culture aesthetic with productivity vibes"},
    "clean_girl_style": {"name": "Clean Girl Aesthetic", "keywords": ["clean girl", "minimal", "slicked back", "dewy", "neutral"], "description": "Minimalist beauty with glowing skin"},
    "mob_wife_style": {"name": "Mob Wife Aesthetic", "keywords": ["mob wife", "fur", "glam", "dramatic", "Sopranos"], "description": "Dramatic glamorous Sopranos-inspired style"},
    "old_money": {"name": "Old Money", "keywords": ["old money", "quiet luxury", "polo", "yacht", "understated"], "description": "Understated inherited wealth aesthetic"},
    "new_money": {"name": "New Money", "keywords": ["new money", "flashy", "luxury", "logos", "ostentatious"], "description": "Flashy nouveau riche aesthetic"},
    "coastal_grandmother": {"name": "Coastal Grandmother", "keywords": ["coastal grandmother", "Diane Keaton", "linen", "beach", "relaxed"], "description": "Relaxed Nancy Meyers beach lifestyle"},
    "dark_romance": {"name": "Dark Romance", "keywords": ["dark romance", "gothic", "dramatic", "passionate", "moody"], "description": "Gothic romantic aesthetic"},
    "whimsigoth": {"name": "Whimsigoth", "keywords": ["whimsigoth", "90s goth", "velvet", "celestial", "mystical"], "description": "Whimsical 90s goth with celestial elements"},
    "indie_aesthetic": {"name": "Indie Aesthetic", "keywords": ["indie", "alternative", "vinyl", "thrift", "film camera"], "description": "Alternative indie culture aesthetic"},
    "grunge": {"name": "Grunge", "keywords": ["grunge", "flannel", "90s", "dark", "distressed", "Seattle"], "description": "90s grunge rock culture aesthetic"},
    "e_girl": {"name": "E-Girl / E-Boy", "keywords": ["e-girl", "e-boy", "tiktok", "chains", "blush", "alternative"], "description": "Internet-native alternative youth aesthetic"},
    "soft_girl": {"name": "Soft Girl", "keywords": ["soft girl", "pastel", "pink", "blush", "cute", "gentle"], "description": "Soft pastel feminine aesthetic"},
    "baddie": {"name": "Baddie", "keywords": ["baddie", "instagram", "glam", "confidence", "snatched"], "description": "Confident glamorous Instagram aesthetic"},
    "dark_fairy": {"name": "Dark Fairy", "keywords": ["dark fairy", "fairy grunge", "dark whimsical", "wings"], "description": "Dark twist on fairy aesthetic"},
    "cluttercore": {"name": "Cluttercore", "keywords": ["cluttercore", "maximalist", "collections", "chaotic", "colorful"], "description": "Organized chaos maximalist aesthetic"},
    "bloomcore": {"name": "Bloomcore", "keywords": ["bloomcore", "flowers", "floral", "garden", "botanical"], "description": "Flower and botanical aesthetic"},
    "dark_fantasy": {"name": "Dark Fantasy", "keywords": ["dark fantasy", "Tolkien", "shadow", "epic", "gothic"], "description": "Dark epic fantasy worlds"},
    "horror_aesthetic": {"name": "Horror Aesthetic", "keywords": ["horror", "scary", "creepy", "blood", "monster"], "description": "Fear and dread visual language"},
    "fantasy_aesthetic": {"name": "Fantasy Art", "keywords": ["fantasy art", "epic fantasy", "magic", "dragons"], "description": "Magical fantasy world imagery"},
    "sci_fi": {"name": "Sci-Fi", "keywords": ["sci-fi", "space", "future", "technology", "spaceship"], "description": "Science fiction futuristic aesthetic"},
    "afrofuturism": {"name": "Afrofuturism", "keywords": ["afrofuturism", "Black Panther", "African", "futuristic", "technology"], "description": "African diaspora futuristic aesthetic"},
    "brutalism_aesthetic": {"name": "Brutalism", "keywords": ["brutalism", "concrete", "raw", "geometric", "monolithic"], "description": "Raw concrete architectural aesthetic"},
    "minimalist_aesthetic": {"name": "Minimalist", "keywords": ["minimalist", "simple", "clean", "white space", "less is more"], "description": "Clean simplicity aesthetic"},
    "maximalist": {"name": "Maximalist", "keywords": ["maximalist", "bold", "patterns", "excess", "colorful", "more is more"], "description": "Bold colorful excess aesthetic"},
    "wabi_sabi": {"name": "Wabi-Sabi", "keywords": ["wabi-sabi", "imperfect", "Japanese", "aged", "natural"], "description": "Japanese beauty of imperfection"},
    "hygge": {"name": "Hygge", "keywords": ["hygge", "Danish", "cozy", "candles", "warm", "blanket"], "description": "Danish cozy comfort lifestyle"},
    "lagom": {"name": "Lagom", "keywords": ["lagom", "Swedish", "balanced", "just right", "moderate"], "description": "Swedish balanced lifestyle aesthetic"},
    "kinfolk": {"name": "Kinfolk", "keywords": ["kinfolk", "natural", "warm tones", "simple living", "earth"], "description": "Natural earthy simple living aesthetic"},

    # === MEME STYLES (EXPANDED) ===
    "deep_fried": {"name": "Deep Fried", "keywords": ["deep fried", "compressed meme", "distorted", "loud", "emojis"], "description": "Heavily compressed and distorted meme format"},
    "blursed": {"name": "Blursed", "keywords": ["blursed", "weird blessed", "cursed", "uncomfortable"], "description": "Both blessed and cursed simultaneously"},
    "wholesome_meme": {"name": "Wholesome", "keywords": ["wholesome", "cute", "heart warming", "pure", "nice"], "description": "Feel-good content restoring faith in humanity"},
    "cringe_meme": {"name": "Cringe", "keywords": ["cringe", "awkward", "secondhand embarrassment"], "description": "Embarrassing uncomfortable content"},
    "brainrot": {"name": "Brainrot", "keywords": ["brainrot", "skibidi", "sigma", "gyatt", "Ohio", "chaos"], "description": "Gen Z/Alpha chaotic meme language"},
    "italian_brainrot": {"name": "Italian Brainrot", "keywords": ["Italian brainrot", "bombardino", "coccodrillo", "tung tung"], "description": "Italian-language brainrot meme trend"},
    "sigma_meme": {"name": "Sigma Male", "keywords": ["sigma", "grindset", "lone wolf", "success", "Patrick Bateman"], "description": "Sigma grindset ironic hustle memes"},
    "npc_meme": {"name": "NPC Meme", "keywords": ["NPC", "non-playable", "repetitive", "scripted"], "description": "People acting like video game NPCs"},
    "wojak": {"name": "Wojak", "keywords": ["wojak", "feels guy", "sad", "reaction", "meme face"], "description": "Simple MS Paint face for various emotions"},
    "chad_meme": {"name": "Chad", "keywords": ["chad", "yes chad", "muscular", "jawline", "gigachad"], "description": "Confident masculine archetype meme"},
    "soyjak": {"name": "Soyjak", "keywords": ["soyjak", "excited", "open mouth", "pointing", "enthusiastic"], "description": "Excited overly enthusiastic character"},
    "doomer": {"name": "Doomer", "keywords": ["doomer", "depressed", "nihilism", "cigarette", "beanie"], "description": "Pessimistic worldview meme character"},
    "bloomer": {"name": "Bloomer", "keywords": ["bloomer", "optimistic", "improving", "hopeful", "growth"], "description": "Optimistic self-improvement character"},
    "pepe": {"name": "Pepe the Frog", "keywords": ["pepe", "frog", "sad", "rare pepe", "feels"], "description": "Green frog with various emotions"},
    "doge": {"name": "Doge", "keywords": ["doge", "shiba", "wow", "such", "much", "Comic Sans"], "description": "Shiba Inu with Comic Sans text"},
    "trollface": {"name": "Trollface", "keywords": ["trollface", "troll", "problem", "classic meme"], "description": "Classic 2000s trolling meme face"},
    "rage_comic": {"name": "Rage Comic", "keywords": ["rage comic", "derp", "herp", "le", "impact font"], "description": "Early 2010s comic strip meme format"},
    "drake_format": {"name": "Drake Format", "keywords": ["drake format", "reject", "approve", "pointing"], "description": "Drake rejecting one thing and approving another"},
    "expanding_brain": {"name": "Expanding Brain", "keywords": ["expanding brain", "galaxy brain", "enlightenment"], "description": "Increasingly enlightened brain stages"},
    "stonks": {"name": "Stonks", "keywords": ["stonks", "meme man", "money", "finance", "surreal"], "description": "Meme man with misspelled stonks"},
    "distracted_bf": {"name": "Distracted Boyfriend", "keywords": ["distracted boyfriend", "looking back", "choice", "jealous"], "description": "Man looking at another woman meme"},
    "cursed_image": {"name": "Cursed Image", "keywords": ["cursed image", "unsettling", "wrong", "cursed"], "description": "Images that feel fundamentally wrong"},
    "shitpost": {"name": "Shitpost", "keywords": ["shitpost", "ironic", "low effort", "random", "absurd"], "description": "Intentionally absurd low-quality content"},
    "greentext": {"name": "Greentext", "keywords": ["greentext", "4chan", "be me", "mfw", "tfw"], "description": "4chan style green text stories"},
    "demotivational": {"name": "Demotivational", "keywords": ["demotivational", "black border", "caption", "ironic"], "description": "Black-bordered ironic motivational posters"},
    "starter_pack": {"name": "Starter Pack", "keywords": ["starter pack", "collection", "stereotype", "grid"], "description": "Grid of items stereotyping a type of person"},
    "alignment_chart": {"name": "Alignment Chart", "keywords": ["alignment chart", "lawful", "chaotic", "good", "evil"], "description": "D&D-style moral alignment grid meme"},
    "iceberg": {"name": "Iceberg", "keywords": ["iceberg", "layers", "deeper", "conspiracy", "hidden"], "description": "Layered iceberg chart going deeper"},
    "tier_list": {"name": "Tier List", "keywords": ["tier list", "S tier", "ranking", "best to worst"], "description": "Ranking items in tiers from S to F"},
    "galaxy_brain": {"name": "Galaxy Brain", "keywords": ["galaxy brain", "genius", "enlightened", "4D chess"], "description": "Increasingly absurd galaxy brain ideas"},
    "loss": {"name": "Loss.jpg", "keywords": ["loss", "minimalist", "lines", "four panels", "abstract"], "description": "Abstract minimalist loss meme"},
    "uncannyvalley": {"name": "Mr. Incredible Uncanny", "keywords": ["mr incredible", "uncanny", "becoming", "creepy", "stages"], "description": "Mr. Incredible becoming increasingly uncanny"},

    # === Y2K / RETRO AESTHETICS ===
    "y2k": {"name": "Y2K", "keywords": ["Y2K", "2000s", "futuristic", "silver", "butterfly", "chrome"], "description": "Late 90s/early 2000s futuristic aesthetic"},
    "y2k_fashion": {"name": "Y2K Fashion", "keywords": ["Y2K fashion", "low rise", "crop top", "tracksuit", "velour"], "description": "Early 2000s clothing trends"},
    "mcbling": {"name": "McBling", "keywords": ["mcbling", "2000s", "pink", "sparkly", "Paris Hilton", "rhinestone"], "description": "Mid-2000s glittery pink aesthetic"},
    "indie_sleaze": {"name": "Indie Sleaze", "keywords": ["indie sleaze", "hipster", "2000s", "grunge", "party"], "description": "Late 2000s hipster party aesthetic"},
    "scene_style": {"name": "Scene", "keywords": ["scene", "emo", "MySpace", "hair", "neon", "2000s"], "description": "2000s MySpace scene subculture"},
    "emo_style": {"name": "Emo", "keywords": ["emo", "emotional", "2000s", "black hair", "eyeliner", "MCR"], "description": "Mid-2000s emotional rock culture"},
    "mall_goth": {"name": "Mall Goth", "keywords": ["mall goth", "Hot Topic", "2000s", "black", "chains"], "description": "Commercial goth style of the 2000s"},
    "retro_80s": {"name": "80s Retro", "keywords": ["80s", "retro", "neon", "grid", "sunset", "VHS"], "description": "1980s nostalgia aesthetic"},
    "retro_90s": {"name": "90s Retro", "keywords": ["90s", "retro", "grunge", "flannel", "VHS", "Nirvana"], "description": "1990s nostalgia aesthetic"},
    "retro_70s": {"name": "70s Retro", "keywords": ["70s", "disco", "orange", "brown", "groovy", "pattern"], "description": "1970s disco and earth tones aesthetic"},
    "retro_60s": {"name": "60s Retro", "keywords": ["60s", "mod", "psychedelic", "Beatles", "pop art"], "description": "1960s mod and psychedelic aesthetic"},
    "retro_50s": {"name": "50s Retro", "keywords": ["50s", "diner", "rock and roll", "pin-up", "chrome"], "description": "1950s Americana diner culture"},
    "vhs_aesthetic": {"name": "VHS Aesthetic", "keywords": ["VHS", "static", "tracking", "distorted", "retro video"], "description": "Analog video tape visual effects"},
    "crt_screen": {"name": "CRT Monitor", "keywords": ["CRT", "monitor", "scanlines", "retro", "gaming"], "description": "Old CRT television display look"},
    "cassette_tape": {"name": "Cassette Tape", "keywords": ["cassette", "tape", "mixtape", "80s", "90s"], "description": "Analog audio tape aesthetic"},
    "vinyl_record": {"name": "Vinyl Record", "keywords": ["vinyl", "record", "retro", "analog", "warmth"], "description": "Vinyl record and turntable aesthetic"},
    "lofi_aesthetic": {"name": "Lo-fi", "keywords": ["lofi", "chill", "study girl", "anime", "relaxing", "beats"], "description": "Low fidelity relaxing study aesthetic"},
    "nostalgiacore": {"name": "Nostalgiacore", "keywords": ["nostalgiacore", "childhood", "early 2000s", "liminal"], "description": "Longing for childhood memories"},
    "webcore": {"name": "Webcore", "keywords": ["webcore", "old internet", "2000s web", "geocities", "cursor"], "description": "Early internet design aesthetic"},
    "old_internet": {"name": "Old Internet", "keywords": ["old internet", "dial up", "geocities", "gif", "under construction"], "description": "1990s-2000s internet culture"},
    "frutiger_aero": {"name": "Frutiger Aero", "keywords": ["frutiger aero", "windows vista", "glossy", "nature", "2007"], "description": "Mid-2000s glossy nature tech aesthetic"},
    "corporate_memphis": {"name": "Corporate Memphis", "keywords": ["corporate memphis", "flat illustration", "silicon valley", "tech art"], "description": "Flat cartoon corporate illustration style"},
    "liminal_space": {"name": "Liminal Space", "keywords": ["liminal space", "empty", "transitional", "eerie", "uncanny"], "description": "Empty transitional spaces that feel eerie"},
    "backrooms": {"name": "Backrooms", "keywords": ["backrooms", "yellow wallpaper", "fluorescent", "infinite", "horror"], "description": "Infinite empty rooms horror aesthetic"},
    "mallsoft": {"name": "Mallsoft", "keywords": ["mallsoft", "vaporwave", "mall", "elevator music", "empty"], "description": "Deserted shopping mall ambient aesthetic"},
    "seapunk": {"name": "Seapunk", "keywords": ["seapunk", "ocean", "3D dolphins", "aqua", "internet"], "description": "Ocean-themed internet subculture"},
    "witch_house": {"name": "Witch House", "keywords": ["witch house", "occult", "electronic", "triangles", "dark"], "description": "Dark electronic occult music aesthetic"},
    "dark_wave": {"name": "Darkwave", "keywords": ["darkwave", "post-punk", "goth", "synth", "80s dark"], "description": "Dark post-punk electronic aesthetic"},

    # === PHONE / SOCIAL MEDIA AESTHETICS ===
    "instagram_aesthetic": {"name": "Instagram Aesthetic", "keywords": ["instagram", "grid", "curated", "filtered", "aesthetic feed"], "description": "Curated Instagram feed visual culture"},
    "tiktok_style": {"name": "TikTok Style", "keywords": ["tiktok", "gen z", "trend", "vertical video", "algorithm"], "description": "TikTok platform visual culture"},
    "snapchat_style": {"name": "Snapchat Style", "keywords": ["snapchat", "filter", "disappearing", "casual", "fun"], "description": "Casual ephemeral social media aesthetic"},
    "pinterest_board": {"name": "Pinterest Board", "keywords": ["pinterest", "mood board", "inspo", "organized", "aesthetic"], "description": "Pinterest-style mood board layout"},
    "tumblr_aesthetic": {"name": "Tumblr Aesthetic", "keywords": ["tumblr", "indie", "2010s", "soft grunge", "fandom"], "description": "2010s Tumblr platform aesthetic culture"},
    "vsco_girl": {"name": "VSCO Girl", "keywords": ["vsco", "hydro flask", "scrunchie", "natural", "sksksk"], "description": "VSCO filter natural girl aesthetic"},
    "be_real_style": {"name": "BeReal", "keywords": ["bereal", "authentic", "no filter", "dual camera", "real"], "description": "Authentic unfiltered photo app culture"},
    "photo_dump": {"name": "Photo Dump", "keywords": ["photo dump", "carousel", "random", "casual"], "description": "Multiple casual photos in one post"},
    "screenshot_aesthetic": {"name": "Screenshot", "keywords": ["screenshot", "UI", "notification", "messages", "phone"], "description": "Phone screenshot as visual format"},
    "notes_app": {"name": "Notes App", "keywords": ["notes app", "iPhone notes", "statement", "apology"], "description": "iPhone Notes app text statement aesthetic"},

    # === FRENCH SPECIFIC ===
    "bd_europeenne": {"name": "BD Européenne", "keywords": ["European comics", "bande dessinée", "ligne claire"], "description": "European comic book tradition"},
    "french_cartoon": {"name": "French Cartoon", "keywords": ["French cartoon", "Lucky Luke", "Asterix", "Tintin"], "description": "Classic French animated style"},
    "ligne_claire": {"name": "Ligne Claire", "keywords": ["ligne claire", "clear line", "Hergé", "Tintin", "clean"], "description": "Clean line art style by Hergé"},
    "franco_belgian": {"name": "Franco-Belgian Comics", "keywords": ["franco belgian", "BD", "Spirou", "Gaston"], "description": "French-Belgian comic tradition"},
    "parisian_chic": {"name": "Parisian Chic", "keywords": ["parisian chic", "effortless", "striped", "beret", "elegant"], "description": "Classic Parisian fashion aesthetic"},
    "french_new_wave": {"name": "French New Wave Cinema", "keywords": ["nouvelle vague", "Godard", "Truffaut", "60s", "black white"], "description": "1960s French cinema movement"},
    "banlieue_style": {"name": "Banlieue", "keywords": ["banlieue", "suburb", "cité", "urban France", "HLM"], "description": "French suburban urban culture aesthetic"},
    "guinguette": {"name": "Guinguette", "keywords": ["guinguette", "Marne", "dance", "retro France", "outdoor"], "description": "Traditional French riverside dance hall"},
    "bistro_aesthetic": {"name": "Bistro", "keywords": ["bistro", "café", "Paris", "terrace", "wine", "zinc"], "description": "Classic French café atmosphere"},
    "french_riviera": {"name": "French Riviera", "keywords": ["riviera", "Côte d'Azur", "Mediterranean", "glamour", "yacht"], "description": "Glamorous French Riviera coastal aesthetic"},
    "provence_style": {"name": "Provence", "keywords": ["Provence", "lavender", "sunflower", "south France", "rustic"], "description": "Provençal countryside aesthetic"},
    "haussmann": {"name": "Haussmann Architecture", "keywords": ["Haussmann", "Paris", "balcony", "limestone", "bourgeois"], "description": "Classic Parisian building architecture"},

    # === FRENCH BDs (BANDE DESSINÉE) ===
    "titeuf": {"name": "Titeuf", "keywords": ["Titeuf", "Nadia", "smiley", "teen humor", "Swiss"], "description": "Swiss teen humor comic"},
    "tintin": {"name": "Tintin", "keywords": ["Tintin", "Hergé", "ligne claire", "adventure", "Snowy"], "description": "Classic Hergé adventure comic"},
    "asterix": {"name": "Astérix", "keywords": ["Astérix", "Obélix", "Gauls", "potion", "Romans"], "description": "Iconic French-Gaulish adventure comic"},
    "lucky_luke": {"name": "Lucky Luke", "keywords": ["Lucky Luke", "Jolly Jumper", "cowboy", "Morris"], "description": "French cowboy comic series"},
    "blake_mortimer": {"name": "Blake et Mortimer", "keywords": ["Blake", "Mortimer", "E.P. Jacobs", "thriller", "détective"], "description": "Belgian detective adventure comic"},
    "spirou": {"name": "Spirou", "keywords": ["Spirou", "Gaston", "Fantasio", "Dupuis"], "description": "Belgian adventure comedy comic"},
    "les_cites_obscures": {"name": "Les Cités Obscures", "keywords": ["Cités Obscures", "Schuiten", "Peeters", "fantasy city"], "description": "Fantastical architectural comic"},
    "valerian": {"name": "Valérian", "keywords": ["Valérian", "Laureline", "spatio-temporel", "sci-fi"], "description": "French sci-fi space adventure comic"},
    "xiii": {"name": "XIII", "keywords": ["XIII", "William Vance", "complot", "amnésie"], "description": "French conspiracy thriller comic"},
    "largo_winch": {"name": "Largo Winch", "keywords": ["Largo Winch", "business", "action", "thriller"], "description": "Business action thriller comic"},
    "akira_style": {"name": "Akira", "keywords": ["Akira", "Otomo", "manga", "cyberpunk", "Neo Tokyo"], "description": "Katsuhiro Otomo cyberpunk manga style"},
    "le_chat": {"name": "Le Chat", "keywords": ["Le Chat", "Philippe Geluck", "philosophical", "cat", "humor"], "description": "Geluck philosophical cat humor"},
    "schtroumpfs": {"name": "Les Schtroumpfs", "keywords": ["Schtroumpfs", "Smurfs", "Peyo", "blue", "village"], "description": "Peyo blue village characters"},
    "gaston_lagaffe": {"name": "Gaston Lagaffe", "keywords": ["Gaston", "Lagaffe", "office", "inventions", "lazy"], "description": "Clumsy office worker comedy"},
    "le_petit_prince": {"name": "Le Petit Prince", "keywords": ["Petit Prince", "Saint-Exupéry", "rose", "stars", "desert"], "description": "Saint-Exupéry watercolor storybook style"},
    "persepolis": {"name": "Persepolis", "keywords": ["Persepolis", "Marjane Satrapi", "black white", "Iran"], "description": "Satrapi black and white autobiographical style"},
    "enki_bilal": {"name": "Enki Bilal", "keywords": ["Enki Bilal", "painted", "sci-fi", "political", "dark"], "description": "Bilal painted sci-fi political style"},
    "moebius": {"name": "Moebius / Jean Giraud", "keywords": ["Moebius", "Giraud", "sci-fi", "detailed", "psychedelic"], "description": "Moebius detailed sci-fi illustration"},
}

def analyze_topic_pillar_match(title, summary):
    """Match topic to editorial pillars"""
    text = (title + " " + summary).lower()
    matched = []
    
    for pillar_id, pillar in PILLARS.items():
        score = 0
        for kw in pillar["keywords"]:
            if kw.lower() in text:
                score += 1
        if score > 0:
            matched.append({
                "pillar": pillar_id,
                "name": pillar["name"],
                "position": pillar["position"],
                "score": score
            })
    
    return sorted(matched, key=lambda x: x["score"], reverse=True)

def calculate_virality_score(topic, pillars):
    """Calculate virality potential score (0-100)"""
    score = 0
    
    # Factor 1: Pillar alignment (25%)
    if pillars:
        score += min(25, len(pillars) * 10)
    
    # Factor 2: Emotional intensity in title (25%)
    emotional_words = ["scandale", "crise", "fiasco", "colère", "débat", "rupture", "mort", "tuer", "exploser", "faux", "menteur"]
    title_lower = topic.get("title", "").lower()
    emotional_count = sum(1 for w in emotional_words if w in title_lower)
    score += min(25, emotional_count * 8)
    
    # Factor 3: Specificity (names, numbers) (20%)
    has_number = any(c.isdigit() for c in topic.get("title", ""))
    has_name = any(c.isupper() for c in topic.get("title", ""))
    if has_number:
        score += 10
    if has_name:
        score += 10
    
    # Factor 4: Meme potential keywords (15%)
    meme_words = ["macron", "le pen", "mélenchon", "attal", "retraite", "immigration", "europe", "brussels"]
    if any(w in title_lower for w in meme_words):
        score += 15
    
    # Factor 5: Timeliness (15%)
    # Fresh topics get boost
    score += 15  # All topics from today get this
    
    return min(100, score)

def generate_opportunities(topics, top_n=5):
    """Generate ranked content opportunities"""
    opportunities = []
    
    for topic in topics[:20]:  # Top 20 topics
        title = topic.get("title", "")
        summary = topic.get("summary", "")[:200]
        
        # Match to pillars
        pillars = analyze_topic_pillar_match(title, summary)
        
        # Calculate virality score
        virality = calculate_virality_score(topic, pillars)
        
        if pillars and virality > 30:
            # Generate character/world combos
            combos = generate_character_world_combos(title, pillars)
            
            opportunities.append({
                "topic": title,
                "summary": summary,
                "pillars": pillars,
                "virality_score": virality,
                "combos": combos[:3],  # Top 3 combos
                "humor_mechanic": pick_humor_mechanic(title, pillars),
                "hook_suggestion": generate_hook(title, pillars[0]),
                "why_viral": explain_virality(title, pillars)
            })
    
    # Sort by virality
    opportunities.sort(key=lambda x: x["virality_score"], reverse=True)
    
    return opportunities[:top_n]

def generate_character_world_combos(topic, pillars):
    """Generate character × world combinations"""
    topic_lower = topic.lower()
    combos = []
    
    for char_id, char in CHARACTERS.items():
        # Check if character mentioned
        if char["name"].lower() in topic_lower or char_id in topic_lower:
            for world_id, world in WORLDS.items():
                combo = {
                    "character": char["name"],
                    "world": world["name"],
                    "aesthetic": world["aesthetic"],
                    "format": world["format_fit"][0] if world["format_fit"] else "generic"
                }
                combos.append(combo)
    
    # If no specific character, create generic combos
    if not combos:
        default_char = CHARACTERS["macron"]
        for world_id, world in list(WORLDS.items())[:3]:
            combos.append({
                "character": default_char["name"],
                "world": world["name"],
                "aesthetic": world["aesthetic"],
                "format": world["format_fit"][0] if world["format_fit"] else "generic"
            })
    
    return combos

def pick_humor_mechanic(topic, pillars):
    """Pick best humor mechanic for topic"""
    topic_lower = topic.lower()
    
    # Escalation for dramatic topics
    if any(w in topic_lower for w in ["crise", "scandale", "expliquer", "pourquoi"]):
        return "escalation"
    
    # Recognition for relatable topics  
    if any(w in topic_lower for w in ["politique", "gouvernement", "pouvoir"]):
        return "recognition"
    
    # Juxtaposition for everything else
    return "juxtaposition"

def generate_hook(topic, pillar):
    """Generate scroll-stopping hook"""
    hooks = [
        f"Ce que {topic.split()[0]} ne veut pas que vous sachiez sur...",
        f"La vérité sur {topic[:50]}...",
        f"Pourquoi {topic.split()[0]} va devoir s'expliquer...",
        f"Le problème avec {topic[:40]} en 60 secondes",
    ]
    return hooks[0] if hooks else f"🧵 {topic}"

def explain_virality(topic, pillars):
    """Explain WHY this will go viral"""
    reasons = []
    
    if pillars:
        reasons.append(f"Maps to {pillars[0]['name']} pillar")
    
    if "macron" in topic.lower():
        reasons.append("Macron content always performs")
    
    if any(w in topic.lower() for w in ["retraite", "argent", "prix"]):
        reasons.append("Economic anxiety = shares")
    
    if len(topic) < 50:
        reasons.append("Short title = screenable")
    
    return " + ".join(reasons) if reasons else "Strong emotional hook"

def rank_opportunities(scan_results):
    """Main function - rank opportunities from scan results"""
    print("\n" + "="*60)
    print("🎯 VIRAL OPPORTUNITY ENGINE")
    print("="*60)
    
    # Extract topics from scan results
    topics = []
    for source in scan_results.get("sources", []):
        if source.get("type") == "news" and "data" in source:
            data = source["data"]
            if "top_political" in data:
                topics.extend(data["top_political"])
    
    if not topics:
        # Use sample topics if no scan data
        topics = [
            {"title": "Mort de Quentin Deranque - LFI sous pression", "summary": "La mort d'un militant d'extrême droite fait des vagues"},
            {"title": "Epstein - Le scandale qui menace Trump", "summary": "Nouvelles révélations sur les liens"}
        ]
    
    print(f"\n📊 Analyzing {len(topics)} topics...")
    
    # Generate opportunities
    opportunities = generate_opportunities(topics, top_n=5)
    
    print(f"\n🔥 TOP {len(opportunities)} OPPORTUNITIES:")
    print("="*60)
    
    for i, opp in enumerate(opportunities, 1):
        print(f"\n{i}. {opp['topic']}")
        print(f"   📈 Score: {opp['virality_score']}/100")
        print(f"   🏷️ Pillars: {', '.join([p['name'] for p in opp['pillars']])}")
        print(f"   🎭 Humor: {opp['humor_mechanic']}")
        print(f"   🎬 {opp['combos'][0]['character']} × {opp['combos'][0]['world']}")
        print(f"   💡 {opp['why_viral']}")
    
    # Save
    result = {
        "timestamp": datetime.now().isoformat(),
        "topics_analyzed": len(topics),
        "opportunities": opportunities
    }
    
    with open("/tmp/viral_opportunities.json", "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print("\n✅ Saved to /tmp/viral_opportunities.json")
    return result

if __name__ == "__main__":
    # Demo with sample data
    sample_scan = {
        "sources": [{
            "type": "news",
            "data": {
                "top_political": [
                    {"title": "Mort de Quentin Deranque - LFI sous pression", "summary": "La mort d'un militant d'extrême droite à Lyon provoque une crise politique"},
                    {"title": "Epstein - Le scandale frappe Trump", "summary": "Nouvelles archives publiées sur le prédateur"},
                    {"title": "Retraites - Le gouvernement recule", "summary": "Nouvelle réforme面对巨大的抗议"}
                ]
            }
        }]
    }
    
    rank_opportunities(sample_scan)
