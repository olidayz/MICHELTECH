#!/usr/bin/env python3
"""
COMPREHENSIVE FRENCH POLITICIAN DATABASE
For MEME MACHINE Character Bible
"""
from datetime import datetime

# ============================================
# PRESIDENTIELLE
# ============================================
PRESIDENT = {
    "macron": {
        "name": "Emmanuel Macron",
        "role": "Président de la République",
        "party": "Renaissance (ex-LREM)",
        "archetype": "Out-of-touch elite / Napoleon complex",
        "traits": [
            "Arrogant", "Condescending", "Out of touch", 
            "Jupiterian", "Elitist", "Tech-bro", " Authoritarian",
            "Smug", "Dismissive", "Patronizing"
        ],
        "catchphrases": [
            "Je suis le responsable", "En même temps",
            "Make our planet great again", "Start-up nation"
        ],
        "memes": [
            "Jupiter", "Pharaoh", "Napoléon", " techno-optimist",
            "Blings", "The walk"
        ],
        "visual_hooks": [
            "Walking away from protests",
            "Fancy restaurants",
            "Expensive watches",
            "Young wife",
            "Ego trips"
        ],
        "worlds": ["Animal Crossing", "GTA", "Dark Souls", "Mario Kart", "The Sims", "Minecraft"],
        "best_formats": ["Juxtaposition", "Deflation", "Recognition"]
    }
}

# ============================================
# GOVERNMENT - Prime Minister & Ministers
# ============================================
GOVERNMENT = {
    "lecornu": {
        "name": "Sébastien Lecornu",
        "role": "Premier Ministre",
        "party": "Horizons",
        "archetype": "Technocrat soldier",
        "traits": ["Serious", "Military background", "Dry", "Competent but boring"],
        "worlds": ["Dark Souls", "Call of Duty", "War simulation"],
        "best_formats": ["Deflation", "Escalation"]
    },
    "attal": {
        "name": "Gabriel Attal",
        "role": "Porte-parole du gouvernement",
        "party": "Renaissance",
        "archetype": "Junior spokesperson / Golden boy",
        "traits": ["Nervous", "Scripted", "Defensive", "Young", "Eager to please", "Smug"],
        "visual_hooks": ["Sweating", "Reading script", "Getting interrupted"],
        "worlds": ["Mario Kart", "School presentation", "Job interview"],
        "best_formats": ["Juxtaposition", "Recognition"]
    },
    "dati": {
        "name": "Rachida Dati",
        "role": "Garde des Sceaux, Ministre de la Justice",
        "party": "LR (divers droite)",
        "archetype": "Tough cop / From the projects to power",
        "traits": ["Fierce", "Combative", "Flashy", "Controversial"],
        "visual_hooks": ["Bold outfits", "Strong statements", "court appearances"],
        "worlds": ["GTA", "Law & Order", "Courtroom drama"],
        "best_formats": ["Juxtaposition", "Deflation"]
    },
    "pannier_runacher": {
        "name": "Agnès Pannier-Runacher",
        "role": "Ministre de la Transition écologique",
        "party": "Renaissance",
        "archetype": "Corporate climate minister",
        "traits": ["Pro-nuclear", "Business-friendly", "Technical", "Boring"],
        "worlds": ["SimCity", "Corporate meeting", "Power plant tour"],
        "best_formats": ["Recognition", "Juxtaposition"]
    },
    "armand": {
        "name": "Antoine Armand",
        "role": "Ministre de l'Économie",
        "party": "Renaissance",
        "archetype": "Tech minister",
        "traits": ["Young", "Tech-savvy", "Pro-business"],
        "worlds": ["Startup pitch", "Silicon Valley fantasy"],
        "best_formats": ["Juxtaposition"]
    },
    "darrieussecq": {
        "name": "Geneviève Darrieussecq",
        "role": "Ministre de la Santé",
        "party": "MoDem",
        "archetype": "Steady hand",
        "traits": ["Bureaucratic", "Calm", "Unremarkable"],
        "worlds": ["Hospital drama", "Administrative office"],
        "best_formats": ["Recognition"]
    },
    "christophe": {
        "name": "Paul Christophe",
        "role": "Ministre des Solidarités",
        "party": "Horizons",
        "archetype": "Quiet fixer",
        "traits": ["Low profile", "Competent", "Boring"],
        "worlds": ["Social services", "Office work"],
        "best_formats": ["Recognition"]
    },
    "letard": {
        "name": "Valérie Letard",
        "role": "Ministre du Logement",
        "party": "UDI",
        "archetype": "Housing minister",
        "traits": ["Technical", "Underfunded"],
        "worlds": ["Construction site", "Budget meeting"],
        "best_formats": ["Recognition"]
    },
    "barrot": {
        "name": "Jean-Noël Barrot",
        "role": "Ministre des Affaires étrangères",
        "party": "MoDem",
        "archetype": "Diplomat",
        "traits": ["Low profile", "Professional"],
        "worlds": ["Summit meeting", "Fancy dinner"],
        "best_formats": ["Deflation"]
    }
}

# ============================================
# OPPOSITION - Les Républicains (LR)
# ============================================
REPUBLICANS = {
    "wauquiez": {
        "name": "Laurent Wauquiez",
        "role": "Président LR",
        "party": "Les Républicains",
        "archetype": "Right-wing leader / Conservative hope",
        "traits": ["Ambitious", "Conservative", "Catholic", "Regional", "Serious"],
        "visual_hooks": ["Skiing", "Auvergne", "Conservative gestures"],
        "worlds": ["Medieval", "Ski resort", "Conservative dinner"],
        "best_formats": ["Juxtaposition", "Recognition"]
    },
    "ciotti": {
        "name": "Eric Ciotti",
        "role": "Dé LR",
        "party": "Les Républicains",
        "archetype": "Hard right / Trump-like",
        "traits": ["Hardline", "Provocative", "Right-wing populist"],
        "catchphrases": ["La Droite", "France d'abord"],
        "worlds": ["GTA", "Action movie"],
        "best_formats": ["Juxtaposition", "Escalation"]
    },
    "sarkozy": {
        "name": "Nicolas Sarkozy",
        "role": "Ancien Président",
        "party": "LR (historique)",
        "archetype": "Combover / Comeback king",
        "traits": ["Hyperactive", "Combative", "Wealthy", "Controversial", "Old school"],
        "memes": ["Combover", "Karcher", "Casse-tête", "Bling"],
        "visual_hooks": ["Tennis", "Nice", "Expensive cars", "Sunglasses"],
        "worlds": ["GTA", "Casino", "Action movie"],
        "best_formats": ["Deflation", "Juxtaposition", "Recognition"]
    },
    "fillon": {
        "name": "François Fillon",
        "role": "Ancien Premier Ministre",
        "party": "LR (historique)",
        "archetype": "Scandalized ex-PM",
        "traits": ["Boring", "Scandal-tarized", "Serious"],
        "memes": ["Penelopegate", "The suit"],
        "worlds": ["courtroom", " Unemployment line"],
        "best_formats": ["Deflation", "Recognition"]
    },
    "juppe": {
        "name": "Alain Juppé",
        "role": "Ancien Premier Ministre",
        "party": "LR (historique)",
        "archetype": "Old guard",
        "traits": ["Bureaucratic", "Boring", "Old school"],
        "worlds": ["Retirement home", "Bureaucracy"],
        "best_formats": ["Recognition"]
    },
    "pezet": {
        "name": "Laurent Pezet",
        "role": "Dé LR",
        "party": "Les Républicains",
        "archetype": "Right-wing firebrand",
        "traits": ["Combative", "Pro-vaccine", "Controversial"],
        "worlds": ["Debate", "Social media"],
        "best_formats": ["Juxtaposition"]
    }
}

# ============================================
# RASSEMBLEMENT NATIONAL (RN)
# ============================================
RN = {
    "lepen": {
        "name": "Marine Le Pen",
        "role": "Présidente RN",
        "party": "Rassemblement National",
        "archetype": "Anti-establishment champion / Populist leader",
        "traits": ["Strong", "Defiant", "Underdog", "Controversial", "Populist"],
        "catchphrases": ["Le peuple", "La France d'abord", "Immigration zéro"],
        "memes": ["Neck", "The gaze", "Gavel"],
        "visual_hooks": ["Strong pose", "Speaking to crowds", "Legal battles"],
        "worlds": ["Game of Thrones", "GTA", "War movie", "Epic fantasy"],
        "best_formats": ["Recognition", "Juxtaposition (against her)"]
    },
    "bardella": {
        "name": "Jordan Bardella",
        "role": "Président par interim RN",
        "party": "Rassemblement National",
        "archetype": "Young rising star / MEP",
        "traits": ["Young", "Media-savvy", "Smooth", "Populist"],
        "visual_hooks": ["Smooth interviews", "European Parliament"],
        "worlds": ["Student council", "Debate club"],
        "best_formats": ["Recognition", "Juxtaposition"]
    },
    "dupont_aignan": {
        "name": "Nicolas Dupont-Aignan",
        "role": "Dé FN/RN",
        "party": "RN",
        "archetype": "Lone wolf",
        "traits": ["Independent", "Gaullist", "Populist right"],
        "worlds": ["Solo mission", "One man army"],
        "best_formats": ["Recognition"]
    },
    "collard": {
        "name": "Gilbert Collard",
        "role": "Avocat / Dé RN",
        "party": "RN",
        "archetype": "Controversial lawyer",
        "traits": ["Combative", "Legal", "Controversial"],
        "worlds": ["Courtroom", "TV debate"],
        "best_formats": ["Juxtaposition"]
    },
    "mollon": {
        "name": "Jean-Paul Mollon",
        "role": "Dé RN",
        "party": "RN",
        "archetype": "Lesser known RN figure",
        "traits": ["Low profile"],
        "worlds": ["Background"],
        "best_formats": ["Recognition"]
    }
}

# ============================================
# LA FRANCE INSoumise (LFI)
# ============================================
LFI = {
    "melenchon": {
        "name": "Jean-Luc Mélenchon",
        "role": "Fondateur / Dé Insoumis",
        "party": "La France Insoumise",
        "archetype": "Theatrical radical / Firebrand",
        "traits": ["Dramatic", "Angry", "Grand gestures", "Theatrical", "Divisive"],
        "catchphrases": ["La Marseillaise", "Le peuple", "C'est la crise"],
        "memes": ["The scream", "Fist pump", "Theatrical speeches", "Cuba"],
        "visual_hooks": ["Screaming", "Dramatic gestures", "Stage presence", "Cuba vacations"],
        "worlds": ["Opera", "Epic fantasy", "GTA", "Revolutionary drama", "Shakespeare"],
        "best_formats": ["Escalation", "Juxtaposition", "Deflation"]
    },
    "ruffin": {
        "name": "François Ruffin",
        "role": "Dé LFI",
        "party": "La France Insoumise",
        "archetype": "Documentarian / Populist left",
        "traits": ["Documentary-maker", "Populist", "Authentic", "Working class hero"],
        "worlds": ["Documentary", "Working class France"],
        "best_formats": ["Recognition", "Juxtaposition"]
    },
    "poutou": {
        "name": "Philippe Poutou",
        "role": "Candidat NPA/LFI",
        "party": "NPA",
        "archetype": "Anticapitalist / Anti-establishment",
        "traits": ["Anti-capitalist", "Autoworker", "Authentic", "Humorous"],
        "memes": ["The car factory", "Worker's hands"],
        "worlds": ["Factory", "Protest", "Labor strike"],
        "best_formats": ["Recognition", "Juxtaposition"]
    },
    "arthaud": {
        "name": "Nathalie Arthaud",
        "role": "Porte-parole NPA",
        "party": "NPA",
        "archetype": "Far-left anticapitalist",
        "traits": ["Radical", "Anti-capitalist"],
        "worlds": ["Protest", "Revolution"],
        "best_formats": ["Recognition"]
    },
    "hautin": {
        "name": "Manon Aubry",
        "role": "Dé LFI / ex-eurodéputée",
        "party": "La France Insoumise",
        "archetype": "Young left-wing voice",
        "traits": ["Young", "Combative", "Media presence"],
        "worlds": ["European Parliament", "TV debates"],
        "best_formats": ["Recognition", "Juxtaposition"]
    }
}

# ============================================
# SOCIALISTES (PS)
# ============================================
SOCIALISTS = {
    "faure": {
        "name": "Olivier Faure",
        "role": "Premier Secrétaire PS",
        "party": "Parti Socialiste",
        "archetype": "Party manager",
        "traits": ["Party loyalist", "Bureaucratic", "Low charisma"],
        "worlds": ["Party headquarters", "Bureaucracy"],
        "best_formats": ["Recognition"]
    },
    "hidalgo": {
        "name": "Anne Hidalgo",
        "role": "Maire de Paris",
        "party": "Parti Socialiste",
        "archetype": "Paris mayor / Environmentalist",
        "traits": ["Pro-bike", "Controversial", "Paris-centric", "Environment"],
        "catchphrases": ["Paris", "Vélo", "Climat"],
        "memes": ["The bike", "Parisian elitism", "Swimming in the Seine"],
        "visual_hooks": ["Bike", "Paris", "Controversial policies"],
        "worlds": ["Bicycle city", "Paris bubble", "Environmental campaign"],
        "best_formats": ["Juxtaposition", "Recognition"]
    },
    "cazebonne": {
        "name": "Sébastien Cazebonne",
        "role": "Sénateur PS",
        "party": "Parti Socialiste",
        "archetype": "PS figure",
        "traits": ["Regional"],
        "worlds": ["Local politics"],
        "best_formats": ["Recognition"]
    },
    "valls": {
        "name": "Manuel Valls",
        "role": "Ancien Premier Ministre",
        "party": "Ex-PS / Horizons",
        "archetype": "Sarkozy of the left / Social liberal",
        "traits": ["Pro-austerity", "Pro-security", "Elitist", "Controversial"],
        "memes": ["The security hardliner", "Catalonia"],
        "worlds": ["Security state", "Corporate board"],
        "best_formats": ["Deflation", "Recognition"]
    },
    "hamon": {
        "name": "Benoît Hamon",
        "role": "Ancien candidat présidentiel",
        "party": "Ex-PS / Génération.s",
        "archetype": "Idealistic left",
        "traits": ["Idealistic", "Basic income proponent", "Defeated"],
        "worlds": ["Utopia", "Lost election"],
        "best_formats": ["Recognition", "Deflation"]
    },
    "蒙特": {
        "name": "Montebourg",
        "role": "Ancien ministre",
        "party": "Ex-PS",
        "archetype": "Anti-globalization / Patriotic left",
        "traits": ["Patriotic economic", "Anti-globalization", "Charismatic"],
        "catchphrases": ["Made in France", "Buying power"],
        "worlds": ["Factory", "Economic patriotism"],
        "best_formats": ["Recognition", "Juxtaposition"]
    }
}

# ============================================
# LAREM / RENAISSANCE
# ============================================
RENAISSANCE = {
    "borne": {
        "name": "Elisabeth Borne",
        "role": "Ancienne Première Ministre",
        "party": "Renaissance",
        "archetype": "Technocrat PM / Defeated",
        "traits": ["Bureaucratic", "Low profile", "Survived no-confidence", "Resigned"],
        "memes": ["The resignation", "The 49.3"],
        "worlds": ["The hot seat", "Administrative building"],
        "best_formats": ["Deflation", "Recognition"]
    },
    "castaner": {
        "name": "Christophe Castaner",
        "role": "Ancien ministre de l'intérieur",
        "party": "Renaissance",
        "archetype": "Security minister / Scandalized",
        "traits": ["Police", "Controversial", "Loyal Macronist"],
        "worlds": ["Police headquarters", "Security"],
        "best_formats": ["Juxtaposition"]
    },
    "lehy": {
        "name": "Stéphane Le Foll",
        "role": "Ancien porte-parole",
        "party": "Renaissance",
        "archetype": "Party loyalist",
        "traits": ["Loyal", "Agricultural"],
        "worlds": ["Farm", "Party"],
        "best_formats": ["Recognition"]
    }
}

# ============================================
# CENTRE / MODEM
# ============================================
CENTRE = {
    "bayrou": {
        "name": "François Bayrou",
        "role": "Ancien Premier Ministre",
        "party": "MoDem",
        "archetype": "Kingmaker / Eternal candidate",
        "traits": ["Kingmaker", "Patronage", "Béarnais", "Long career"],
        "memes": ["The kingmaker", "Béarn"],
        "worlds": ["Kingmaker", "Regional politics"],
        "best_formats": ["Recognition", "Juxtaposition"]
    },
    "joun": {
        "name": "François Joun",
        "role": "Ministre",
        "party": "MoDem",
        "archetype": "MoDem figure",
        "traits": ["Center", "Pro-European"],
        "worlds": ["Center", "Brussels"],
        "best_formats": ["Recognition"]
    }
}

# ============================================
# AUTRES FIGURES
# ============================================
OTHERS = {
    " Zemmour": {
        "name": "Eric Zemmour",
        "role": "Candidat RN / CNews",
        "party": "Reconquête (historique)",
        "archetype": "Far-right polemicist / TV personality",
        "traits": ["Controversial", "Polemicist", "TV star", "Divisive", "Anti-immigration"],
        "catchphrases": ["Grand remplacement", "Decadence"],
        "memes": ["The finger", "TV confrontations", "The trial"],
        "visual_hooks": ["Finger point", "TV debates", "Courtroom"],
        "worlds": ["TV show", "Courtroom", "Polemic"],
        "best_formats": ["Juxtaposition", "Escalation", "Deflation"]
    },
    "asselineau": {
        "name": "François Asselineau",
        "role": "Candidat Frexit",
        "party": "UPR",
        "archetype": "Frexit obsessive",
        "traits": ["Frexit only", "Obsessive", "Iconic"],
        "memes": ["The Frexit guy", "Always the same speech"],
        "worlds": ["One issue", "Protest"],
        "best_formats": ["Recognition", "Juxtaposition"]
    },
    "philippe": {
        "name": "Edouard Philippe",
        "role": "Ancien PM / Maire du Havre",
        "party": "Horizons",
        "archetype": "Smooth operator / Future candidate",
        "traits": ["Smooth", "Charismatic", "Ambiguous", "Future presidential"],
        "catchphrases": ["En même temps"],
        "worlds": ["The Hague", "Future", "Smooth interview"],
        "best_formats": ["Recognition", "Juxtaposition"]
    },
    "peillon": {
        "name": "Vincent Peillon",
        "role": "Ancien ministre",
        "party": "Ex-PS",
        "archetype": "Philosophy professor turned politician",
        "traits": ["Academic", "Controversial"],
        "worlds": ["University", "Philosophy class"],
        "best_formats": ["Juxtaposition"]
    },
    "yade": {
        "name": "Rama Yade",
        "role": "Ancienne ministre",
        "party": "Ex-PS / Libéraux",
        "archetype": "Rising star / Lost",
        "traits": ["Diplomat", "Charismatic"],
        "worlds": ["Diplomacy", "UN"],
        "best_formats": ["Recognition"]
    }
}

# ============================================
# COMPILE ALL
# ============================================
def compile_all_characters():
    """Compile all characters into one database"""
    all_characters = {}
    
    all_characters.update(PRESIDENT)
    all_characters.update(GOVERNMENT)
    all_characters.update(REPUBLICANS)
    all_characters.update(RN)
    all_characters.update(LFI)
    all_characters.update(SOCIALISTS)
    all_characters.update(RENAISSANCE)
    all_characters.update(CENTRE)
    all_characters.update(OTHERS)
    
    return all_characters

# Generate JSON
if __name__ == "__main__":
    import json
    
    characters = compile_all_characters()
    
    # Save as JSON
    with open("/home/oli/.openclaw/workspace/meme-machine/character_bible.json", "w") as f:
        json.dump(characters, f, ensure_ascii=False, indent=2)
    
    # Print summary
    print("\n" + "="*60)
    print("📋 FRENCH POLITICIAN DATABASE")
    print("="*60)
    
    categories = {
        "Président": PRESIDENT,
        "Gouvernement": GOVERNMENT,
        "Les Républicains": REPUBLICANS,
        "Rassemblement National": RN,
        "La France Insoumise": LFI,
        "Parti Socialiste": SOCIALISTS,
        "Renaissance": RENAISSANCE,
        "Centre/MoDem": CENTRE,
        "Autres": OTHERS
    }
    
    total = 0
    for cat, chars in categories.items():
        print(f"\n{cat}: {len(chars)}")
        for key, char in chars.items():
            print(f"  - {char['name']} ({char.get('role', 'N/A')})")
            total += 1
    
    print(f"\n\n📊 TOTAL: {total} politicians")
    print(f"\n✅ Saved to meme-machine/character_bible.json")
