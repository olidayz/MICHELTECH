# MEME MACHINE — Full System Specification

## Political Absurdist Content Engine for French Right-Wing Short-Form Media

**Version**: 1.0
**Infrastructure**: OpenClaw + Claude API + Supabase
**Author**: Oli / Kiki Studios

---

## Overview

An automated intelligence and creative pipeline that:

1. Continuously monitors French political/social trends AND global internet culture
2. Generates absurdist short-form content concepts (memes, 15-60s shorts)
3. Maps audiences, embeds editorial messaging, and scores virality potential
4. Produces ready-to-assemble production packages (image prompts, scripts, edit blueprints)
5. Learns from performance data to improve over time

The system operates in two modes:
- **Autopilot**: Scans, ranks, and generates concepts on a scheduled cadence
- **Manual Injection**: User inputs a topic, policy, theme, or vague idea → full pipeline runs on it

---

## System Architecture

```
┌─────────────────────────────────────────────────────┐
│                    INGESTION LAYER                    │
│                                                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐ │
│  │ French   │ │ Social   │ │ Cultural │ │ Format  │ │
│  │ News/X   │ │ Media    │ │ Verticals│ │ Intel   │ │
│  │ Politics │ │ TikTok/IG│ │ Gaming/  │ │ What's  │ │
│  │ Trends   │ │ YouTube  │ │ Anime/   │ │ Working │ │
│  │          │ │ Reddit   │ │ Music/   │ │ Now     │ │
│  │          │ │          │ │ Sports   │ │         │ │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬────┘ │
│       └──────────┬──┴───────────┴──────────┬──┘      │
│                  ▼                          ▼         │
│          ┌──────────────┐     ┌──────────────────┐   │
│          │ TOPIC RANKING│     │ CROSS-POLLINATION│   │
│          │ & EDITORIAL  │     │ ENGINE           │   │
│          │ FILTERING    │     │ (Module 13)      │   │
│          └──────┬───────┘     └────────┬─────────┘   │
│                 └───────────┬──────────┘              │
│                             ▼                         │
│                  ┌─────────────────┐                  │
│          ┌──────►│ CREATIVE ENGINE │◄──────┐          │
│          │       │ (Core Brain)    │       │          │
│          │       └────────┬────────┘       │          │
│          │                │                │          │
│   ┌──────┴──────┐        │        ┌───────┴───────┐  │
│   │ CHARACTER   │        │        │ VIRALITY      │  │
│   │ BIBLE       │        │        │ FRAMEWORK     │  │
│   └─────────────┘        │        └───────────────┘  │
│                          ▼                            │
│              ┌───────────────────┐                    │
│              │ DAILY BRIEF       │                    │
│              │ → WhatsApp/TG     │                    │
│              └─────────┬─────────┘                    │
│                        │ [USER GREENLIGHTS]           │
│                        ▼                              │
│              ┌───────────────────┐                    │
│              │ PRODUCTION        │                    │
│              │ PACKAGE           │                    │
│              │ GENERATOR         │                    │
│              └─────────┬─────────┘                    │
│                        │ [USER POSTS]                 │
│                        ▼                              │
│              ┌───────────────────┐                    │
│              │ PERFORMANCE       │                    │
│              │ FEEDBACK LOOP     │                    │
│              └───────────────────┘                    │
└─────────────────────────────────────────────────────┘
```

---

## Module 1 — Trend Ingestion

**Purpose**: Continuously scan French political and social landscape for trending topics.

**Schedule**: Every 4-6 hours via OpenClaw cron job.

### Sources

| Source | Method | What to Extract |
|--------|--------|-----------------|
| X/Twitter FR | Apify Twitter Scraper or X API | Trending hashtags FR, high-engagement political tweets, quote tweet ratio (indicates controversy) |
| Le Monde, Le Figaro, Libération, Mediapart | RSS feeds | Headlines, topic clustering, framing differences between outlets |
| CNews, Valeurs Actuelles, BFM | RSS feeds | Right-leaning coverage angles, talking points already in circulation |
| Google Trends FR | PyTrends library | Search volume spikes, breakout queries, rising topics |
| Reddit r/france, r/rance | Reddit API | What's being discussed/mocked, comment sentiment, meme formats emerging |
| YouTube Trending FR | Apify YouTube Scraper | Political commentary videos gaining traction, comment themes |

### Output Schema (per topic)

```json
{
  "topic_id": "uuid",
  "title": "Macron pension reform speech",
  "summary": "2-3 sentence summary of the topic",
  "sources": ["le_monde", "x_trending", "google_trends"],
  "engagement_signals": {
    "x_tweet_volume": 45000,
    "x_avg_engagement_rate": 4.2,
    "google_trend_score": 87,
    "reddit_thread_count": 12,
    "reddit_avg_comments": 340
  },
  "sentiment": "outrage/mockery/confusion/fear/exhaustion",
  "time_sensitivity": "hot_now | simmering | evergreen",
  "hours_until_stale": 12,
  "first_detected": "2026-02-09T08:00:00Z",
  "raw_quotes": ["notable quotes from politicians/commentators"],
  "media_framings": {
    "left": "summary of left framing",
    "right": "summary of right framing",
    "mainstream": "summary of mainstream framing"
  }
}
```

### Storage

Supabase table: `trending_topics`

---

## Module 2 — Format Intelligence

**Purpose**: Monitor what creative formats are currently performing on short-form platforms, specifically in the French market.

**Schedule**: Every 6-8 hours via OpenClaw cron job.

### Sources

| Source | Method | What to Extract |
|--------|--------|-----------------|
| TikTok FR | Apify TikTok Scraper + OpenClaw browser | Top performing French political/meme accounts, trending sounds FR, format patterns |
| Instagram Reels FR | Apify Instagram Scraper | Same — engagement ratios (shares + saves vs views), not just likes |
| YouTube Shorts FR | Apify YouTube Scraper | What's getting outsized engagement in FR market |

### Accounts to Monitor

[TO BE FILLED BY USER — list of 20-30 French accounts across political memes, general memes, satire, commentary]

### What to Extract Per Post

```json
{
  "post_id": "uuid",
  "platform": "tiktok | instagram | youtube",
  "account": "@accountname",
  "account_followers": 125000,
  "views": 2400000,
  "likes": 180000,
  "comments": 4500,
  "shares": 32000,
  "saves": 8000,
  "engagement_ratio": 9.3,
  "virality_score": "shares / followers ratio",
  "format_type": "POV | fake_text_convo | game_footage_voiceover | silent_captions | reaction | sketch | monologue | edit_compilation",
  "hook_type": "absurd_image_cold_open | text_first_frame | zoom_reveal | question_hook | pattern_interrupt",
  "hook_description": "Description of what the first 1-2 seconds show",
  "audio_type": "trending_sound | original_audio | voiceover | no_audio_text_only",
  "audio_id": "TikTok sound ID if applicable",
  "edit_style": "fast_cuts | slow_reveal | single_shot | transition_heavy",
  "duration_seconds": 18,
  "text_overlay": true,
  "is_political": true,
  "topic_if_political": "immigration",
  "detected_at": "2026-02-09T10:00:00Z"
}
```

### Format Trend Report

The system aggregates individual posts into a rolling trend report:

- **Hot formats this week**: Top 5 format/hook combinations by average virality score
- **Rising sounds**: Audio trending upward in FR market
- **Declining formats**: Formats showing engagement decay (avoid these)
- **Platform-specific winners**: What works on TikTok vs Reels vs Shorts right now

Storage: Supabase table `format_intelligence`

---

## Module 3 — Cross-Pollination Engine

**Priority**: HIGH — this is the growth engine that breaks out of the political content bubble.

**Purpose**: Monitor viral content OUTSIDE politics across all major French cultural verticals. Extract the creative DNA (format, mechanic, aesthetic, emotional trigger) and generate political adaptations.

**Schedule**: Every 4 hours — speed is critical. Format trends have a 48-72 hour window.

### Cultural Verticals to Monitor

| Vertical | Why | Specific Sources |
|----------|-----|------------------|
| Gaming | Huge overlap with target demo, visual language of game worlds is your content medium | Twitch FR clips, gaming TikTok FR, Twitter gaming FR, r/jeuxvideo |
| Anime/Manga | France is biggest market outside Japan, massive engaged community | Anime TikTok FR, anime edit trends, r/animefrance |
| Football | Universal emotional triggers, celebration/defeat memes spread fast | Ligue 1 memes, Champions League moments, transfer drama accounts |
| French Rap | Cultural backbone of young France, audio trends originate here | Booba, SDM, Ninho, PLK — track new releases, viral clips, beef moments |
| Reality TV | Insane engagement in France, formats are highly memeable | Les Marseillais, Koh-Lanta reaction formats |
| Global Viral | US/international content that crosses into French feeds | r/all top posts, global TikTok trending |
| Internet Culture | French-specific meme evolution | French meme pages (Neurchi de X), copypastas, inside jokes |

### Extraction — Creative DNA (not the topic)

For each viral non-political piece of content, extract:

```json
{
  "source_content_id": "uuid",
  "vertical": "gaming | anime | football | rap | reality_tv | global | internet_culture",
  "platform": "tiktok | instagram | youtube | twitter | twitch",
  "virality_metrics": { "views": 0, "shares": 0, "engagement_ratio": 0 },
  "creative_dna": {
    "format_structure": "Description of the edit pattern / format skeleton",
    "emotional_mechanic": "What feeling this triggers — recognition, outrage, absurdity, nostalgia, schadenfreude",
    "visual_language": "Aesthetic, reference style, color palette, game world",
    "audio_signature": "Sound, music trend, voice pattern, beat timing",
    "community_language": "Slang, inside jokes, references that signal belonging",
    "shareability_trigger": "Why people share this — 'this is so me' | 'my friend needs to see this' | 'I can't believe this exists' | 'I need to argue about this'"
  },
  "political_adaptation_potential": "high | medium | low",
  "freshness_window_hours": 48,
  "detected_at": "timestamp"
}
```

### Political Adaptation Generation

For each high-potential cross-pollination opportunity, the system generates:

```
CROSS-POLLINATION ALERT
━━━━━━━━━━━━━━━━━━━━━━

Source: [Anime edit trend] going viral — dramatic reveal format with zoom + bass drop
Vertical: Anime
Current virality: 2.3M average views on FR TikTok
Freshness window: ~36 hours remaining

POLITICAL ADAPTATIONS:

1. Same dramatic reveal format → "What Macron actually said vs what he meant"
   Character: [Character X]
   World: Anime-style edit
   Editorial angle: Media manipulation / doublespeak

2. Same format → Reveal of actual EU regulation text vs how it was reported
   Character: [Character Y]
   World: Same anime edit aesthetic
   Editorial angle: Anti-EU / sovereignty

3. Same format → "Your député's promises vs their voting record"
   Character: None — real footage + edit
   Editorial angle: Anti-establishment
```

### Speed Pipeline

1. Cultural trend detected (viral format outside politics)
2. System immediately generates 3-5 political adaptations using character bible + editorial pillars
3. Alert sent to user via WhatsApp/Telegram: "This [vertical] format is blowing up — here are 3 ways to hijack it"
4. User greenlights → production package generated
5. User produces and posts within the freshness window

Storage: Supabase tables `cultural_trends` and `cross_pollination_concepts`

---

## Module 4 — Topic Ranking & Editorial Filtering

**Purpose**: Take raw trending topics and filter/rank them through editorial and creative lenses.

**Trigger**: Runs after each trend ingestion cycle, or immediately on manual topic injection.

### Ranking Criteria

Each topic scored 1-10 on:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Emotional intensity | 25% | How strongly are people feeling about this right now? |
| Absurdist potential | 25% | Can this be translated into a surreal visual metaphor? If not, kill it. |
| Editorial alignment | 20% | Does this map to one of our core editorial pillars? |
| Time sensitivity | 15% | How quickly does this need to be posted to matter? |
| Content gap | 15% | Is anyone else making this specific take? If yes, is ours better? |

### Editorial Pillar Mapping

[TO BE FILLED BY USER — core editorial positions]

Example framework:

| Pillar | Core Position | Emotional Register |
|--------|---------------|-------------------|
| Sovereignty | France should control its own destiny, not Brussels | Pride, frustration |
| Cultural Identity | French culture is worth preserving and celebrating | Nostalgia, defiance |
| Anti-Establishment | The political class is disconnected from real people | Mockery, anger |
| Economic Populism | The system is rigged against working/middle class | Resentment, solidarity |
| Anti-Woke | Imported ideology doesn't fit French values | Ridicule, exasperation |
| Immigration | Current policy is failing French citizens | Concern, pragmatism |
| Media Critique | Legacy media frames narratives, not reports truth | Skepticism, humor |

Each trending topic gets assigned 1-2 pillars and a specific editorial angle.

### Kill Criteria

A topic gets killed (not sent to creative engine) if:
- No clear absurdist visual metaphor comes to mind (scored < 4 on absurdist potential)
- It's already oversaturated with meme content (no content gap)
- Legal risk is too high without enough reward
- It doesn't map to any editorial pillar

### Output

Top 5-10 ranked topics with:
- Topic summary
- Editorial pillar + specific angle
- Time sensitivity flag
- Absurdist metaphor seed (initial idea for visual treatment)

Storage: Supabase table `ranked_topics`

---

## Module 5 — Audience Mapping

**Purpose**: For each ranked topic, identify exactly who this content should reach and what emotional state they're in.

### Per Topic Output

```json
{
  "topic_id": "uuid",
  "primary_audience": {
    "description": "Gen Z urban French, politically disengaged but economically anxious, 18-28",
    "platforms": ["tiktok", "instagram"],
    "content_consumption": "Memes, gaming content, French rap clips",
    "emotional_state": "Cynical, feels unheard, uses humor as coping",
    "language_register": "Informal, slang-heavy, meme-literate"
  },
  "secondary_audience": {
    "description": "Suburban parents 35-50, quietly frustrated, don't post but share privately",
    "platforms": ["facebook", "whatsapp_groups"],
    "content_consumption": "News, reality TV, family content",
    "emotional_state": "Worried about future, feels things are getting worse",
    "language_register": "Conversational, less meme-aware"
  },
  "crossover_audience": {
    "description": "Non-political audiences reachable via format (gaming, anime, football fans)",
    "entry_point": "The format/aesthetic, not the political content",
    "conversion_path": "They share because it's funny/well-made, absorb the message passively"
  },
  "content_gap": "What angle is NOT being said by other creators on this topic",
  "predicted_comment_themes": ["Top 3-5 predicted comment reactions"]
}
```

Storage: Supabase table `audience_maps`

---

## Module 6 — Meme Intelligence Engine (Core Brain)

**Purpose**: The central creative intelligence that generates absurdist short-form content concepts. This is not just a concept generator — it's a deep reasoning system that understands humor mechanics, virality physics, combination logic, platform behavior, and French cultural context. Everything else in the system is plumbing. This is the brain.

**This module absorbs the former Module 11 (Virality Framework). All virality knowledge is now integrated directly into the creative engine rather than being a separate reference.**

### Inputs

The engine receives:
1. Ranked topic + editorial angle (from Module 4)
2. Audience profile (from Module 5)
3. Current hot formats (from Module 2 — Format Intelligence)
4. Cross-pollination opportunities (from Module 3)
5. Character bible + world library (from Module 10)
6. Performance history (from Module 9 — what's worked before)
7. Meme template library (from Module 17 — proven formulas)
8. Narrative arc state (from Module 13 — running storylines)

---

### LAYER 1: Humor Mechanics

The engine must understand WHY things are funny, not just generate "funny-sounding" concepts. Every concept must be built on one or more proven humor mechanics:

#### Core Humor Mechanics

**Juxtaposition (The Primary Weapon)**
Placing something serious in an unserious context, or vice versa. The wider the tonal gap, the stronger the humor. This is the foundational mechanic of the entire content strategy — politicians in game worlds IS juxtaposition.

Subtypes:
- **Tonal juxtaposition**: Grim topic + wholesome setting (pension reform + Animal Crossing)
- **Scale juxtaposition**: Massive political issue treated as trivial (EU sovereignty debate as a Minecraft server admin dispute)
- **Competence juxtaposition**: Powerful person shown as incompetent in a simple context (Macron failing at basic Animal Crossing tasks while claiming to run a country)
- **Temporal juxtaposition**: Modern political crisis rendered in a retro or fantasy context (current immigration debate as a medieval Dark Souls scenario)

**Recognition ("C'est trop vrai")**
The audience sees their own experience reflected back. This is the most powerful shareability driver. The humor isn't in the absurdity — it's in the truth underneath.

Rules:
- The observation must be SPECIFIC, not general. "Politicians are out of touch" = weak. "They're debating retirement age as if any of us will retire" = strong.
- The specificity should feel like something the viewer has thought but never articulated. The meme says it for them.
- The more niche the recognition, the more intensely it's shared within that niche. A meme that 100K people mildly relate to loses to a meme that 10K people feel DEEPLY seen by.

**Escalation**
Something starts normal (or slightly off) and gets progressively more absurd. Each beat raises the stakes. The audience stays because they want to see how far it goes.

Rules:
- Minimum 3 beats of escalation for a short (setup → escalation → peak/punchline)
- Each beat must be MORE absurd than the last — if the escalation plateau, the viewer leaves
- The final beat should be the most visually striking — this is the frame people screenshot

**Deflation**
The opposite of escalation — something is built up as grand or important, then punctured. Politicians giving soaring speeches → cut to the actual mundane/disastrous result.

Rules:
- The buildup must feel genuine enough that the deflation lands. If it's obviously sarcastic from the start, the punchline has no impact.
- Works best with real footage or real quotes as the setup, then absurdist game-world rendering as the deflation.

**Specificity Over Generality**
This is not a humor mechanic itself but a rule that applies to ALL mechanics above. Vague satire fails. Specific satire goes viral.

- BAD: "The government doesn't care about you"
- GOOD: "Macron celebrating 0.3% GDP growth while your electricity bill went up 45%"
- BAD: "EU regulations are annoying"
- GOOD: "Brussels just regulated the curvature of bananas while French farmers can't afford diesel"

The engine must always push toward maximum specificity. Use real numbers, real quotes, real policy details. The absurdist rendering makes it digestible — the specificity makes it shareable.

---

### LAYER 2: Combination Logic (Why THIS Character × THIS World × THIS Topic)

Before generating any concept, the engine must justify the character/world/topic combination. Random combinations feel like AI slop. Justified combinations feel like creative genius.

#### Combination Justification Framework

Every combination is evaluated on four axes:

**Axis 1 — Tonal Equation**
What type of contrast or parallel does this world create with the topic?

| Equation Type | Example | Effect |
|--------------|---------|--------|
| Wholesome × Dark | Animal Crossing + pension crisis | Absurdist dissonance — the gap IS the joke |
| Chaotic × Bureaucratic | GTA + EU regulation | Satirical commentary — the chaos mirrors political chaos |
| Punishing × Mundane | Dark Souls + French bureaucracy | Relatable suffering — the difficulty IS the metaphor |
| Competitive × Political | Mario Kart + election race | Direct parallel — game mechanics map to political mechanics |
| Domestic × Governmental | The Sims + cost of living | Grounding — shows policy impact at human scale |
| Creative × Destructive | Minecraft + policy reform | Building/demolishing — the mechanic IS the political action |

The engine must identify WHICH tonal equation is at play and articulate why it works. If no clear equation exists, the combination is weak.

**Axis 2 — Metaphorical Depth**
The best combinations work on multiple levels simultaneously.

Scoring:
- **1 layer** (surface visual joke only): "Macron in a game world, lol" — WEAK, won't share
- **2 layers** (visual + one metaphorical read): "Macron doing surgery = trying to fix France" — DECENT, might share
- **3+ layers** (visual + metaphor + cultural subtext): "Macron doing surgery in Animal Crossing = trying to fix France + the wholesome setting implies he thinks everything is fine + the patient is dead = the system can't be saved + Animal Crossing is escapism = he's living in fantasy while reality burns" — STRONG, viral potential

The engine should aim for 3+ layers on every concept. If it can only find 1 layer, the combination isn't rich enough.

**Axis 3 — Audience Bridge**
Does this world pull in a non-political audience?

Questions:
- Does this game world have an active, engaged community right now? (Not just historically — RIGHT NOW)
- Is there a cultural moment around this game? (New release, update, meme trend, nostalgia cycle)
- Will fans of this game share it BECAUSE it's in their game's world, regardless of the political content?
- Does the cross-pollination engine (Module 3) show any current trending content from this game's community that we can ride?

If the world has no active audience, the cross-pollination value drops to zero and the concept must survive purely on political audience engagement.

**Axis 4 — Visual Clarity (The One-Frame Test)**
Can someone understand the joke from a single still frame?

This is the ultimate filter. If you screenshot the first frame of this concept and post it with no context:
- Would people stop scrolling? (Hook strength)
- Would they understand what they're looking at? (Clarity)
- Would they want to see what happens next? (Curiosity)

If the combo requires a caption to explain WHY the character is in that world, it fails the one-frame test.

#### Combination Verdict

```
COMBINATION: Macron × Animal Crossing × Pension Reform Surgery

TONAL EQUATION: Wholesome × Dark = Absurdist Dissonance ✅
The pastel Nintendo world vs literally cutting open France = maximum tonal gap

METAPHORICAL DEPTH: 4 layers ✅
L1: Funny image (surface)
L2: Surgery = attempting to "fix" France (political metaphor)
L3: Wholesome setting = Macron thinks everything is fine (character commentary)
L4: Patient is dead = system beyond saving (editorial thesis)

AUDIENCE BRIDGE: Strong ✅
Animal Crossing community: 30M+ active players
Current cultural moment: Evergreen nostalgia, no specific spike but consistent
Cross-pollination value: Gaming meme audiences will share for the AC reference alone

VISUAL CLARITY: Passes one-frame test ✅
First frame: Macron in scrubs, Animal Crossing surgery room, France on table
Readable instantly. No caption needed. Absurd enough to stop scroll.

VERDICT: ████████ STRONG — proceed to full concept generation
```

Weak example:
```
COMBINATION: Darmanin × Pokémon × Pension Reform

TONAL EQUATION: Collecting × Economic policy = ??? ❌
No clear tonal equation. The game's core mechanic (catching creatures) has no
natural metaphorical connection to pension reform.

METAPHORICAL DEPTH: 1 layer ❌
L1: Darmanin in a Pokémon world (surface visual only)
No deeper read emerges naturally.

AUDIENCE BRIDGE: Medium ⚠️
Pokémon community is large but this isn't doing anything WITH the Pokémon
mechanic that would make fans engage.

VISUAL CLARITY: Fails one-frame test ❌
First frame: Darmanin in Pokémon world... doing what? Looking at pension
documents? The image doesn't tell a joke by itself.

VERDICT: ░░░░░░░░ WEAK — kill combination, try different world
```

The engine generates 6-8 initial combinations per topic, runs justification on each, kills the weak ones, and only develops full concepts for the 3-5 that survive.

---

### LAYER 3: Virality Engineering

Every concept must be engineered for maximum spread. This is not intuition — it's structural mechanics.

#### 3A — Hook Engineering (First 0.5-1 Second)

The hook decides everything. A perfect concept with a weak hook gets 500 views. A decent concept with a perfect hook gets 500K.

**Hook Types (ranked by effectiveness for this content style):**

1. **Absurd Image Cold Open** (Primary weapon)
   The first frame is visually "wrong" enough to stop the scroll. No text needed — the image IS the hook.
   - Macron in surgical scrubs in Animal Crossing
   - Le Pen as a GTA nightclub bouncer
   - Mélenchon running a cult in The Sims
   The brain processes images faster than text. An absurd image creates a 0.3-second "wait, what?" that buys you the next 5 seconds.

2. **Pattern Interrupt**
   Something that breaks the expected visual pattern of the platform feed. Among a feed of talking heads and selfies, a pastel Animal Crossing surgical scene is a pattern interrupt.
   Rules: The interrupt must be visually distinct from what surrounds it in a typical feed. High saturation, unusual angles, unexpected characters.

3. **Familiar Format Subversion**
   Uses a trending format template but the content is unexpected. The viewer recognizes the format (comfort) but the content is absurd (surprise). This is the cross-pollination play — hijack a trending format from gaming/anime/music and fill it with political content.

4. **Text Hook**
   Bold text on first frame that creates a question or tension. "POV: They're arguing about whether you retire at 62 or 64." Works but weaker than visual hooks for THIS content style because the visual absurdity IS the brand.

5. **Zoom Reveal**
   Camera slowly reveals something absurd. Creates curiosity gap. Works for escalation-based concepts where the punchline is visual.

**Hook Rules:**
- The hook must work with SOUND OFF. 80%+ of initial views are on mute.
- If the first frame is a black screen, loading screen, or text card, you've already lost.
- Test: would someone stop scrolling if they saw this as a still thumbnail? If not, the hook is weak.

#### 3B — Emotional Compression

The best shorts deliver a complete emotional arc in under 15 seconds:

```
SETUP (0-3s): Establish the absurd situation
     ↓
TENSION (3-7s): The absurdity escalates or the contrast deepens
     ↓
RELEASE (7-12s): Punchline lands — either visual, textual, or both
     ↓
LINGER (12-15s): Hold on the final frame so the brain processes the joke
```

No wasted frames. Every second must either advance the joke, deepen the metaphor, or deliver the punchline. If you can cut a frame without losing anything, cut it.

#### 3C — Shareability Engineering

People share for social currency. Every concept must have a clear share impulse:

| Share Trigger | What It Feels Like | Design Strategy | Performance Indicator |
|--------------|-------------------|-----------------|----------------------|
| "This is so me" | Viewer feels personally seen | Build on specific, widely-felt but rarely-articulated experiences | High shares, "trop vrai" comments |
| "My friend needs to see this" | Viewer thinks of specific person | Make it relatable to a specific TYPE of person, not everyone | High DM shares |
| "I can't believe someone made this" | Craft appreciation + absurdity | Push the visual absurdity to a level that feels unprecedented | High shares + saves |
| "I need to argue about this" | Controversial take provokes response | Frame the editorial angle as a debatable position, not a settled fact | High comments, quote tweets, ratio |
| "I found this first" | Discovery/curation flex | Be first on a topic or format — speed matters | Early shares before peak |

The engine must tag every concept with its primary share trigger and design the concept to maximize that specific trigger.

#### 3D — Comment Bait Architecture

Comments drive algorithmic reach on every platform. The concept should be designed to provoke specific types of comments:

**Completion bait**: Leave something unsaid so viewers comment the punchline themselves. E.g., show 4 problems getting worse, end before showing the 5th — viewers will comment what the 5th should be.

**Debate bait**: Frame the topic so two sides HAVE to argue in comments. Not "this is right" but "is this right?" The question mark is the bait.

**Tag bait**: Make the concept so specific to a type of person that viewers tag friends: "c'est toi mdr" / "@marc regarde ça"

**Correction bait**: Intentionally include a minor factual "mistake" (wrong date, slightly off number) that pedantic commenters will rush to correct. Every correction is engagement the algorithm counts.

**Prediction bait**: End the concept with an implicit question about what happens next. "Part 2?" comments boost engagement.

The engine should specify which comment bait strategy each concept uses and predict the top 3-5 comments.

#### 3E — Rewatch Engineering

Content that rewards multiple views gets algorithmically boosted because watch time increases.

Strategies:
- **Background details**: Put secondary jokes or references in the background of the game world that viewers won't catch on first watch
- **Speed**: Make the text overlay slightly fast so people rewatch to read it fully
- **Recontextualization**: A punchline that makes the viewer reinterpret the opening (they rewatch to see it differently)
- **Visual density**: Pack the frame with enough detail that one viewing can't absorb it all
- **Easter eggs**: References to previous shorts that only followers will catch (rewards loyalty + creates "did you notice?" comments)

---

### LAYER 4: Platform Intelligence

Each platform has invisible rules. The engine must generate platform-specific optimizations for every concept.

#### Platform Behavior Models

**TikTok**
- Algorithm priority: Watch-through rate > shares > comments > likes
- A 10s video watched twice beats a 30s video watched once — design for rewatchability
- Trending sounds give discovery boost but only for ~72 hours — check Module 2 for freshness
- First 1 second decides 80% of watch-through
- Stitches and duets extend reach — design concepts that are "stitchable" (leave room for reaction)
- Text-on-screen is essential — most views are sound-off
- Vertical 9:16 only
- Best posting times FR: 12:00-13:00 (lunch), 18:00-20:00 (commute/evening)
- Hashtags: 4-6 targeted, mix of broad (#politique) and niche (#retraites2026)

**Instagram Reels**
- Algorithm priority: Shares > saves > comments > likes (shares via DM are gold)
- Polished aesthetics rewarded more than TikTok — slightly higher production value
- Explore page favors visually striking thumbnails
- Carousel posts can complement Reels for deeper takes
- Story reshares extend reach — make it story-reshare-friendly (clean, single-message frame)
- Best posting times FR: 11:00-13:00, 19:00-21:00
- Hashtags: 8-12 mixed strategy

**YouTube Shorts**
- Click-through rate on thumbnail matters more than other platforms
- Title/description matters more than TikTok/Reels
- Slightly longer content (15-45s) can work — audience is more patient
- Audience skews slightly older than TikTok
- Subscribe prompt at end can work (TikTok follow prompts feel desperate)
- Best posting times FR: 17:00-20:00

**X/Twitter**
- Native format is image/GIF meme or short clip, not vertical video
- The text IS the hook — tweet copy matters more than thumbnail
- Quote tweets and ratio potential drive reach
- Controversy is algorithmic fuel on X more than any other platform
- Thread format for deeper takes that complement the meme
- Image memes can be repurposed stills from the video concepts
- Best posting times FR: 8:00-9:00, 12:00-13:00, 18:00-19:00

#### Platform-Specific Output

Every concept includes platform-specific optimization notes:

```
PLATFORM OPTIMIZATION:

TikTok (PRIMARY):
- Duration: 12s (optimized for 2x watch-through)
- Sound: [trending sound ID] — 48hrs freshness left
- Hook: Absurd image cold open, text at 0.0s
- Comment bait: Completion bait — end before showing the "solution"

Instagram Reels (SECONDARY):
- Duration: 15s (slightly extended final frame for story reshare)
- Sound: Same or original audio (trending sounds less important on IG)
- Adjust: Slightly more polished color grading
- CTA: Design final frame as standalone story-reshare image

X (TERTIARY):
- Format: Still image extract from Frame 1 + tweet text
- Tweet: "[Punchline text] 🇫🇷" — keep under 200 chars
- Thread option: Add context/real data in reply thread
```

---

### LAYER 5: French Cultural Intelligence

The engine must understand French internet culture, political humor tradition, and linguistic nuances at a native level.

#### French Humor DNA

French political satire has a long, sophisticated tradition. The audience isn't naive — they've grown up with Les Guignols, Le Canard Enchaîné, Groland, Charlie Hebdo. They can smell lazy satire instantly.

**What works in French political humor:**
- Absurdism pushed to extremes (Groland energy)
- Intellectual references made accessible through humor (not dumbed down, but made funny)
- Self-deprecating national humor ("la France c'est foutu mais au moins on rigole")
- Cynicism as a love language — mocking France IS French patriotism
- Mockery that punches up (at power) not down (at vulnerable groups)
- Specific cultural references that signal "I'm one of you" to French audiences

**What fails in French political humor:**
- American-style earnest political messaging (too direct, feels preachy)
- Generic "politician bad" content without a specific, intelligent angle
- Content that talks DOWN to the audience (French audiences are sophisticated about politics)
- Humor that feels imported/translated from American internet culture
- Anything that smells like a brand or campaign trying to be memey

#### Linguistic Nuance

The engine must understand and appropriately use:
- **Verlan**: Inverted slang that signals youth/street culture (meuf, relou, chelou, vénère)
- **Text speak**: Abbreviated French (mdr, ptdr, jsp, slt, tkt, ptn)
- **Generational markers**: Language that signals which age group you're talking to
- **Register shifts**: Mixing formal political language with informal meme language = humor
- **Cultural references**: Knowing which references land with which audience (Kaamelott quotes, OSS 117, Brice de Nice, etc.)

Rules:
- Text overlays should match the audience register — too formal feels like a news channel, too informal feels try-hard
- Caption language should be platform-native (TikTok captions are more informal than Instagram)
- Never use verlan or slang incorrectly — one wrong usage destroys credibility
- When in doubt, slightly understated is better than overcorrected — the audience should feel like the creator is naturally funny, not performing

#### French Political Landscape Awareness

The engine needs a working model of French political dynamics:
- The left/right spectrum in France is NOT the same as the US
- Macronisme is its own thing — neither traditionally left nor right
- The RN (ex-FN) has undergone a normalization process — content about them requires nuance
- LFI is polarizing — Mélenchon is simultaneously loved and hated, often by the same people
- French relationship with the EU is complex — not simply pro or anti
- Laïcité debates have a specifically French context that doesn't translate to American "culture war"
- Class dynamics in France are different — the gilets jaunes revealed fault lines that persist

The engine should never generate concepts that flatten these nuances into simplistic takes. The audience will reject it.

---

### LAYER 6: Anti-Patterns (What the Engine Must NEVER Do)

Hard-coded rules that override everything else:

**Content Anti-Patterns:**
- NEVER start with a logo, intro, or brand card
- NEVER explain the joke — if it needs explanation, the concept is weak
- NEVER let more than 1 second pass before the hook
- NEVER use text too small to read on mobile at arm's length
- NEVER make political content that LOOKS like political content (defeats the entire strategy)
- NEVER recycle a trending sound that peaked > 5 days ago
- NEVER use a format that the performance data shows is declining
- NEVER generate a concept with only 1 layer of metaphorical depth
- NEVER pair a character with a world that fails the one-frame test

**Tone Anti-Patterns:**
- NEVER be earnest or preachy — this is satire, not activism
- NEVER punch down at vulnerable groups — always punch up at power
- NEVER be mean-spirited toward the audience — mock politicians, not voters
- NEVER feel like advertising, propaganda, or a campaign (even though editorially driven)
- NEVER use American political humor conventions that don't translate to French culture
- NEVER be generic — every concept must have a specific, surprising angle

**Strategic Anti-Patterns:**
- NEVER generate concepts for topics past their engagement window (check time sensitivity)
- NEVER flood a single topic — max 2 concepts per topic per day to avoid audience fatigue
- NEVER use the same character × world combination more than 3 times in a week (unless it's a deliberate series)
- NEVER ignore the cross-pollination engine — at least 1 concept per daily brief should be a format hijack from a non-political vertical

---

### Concept Generation Output

After running through all 6 layers, each concept output looks like:

```
CONCEPT #3
━━━━━━━━━━

── TOPIC ──
Macron's latest pension reform comments
Editorial Pillar: Anti-Establishment + Economic Populism
Editorial Angle: The debate framing itself is the manipulation — both "sides"
assume you'll retire in a system that won't exist

── AUDIENCE ──
Target: 20-30 year old workers, politically disengaged but economically anxious
Emotional State: Cynical, gallows humor, feels like the system is rigged
Share Trigger: "This is so me" — dark humor recognition

── COMBINATION JUSTIFICATION ──
Character: Macron (The Disconnected Technocrat)
World: Animal Crossing
Tonal Equation: Wholesome × Dark = Absurdist Dissonance ✅
Metaphorical Depth: 4 layers ✅
  L1: Funny image (surface)
  L2: Surgery = attempting to fix France (political metaphor)
  L3: Wholesome setting = he thinks everything is fine (character irony)
  L4: Patient dead on table = system beyond saving (editorial thesis)
Audience Bridge: Gaming community, Animal Crossing nostalgia ✅
One-Frame Test: Passes ✅

── HUMOR MECHANICS ──
Primary: Juxtaposition (tonal — wholesome × dark)
Secondary: Recognition ("trop vrai" — the retirement observation)
Tertiary: Deflation (grand political debate → absurd game world reality)

── CONCEPT ──
METAPHOR: Macron performing open heart surgery on a France-shaped island
in Animal Crossing, but the patient is clearly already dead and he's
just rearranging the organs. Heart monitor flatline visible.

FORMAT: Silent, text overlay only, trending sound
HOOK (First Frame): Wide shot of Animal Crossing surgery room. Macron
character in scrubs. France on the table. Text overlay appears instantly.
DURATION: 12 seconds
EDIT STYLE: Slow zoom in → hard cut to close-up → hold on flatline

TEXT OVERLAYS:
- Frame 1 (0-5s): "POV: They're arguing about whether you retire at 62 or 64"
- Frame 2 (5.5-10s): "as if you'll ever retire at all"
- Frame 3 (10-12s): [no text, just flatline — let the image land]

── VIRALITY ENGINEERING ──
Hook Type: Absurd Image Cold Open (strongest type for this content)
Share Trigger: "This is so me" — targets recognition response
Comment Bait: Debate bait ("62 vs 64 vs never" will split comments)
  + Completion bait (viewers will comment their own retirement predictions)
Rewatch Factor: Background details in surgery room (secondary jokes),
  text speed slightly fast on first read

PREDICTED TOP COMMENTS:
1. "pourquoi c'est trop vrai 😭"
2. "mdr le patient est déjà mort"
3. "62, 64, 84 quelle différence"
4. "@[friend] c'est nous dans 30 ans"
5. "partie 2 avec la sécu svp"

── CROSS-POLLINATION ──
Uses the "POV: slow zoom" format currently trending in gaming TikTok FR
(avg 1.8M views this week, ~36hrs freshness remaining)

── PLATFORM OPTIMIZATION ──
TikTok (PRIMARY): 12s, trending sound [ID], optimized for 2x rewatch
Instagram Reels (SECONDARY): 15s version, extended final frame, story-reshare optimized
X (TERTIARY): Still frame extract + tweet "Ils débattent 62 vs 64 comme si on allait
  un jour prendre notre retraite 🏥🇫🇷"

── NARRATIVE ARC ──
Connects to running arc: "Macron tries to fix France" (episode 5)
Callback potential: "Remember when Macron tried surgery? Well now he's trying..."

── SCORING ──
VIRALITY SCORE: 8.2/10
  Hook strength: 9/10 (absurd image + relatable text)
  Humor depth: 8/10 (4 metaphorical layers)
  Format freshness: 8/10 (trending format, not oversaturated)
  Shareability: 9/10 (strong "this is so me" trigger)
  Topic heat: 7/10 (simmering, not peak)
  Content gap: 8/10 (nobody doing this specific angle)
  Combination strength: 9/10 (perfect tonal equation + multi-layer metaphor)

RISK ASSESSMENT:
  Legal: GREEN (satire of public figure, clearly absurdist)
  Platform: GREEN (no violence, no hate speech)
  Backlash: GREEN-YELLOW (both left and right may engage, net positive)
```

### Concept Ranking

All concepts across all topics ranked by:
1. Virality score (weighted composite from all sub-scores)
2. Combination strength (justification score)
3. Production feasibility (can this actually be made quickly with available tools?)
4. Narrative arc fit (does it connect to ongoing storylines?)
5. Time urgency (does it need to go out today before the topic cools?)
6. Cross-pollination bonus (concepts using trending non-political formats get a boost)

Top 5 concepts delivered in daily brief.

Storage: Supabase table `concepts`

---

## Module 7 — Manual Injection Mode

**Purpose**: Allow user to bypass the trend detection layer and inject any topic, policy, theme, or vague idea directly into the creative engine.

### Input Flexibility

The system accepts various levels of specificity:

| Input Type | Example | System Behavior |
|------------|---------|-----------------|
| Just a topic | "pension reform" | System does full editorial analysis, audience mapping, and concept generation |
| Topic + angle | "pension reform — frame as generational theft" | System takes the editorial direction, handles everything else |
| Topic + target | "pension reform — reach apolitical 20-somethings" | System optimizes audience mapping and format selection for that demo |
| Topic + format | "pension reform — Animal Crossing short" | System works within the specified world/format constraint |
| Policy text | [paste actual policy text or article link] | System analyzes the policy, extracts the most absurdist/memeable elements, generates concepts |
| Vague theme | "the French middle class is disappearing" | System sharpens into specific angles, finds supporting data points, generates concepts |
| Quote | "Macron: 'la France est un pays d'entrepreneurs'" | System treats the quote as raw material, generates satirical responses |
| Batch | 10 policy positions for election season | System generates full content calendar with sequencing and narrative arcs |

### Reactive Mode

For breaking news / live events:

1. User pastes a link, quote, or brief description
2. System immediately runs: editorial angle → audience map → top 3 concepts → production package for #1
3. Total time from injection to production package: < 5 minutes
4. Goal: post while the topic is still breaking

### Via Messaging

User sends OpenClaw a WhatsApp/Telegram message:

```
"Macron just said [quote]. Give me 5 concepts."
```

OpenClaw runs the full pipeline and responds with ranked concepts within minutes.

---

## Module 8 — Production Package Generator

**Purpose**: When user greenlights a concept, generate everything needed to assemble the final content.

**Trigger**: User responds to daily brief or manual injection with "greenlight concept [N]"

### Package Contents

#### 1. Image/Video Generation Prompts

```
PRIMARY IMAGE PROMPT (Midjourney/Flux/etc):
"Animal Crossing style surgical operating room, bright pastel colors,
isometric view, a character resembling Emmanuel Macron wearing green
surgical scrubs and mask, standing over an operating table, on the table
is a heart-shaped object colored in blue white and red (French flag),
the heart monitor in background shows a flatline, cute Nintendo-style
aesthetic, clean cel-shaded rendering, soft ambient lighting"

VARIATION A: Same scene, closer angle on Macron's face, confused expression
VARIATION B: Same scene, wide shot showing other Animal Crossing villagers watching in horror
VARIATION C: Same scene but the surgery room is falling apart

CHARACTER CONSISTENCY NOTE: Use same Macron character design as
[reference to previous shorts if applicable]
```

#### 2. Text Overlays

```
FRAME 1 TEXT: "POV: They're arguing about whether you retire at 62 or 64"
- Font: Bold sans-serif, white with black outline
- Position: Center-top third
- Size: Large enough to read on mobile in 0.5 seconds
- Timing: Appears at 0.0s, holds for 4s

FRAME 2 TEXT: "as if you'll ever retire at all"
- Font: Same
- Position: Center
- Timing: Appears at 4.5s after cut, holds to end
```

#### 3. Audio Direction

```
SUGGESTED SOUND: [Specific TikTok sound ID] — currently trending,
[X]M uses this week

ALTERNATIVE: [Backup sound] if primary gets DMCA'd

TIMING NOTES:
- Beat drop at 4.2s — align with the cut to close-up
- Let the silence after the drop carry the punchline text

IF VOICEOVER: N/A for this concept (silent + text is stronger)
```

#### 4. Editing Blueprint

```
SHOT LIST:
━━━━━━━━━

0.0s - 4.0s | SHOT 1: Wide shot of Animal Crossing surgery room
             | Slow zoom in (105% over 4 seconds)
             | Text overlay appears immediately
             | Macron character doing surgery animation

4.0s - 4.5s | TRANSITION: Hard cut (no transition effect)

4.5s - 8.0s | SHOT 2: Close-up of Macron character's face
             | Confused/blank expression
             | Punchline text appears at 4.5s
             | Hold on this frame, very slight zoom (102%)

8.0s - 10.0s | SHOT 3: Pull back to wide, heart monitor flatline visible
              | No text, let the image land
              | Music fades

TOTAL DURATION: 10 seconds
ASPECT RATIO: 9:16
RESOLUTION: 1080x1920
```

#### 5. Caption & Hashtags

```
TIKTOK CAPTION: "at this point just let me retire in animal crossing 🏥🇫🇷"

INSTAGRAM CAPTION: "La réforme des retraites version Nintendo 🎮"

X CAPTION: "They're debating 62 vs 64 like any of us will ever see retirement"

HASHTAGS (TikTok): #retraites #macron #animalcrossing #politique #france #satire #mdr

ENGAGEMENT BAIT: Pin comment — "wait until you see what he does to healthcare 💀"
```

#### 6. Posting Strategy

```
OPTIMAL POST TIME: 12:00-13:00 CET (lunch break scroll peak)
or 18:00-19:00 CET (commute scroll)

PLATFORM PRIORITY:
1. TikTok (format + audience match)
2. Instagram Reels (cross-post, adjust caption)
3. X (still image version with caption, link to TikTok in reply)

FOLLOW-UP STRATEGY:
- If >100K views in 2 hours: immediately produce Variation B (wider shot, different angle)
- If comments focus on healthcare: queue up healthcare concept from Module 12 (Trend Prediction)
- Reply to top 3 comments within first hour
```

Storage: Supabase table `production_packages`

---

## Module 9 — Performance Feedback Loop

**Purpose**: Track what works, learn from it, improve future concept generation.

### Data Collection

After posting, user inputs (or system scrapes if accounts are connected):

```json
{
  "concept_id": "uuid",
  "platform": "tiktok",
  "posted_at": "timestamp",
  "metrics_24h": {
    "views": 450000,
    "likes": 38000,
    "comments": 2100,
    "shares": 12000,
    "saves": 3400,
    "followers_gained": 890,
    "profile_visits": 4200
  },
  "metrics_7d": { "...same structure..." },
  "top_comments": ["actual top comments"],
  "comment_sentiment": "positive/mixed/negative/argumentative",
  "predicted_vs_actual": {
    "predicted_virality_score": 8.2,
    "actual_virality_indicator": "shares/followers ratio",
    "prediction_accuracy": "how close were we"
  }
}
```

### Learning Outputs

The system analyzes performance data to update:

1. **Character effectiveness**: Which characters consistently outperform?
2. **World effectiveness**: Which game worlds get the most engagement?
3. **Format effectiveness**: Which format/hook combinations work for YOUR audience?
4. **Editorial angle effectiveness**: Which pillars resonate most?
5. **Timing patterns**: When does your audience engage most?
6. **Audience model**: Refined understanding of who follows, shares, comments

### Virality Post-Mortem

When something pops off (>2x average performance), the system automatically generates:

```
VIRALITY POST-MORTEM
━━━━━━━━━━━━━━━━━━━

Concept: [Title]
Performance: 2.4M views (5x average)

WHY IT WORKED:
- Hook: Absurd image (Animal Crossing surgery) created immediate pattern interrupt — 92% of viewers watched past 3 seconds
- Format: Silent + text matched current TikTok FR trend (8/10 freshness)
- Topic timing: Posted 2 hours after Macron's speech, rode the wave
- Emotional trigger: "Dark humor recognition" — shares driven by "this is so true" sentiment
- Cross-pollination: Gaming aesthetic pulled in non-political viewers (18% of comments reference Animal Crossing not politics)

REPLICATION STRATEGY:
- The "politician doing mundane task in game world while France suffers" formula scored 9/10
- Queue 3 more concepts using this template with different topics
- Rotate game worlds to avoid format decay

UPDATED WEIGHTS:
- Animal Crossing world: effectiveness +15%
- Silent + text format: effectiveness +10%
- "Dark humor recognition" trigger: weight +20%
```

### Content Decay Tracking

System monitors engagement trends over time:
- If a format (e.g., "politician in Animal Crossing") shows declining engagement over 3-4 weeks, flag it
- Suggest pivoting to a new world or format BEFORE it goes stale
- Track format lifecycle: fresh → peak → plateau → decline → dead

Storage: Supabase tables `post_performance` and `learning_weights`

---

## Module 10 — Character Bible & World Library

**Purpose**: Structured database of all characters and game worlds available for content creation.

**Philosophy**: Text-first, image-later. Every character is a text description. Every world is a text description. The AI creative engine combines any character with any world on the fly and generates the appropriate visual direction in the image prompts. No pre-built character/world combinations needed. Any character works in any world instantly.

### How It Works

```
Character text: "Macron — smug, cerebral, always celebrating while things burn"
+
World text: "Animal Crossing — pastel, cute, Nintendo aesthetic"
+
Concept: "performing surgery on France"
=
AI generates the image prompt, specifying how Macron looks in Animal Crossing style,
what the environment looks like, lighting, composition — all from text descriptions.
```

No pre-built assets. No character/world matrix to populate. Add a character in 30 seconds, add a world in 15 seconds. The system handles the rest.

### Character Schema (MVP — Text Only)

```json
{
  "character_id": "uuid",
  "name": "Emmanuel Macron",
  "role": "President",
  "party": "Renaissance",
  "tier": "1 | 2 | 3",
  "archetype": "The Disconnected Technocrat",
  "traits": "smug, cerebral, condescending, celebrates small wins while ignoring big failures, thinks he's the smartest in the room",
  "comedic_function": "The guy who thinks he's fixing things while making them worse",
  "best_for_pillars": ["anti_establishment", "economic_populism"],
  "paired_well_with": ["Mélenchon (rivalry)", "Darmanin (incompetent deputy)"],
  "notes": "Free text — anything useful for the creative engine",
  "locked_prompts": {},
  "created_at": "timestamp",
  "last_used": "timestamp",
  "times_used": 0,
  "avg_performance": 0
}
```

**Tier System**:
- **Tier 1**: Core cast (5-10). Used constantly. Macron, Le Pen, Mélenchon, Bardella, Darmanin, Attal, etc.
- **Tier 2**: Supporting cast (10-15). Used when topically relevant. Ministers, EU commissioners, media figures.
- **Tier 3**: Everyone else. Added on the fly when they become relevant. Minimal info needed — name, role, 1-line archetype.

**Quick Add flow**: A politician trends unexpectedly. You add: name + role + 3 traits. Done. The system can generate concepts with them immediately. Enrich later.

### World Schema (MVP — Text Only)

```json
{
  "world_id": "uuid",
  "name": "Animal Crossing",
  "aesthetic": "Pastel colors, cute rounded characters, isometric view, Nintendo rendering, soft ambient lighting",
  "tonal_contrast": "Wholesome setting + dark political reality = absurdist humor",
  "best_for": "Making grim realities feel approachable and shareable",
  "audience_association": "Gaming community, nostalgia, wholesome internet culture",
  "environment_examples": "Village, store, beach, town hall, surgery room, museum",
  "notes": "Free text — anything useful for prompt generation",
  "locked_prompts": {},
  "created_at": "timestamp",
  "last_used": "timestamp",
  "times_used": 0,
  "avg_performance": 0
}
```

**Adding a new world is instant**: Type "Dark Souls — gothic, punishing, brutal difficulty, dark fantasy" and every character is available in that world immediately.

### Locked Prompts (Progressive Enhancement)

Over time, when you produce content and a specific character/world combination looks great, you save the image prompt that worked:

```json
"locked_prompts": {
  "animal_crossing": "Short villager character with swept-back dark hair, wearing miniature suit, slightly smug round face, pastel cel-shaded rendering, Animal Crossing art style...",
  "gta": "Stylized 3D character in suit with exaggerated jawline, GTA loading screen art style, neon city background..."
}
```

This is optional and happens organically. The system works without any locked prompts — they just improve visual consistency once you have them.

### Suggested Starter Characters (Tier 1)

| Character | Role | Archetype | Traits |
|-----------|------|-----------|--------|
| Emmanuel Macron | President | The Disconnected Technocrat | Smug, cerebral, celebrates while things burn |
| Marine Le Pen | RN Leader | The Eternal Challenger | Persistent, populist rage, "I told you so" energy |
| Jean-Luc Mélenchon | LFI Leader | The Revolutionary Grandpa | Theatrical, explosive, messianic complex |
| Jordan Bardella | RN President | The TikTok Politician | Polished, young, media-savvy, suspiciously perfect |
| Gérald Darmanin | Minister | The Bumbling Enforcer | Tries to be tough, creates more chaos |
| Gabriel Attal | PM/Former PM | The Golden Boy | Young, ambitious, Macron's mini-me |
| Sandrine Rousseau | EELV | The Culture War Lightning Rod | Provocative, polarizing, generates engagement |
| Éric Zemmour | Reconquête | The Provocateur Intellectual | Inflammatory, bookish, loves controversy |
| François Hollande | Former President | The Comeback Nobody Asked For | Bumbling, surprisingly resilient, rain metaphors |
| Ursula von der Leyen | EU Commission | The Brussels Boss | Bureaucratic, detached from national reality |

### Suggested Starter Worlds

| World | Aesthetic | Tonal Contrast | Best For |
|-------|-----------|---------------|----------|
| Animal Crossing | Pastel, cute, isometric, Nintendo | Wholesome + dark | Making grim realities shareable |
| GTA | Neon, crime, urban chaos, Rockstar style | Criminal chaos + politics | Corruption, power dynamics, chaos |
| Minecraft | Blocky, pixelated, construction/destruction | Building/destroying + policy | Systems being built or demolished |
| The Sims | Suburban simulation, mundane domestic | Domestic life + governance | Bureaucracy, daily life impact |
| Dark Souls | Gothic, brutal, punishing difficulty | Suffering + French life | Navigating French bureaucracy/economy |
| Mario Kart | Colorful, competitive, racing | Competition + elections | Political races, rivalry, items as policies |
| Pokémon | Bright, collecting, evolution | Cataloguing + policy | Collecting problems, politician evolution |
| FIFA | Stadium, football, competition | National sport + politics | National pride, referee (EU) metaphors |

Storage: Supabase tables `characters` and `worlds`

---

## Module 12 — Trend Prediction

**Purpose**: Instead of only reacting to what's trending NOW, identify topics that are ABOUT to trend.

### Predictable Event Calendar

Maintained and updated:
- Parliament session schedule (committee hearings, votes)
- EU summit and vote calendar
- Planned protests / strike dates
- Political party congress dates
- Anniversary dates of politically charged events (gilets jaunes anniversary, terror attack anniversaries, etc.)
- Election cycles (municipal, regional, presidential, EU)
- Budget cycle (spending announcements, tax changes)
- School calendar (rentrée generates annual debates)

### Simmering Topic Detection

System monitors topics that are:
- Gaining momentum on Reddit/X but haven't hit mainstream news yet
- Being discussed in niche political forums before mainstream pickup
- Showing rising Google Trends trajectory (not yet peaked)

### Pre-Production Queue

For predictable events, the system pre-generates concept skeletons:

```
EVENT: EU Agriculture Vote — March 15
PRE-BUILT CONCEPTS (details TBD until day-of):
1. [Character] plays Farmville while real farms burn — template ready, specifics to be filled when vote results are known
2. [Character] as EU bureaucrat in Stardew Valley — template ready
3. [Character] reaction format — template ready, quote to be inserted
```

When the event happens, system fills in specifics and generates full concepts within minutes.

Storage: Supabase tables `event_calendar` and `pre_production_queue`

---

## Module 13 — Narrative Arc Tracker

**Purpose**: Track running storylines across shorts to build lore, recurring jokes, and reasons to follow (not just watch one and leave).

### Character Arc Tracking

```json
{
  "character_id": "uuid",
  "appearances_this_month": 12,
  "running_storylines": [
    {
      "arc_name": "Macron tries to fix France",
      "arc_type": "recurring_failure",
      "episodes": ["concept_id_1", "concept_id_2", "concept_id_3"],
      "current_state": "Has now failed in 4 different game worlds",
      "next_beat": "Should try a 5th world and fail in a new way",
      "audience_investment": "HIGH — comments asking 'what game is next?'"
    }
  ],
  "callbacks_available": [
    "Reference to the Animal Crossing surgery in future shorts",
    "'Remember when Macron tried to...' format"
  ]
}
```

### Series Potential

When a topic has legs (pension reform, immigration debate, EU tensions), the system suggests multi-part series:

- Part 1: Introduce the absurd metaphor
- Part 2: Escalate (same world, bigger stakes)
- Part 3: Cross-world callback (the problem follows the character to a different game)
- Part 4: Audience participation (ask viewers which game world is next)

### Lore Database

Track all established jokes, callbacks, and world details so the system never contradicts its own universe.

Storage: Supabase table `narrative_arcs`

---

## Module 14 — Controversy Radar

**Purpose**: Flag legal and platform risks before content is produced.

### Legal Checks (French Law)

| Law | Risk | System Response |
|-----|------|----------------|
| Loi Pleven (1972) | Incitement to discrimination, hatred, or violence | Flag any concept that could be interpreted as targeting a group rather than a policy or politician |
| Loi Gayssot (1990) | Holocaust denial | Automatic kill — never generate concepts in this territory |
| Droit à l'image | Using someone's likeness | Low risk for politicians (public figures, satire exemption) but flag if using private citizens |
| Diffamation | False claims presented as fact | Ensure all concepts are clearly satirical/absurdist, never presented as factual claims |
| Apologie du terrorisme | Glorifying terrorism | Automatic kill |

### Platform Risk Assessment

| Risk Level | Description | System Action |
|------------|-------------|---------------|
| GREEN | Standard political satire, clearly absurdist | No flag |
| YELLOW | Edgy but within platform guidelines | Note: "May get limited reach but not removed" |
| ORANGE | Likely to trigger manual review | Generate a "safe version" alongside the "spicy version" |
| RED | Likely to be removed or result in strike | Kill concept or rework entirely |

### Output

Every concept includes:
- Legal risk: GREEN/YELLOW/ORANGE/RED
- Platform risk: GREEN/YELLOW/ORANGE/RED per platform
- If ORANGE: alternative "safe version" provided
- If RED: concept killed with explanation

---

## Module 15 — Competitor Intelligence

**Purpose**: Monitor competing French political meme/content accounts.

### Accounts to Monitor

[TO BE FILLED BY USER — competing French political content accounts]

### What to Track

- What they're posting about today (topic overlap detection)
- What's performing for them (engagement analysis)
- What topics they're NOT covering (your opportunity)
- When they go viral, reverse engineer why
- Format evolution (are they innovating or recycling?)
- If they copy YOUR format (detect and alert)

### Output

Weekly competitor report:
- Competitor content performance summary
- Topics they covered that you didn't (missed opportunities)
- Topics you covered that they didn't (unique angles)
- Format trends across competitor accounts
- Your share of voice vs competitors on key topics

Storage: Supabase table `competitor_intelligence`

---

## Module 16 — A/B Testing Framework

**Purpose**: For top concepts, generate variations to test what variables actually matter.

### Variation Types

| Variable | Variation A | Variation B |
|----------|-------------|-------------|
| Hook | Text-first hook | Image-first hook |
| Character | Macron | Different character, same concept |
| World | Animal Crossing | Minecraft |
| Duration | 10 seconds | 20 seconds |
| Audio | Trending sound | Original audio |
| Platform | TikTok-native | Cross-posted from Reels |

### Testing Protocol

- Post Variation A and B within 2 hours of each other (or across different accounts/platforms)
- Track performance for 48 hours
- Feed results back into Module 9 (Performance Feedback Loop)
- System learns which variables matter most for YOUR audience

---

## Module 17 — Meme Template Library

**Purpose**: Over time, build a library of proven, reusable concept templates.

### Template Schema

```json
{
  "template_id": "uuid",
  "template_name": "Politician does X in game world while France suffers",
  "times_used": 8,
  "avg_performance": "1.2M views, 8.4% engagement",
  "template_structure": {
    "frame_1": "[Character] in [World] doing [Mundane Activity]",
    "text_1": "[Current political issue framed as absurd contrast]",
    "frame_2": "Close-up or reveal of consequences",
    "text_2": "[Punchline that reframes the issue]"
  },
  "best_topics_for": ["economic policy", "disconnect between leaders and people"],
  "fatigue_status": "fresh | reliable | approaching_stale | retired",
  "last_used": "timestamp"
}
```

### Auto-Matching

When new topics come in, system checks if they fit existing winning templates:
- If yes: generate concept using proven template (lower risk, faster production)
- If no: generate original concept (higher creative effort, potential for new template)

Storage: Supabase table `meme_templates`

---

## Module 18 — Newsjacking Templates

**Purpose**: Pre-built concept skeletons for predictable event types that can be deployed in minutes.

### Event Type Templates

| Event Type | Template | Fill-in-the-Blank |
|------------|----------|-------------------|
| Macron press conference | [Character] watches conference in [World], reaction format | Insert actual quote + reaction |
| Protest/Strike | [Characters] in [World] recreating the protest in absurd way | Insert cause + visual |
| EU regulation | EU bureaucrat character in [World] implementing absurd rule | Insert actual regulation |
| Terror incident | [HANDLE WITH EXTREME CARE — see Controversy Radar] | Likely skip |
| Election/Vote result | [Characters] reacting to scoreboard in [World] | Insert actual results |
| Economic data release | [Character] reading the numbers in [World], world reacts | Insert actual data |
| Political scandal | [Character] in [World] doing the scandal activity | Insert scandal details |
| International incident | France character in [World] dealing with situation | Insert specifics |

### Deployment Speed

1. Event happens
2. System matches event type to template
3. Fills in specifics from live news ingestion
4. Generates full concept + production package
5. Alert sent to user
6. User greenlights
7. Target: concept ready within 15 minutes of event

---

## Module 20 — Configuration CMS (Admin Panel)

**Purpose**: A simple, fast interface where you populate and manage all system configuration — characters, worlds, editorial pillars, accounts to monitor, and settings — at your own pace while the rest of the system gets built in parallel.

**Priority**: Built FIRST (Week 1). Everything else can use placeholder data until you fill this in.

**Tech**: Part of the private dashboard React app. A "Configure" tab in the command center.

### Design Principle

Every input should take < 30 seconds to add. No required image uploads. No complex forms. Text fields with sensible defaults. Enrich later.

### CMS Sections

#### 1. Characters

**List View**:
```
┌─────────────────────────────────────────────────────────────┐
│  CHARACTERS                                    [+ Quick Add] │
│                                                              │
│  Filter: [All] [Tier 1] [Tier 2] [Tier 3]    Search: [___] │
│                                                              │
│  Name              Role            Archetype      Tier  Used │
│  ──────────────────────────────────────────────────────────  │
│  Macron            President       Disconnected    T1    24x │
│  Le Pen            RN Leader       Eternal         T1    18x │
│  Mélenchon         LFI Leader      Revolutionary   T1    15x │
│  Bardella          RN President    TikTok Pol.     T1    12x │
│  Darmanin          Minister        Bumbling        T2     6x │
│  ...                                                         │
│                                                              │
│  [Import from CSV]                                           │
└─────────────────────────────────────────────────────────────┘
```

**Quick Add** (minimal — get a character in the system fast):
```
┌────────────────────────────────────────────┐
│  QUICK ADD CHARACTER                        │
│                                             │
│  Name: [________________]                   │
│  Role: [________________]                   │
│  Party: [________________]                  │
│  Tier: [1] [2] [3]                         │
│  Archetype (one line): [________________]  │
│  Traits (comma separated): [____________]  │
│                                             │
│  [Save — I'll add more detail later]       │
└────────────────────────────────────────────┘
```

**Full Edit** (enrich when you have time):
```
┌────────────────────────────────────────────┐
│  EDIT: Emmanuel Macron                      │
│                                             │
│  ── Basic Info ──                           │
│  Name: [Emmanuel Macron]                    │
│  Role: [President]                          │
│  Party: [Renaissance]                       │
│  Tier: [1]                                 │
│                                             │
│  ── Creative Profile ──                     │
│  Archetype: [The Disconnected Technocrat]  │
│  Traits: [smug, cerebral, condescending,   │
│           celebrates while things burn]     │
│  Comedic function: [The guy who thinks     │
│   he's fixing things while making them     │
│   worse]                                    │
│  Pairs well with: [Mélenchon, Darmanin]    │
│                                             │
│  ── Editorial Mapping ──                    │
│  Best for pillars: [☑ Anti-establishment]  │
│                     [☑ Economic populism]   │
│                     [☐ Sovereignty]         │
│                     [☐ Immigration]         │
│                                             │
│  ── Notes ──                                │
│  [Free text for anything else the           │
│   creative engine should know]              │
│                                             │
│  ── Locked Prompts (optional) ──            │
│  Animal Crossing: [paste prompt that worked]│
│  GTA: [empty — not yet produced]           │
│                                             │
│  ── Stats (auto-populated) ──               │
│  Times used: 24                             │
│  Avg performance: 340K views                │
│  Best world: Animal Crossing                │
│  Last used: 2 days ago                      │
│                                             │
│  [Save]  [Delete]                           │
└────────────────────────────────────────────┘
```

**Bulk Import**: Upload a CSV with columns (name, role, party, archetype, traits) to populate 50 politicians at once with minimal info. Enrich individually over time.

#### 2. Worlds

**List View**:
```
┌─────────────────────────────────────────────────────────────┐
│  WORLDS                                        [+ Add World] │
│                                                              │
│  Name              Aesthetic           Contrast     Used     │
│  ──────────────────────────────────────────────────────────  │
│  Animal Crossing   Pastel, cute        Wholesome     18x    │
│  GTA               Neon, crime         Chaos          12x    │
│  Minecraft         Blocky, pixel       Build/destroy   9x    │
│  Dark Souls        Gothic, brutal      Suffering       4x    │
│  ...                                                         │
└─────────────────────────────────────────────────────────────┘
```

**Add/Edit**:
```
┌────────────────────────────────────────────┐
│  ADD WORLD                                  │
│                                             │
│  Name: [________________]                   │
│  Aesthetic (describe the look):             │
│  [________________________________]         │
│  [________________________________]         │
│  Tonal contrast (why it's funny):           │
│  [________________________________]         │
│  Best for (what topics/messages):           │
│  [________________________________]         │
│  Example environments:                      │
│  [________________________________]         │
│  Notes:                                     │
│  [________________________________]         │
│                                             │
│  [Save]                                     │
└────────────────────────────────────────────┘
```

#### 3. Editorial Pillars

```
┌─────────────────────────────────────────────────────────────┐
│  EDITORIAL PILLARS                           [+ Add Pillar]  │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ ANTI-ESTABLISHMENT                              [Edit] │ │
│  │ Position: The political class is disconnected from     │ │
│  │ real people and serves its own interests               │ │
│  │ Emotional register: Mockery, anger                     │ │
│  │ Off-limits: Conspiracy theories, antisemitism          │ │
│  │ Example angles: "They don't live in the same France"   │ │
│  │ Mapped characters: Macron, Attal, Hollande             │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ SOVEREIGNTY                                     [Edit] │ │
│  │ Position: France should control its own destiny,       │ │
│  │ not Brussels                                           │ │
│  │ Emotional register: Pride, frustration                 │ │
│  │ Off-limits: Xenophobia                                 │ │
│  │ Example angles: "When did we vote for this?"           │ │
│  │ Mapped characters: Le Pen, Bardella, von der Leyen     │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ...                                                         │
└─────────────────────────────────────────────────────────────┘
```

#### 4. Accounts to Monitor

```
┌─────────────────────────────────────────────────────────────┐
│  MONITORED ACCOUNTS                        [+ Add Account]  │
│                                                              │
│  Filter: [All] [Format Intel] [Competitor] [Cultural]       │
│  Platform: [All] [TikTok] [Instagram] [X] [YouTube]        │
│                                                              │
│  Handle            Platform   Category        Priority      │
│  ──────────────────────────────────────────────────────────  │
│  @compte_meme_fr   TikTok     Format Intel    High          │
│  @politique_lol    Instagram  Competitor       High          │
│  @gaming_france    TikTok     Cultural/Gaming  Medium        │
│  @rap_fr_clips     TikTok     Cultural/Music   Medium        │
│  ...                                                         │
│                                                              │
│  [Bulk Import from CSV]                                      │
└─────────────────────────────────────────────────────────────┘
```

**Add Account**:
```
┌────────────────────────────────────────────┐
│  ADD ACCOUNT                                │
│                                             │
│  Handle: [@________________]                │
│  Platform: [TikTok ▼]                      │
│  Category: [Format Intel ▼]                │
│    Options: Format Intelligence             │
│             Competitor                      │
│             Cultural — Gaming               │
│             Cultural — Anime                │
│             Cultural — Football             │
│             Cultural — Rap/Music            │
│             Cultural — Reality TV           │
│             Cultural — General Memes        │
│             News/Political Commentary       │
│  Priority: [High] [Medium] [Low]           │
│  Notes: [________________]                  │
│                                             │
│  [Save]                                     │
└────────────────────────────────────────────┘
```

#### 5. System Settings

```
┌─────────────────────────────────────────────────────────────┐
│  SYSTEM SETTINGS                                             │
│                                                              │
│  ── Scan Schedule ──                                         │
│  Trend scan frequency: [Every 4 hours ▼]                    │
│  Format scan frequency: [Every 6 hours ▼]                   │
│  Cultural scan frequency: [Every 4 hours ▼]                 │
│                                                              │
│  ── Daily Brief ──                                           │
│  Delivery time: [08:00 CET]                                 │
│  Delivery channel: [☑ WhatsApp] [☐ Telegram] [☐ Discord]   │
│  Concepts per brief: [5]                                    │
│                                                              │
│  ── Content Defaults ──                                      │
│  Primary platform: [TikTok ▼]                               │
│  Default duration target: [15 seconds]                       │
│  Image gen tool: [Midjourney ▼]                             │
│  Risk tolerance: [Medium — show ORANGE, skip RED]           │
│                                                              │
│  ── Production Capacity ──                                   │
│  Shorts per week target: [5]                                │
│  Solo or team: [Solo]                                       │
│                                                              │
│  [Save Settings]                                             │
└─────────────────────────────────────────────────────────────┘
```

### CMS Build Priority

This is the FIRST thing built because:
1. You can start populating data immediately while other modules are in development
2. The creative engine needs at least 1 character + 1 world + 1 pillar to function
3. Scraping modules need account handles to know what to monitor
4. No other module is blocked — they all work with placeholder data until the CMS is populated

### Pre-Populated Data

On first launch, the CMS comes pre-loaded with:
- 10 Tier 1 characters (from the starter list above) with basic archetype and traits
- 8 starter worlds with aesthetic descriptions
- 7 editorial pillar templates (from Module 4) ready to customize
- System settings with sensible defaults

You review, edit, add, delete — but you're not starting from zero.

Storage: Reads/writes to existing Supabase tables (`characters`, `worlds`, `editorial_pillars`, `monitored_accounts`, `system_settings`)

---

## Module 21 — Virality Maximization Engine

**Purpose**: An active optimization layer that sits on top of the entire system. While the Meme Intelligence Engine (Module 6) generates smart concepts, this module maximizes their performance through predictive modeling, real-time optimization, A/B testing, timing intelligence, and post-publish management. This is the difference between creating good content and engineering viral content.

**Philosophy**: Don't post and pray. Post, monitor, adapt, amplify, learn.

---

### 21A — Predictive Virality Model

**What it is**: A scoring model trained on YOUR actual performance data that pressure-tests the creative engine's judgment.

**How it works**:

Phase 1 — Data Collection (First 50 posts):
The system logs every greenlit concept as a feature vector paired with actual performance:

```
FEATURE VECTOR (per concept):
├── Topic features
│   ├── topic_category (economy, immigration, EU, scandal, etc.)
│   ├── topic_heat_score_at_post_time
│   ├── topic_age_hours (how long since topic started trending)
│   ├── topic_saturation (how many other accounts covered it)
│   └── topic_emotional_profile (anger %, mockery %, etc.)
│
├── Creative features
│   ├── character_id
│   ├── character_tier
│   ├── world_id
│   ├── combination_tonal_equation_type
│   ├── metaphorical_depth_layers
│   ├── humor_mechanic_primary (juxtaposition, recognition, etc.)
│   ├── humor_mechanic_secondary
│   └── editorial_pillar
│
├── Format features
│   ├── hook_type (absurd_image, pattern_interrupt, text_hook, etc.)
│   ├── format_type (silent_text, voiceover, trending_sound, etc.)
│   ├── duration_seconds
│   ├── text_overlay_count
│   ├── format_trend_age_days (how old is this format trend)
│   ├── format_trend_multiplier (from Module 2)
│   └── is_cross_pollination (yes/no)
│
├── Distribution features
│   ├── platform
│   ├── post_time_hour
│   ├── post_day_of_week
│   ├── topic_lifecycle_position (early, sweet_spot, peak, late)
│   └── competitor_activity_same_topic (0-10)
│
└── Engagement bait features
    ├── share_trigger_type
    ├── comment_bait_type
    └── rewatch_mechanics_count

ACTUAL PERFORMANCE (measured at 24h and 7d):
├── views
├── likes
├── comments
├── shares
├── saves
├── watch_through_rate
├── avg_watch_time
├── follower_gain
├── profile_visits
└── viral_coefficient (shares / views)
```

Phase 2 — Model Training (After 50+ posts):
- Train a lightweight model (gradient boosting or similar — doesn't need to be deep learning) on the feature vector → performance mapping
- The model learns what combinations of features predict high performance FOR YOUR SPECIFIC AUDIENCE
- Retrained weekly as new data comes in

Phase 3 — Active Scoring (Ongoing):
Every concept from Module 6 now gets TWO scores:
1. **Creative Engine Score** (Module 6's judgment based on humor/virality theory)
2. **Predictive Model Score** (statistical prediction based on what's actually worked)

```
CONCEPT: Macron × Animal Crossing × Pension Surgery

Creative Engine Score: 8.2/10
Predictive Model Score: 7.8/10  ✅ ALIGNED

Confidence: HIGH — both scores agree, proceed with confidence.
```

```
CONCEPT: Bardella × Dark Souls × Immigration Policy

Creative Engine Score: 7.5/10
Predictive Model Score: 4.2/10  ⚠️ DIVERGENCE

WARNING: The creative engine thinks this is strong, but the model 
predicts underperformance based on historical data:
- Dark Souls world has averaged 40% below your mean for political topics
- Immigration topics from your account get 30% lower shares (audience 
  may not want to share controversial topics publicly)
- Recommendation: Try same concept in GTA world (historically +65% 
  for controversial topics) or soften the topic angle to increase 
  shareability

OVERRIDE OPTION: Post anyway if you believe the creative judgment. 
The model learns from overrides too.
```

When scores diverge, the system explains WHY and suggests adjustments. The user can override — and the model learns from overrides, potentially discovering that the creative engine was right about a new pattern.

Storage: Supabase tables `virality_predictions`, `feature_vectors`, `model_weights`

---

### 21B — Hook A/B Testing Engine

**What it is**: A system that generates multiple hook variations for every concept and tests them to find the winner.

**How it works**:

For every greenlit concept, the system generates 3-5 hook variations:

```
CONCEPT: Macron × Animal Crossing × Pension Surgery

HOOK A (Absurd Image Cold Open):
First frame: Wide shot of Animal Crossing surgery room, Macron in scrubs,
France on table. No text for 0.5s, then text appears.
Hypothesis: Pure visual shock stops the scroll.

HOOK B (Text-First):
First frame: Black background, white text "POV: They're arguing about 
whether you retire at 62 or 64" — then cut to the surgery scene at 1.5s.
Hypothesis: Relatable text creates curiosity before the visual payoff.

HOOK C (Zoom Reveal):
First frame: Extreme close-up of the heart monitor showing flatline, 
slowly zoom out to reveal the full surgery scene over 2s.
Hypothesis: Mystery creates curiosity — "what am I looking at?"

HOOK D (Format Subversion):
First frame: Uses the exact trending TikTok format template from gaming 
but immediately subverts it with political content at 1s.
Hypothesis: Familiar format hooks gamers, political content surprises them.
```

**Testing Strategy**:

Option 1 — Multi-platform split:
- Hook A → TikTok
- Hook B → Instagram Reels
- Hook C → YouTube Shorts
- Compare watch-through rates at 2 hours
- Winner gets reposted on all platforms

Option 2 — Time-split on single platform:
- Post Hook A on TikTok at 12:00
- If underperforming your average curve at 1 hour, delete and repost Hook B at 13:30
- TikTok's algorithm treats reposts as new content if timing is spaced

Option 3 — Secondary account testing:
- Post Hook A on main account
- Post Hook B on test/secondary account simultaneously
- Compare first-hour velocity
- Use learnings for future concepts (don't repost — avoid duplicate content)

**Learning Output**:

After every test, the system logs:

```
HOOK TEST RESULT — Feb 9, 2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

Concept: Macron × AC × Pension Surgery

Hook A (Absurd Image): Watch-through 68%, 12K views/hr ← WINNER
Hook B (Text-First): Watch-through 52%, 7K views/hr
Hook C (Zoom Reveal): Watch-through 45%, 5K views/hr

INSIGHT: For this audience + topic type + world combination,
absurd image cold opens outperform text-first by 1.7x.

Running averages updated:
- Absurd Image Cold Open: avg 64% watch-through (+2% from last week)
- Text-First: avg 49% watch-through (stable)
- Zoom Reveal: avg 42% watch-through (-3% from last week, declining)
- Format Subversion: avg 58% watch-through (+5%, rising)
```

Over time, the system builds a hook effectiveness matrix specific to your audience:

```
HOOK EFFECTIVENESS BY CONTEXT (your audience):

                    Political  Economic  Cultural  Scandal
Absurd Image         ★★★★★     ★★★★☆    ★★★☆☆    ★★★★★
Text-First           ★★★☆☆     ★★★★★    ★★★★☆    ★★☆☆☆
Zoom Reveal          ★★☆☆☆     ★★☆☆☆    ★★★★☆    ★★★☆☆
Format Subversion    ★★★★☆     ★★★☆☆    ★★★★★    ★★★☆☆
Pattern Interrupt    ★★★☆☆     ★★★☆☆    ★★★☆☆    ★★★★☆
```

Storage: Supabase tables `hook_tests`, `hook_effectiveness`

---

### 21C — Timing Optimization Engine

**What it is**: A system that determines the OPTIMAL moment to post each concept, considering time of day, topic lifecycle, audience behavior, and competitive landscape.

#### Time-of-Day Optimization

Starts with platform default best times, then learns YOUR specific audience behavior:

```
YOUR AUDIENCE ACTIVITY HEATMAP (learned over time):

         Mon   Tue   Wed   Thu   Fri   Sat   Sun
06:00    ░░    ░░    ░░    ░░    ░░    ░░    ░░
08:00    ▓░    ▓░    ▓░    ▓░    ▓░    ░░    ░░
10:00    ▓▓    ▓▓    ▓▓    ▓▓    ▓▓    ▓░    ░░
12:00    ██    ██    ██    ██    ██    ▓▓    ▓░  ← PEAK
14:00    ▓▓    ▓▓    ▓▓    ▓▓    ▓░    ▓░    ▓░
16:00    ▓░    ▓░    ▓░    ▓░    ▓░    ▓░    ▓░
18:00    ██    ██    ██    ██    ▓▓    ▓▓    ▓▓  ← PEAK
20:00    ▓▓    ▓▓    ▓▓    ▓▓    ▓▓    ██    ██  ← WEEKEND PEAK
22:00    ▓░    ▓░    ▓░    ▓░    ▓▓    ▓▓    ▓░
00:00    ░░    ░░    ░░    ░░    ░░    ░░    ░░
```

#### Topic Lifecycle Timing

This is more important than time of day. Every trending topic has a lifecycle:

```
TOPIC LIFECYCLE CURVE:

Volume
  │
  │                    ╭──── PEAK (too late — oversaturated)
  │                   ╱    ╲
  │                  ╱      ╲
  │         ╭──────╱        ╲────── DECLINE
  │        ╱  ↑                ╲
  │       ╱   │ SWEET SPOT      ╲
  │      ╱    │ (2-6hrs after    ╲
  │     ╱     │  emergence)       ╲───────
  │    ╱      │                    
  │───╱───────┼──────────────────────────── Time
  │  ↑        
  │  EMERGENCE (too early — audience
  │  doesn't know topic yet)
```

The engine monitors each topic in real time and calculates:

```
TOPIC TIMING ANALYSIS: Macron Pension Speech

Current lifecycle position: SWEET SPOT ✅
Topic emerged: 3.2 hours ago
Estimated peak: 2-4 hours from now
Content saturation: LOW (only 4 meme accounts have posted)
Your concept status: Ready, awaiting greenlight

RECOMMENDATION: ████ POST NOW
Window remaining: ~2-3 hours before saturation
Urgency: HIGH

If you wait 4+ hours:
- Content saturation will be 3x higher
- Topic will be past peak
- Estimated performance drop: -40%
```

Vs:

```
TOPIC TIMING ANALYSIS: EU Budget Regulation

Current lifecycle position: EMERGENCE ⚠️
Topic emerged: 45 minutes ago
Estimated peak: 8-12 hours from now
Content saturation: ZERO
Your concept status: In generation

RECOMMENDATION: ░░░░ WAIT
Optimal post window: 4-6 hours from now
Set auto-alert for when topic enters sweet spot

If you post now:
- Audience doesn't know the topic yet
- No existing conversation to ride
- Estimated performance: -55% vs optimal timing
```

#### Competitive Timing

The engine monitors competitor accounts and factors their activity:

```
COMPETITIVE TIMING CHECK:

Your concept: Macron × Animal Crossing × Pension
Competitor @politique_memes: Just posted a pension meme (12 mins ago)
Competitor @france_gaming: Nothing on this topic yet

OPTIONS:
A) Post now anyway — your angle is different (surgery metaphor vs their take)
   Risk: Some audience overlap, slight saturation
   Estimated impact: -10% vs no competition

B) Wait 2 hours — let their post peak and decline, then post
   Benefit: Fresh content when feed is clearing
   Risk: Topic may cool further
   Estimated impact: +5% vs posting now

C) Post on different platform first — they posted on TikTok, 
   you post on Instagram Reels first, TikTok in 2 hours
   Benefit: Avoid direct head-to-head
   Estimated impact: +15% on Reels

RECOMMENDATION: Option C
```

#### Combined Timing Output

Every greenlit concept gets a timing recommendation:

```
OPTIMAL POST TIMING
━━━━━━━━━━━━━━━━━━

Concept: Macron × AC × Pension Surgery
Generated: 09:15 CET

Best time to post: 12:20 CET today
├── Audience peak: 12:00-13:00 ✅
├── Topic lifecycle: Sweet spot (emerged 4hrs ago) ✅
├── Competitor gap: @politique_memes posted at 11:00, 
│   will be declining by 12:20 ✅
├── Format freshness: Trending format has ~36hrs left ✅
└── Day bonus: Tuesday = your 2nd best performing day ✅

Confidence: 87%

ALERT SET: You will be notified at 12:00 CET with final go/no-go.
```

Storage: Supabase tables `timing_data`, `topic_lifecycle`, `audience_activity`

---

### 21D — Post-Publish Optimization Engine

**What it is**: Active management of content AFTER publishing. Most creators post and walk away. This system monitors, reacts, amplifies, and extends the life of every post.

#### Real-Time Performance Monitor

Every post is tracked against your historical performance curve:

```
PERFORMANCE CURVE (first 6 hours):

Views
  │
  │     YOUR AVERAGE CURVE
  │     (based on last 30 posts)
  │         ╱─────── expected trajectory
  │        ╱
  │       ╱   ★ ← THIS POST (above curve = good)
  │      ╱  ★
  │     ╱ ★
  │    ╱★
  │   ★
  │  ╱
  │─╱────────────────────────── Time
  0   30m   1hr   2hr   4hr   6hr
```

#### Alert System

The engine sends real-time alerts based on performance:

**Underperformance Alert (30 min check)**:
```
⚠️ UNDERPERFORMANCE: "Macron AC Surgery" is tracking 40% below 
your average curve at 30 minutes.

Views: 2,100 (expected: 3,500)
Watch-through: 45% (your avg: 62%)

DIAGNOSIS:
- Hook may be weak for this time slot
- 3 competitor posts on same topic in last hour (saturation)

RECOMMENDED ACTIONS:
1. Delete and repost with Hook B (text-first) in 2 hours
2. Keep and boost with a pinned comment to drive engagement
3. Let it ride — sometimes slow starters pick up at hour 2-3

[DELETE & REPOST] [ADD PINNED COMMENT] [LET IT RIDE]
```

**Viral Trajectory Alert (1-2 hour check)**:
```
🚀 VIRAL TRAJECTORY: "Macron AC Surgery" is tracking 3.2x above 
your average curve!

Views: 45,000 in 1.5 hours (your average at 1.5hr: 14,000)
Watch-through: 78% (your avg: 62%)
Shares: 2,400 (3x your average share rate)
Viral coefficient: 0.12 (anything above 0.08 = strong viral signal)

CURRENT TRAJECTORY: If this holds, estimated 24hr total: 380K-520K views

IMMEDIATE ACTIONS:
1. Cross-post to Instagram Reels NOW (ride the momentum) [DO IT]
2. Cross-post to YouTube Shorts in 1 hour [SCHEDULE]
3. Post X/Twitter still version with this tweet:
   "Ils débattent 62 vs 64 comme si on allait un jour prendre 
   notre retraite 🏥🇫🇷" [COPY TWEET]
4. Pin this comment to drive more engagement:
   "attendez de voir ce qu'il fait à la sécu 💀" [PIN IT]

SEQUEL CONCEPT GENERATED:
"Part 2: Macron tries to fix healthcare in Animal Crossing"
Estimated virality boost from Part 1 momentum: +40%
[GREENLIGHT PART 2] [SAVE FOR LATER]
```

**Mega-Viral Alert (6+ hour check)**:
```
🔥🔥🔥 MEGA-VIRAL: "Macron AC Surgery" has crossed 1M views in 6 hours

This is your best-performing post EVER.

EXTENDED PLAYBOOK:
1. DO NOT post anything else today — let this dominate your profile
2. Part 2 should go out tomorrow at 12:00 (ride the wave, don't compete)
3. I've generated 3 follow-up concepts that reference this post:
   a) "Macron tries physical therapy on France" (Part 2) [8.5 predicted]
   b) "Le Pen as competing surgeon" (spin-off) [7.8 predicted]
   c) "The funeral" (Part 3 — series finale) [8.9 predicted]
4. Engage with TOP comments personally — reply to the top 10
5. Save the best fan comments for a future "reading comments" follow-up
6. Monitor for stitches/duets — reshare the best ones to your story

MEDIA MONITORING:
- 2 journalists have shared your post
- 1 news outlet has embedded it in an article
- 4 competing accounts have posted reaction content
```

#### Comment Management Intelligence

The engine monitors comments and recommends engagement actions:

```
COMMENT INTELLIGENCE — "Macron AC Surgery" (2 hours post)

TOP COMMENTS BY ENGAGEMENT:
1. "mdr le patient est déjà mort depuis 2017" — 340 likes
   → RECOMMEND: Reply with "💀" (minimal, funny, boosts thread)

2. "c'est pas animal crossing c'est la france" — 280 likes
   → RECOMMEND: Pin this comment (perfect audience articulation)

3. "@marie regarde ça c'est toi au taff" — 190 likes
   → RECOMMEND: Don't engage (tag comments are self-sustaining)

4. "partie 2 svp" — 450 likes
   → RECOMMEND: Reply "👀" (tease without confirming, builds anticipation)

DEBATE THREAD DETECTED:
- Comments #7-#34 are arguing about retirement age
- This thread has 89 replies and counting
- RECOMMEND: Do NOT engage — let the debate run, it's driving algorithm

CORRECTION BAIT WORKING:
- 12 comments correcting the heart monitor display
- Each correction drives 3-5 reply threads
- Working as designed ✅
```

Storage: Supabase tables `post_realtime_metrics`, `performance_alerts`, `comment_intelligence`

---

### 21E — Format Trend Velocity Tracker

**What it is**: A real-time tracker of format trend lifecycles that applies multipliers to virality scoring.

Every trending format has a lifecycle. The system tracks WHERE each format is in its curve and applies a multiplier:

```
FORMAT LIFECYCLE TRACKER

Format: "POV: slow zoom + text overlay" (Gaming TikTok origin)

DAY 1 (Emergence):   ████░░░░░░ Multiplier: 3.0x
  First creators using it. High novelty. Algorithm rewards novelty.
  Status: USE IMMEDIATELY if you have a concept that fits.

DAY 2-3 (Growth):    ██████░░░░ Multiplier: 2.5x
  More creators adopting. Still feels fresh. High discovery potential.
  Status: STRONG window. Prioritize concepts using this format.

DAY 4-5 (Peak):      ████████░░ Multiplier: 1.5x
  Mainstream adoption. Audience recognizes the format. Less novelty.
  Status: STILL VIABLE but don't force it. Only use if concept is strong.

DAY 6-7 (Plateau):   ██████████ Multiplier: 1.0x
  Oversaturated. Audience starts scrolling past. No novelty bonus.
  Status: AVOID unless your execution is clearly superior.

DAY 8+ (Decline):    ░░░░░░░░░░ Multiplier: 0.5x
  Actively cringe. Audience associates with latecomer accounts.
  Status: DO NOT USE. Using a dead format signals "not in the loop."

CURRENTLY ACTIVE FORMATS:
┌─────────────────────────────────┬──────────┬────────────┬──────────┐
│ Format                          │ Age      │ Lifecycle  │ Multiplier│
├─────────────────────────────────┼──────────┼────────────┼──────────┤
│ POV: slow zoom + text           │ Day 2    │ Growth     │ 2.5x     │
│ "Put a finger down" subversion  │ Day 5    │ Peak       │ 1.5x     │
│ Anime dramatic reveal edit      │ Day 1    │ Emergence  │ 3.0x  ⚡ │
│ Split-screen reaction           │ Day 7    │ Plateau    │ 1.0x     │
│ Greenscreen news commentary     │ Day 10   │ Decline    │ 0.5x  ⛔│
└─────────────────────────────────┴──────────┴────────────┴──────────┘

⚡ ALERT: "Anime dramatic reveal edit" just entered emergence.
   You have a ~48hr window for maximum novelty bonus.
   Cross-pollination engine has generated 2 political adaptations.
   [VIEW CONCEPTS]
```

The multiplier is applied to the concept's virality score:

```
CONCEPT: Mélenchon × Dark Souls × EU Summit

Base virality score: 7.0
Format: Anime dramatic reveal edit
Format multiplier: 3.0x (Day 1 — Emergence)

ADJUSTED SCORE: 7.0 × 1.43 = 10.0 (capped) 🔥
(Multiplier scaled: 3.0x raw → 1.43x on score to prevent runaway scores)

NOTE: This concept would score 7.0 normally but the format freshness 
bonus makes it a top-priority post. The window closes in ~48 hours.
RECOMMENDATION: Fast-track production, post within 24 hours.
```

Storage: Supabase tables `format_lifecycle`, `format_multipliers`

---

### 21F — Audience Graph Intelligence

**What it is**: Understanding not just WHO your audience is but HOW they share, WHERE content spreads, and which audience clusters drive viral cascades.

#### Share Path Mapping

When your content goes viral, WHERE does it spread?

```
SHARE PATH ANALYSIS — "Macron AC Surgery" (48hr post-mortem)

INITIAL SPREAD (0-2 hours):
Your followers → Direct shares to friends (65% of initial shares)
                → Gaming community accounts (20%)
                → Political commentary accounts (15%)

SECONDARY SPREAD (2-6 hours):
Gaming community → Wider gaming audience (the cross-pollination worked)
Political accounts → Political debate audience
Friend shares → Group chats → Individual reshares

TERTIARY SPREAD (6-24 hours):
Large meme aggregator accounts picked it up (3 accounts, combined 2M followers)
Journalist shares (2 journalists, combined reach 180K)
International French-speaking accounts (Belgium, Quebec, Senegal)

SHARE CLUSTERS IDENTIFIED:
1. Gaming cluster: 34% of total reach
   Entered via: Animal Crossing visual reference
   Engagement type: "I can't believe someone made this" shares
   
2. Political cynicism cluster: 28% of total reach
   Entered via: The editorial angle on pension reform
   Engagement type: "This is so me" shares
   
3. General humor cluster: 22% of total reach
   Entered via: Meme aggregator accounts
   Engagement type: "My friend needs to see this" tag shares
   
4. Media/journalist cluster: 8% of total reach
   Entered via: Quality of satirical commentary
   Engagement type: Quote tweets with commentary
   
5. International francophone cluster: 8% of total reach
   Entered via: French language + universal political humor
   Engagement type: Cross-cultural recognition
```

#### Super-Spreader Identification

```
SUPER-SPREADER ACCOUNTS (accounts that consistently amplify your content):

@gaming_memes_fr (145K followers)
- Has shared 6 of your last 20 posts
- Average amplification: +35K views per share
- Trigger: Gaming world references
- STRATEGY: Prioritize gaming worlds to maintain this amplification channel

@politique_sans_filtre (89K followers)
- Has shared 4 of your last 20 posts
- Average amplification: +22K views per share
- Trigger: Anti-establishment editorial angles
- STRATEGY: Tag or mention them subtly (not directly — feels organic)

@memes_francais (340K followers)
- Has shared 2 of your last 20 posts
- Average amplification: +80K views per share
- Trigger: High production value + absurdist visual
- STRATEGY: These shares are gold. Optimize visual quality for this account.
```

#### Audience Crossover Intelligence

```
AUDIENCE CROSSOVER MAP

Your followers who also follow:
├── Gaming accounts: 42% ← Strongest crossover, validates gaming world strategy
├── Music/Rap accounts: 31% ← Opportunity for rap culture cross-pollination
├── Football accounts: 28% ← Football metaphors will resonate
├── Anime accounts: 24% ← Anime visual styles could work
├── Traditional media: 18% ← Smaller overlap, but these are the sharers
└── Political accounts: 15% ← Surprisingly low — your audience ISN'T political junkies

INSIGHT: Your audience is primarily entertainment-first, not politics-first.
They follow you for the gaming world satire, not for political commentary.
This CONFIRMS the cross-pollination strategy — lead with culture, embed politics.
```

Storage: Supabase tables `share_paths`, `super_spreaders`, `audience_crossover`

---

### 21G — Semantic Trend Matching

**What it is**: Use AI embeddings to find non-obvious connections between topics, formats, characters, and worlds that the creative engine might miss.

**How it works**:

Every element in the system is embedded as a vector:
- All trending topics (from Module 1)
- All trending formats (from Module 2)
- All cultural trends (from Module 3)
- All characters (from Module 10)
- All worlds (from Module 10)
- All past successful concepts (from Module 9)

The system runs cosine similarity searches to find non-obvious connections:

```
SEMANTIC MATCH ALERT — Non-Obvious Connection Detected

TRENDING TOPIC: French farmers blocking highways in protest
CULTURAL TREND: Minecraft "highway to hell" build trend (1.2M views on TikTok FR)

Semantic similarity: 0.82 (HIGH)
Connection: Both involve highways + destruction/obstruction

SUGGESTED CONCEPT:
French farmers building a Minecraft highway blockade, 
tractors as Minecraft vehicles, crops rotting while 
EU regulations spawn as hostile mobs

This connection is NON-OBVIOUS — the creative engine would 
likely not match "farmer protest" with "Minecraft highway trend" 
without semantic similarity analysis.

PREDICTED AUDIENCE BRIDGE:
- Minecraft community: 28M active players in France
- Farmer protest supporters: High emotional engagement
- Crossover: "I can't believe someone made this" share trigger
```

```
SEMANTIC MATCH ALERT — Audience Overlap Detected

DATA: People who engage with anime edit content also engage with 
economic anxiety content at a 2.8x higher rate than average.

INSIGHT: The anime audience has significant economic anxiety overlap.
Anime dramatic reveal formats may be uniquely effective for economic topics.

RECOMMENDATION: Next economic topic (cost of living, wages, etc.) — 
try anime dramatic reveal format instead of default gaming world.
```

The system runs these similarity searches every time new trends are ingested and surfaces the highest-potential non-obvious connections as alerts in the command center.

Storage: Supabase tables `semantic_embeddings`, `semantic_matches`

---

### 21H — Virality Cascade Manager

**What it is**: When one of your posts enters viral territory, this system manages the cascade — amplifying momentum, feeding follow-up content, and maximizing the total impact of the viral moment.

#### Cascade Detection

```
CASCADE DETECTION — Triggers when:
- Your post exceeds 5x average velocity for 2+ hours
- Other accounts start creating response/remix/reaction content
- Your post is being stitched/dueted 10+ times
- Media outlets reference or embed your content
- A hashtag associated with your content starts trending independently
```

#### Cascade Playbook

When a cascade is detected, the system activates a staged playbook:

```
CASCADE PLAYBOOK — "Macron AC Surgery" (Detected at Hour 3)

STAGE 1 — RIDE THE WAVE (Hour 0-6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ Cross-post to all platforms (Reels, Shorts, X) — DONE
✅ Pin optimized comment — DONE
✅ Engage with top 10 comments — DO NOW
☐ Reply to the 3 best duets/stitches with "💀" or "👀"
☐ Repost the best fan remix to your story with credit
☐ DO NOT post any other content today — let this breathe

STAGE 2 — FEED THE FIRE (Hour 6-24)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

☐ Post a "behind the concept" story (how you made it)
☐ Respond to the most popular counter-argument comment with a follow-up image
☐ If journalists shared it, screenshot and post to story ("merci @journalist")
☐ Part 2 concept is queued — DO NOT post yet, wait for Stage 3

STAGE 3 — EXTEND THE ARC (Hour 24-48)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

☐ Post Part 2 — timing: exactly 24hrs after original post
☐ Part 2 hook should reference Part 1: "après la chirurgie..."
☐ This rides the follow-up audience who subscribed from Part 1
☐ If Part 2 also cascades → prepare Part 3 (the trilogy effect)

STAGE 4 — HARVEST (Hour 48-72)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

☐ Post a "reading your comments" compilation (if applicable)
☐ Save the best remix/reactions for a future compilation
☐ Update character and world effectiveness scores
☐ Full cascade post-mortem (automatic)
☐ Extract new meme templates from what worked
☐ Identify super-spreaders from this cascade for future outreach
```

#### Counter-Content Engine

When someone dunks on your viral post or creates a counter-meme:

```
COUNTER-CONTENT DETECTED:

@competing_account posted a response meme to your "Macron AC Surgery"
Their take: "POV: this meme creator thinks they understand economics"
Performance: 45K views in 2 hours (decent, not viral)

OPTIONS:
A) IGNORE — Their post is riding your momentum, responding gives them more.
   Best if: Their engagement is <20% of yours.

B) RESPOND WITH HUMOR — Generate a counter-counter meme that acknowledges 
   them and escalates the joke.
   Best if: They have a large audience and the exchange benefits both.
   GENERATED CONCEPT: [Counter-concept with their meme as setup, your 
   punchline as escalation]

C) ABSORB — Stitch/duet their post with a funny reaction, pulling their 
   audience to your profile.
   Best if: Their content is actually funny and the collaboration benefits you.

RECOMMENDATION: Option A — their reach is 15% of yours, responding 
elevates them without benefiting you.
```

Storage: Supabase tables `cascade_events`, `cascade_stages`, `counter_content`

---

### Module 21 Summary

The Virality Maximization Engine adds 8 sub-systems:

| Sub-Module | Function | When Active |
|-----------|----------|-------------|
| 21A Predictive Model | Pressure-tests creative judgment with data | Pre-publish |
| 21B Hook A/B Testing | Tests multiple hooks to find the winner | Pre/post-publish |
| 21C Timing Optimization | Determines optimal post moment | Pre-publish |
| 21D Post-Publish Engine | Monitors, alerts, amplifies after posting | Post-publish |
| 21E Format Velocity | Tracks format lifecycle, applies multipliers | Continuous |
| 21F Audience Graph | Maps share paths and super-spreaders | Post-publish learning |
| 21G Semantic Matching | Finds non-obvious creative connections | Continuous |
| 21H Cascade Manager | Manages viral moments with staged playbook | Triggered by cascade |

**Key Principle**: The system gets smarter with every post. By post 20, the timing engine is calibrated. By post 50, the predictive model is trained. By post 100, the system knows your audience better than you do and every concept, hook, and post time is optimized for YOUR specific audience behavior patterns.

Storage: 12 new Supabase tables across all sub-modules

---

## OpenClaw Implementation

### Skill Structure

Each module maps to one or more OpenClaw skills:

```
openclaw-skills/
├── trend-scanner/          # Modules 1, 12
│   ├── SKILL.md
│   ├── news-scanner.ts
│   ├── x-scanner.ts
│   ├── google-trends.ts
│   └── event-calendar.ts
├── format-intelligence/    # Module 2
│   ├── SKILL.md
│   ├── tiktok-scanner.ts
│   ├── instagram-scanner.ts
│   └── format-report.ts
├── cross-pollination/      # Module 3
│   ├── SKILL.md
│   ├── cultural-scanner.ts
│   └── adaptation-generator.ts
├── editorial-engine/       # Modules 4, 5
│   ├── SKILL.md
│   ├── topic-ranker.ts
│   ├── editorial-filter.ts
│   └── audience-mapper.ts
├── creative-engine/        # Module 6
│   ├── SKILL.md
│   ├── concept-generator.ts
│   ├── character-bible.json
│   ├── world-library.json
│   └── virality-framework.md
├── manual-injection/       # Module 7
│   ├── SKILL.md
│   └── topic-injector.ts
├── production-packager/    # Module 8
│   ├── SKILL.md
│   ├── image-prompt-gen.ts
│   ├── edit-blueprint-gen.ts
│   ├── caption-gen.ts
│   └── audio-direction-gen.ts
├── feedback-loop/          # Module 9
│   ├── SKILL.md
│   ├── performance-tracker.ts
│   ├── virality-postmortem.ts
│   └── decay-detector.ts
├── controversy-radar/      # Module 14
│   ├── SKILL.md
│   ├── legal-checker.ts
│   └── platform-risk.ts
├── competitor-intel/       # Module 15
│   ├── SKILL.md
│   └── competitor-tracker.ts
├── ab-testing/             # Module 16
│   ├── SKILL.md
│   └── variation-generator.ts
├── template-library/       # Modules 17, 18
│   ├── SKILL.md
│   ├── template-matcher.ts
│   └── newsjack-deployer.ts
└── narrative-tracker/      # Module 13
    ├── SKILL.md
    └── arc-tracker.ts
├── virality-engine/       # Module 21
│   ├── SKILL.md
│   ├── predictive-model.ts        # 21A
│   ├── hook-ab-testing.ts         # 21B
│   ├── timing-optimizer.ts        # 21C
│   ├── post-publish-monitor.ts    # 21D
│   ├── format-velocity-tracker.ts # 21E
│   ├── audience-graph.ts          # 21F
│   ├── semantic-matcher.ts        # 21G
│   └── cascade-manager.ts        # 21H
└── config-cms/            # Module 20
    ├── SKILL.md
    └── admin-panel/
```

### Cron Schedule

| Job | Frequency | Skill |
|-----|-----------|-------|
| French news/X scan | Every 4 hours | trend-scanner |
| TikTok/IG format scan | Every 6 hours | format-intelligence |
| Cultural vertical scan | Every 4 hours | cross-pollination |
| Topic ranking + concept generation | After each trend scan | editorial-engine + creative-engine |
| Daily brief delivery | 8:00 AM CET | creative-engine |
| Performance data collection | Every 24 hours | feedback-loop |
| Competitor scan | Every 12 hours | competitor-intel |
| Event calendar check | Daily at 6:00 AM CET | trend-scanner |
| Decay detection | Weekly | feedback-loop |
| Template library update | After each performance review | template-library |
| Post-publish monitoring | Every 15 minutes (active posts only) | virality-engine |
| Format lifecycle tracking | Every 6 hours | virality-engine |
| Semantic similarity scan | After each trend ingestion | virality-engine |
| Predictive model retraining | Weekly | virality-engine |
| Audience graph update | After each post reaches 24hr mark | virality-engine |
| Cascade detection | Every 5 minutes (when any post >2x avg velocity) | virality-engine |

### Messaging Interface

User interacts with the system primarily via WhatsApp or Telegram:

```
DAILY BRIEF (8:00 AM):
"Morning. 5 concepts ready. Top pick:

🎮 Macron does open heart surgery on France in Animal Crossing
📊 Virality score: 8.2/10
⏰ Best posted before 13:00

Reply:
1 — Greenlight this
2 — Show all 5
3 — Inject my own topic
4 — Show cross-pollination alerts"

USER: "1"

SYSTEM: "Production package ready:
- 3 image prompt variations generated
- Edit blueprint: 10s, 3 shots
- Caption + hashtags for TikTok, IG, X
- Optimal post time: 12:15 CET

[Full package in Notion/Google Doc link]"
```

---

## Supabase Database Schema

### Tables

| Table | Purpose |
|-------|---------|
| `trending_topics` | Raw ingested topics with engagement signals |
| `format_intelligence` | Current platform format trends |
| `cultural_trends` | Non-political viral content DNA |
| `cross_pollination_concepts` | Political adaptations of cultural trends |
| `ranked_topics` | Filtered and scored topics with editorial angles |
| `audience_maps` | Per-topic audience profiles |
| `concepts` | Generated content concepts with full briefs |
| `production_packages` | Ready-to-assemble content packages |
| `post_performance` | Published content performance metrics |
| `learning_weights` | System learning — what works, what doesn't |
| `characters` | Character bible |
| `worlds` | Game world library |
| `narrative_arcs` | Running storylines and callbacks |
| `event_calendar` | Predicted upcoming events |
| `pre_production_queue` | Pre-built concept skeletons for predicted events |
| `competitor_intelligence` | Competing account tracking |
| `meme_templates` | Proven reusable concept templates |
| `injected_topics` | Manually injected topics and their pipeline results |

---

## User Inputs Required Before Build

The following sections need to be filled in by the user to make the system operational:

### 1. Character Bible
- List of all characters (real politicians as game avatars? Original characters? Both?)
- For each: visual description, personality, comedic function, which worlds they appear in

### 2. Editorial Pillars
- 5-10 core political positions/themes
- For each: the specific take, the emotional register, what's off-limits

### 3. Accounts to Monitor
- 20-30 French accounts for format intelligence (political memes, general memes, satire)
- 10-20 French accounts per cultural vertical (gaming, anime, football, rap, etc.)
- 5-10 competing political content accounts

### 4. Production Capacity
- How many shorts per day/week?
- Which generation tools are you using? (Midjourney, Flux, Runway, Kling, etc.)
- Solo production or team?

### 5. Tone References
- 3-5 existing accounts or pieces of content that nail the tone you're going for
- What's too far? What's not far enough?

### 6. Platform Priority
- Which platforms are primary? TikTok, Instagram, X, YouTube Shorts?
- Separate accounts per platform or cross-posting?

---

## Build Phases

### Phase 1 — Foundation (Week 1-2)
- Supabase schema setup
- OpenClaw installation and configuration
- Character bible and world library populated
- Trend scanning skills (news, X, Google Trends)
- Basic creative engine prompt

### Phase 2 — Intelligence Layer (Week 3-4)
- TikTok/Instagram format intelligence via Apify
- Cross-pollination engine
- Virality framework integrated into creative engine
- Manual injection mode

### Phase 3 — Production Pipeline (Week 5-6)
- Production package generator
- Messaging interface (WhatsApp/Telegram daily briefs)
- Newsjacking templates
- Controversy radar

### Phase 4 — Learning & Optimization (Week 7-8)
- Performance feedback loop
- A/B testing framework
- Meme template library
- Content decay tracking
- Narrative arc tracker

### Phase 5 — Competitive Edge (Ongoing)
- Competitor intelligence
- Trend prediction refinement
- System prompt optimization based on performance data
- New world/character additions

### Phase 6 — Dashboards (Week 9-14)
- Private dashboard MVP (React + Supabase Realtime)
- Public dashboard design and build
- Real-time data visualization layer
- Public dashboard launch and SEO strategy

---

## Module 19 — Dashboards

Two separate applications reading from the same data layer.

---

### 19A — Private Dashboard (Command Center)

**Purpose**: Internal tool for content creation decisions. The cockpit of the meme machine.

**Access**: Private, password-protected, single user.

**Tech**: React + Supabase Realtime + Tailwind + Recharts/D3

#### Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  MEME MACHINE — COMMAND CENTER                    [Live] 14:32  │
├────────────────────┬────────────────────┬───────────────────────┤
│                    │                    │                       │
│  TRENDING TOPICS   │  EMOTION RADAR     │  ENGAGEMENT VELOCITY  │
│  (Live ranked      │  (What France is   │  (What's accelerating │
│   list with heat   │   feeling right    │   fastest right now)  │
│   scores, trend    │   now — radar      │                       │
│   direction,       │   chart)           │  ▲ Topic A  +400%/hr  │
│   time left)       │                    │  ▲ Topic B  +280%/hr  │
│                    │   😡 Anger: 42%    │  ▲ Topic C  +190%/hr  │
│  🔴 Topic 1  9.2  │   😤 Cynicism: 28% │  ▼ Topic D  -50%/hr   │
│  🔴 Topic 2  8.7  │   😂 Mockery: 18%  │                       │
│  🟠 Topic 3  7.4  │   😰 Fear: 8%      │                       │
│  🟠 Topic 4  6.9  │   🤷 Fatigue: 4%   │                       │
│  🔵 Topic 5  5.1  │                    │                       │
│                    │                    │                       │
├────────────────────┴────────────────────┴───────────────────────┤
│                                                                 │
│  CONTENT GAP DETECTOR                                           │
│  Topics with high engagement but LOW content coverage           │
│                                                                 │
│  🟢 [Topic X] — 45K tweets, only 3 meme accounts covering it   │
│  🟢 [Topic Y] — Rising fast, ZERO satirical content exists      │
│  🟢 [Topic Z] — Mainstream media ignoring, Reddit exploding     │
│                                                                 │
├─────────────────────────────────┬───────────────────────────────┤
│                                 │                               │
│  CROSS-POLLINATION ALERTS       │  YOUR PERFORMANCE             │
│  🎮 Gaming format trending      │                               │
│     ⏰ ~36hrs left              │  Last post: 450K views        │
│     "Adaptation: Macron as..."  │  Avg this week: 280K          │
│                                 │  Follower growth: +2.1K/week  │
│  🎵 Rap clip format viral       │  Best performer: [Concept X]  │
│     ⏰ ~24hrs left              │                               │
│     "Adaptation: EU as..."      │  Concepts generated: 34       │
│                                 │  Concepts greenlit: 8         │
│  ⚽ Football meme format        │  Greenlight rate: 23%         │
│     ⏰ ~48hrs left              │                               │
│                                 │                               │
├─────────────────────────────────┴───────────────────────────────┤
│                                                                 │
│  CONCEPT QUEUE                                                  │
│  Ready for greenlight — ranked by virality score                │
│                                                                 │
│  ⭐ 8.2  Macron surgery in Animal Crossing  [GREENLIGHT] [PASS] │
│  ⭐ 7.8  Darmanin as GTA bouncer           [GREENLIGHT] [PASS] │
│  ⭐ 7.5  EU Farmville while farms burn      [GREENLIGHT] [PASS] │
│  ⭐ 7.1  Mélenchon Sims cult compound      [GREENLIGHT] [PASS] │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  MANUAL INJECTION                                               │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ Drop a topic, policy, quote, or link here...            │    │
│  └─────────────────────────────────────────────────────────┘    │
│  [Generate Concepts]  [Reactive Mode — URGENT]                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Private Dashboard — Key Interactions

| Action | What Happens |
|--------|-------------|
| Click any trending topic | Expands to full breakdown: sources, quotes, audience sentiment, editorial angle suggestions, existing concepts |
| Click "GREENLIGHT" on concept | Triggers Module 8 — production package generated, notification sent |
| Click "PASS" on concept | Concept archived, system learns from rejection |
| Click cross-pollination alert | Shows full adaptation concepts, one-click greenlight |
| Click emotion on radar | Filters trending topics by that emotion |
| Submit manual injection | Runs full pipeline (Modules 4-8), concepts appear in queue within minutes |
| Click "Reactive Mode — URGENT" | Prioritizes speed over depth, generates top concept + production package immediately |

#### Real-Time Updates

Supabase Realtime subscriptions on:
- `trending_topics` — new topics appear as they're detected
- `concepts` — new concepts appear when generated
- `post_performance` — live metrics update
- `cultural_trends` — cross-pollination alerts appear in real time

---

### 19B — Public Dashboard (Le Pouls de la France)

**Purpose**: A real-time political sentiment tracker for France. Open to anyone. Beautifully designed. Inherently shareable.

**Access**: Public, no login required.

**Tech**: React + Supabase Realtime + D3.js + Three.js (for hero visualization) + Tailwind

**Domain suggestion**: `lepouls.fr` or `pouls.fr` or `pulse.france` or similar

**Design Language**:
- Dark mode primary (deep navy/charcoal, not pure black)
- Accent colors map to emotions (red = anger, blue = sadness, yellow = mockery, purple = fear, green = hope, orange = defiance)
- Fluid animations — everything breathes and shifts, nothing static
- Data as art — the visualizations should be beautiful enough to screenshot
- Typography: clean, modern, slightly editorial (think Bloomberg meets Le Monde meets a museum installation)
- Mobile-first — most traffic will come from social shares on phones
- Every view has a one-click share button that generates an OG image

#### Page 1 — The Mood (Hero / Landing)

The first thing anyone sees. One massive visualization that communicates France's emotional state RIGHT NOW.

**Option A — Breathing Orb**
A large 3D sphere (Three.js) that shifts color based on dominant emotion. Surface texture ripples with activity. Particles emanate faster when engagement is high. Below it, a single line: "France is feeling: [dominant emotion]" with percentage breakdown.

**Option B — Weather Map**
France as a geographic outline, regions colored by dominant local emotion/topic. Storms (particle effects) over areas with highest engagement. Weather-style language: "An anger front is moving across Île-de-France, with pockets of cynicism in the south."

**Option C — Pulse Line**
A massive heartbeat/EKG-style line that represents France's emotional intensity in real time. Spikes correspond to moments of high engagement. The line's color shifts with dominant emotion. Below: "France's pulse: [BPM metaphor for engagement intensity]"

All options should:
- Be mesmerizing enough that people pause and watch
- Update visibly in real time (not just every 5 minutes)
- Generate a unique OG image for social sharing
- Work beautifully on mobile

Below the hero: quick stats strip showing:
```
📊 12.4M posts analyzed today | 🔥 Top topic: [X] | 😡 Dominant mood: Anger (42%) | ⏰ Updated: 3 seconds ago
```

#### Page 2 — Topics (Le Débat)

**Topic Heatmap / Bubble Chart**

Interactive visualization where:
- Each bubble = one topic
- Bubble SIZE = volume of conversation
- Bubble COLOR = dominant emotion about that topic
- Bubble ANIMATION = velocity (pulsing = growing fast, still = stable, shrinking = cooling)
- Bubbles jostle and interact with each other (physics simulation)
- Hover/tap any bubble → preview card with topic summary and key stats
- Click → full topic detail page

**Topic Detail Page**

For each topic:
```
┌─────────────────────────────────────────────────────┐
│  PENSION REFORM                                      │
│  ━━━━━━━━━━━━━━                                     │
│                                                      │
│  🔥 Heat Score: 8.7/10                              │
│  📈 Trending for: 14 hours                          │
│  💬 Est. posts: 145,000                             │
│  📊 Sentiment: 64% angry, 22% mocking, 14% fearful │
│                                                      │
│  ┌─────────────────────────────────────────────┐    │
│  │  EMOTION TIMELINE                            │    │
│  │  [Line chart showing sentiment shift over    │    │
│  │   the last 24-48 hours for this topic]       │    │
│  └─────────────────────────────────────────────┘    │
│                                                      │
│  THE DEBATE                                          │
│  ┌──────────────────┬──────────────────┐            │
│  │ SIDE A           │ SIDE B           │            │
│  │ "Reform is       │ "This is an      │            │
│  │  necessary for   │  attack on       │            │
│  │  fiscal health"  │  workers' rights" │            │
│  │                  │                  │            │
│  │ 23% of posts     │ 61% of posts     │            │
│  │ Tone: pragmatic  │ Tone: outraged   │            │
│  └──────────────────┴──────────────────┘            │
│                                                      │
│  KEY QUOTES                                          │
│  Representative posts from each side, curated        │
│                                                      │
│  RELATED TOPICS                                      │
│  [Linked bubbles showing connected issues]           │
│                                                      │
│  [SHARE THIS TOPIC] [EMBED]                         │
└─────────────────────────────────────────────────────┘
```

#### Page 3 — Emotions (Les Émotions)

**Emotion Deep Dive**

Full-page view of France's emotional landscape:

```
┌─────────────────────────────────────────────────────┐
│  HOW FRANCE FEELS RIGHT NOW                          │
│                                                      │
│  ┌─────────────────────────────────────────────┐    │
│  │  EMOTION RADAR                               │    │
│  │  [Large radar/spider chart]                  │    │
│  │                                              │    │
│  │        Anger ████████████░░ 42%              │    │
│  │      Mockery ██████░░░░░░░░ 22%              │    │
│  │     Cynicism █████░░░░░░░░░ 18%              │    │
│  │         Fear ███░░░░░░░░░░░ 10%              │    │
│  │    Defiance  ██░░░░░░░░░░░░  5%              │    │
│  │        Hope  █░░░░░░░░░░░░░  3%              │    │
│  └─────────────────────────────────────────────┘    │
│                                                      │
│  Click any emotion to see what's driving it:         │
│                                                      │
│  😡 ANGER — driven by:                              │
│     1. Pension reform (52% of anger)                 │
│     2. Immigration policy (23%)                      │
│     3. Cost of living (15%)                          │
│     4. Other (10%)                                   │
│                                                      │
│  ┌─────────────────────────────────────────────┐    │
│  │  EMOTION HISTORY (Past 30 Days)              │    │
│  │  [Stacked area chart showing how emotions    │    │
│  │   have shifted over time]                    │    │
│  │                                              │    │
│  │  Notable moments:                            │    │
│  │  • Feb 3: Anger spiked 40% after [event]    │    │
│  │  • Jan 28: Mockery peaked during [event]    │    │
│  │  • Jan 15: Fear rose 25% following [event]  │    │
│  └─────────────────────────────────────────────┘    │
│                                                      │
│  [SHARE] [EMBED] [DOWNLOAD REPORT]                  │
└─────────────────────────────────────────────────────┘
```

#### Page 4 — The Divide (La Fracture)

**Polarization Tracker**

The most shareable page — shows where France is most divided:

```
┌─────────────────────────────────────────────────────┐
│  WHERE FRANCE IS MOST DIVIDED                        │
│                                                      │
│  TOPIC              DIVISION INDEX    INTENSITY      │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    │
│                                                      │
│  Immigration    ◄████████|████████►   🔴 Extreme    │
│                   38%    │    62%                     │
│                                                      │
│  Pension Reform ◄██████|██████████►   🔴 Extreme    │
│                   31%  │    69%                       │
│                                                      │
│  EU Membership  ◄███████|█████████►   🟠 High       │
│                   42%   │   58%                       │
│                                                      │
│  Climate Policy ◄████████|████████►   🟠 High       │
│                   45%    │   55%                      │
│                                                      │
│  Education      ◄█████████|███████►   🟡 Moderate   │
│                    52%    │  48%                      │
│                                                      │
│  Click any topic to see what each side is saying     │
│                                                      │
│  DIVISION TREND (Past 90 Days)                       │
│  [Line chart: is France becoming MORE or LESS        │
│   divided over time?]                                │
│                                                      │
│  [SHARE] [EMBED]                                     │
└─────────────────────────────────────────────────────┘
```

#### Page 5 — Rising (L'Émergent)

**Early Warning / What's Next**

Topics that are small but growing fast — the "what to watch" section:

```
┌─────────────────────────────────────────────────────┐
│  RISING — WHAT FRANCE WILL BE TALKING ABOUT NEXT     │
│                                                      │
│  ⚡ [Topic A]                                        │
│     Volume: Low (2,400 posts) but growing +380%/hr   │
│     First detected: 2 hours ago                      │
│     Source: Started on Reddit, now spreading to X     │
│     Emotion: Anger                                   │
│     Why it matters: [1-line context]                 │
│                                                      │
│  ⚡ [Topic B]                                        │
│     Volume: Medium (8,100 posts) growing +190%/hr    │
│     First detected: 5 hours ago                      │
│     Source: X political accounts, picked up by BFM   │
│     Emotion: Mockery                                 │
│     Why it matters: [1-line context]                 │
│                                                      │
│  ⚡ [Topic C]                                        │
│     Volume: Low (900 posts) but growing +520%/hr     │
│     First detected: 45 minutes ago                   │
│     Source: TikTok — single video going viral         │
│     Emotion: Outrage                                 │
│     Why it matters: [1-line context]                 │
│                                                      │
│  PAST PREDICTIONS                                    │
│  Topics we flagged early that later trended:         │
│  ✅ [Topic X] — flagged 6hrs before peak             │
│  ✅ [Topic Y] — flagged 12hrs before mainstream      │
│  ❌ [Topic Z] — flagged but never peaked             │
│  Prediction accuracy: 73%                            │
│                                                      │
│  [SHARE] [EMBED]                                     │
└─────────────────────────────────────────────────────┘
```

#### Page 6 — Timeline (La Chronologie)

**Historical View**

```
┌─────────────────────────────────────────────────────┐
│  FRANCE'S EMOTIONAL TIMELINE                         │
│                                                      │
│  [Interactive timeline — scroll horizontally]        │
│                                                      │
│  ──●─────────●──────●────────●──────●───────●──►    │
│    Jan 15    Jan 22  Jan 28   Feb 1  Feb 5   Now    │
│    Fear      Anger   Mockery  Anger  Cynicism        │
│    spike     spike   peak     wave   rising          │
│    │         │       │        │      │               │
│    Terror    Pension Macron   EU     Cost of         │
│    threat    debate  gaffe    vote   living data     │
│                                                      │
│  Click any point to see full topic breakdown         │
│  Drag to select range for comparison                 │
│                                                      │
│  [Filter: Last 7 days | 30 days | 90 days | Year]   │
│  [SHARE] [EMBED] [DOWNLOAD DATA]                    │
└─────────────────────────────────────────────────────┘
```

#### Shareability Engine

Every single view on the public dashboard must be shareable:

**Auto-generated OG images**: When someone shares a link to any page or topic, the preview image is a dynamically generated snapshot of the current data. Not a static logo — the actual live visualization as an image. This makes every share a piece of content in itself.

**Embed widgets**: Media outlets, bloggers, and commentators can embed specific views (emotion radar, topic heatmap, divide tracker) on their own sites. Each embed links back to the full dashboard. Free distribution.

**Daily/Weekly auto-posts**: The system auto-generates shareable image summaries:
- "France's mood today" — daily summary card
- "This week in French emotions" — weekly recap
- "The most divisive topic this month" — monthly highlight
- These can be auto-posted to the dashboard's own X/Instagram accounts

**Screenshot optimization**: Every visualization is designed to look good as a screenshot on mobile. Clean backgrounds, high contrast text, no UI chrome that looks ugly when cropped. People WILL screenshot this and post it — design for that.

#### SEO Strategy

The public dashboard is an SEO play:

| Target Keyword | Page |
|---------------|------|
| "French political trends" | Landing page |
| "What is France talking about" | Topics page |
| "French public opinion [topic]" | Topic detail pages |
| "France political sentiment" | Emotions page |
| "Most divisive topics France" | Divide page |
| "[Specific topic] French opinion" | Auto-generated topic pages |

Each topic detail page is a unique URL that gets indexed. As the system tracks hundreds of topics, you build a massive long-tail SEO footprint over time.

#### Data Sources Attribution

The public dashboard should transparently show its methodology:
- "Analysis based on [X] million posts across Twitter/X, Reddit, French news outlets, and public forums"
- "Sentiment analysis powered by AI"
- "Updated in real time"
- No mention of TikTok/Instagram scraping (gray area legally)
- No mention of the private content creation pipeline

#### Monetization Potential (Future)

| Model | Description |
|-------|-------------|
| API access | Sell real-time French sentiment data to media companies, political consultants, brands |
| Premium tier | Historical data, custom topic tracking, detailed reports, CSV exports |
| Embedded analytics | White-label version for news sites |
| Sponsored insights | Brands pay to see sentiment around their industry (without influencing the data) |
| Political consulting | Real-time sentiment briefings for campaigns |

This is optional and future-state but worth designing the data layer to support it.

---

### Dashboard Data Architecture

Both dashboards read from the same Supabase layer:

```
SHARED DATA (powers both dashboards):
├── trending_topics          → Topic data, engagement signals
├── topic_sentiment          → Emotion breakdown per topic
├── national_mood            → Aggregated emotion scores
├── national_mood_history    → Historical mood data
├── topic_polarization       → Division index per topic
├── rising_topics            → Early detection data
├── platform_quotes          → Representative posts/quotes
└── event_timeline           → Historical events + emotion spikes

PRIVATE DATA (command center only):
├── concepts                 → Generated content concepts
├── production_packages      → Ready-to-assemble packages
├── post_performance         → Your content metrics
├── characters               → Character bible
├── worlds                   → World library
├── learning_weights         → System learning data
├── competitor_intelligence  → Competitor tracking
├── editorial_pillars        → Your editorial framework
├── cross_pollination_concepts → Adaptation ideas
└── meme_templates           → Proven templates
```

### New Supabase Tables for Dashboards

```sql
-- National mood aggregate (updates every 5-15 minutes)
CREATE TABLE national_mood (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  timestamp TIMESTAMPTZ NOT NULL,
  anger DECIMAL,
  mockery DECIMAL,
  cynicism DECIMAL,
  fear DECIMAL,
  defiance DECIMAL,
  hope DECIMAL,
  exhaustion DECIMAL,
  overall_intensity DECIMAL,
  dominant_emotion TEXT,
  posts_analyzed INTEGER
);

-- Per-topic sentiment breakdown
CREATE TABLE topic_sentiment (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  topic_id UUID REFERENCES trending_topics(id),
  timestamp TIMESTAMPTZ NOT NULL,
  anger DECIMAL,
  mockery DECIMAL,
  cynicism DECIMAL,
  fear DECIMAL,
  defiance DECIMAL,
  hope DECIMAL,
  side_a_summary TEXT,
  side_a_percentage DECIMAL,
  side_b_summary TEXT,
  side_b_percentage DECIMAL,
  key_quotes JSONB
);

-- Polarization tracking
CREATE TABLE topic_polarization (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  topic_id UUID REFERENCES trending_topics(id),
  timestamp TIMESTAMPTZ NOT NULL,
  division_index DECIMAL,
  intensity TEXT,
  side_a_position TEXT,
  side_b_position TEXT,
  trend_direction TEXT
);

-- Historical mood for timeline
CREATE TABLE national_mood_history (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  date DATE NOT NULL,
  hour INTEGER,
  anger DECIMAL,
  mockery DECIMAL,
  cynicism DECIMAL,
  fear DECIMAL,
  defiance DECIMAL,
  hope DECIMAL,
  dominant_emotion TEXT,
  trigger_event TEXT,
  posts_analyzed INTEGER
);

-- Representative quotes for public display
CREATE TABLE platform_quotes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  topic_id UUID REFERENCES trending_topics(id),
  platform TEXT,
  quote_text TEXT,
  author_handle TEXT,
  engagement_score DECIMAL,
  sentiment TEXT,
  side TEXT,
  detected_at TIMESTAMPTZ
);
```

---

### Updated Build Phases (Final)

### Phase 1 — Foundation + CMS (Week 1-2)
- Supabase schema setup (ALL tables including Module 21 tables)
- **CMS/Admin panel built and deployed (Module 20) — PRIORITY**
- Pre-populated starter data (10 characters, 8 worlds, 7 pillars)
- User begins populating characters, worlds, pillars, accounts at own pace
- OpenClaw installation and configuration
- Trend scanning skills (news, X, Google Trends)
- Basic creative engine prompt (Module 6 Layer 1-3)

### Phase 2 — Intelligence Layer (Week 3-4)
- TikTok/Instagram format intelligence via Apify (Module 2)
- Cross-pollination engine (Module 3)
- Full Meme Intelligence Engine prompt (Module 6 all layers)
- Manual injection mode (Module 7)
- Sentiment analysis pipeline (powers both dashboards)
- Format Velocity Tracker (Module 21E)

### Phase 3 — Production Pipeline (Week 5-6)
- Production package generator (Module 8)
- Messaging interface (WhatsApp/Telegram daily briefs)
- Newsjacking templates (Module 18)
- Controversy radar (Module 14)
- Timing Optimization Engine (Module 21C)

### Phase 4 — Learning & Optimization (Week 7-8)
- Performance feedback loop (Module 9)
- Hook A/B testing framework (Module 21B)
- Post-publish optimization engine (Module 21D)
- Meme template library (Module 17)
- Content decay tracking
- Narrative arc tracker (Module 13)

### Phase 5 — Virality Intelligence (Week 9-10)
- Predictive virality model training (Module 21A — needs 50+ posts of data)
- Semantic trend matching (Module 21G)
- Audience graph intelligence (Module 21F)
- Virality cascade manager (Module 21H)
- Competitor intelligence (Module 15)

### Phase 6 — Private Dashboard (Week 9-12)
- React app scaffolding (parallel with Phase 5)
- Supabase Realtime integration
- All command center panels
- Greenlight/pass workflow
- Manual injection interface
- Module 21 alerts and optimization panels
- Mobile responsive

### Phase 7 — Public Dashboard (Week 13-16)
- Design system and visual language
- Hero visualization (The Mood — Three.js)
- Topic heatmap (D3.js)
- Emotion deep dive
- The Divide (polarization tracker)
- Rising topics
- Historical timeline
- Share/embed system with dynamic OG images
- SEO optimization
- Launch

### Phase 8 — Competitive Edge (Ongoing)
- Trend prediction refinement
- System prompt optimization based on performance data
- New world/character additions
- Public dashboard iteration based on user analytics
- API/monetization layer (future)
- Predictive model retraining (weekly after Phase 5)

---

## ACTION PLAN — Parallel Build Tracks

The system has 4 independent build tracks that can be developed in parallel. Dependencies are marked clearly.

```
WEEK  1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TRACK A — DATA INFRASTRUCTURE
[████ Supabase ████]
[████ CMS ████████████]
      [████ Sentiment Pipeline ████]
                              [████ Module 21 Tables ████]

TRACK B — INTELLIGENCE & CONTENT ENGINE
      [████ Trend Scanning ████]
            [████ Format Intel ████]
            [████ Cross-Pollination ████]
                  [████ Creative Engine (Full) ████]
                  [████ Manual Injection ████]
                        [████ Production Packages ████]
                        [████ Controversy Radar ████]
                        [████ Timing Engine ████]
                              [████ Newsjacking ████]
                              [████ Messaging ████]

TRACK C — LEARNING & OPTIMIZATION
                                    [████ Feedback Loop ████]
                                    [████ Hook A/B Testing ████]
                                    [████ Post-Publish Engine ████]
                                          [████ Template Library ████]
                                          [████ Narrative Tracker ████]
                                                [████ Predictive Model ████]
                                                [████ Semantic Matching ████]
                                                [████ Audience Graph ████]
                                                [████ Cascade Manager ████]
                                                [████ Competitor Intel ████]

TRACK D — DASHBOARDS
[████ CMS (shared with Track A) ████]
                                                [████ Private Dashboard ████████████]
                                                                  [████ Public Dashboard ████████████████]

YOUR TRACK — CONTENT POPULATION (continuous, no blocking)
[░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]
  Fill CMS: characters, worlds, pillars, accounts → ongoing enrichment
  START POSTING (manual at first) by Week 3-4 → feeds the learning engine
```

---

### DETAILED ACTION PLAN

#### WEEK 1 — Foundation

**Track A: Data Infrastructure**
| Day | Task | Deliverable |
|-----|------|-------------|
| 1 | Supabase project creation | Project live, API keys generated |
| 1-2 | Core schema: `characters`, `worlds`, `editorial_pillars`, `monitored_accounts`, `system_settings` | Tables with RLS policies |
| 2-3 | Intelligence schema: `trending_topics`, `format_intelligence`, `cultural_trends`, `cross_pollination_concepts` | Tables ready |
| 3-4 | Content schema: `ranked_topics`, `audience_maps`, `concepts`, `production_packages` | Tables ready |
| 4-5 | Learning schema: `post_performance`, `learning_weights`, `meme_templates`, `narrative_arcs` | Tables ready |
| 5 | Dashboard schema: `national_mood`, `topic_sentiment`, `topic_polarization`, `national_mood_history`, `platform_quotes` | Tables ready |
| 5 | Module 21 schema: `virality_predictions`, `feature_vectors`, `hook_tests`, `timing_data`, `topic_lifecycle`, etc. | All 12 Module 21 tables ready |

**Track B: Intelligence (Setup)**
| Day | Task | Deliverable |
|-----|------|-------------|
| 3-5 | OpenClaw installation and configuration | OpenClaw running, connected to Supabase |
| 4-5 | Basic trend scanner skill — French news RSS (Le Monde, Le Figaro, etc.) | Skill scans every 4 hours, writes to `trending_topics` |

**Track D: Dashboard (CMS only)**
| Day | Task | Deliverable |
|-----|------|-------------|
| 1-5 | CMS React app scaffold — character CRUD, world CRUD, pillar CRUD, accounts CRUD, settings | Working admin panel |
| 5 | Pre-populate starter data (10 characters, 8 worlds, 7 pillars) | Ready for user to edit/enrich |

**Your Track:**
| Day | Task |
|-----|------|
| 5+ | Start editing pre-populated characters — add traits, archetypes, comedic functions |
| 5+ | Review editorial pillars — adjust positions, add off-limits topics |
| 5+ | Start adding accounts to monitor (TikTok, Instagram, X handles) |

---

#### WEEK 2 — Core Scanning

**Track A: Data Infrastructure**
| Task | Deliverable |
|------|-------------|
| Event calendar table (`event_calendar`, `pre_production_queue`) | Tables ready |
| Competitor tables (`competitor_intelligence`) | Tables ready |
| All remaining schema finalized | Complete database |

**Track B: Intelligence**
| Task | Deliverable |
|------|-------------|
| X/Twitter FR scanner skill | Scans trending topics, writes to `trending_topics` |
| Google Trends FR scanner skill | Scans rising queries, writes to `trending_topics` |
| Reddit scanner (r/france, r/rance) | Community sentiment data |
| Topic ranking skill (Module 4) — scoring logic | Ranks topics by emotional intensity, absurdist potential, etc. |
| Basic creative engine prompt (Module 6 Layers 1-2 — humor mechanics + combination logic) | Generates first concepts from ranked topics |
| First daily brief generation (simple text output) | System produces ranked topics + basic concepts |

**Your Track:**
| Task |
|------|
| Continue enriching characters and worlds in CMS |
| Add 20-30 monitored accounts across platforms |
| Review first automated topic rankings — provide feedback on what's relevant/irrelevant |

---

#### WEEK 3 — Format Intelligence & Cross-Pollination

**Track B: Intelligence**
| Task | Deliverable | Dependency |
|------|-------------|------------|
| Apify scraper setup for TikTok FR trending | Working scraper | Account handles from CMS |
| Apify scraper setup for Instagram Reels FR | Working scraper | Account handles from CMS |
| Format Intelligence skill (Module 2) — detect trending formats, hooks, edit styles | Writes to `format_intelligence`, produces format trend reports |  |
| Cross-Pollination scanner — gaming, anime, football, rap verticals (Module 3) | Scans cultural verticals, writes to `cultural_trends` | Cultural account handles from CMS |
| Cross-Pollination concept generator — adapts cultural trends to political content | Writes adaptation concepts to `cross_pollination_concepts` |  |
| Format Velocity Tracker (Module 21E) — lifecycle tracking + multipliers | Tracks format age, assigns multipliers | Depends on format intelligence data |

**Track B: Creative Engine Enhancement**
| Task | Deliverable |
|------|-------------|
| Expand creative engine prompt to full Module 6 (all 6 layers) | Complete Meme Intelligence Engine |
| Integrate format intelligence into concept generation | Concepts reference current trending formats |
| Integrate cross-pollination into concept generation | Concepts include cultural format hijacks |
| Manual injection mode (Module 7) | User can inject topics via messaging |

**Your Track:**
| Task |
|------|
| START POSTING CONTENT (manual production, system-suggested concepts) |
| Review generated concepts — greenlight/pass to start training the system |
| Your posts from now on feed the learning engine |

---

#### WEEK 4 — Sentiment & Production Prep

**Track A: Data Infrastructure**
| Task | Deliverable |
|------|-------------|
| Sentiment analysis pipeline | Processes topics into emotion breakdowns, writes to `topic_sentiment` and `national_mood` |
| Real-time Supabase subscriptions configured | Data flows in real time |

**Track B: Intelligence**
| Task | Deliverable |
|------|-------------|
| Audience mapping skill (Module 5) | Per-topic audience profiles |
| Virality scoring refinement — integrate all Module 6 scoring criteria | Concepts scored with full virality framework |
| Concept output format finalized — matches the full spec template | Complete concept briefs with all sections |

**Your Track:**
| Task |
|------|
| Continue posting (target: 2-3 posts/week minimum) |
| Manually log performance data for each post (until Module 9 is automated) |
| Feed back: which concepts worked, which didn't, what surprised you |

---

#### WEEK 5 — Production Pipeline

**Track B: Production**
| Task | Deliverable | Dependency |
|------|-------------|------------|
| Production package generator (Module 8) — image prompts, text overlays, audio direction, editing blueprint | Full production packages from greenlit concepts | Creative engine must be working |
| Controversy radar (Module 14) — legal + platform risk assessment | Every concept tagged with risk level | |
| Timing Optimization Engine (Module 21C) — time-of-day + topic lifecycle | Post timing recommendations | Needs trending topic lifecycle data |

**Track B: Messaging**
| Task | Deliverable |
|------|-------------|
| WhatsApp/Telegram bot setup | Connected to OpenClaw |
| Daily brief delivery — 8:00 AM CET | 5 concepts ranked + top pick + greenlight buttons |
| Manual injection via messaging | User texts a topic → system responds with concepts |

**Your Track:**
| Task |
|------|
| Start using daily brief workflow — greenlight concepts via WhatsApp |
| Use production packages to speed up your content creation |
| Continue posting (target: 3-4 posts/week with production packages) |

---

#### WEEK 6 — Newsjacking & Speed

**Track B: Production**
| Task | Deliverable |
|------|-------------|
| Newsjacking templates (Module 18) — pre-built concept skeletons for event types | 8 event type templates ready |
| Reactive mode — urgent concept generation from breaking news | Concepts in <5 minutes from injection |
| Event calendar population (Module 12) — parliament sessions, EU summits, strikes, etc. | Calendar populated for next 3 months |
| Pre-production queue — concept skeletons for upcoming predictable events | Skeletons ready to fill when events happen |

**Your Track:**
| Task |
|------|
| Test reactive mode — inject a breaking news topic and see how fast concepts arrive |
| Review newsjacking templates — adjust to your style |
| Continue posting (system is now producing most of what you need) |

---

#### WEEK 7 — Learning Loop

**Track C: Learning & Optimization**
| Task | Deliverable | Dependency |
|------|-------------|------------|
| Performance feedback loop (Module 9) — automated data collection from platforms | `post_performance` auto-populated | Needs API access to TikTok/IG analytics or manual input |
| Learning weights calculation — character, world, format effectiveness | System knows what works for YOUR audience | Needs 15+ posts of data |
| Virality post-mortem auto-generation | Automatic analysis for posts >2x average | |
| Content decay tracking — format lifecycle monitoring for YOUR content | Flags when formats are getting stale | |

**Track C: Hook Testing**
| Task | Deliverable |
|------|-------------|
| Hook A/B testing framework (Module 21B) | System generates 3-5 hook variants per concept |
| Hook test logging and analysis | Tracks which hooks win, builds effectiveness matrix |

**Your Track:**
| Task |
|------|
| Start A/B testing hooks — post variants, report results |
| Review learning outputs — does the system's understanding match your intuition? |
| By now: 15-25 posts of data feeding the system |

---

#### WEEK 8 — Advanced Learning

**Track C: Learning & Optimization**
| Task | Deliverable |
|------|-------------|
| Post-publish optimization engine (Module 21D) — real-time monitoring + alerts | Underperformance alerts, viral trajectory alerts, action recommendations |
| Comment intelligence | Recommends which comments to reply to, pin, ignore |
| Meme template library (Module 17) | Extracts winning templates from your best performers |
| Narrative arc tracker (Module 13) | Tracks running storylines, suggests callbacks |
| A/B testing framework (Module 16) | System auto-generates variations for testing |

**Your Track:**
| Task |
|------|
| Respond to real-time alerts from the post-publish engine |
| Review meme templates — approve/reject extracted patterns |
| By now: 25-40 posts of data, system is noticeably smarter |

---

#### WEEK 9-10 — Virality Intelligence + Private Dashboard Start

**Track C: Virality Intelligence**
| Task | Deliverable | Dependency |
|------|-------------|------------|
| Predictive virality model — initial training (Module 21A) | Model trained on 50+ posts | HARD DEPENDENCY: needs 50+ posts with performance data |
| Dual scoring — creative engine score + predictive model score with divergence alerts | Two-score system live | |
| Semantic trend matching (Module 21G) — embedding pipeline | Non-obvious connection alerts | |
| Audience graph intelligence (Module 21F) — share path mapping | Super-spreader identification, cluster analysis | Needs several viral/high-performing posts to map |
| Virality cascade manager (Module 21H) — detection + playbook | Automated cascade management | |
| Competitor intelligence (Module 15) — automated scanning | Competitor activity tracking, gap detection | Needs competitor account handles from CMS |

**Track D: Private Dashboard**
| Task | Deliverable |
|------|-------------|
| React app scaffold (extends CMS app) | App structure, routing, auth |
| Supabase Realtime integration | Live data subscriptions |
| Trending Topics panel | Real-time ranked topic list |
| Emotion Radar panel | France's emotional state visualization |
| Engagement Velocity panel | Fastest-accelerating topics |
| Content Gap Detector panel | High engagement, low coverage opportunities |

**Your Track:**
| Task |
|------|
| If you don't have 50 posts yet, ACCELERATE posting — the predictive model needs data |
| Review predictive model vs creative engine scores — does the model make sense? |
| Start using private dashboard instead of just messaging interface |

---

#### WEEK 11-12 — Private Dashboard Complete

**Track D: Private Dashboard**
| Task | Deliverable |
|------|-------------|
| Cross-Pollination Alerts panel | Live cultural trend alerts with adaptation concepts |
| Performance Tracker panel | Your content metrics, running averages |
| Concept Queue with greenlight/pass buttons | Full workflow in the dashboard |
| Manual Injection interface | Drop topics into the UI, concepts appear in minutes |
| Module 21 integration — timing recommendations, hook variants, post-publish alerts, predictive scores all visible | Complete optimization layer in dashboard |
| Mobile responsive | Dashboard works on phone |
| Competitor Activity panel | What competitors are posting |

**Your Track:**
| Task |
|------|
| Full workflow now in dashboard — use it daily |
| By now: 50-80 posts, predictive model is calibrated |
| System is running semi-autonomously — you're mostly greenlighting and producing |

---

#### WEEK 13-16 — Public Dashboard

**Track D: Public Dashboard**
| Week | Task | Deliverable |
|------|------|-------------|
| 13 | Design system — dark mode, emotion color mapping, typography, component library | Complete design system |
| 13 | Hero visualization — The Mood (Three.js breathing orb or chosen option) | Mesmerizing hero section |
| 14 | Topic heatmap — bubble chart with physics (D3.js) | Interactive topic visualization |
| 14 | Topic detail pages — sentiment breakdown, the debate, key quotes | Individual topic pages (SEO) |
| 14 | Emotions page — radar chart, emotion drivers, historical timeline | Emotion deep dive |
| 15 | The Divide — polarization tracker, tug of war visualization | Most shareable page |
| 15 | Rising Topics — early warning section | "What France will talk about next" |
| 15 | Historical Timeline — scrollable, event-linked | Full emotional history |
| 16 | Shareability engine — dynamic OG images, embed widgets, share buttons | Every view shareable |
| 16 | SEO optimization — meta tags, sitemaps, topic page indexing | Long-tail SEO |
| 16 | Launch — soft launch to journalists/commentators, then public | Public dashboard live |

---

### DEPENDENCY MAP

```
CRITICAL PATH (must happen in order):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Supabase Schema → CMS → User populates data → Trend scanning works
                                             → Creative engine has characters/worlds
                                             → Format intel has accounts to monitor

Trend scanning → Topic ranking → Creative engine → Concept generation
                                                  → Production packages
                                                  → Daily briefs

User starts posting → Performance data accumulates → Feedback loop activates
                                                    → Predictive model can train (50+ posts)
                                                    → Audience graph has data to map


PARALLEL TRACKS (can happen simultaneously):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Track A (Data) ←→ Track B (Intelligence) — share Supabase, otherwise independent
Track C (Learning) ←→ Track D (Dashboards) — share data, otherwise independent
Track B (Intelligence) → Track C (Learning) — Learning needs intelligence output
Track A (Data) → Track D (Dashboards) — Dashboards need data infrastructure


HARD DEPENDENCIES (cannot skip):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. CMS must exist before user can populate data
2. User must populate ≥1 character + ≥1 world + ≥1 pillar before creative engine works
3. User must start posting before learning engine has data
4. User must have 50+ posts before predictive model can train
5. Sentiment pipeline must work before dashboards can show emotion data
6. Trend scanning must work before format intelligence can layer on top
7. Creative engine must work before production packages make sense
```

### MILESTONE CHECKLIST

```
WEEK 1:  ☐ Supabase live ☐ CMS deployed ☐ User editing characters
WEEK 2:  ☐ Trend scanning live ☐ First automated topic rankings
WEEK 3:  ☐ Format intelligence live ☐ Cross-pollination live ☐ USER STARTS POSTING
WEEK 4:  ☐ Full creative engine ☐ Sentiment pipeline live
WEEK 5:  ☐ Production packages ☐ Daily briefs via WhatsApp ☐ Timing engine
WEEK 6:  ☐ Newsjacking ready ☐ Reactive mode working
WEEK 7:  ☐ Feedback loop live ☐ Hook A/B testing ☐ 15+ posts
WEEK 8:  ☐ Post-publish engine ☐ Template library ☐ 25+ posts
WEEK 10: ☐ Predictive model trained (needs 50+ posts) ☐ Private dashboard MVP
WEEK 12: ☐ Private dashboard complete ☐ Full virality engine active
WEEK 16: ☐ Public dashboard launched ☐ System fully operational
```

### ONGOING (Post-Launch)

| Cadence | Task |
|---------|------|
| Daily | Review daily brief, greenlight concepts, respond to alerts |
| Weekly | Review learning outputs, retrain predictive model, review competitor intel |
| Bi-weekly | Add new characters/worlds as needed, review template library |
| Monthly | Full system performance review, update editorial pillars, adjust scan targets |
| Quarterly | Major system prompt optimization, new feature development, public dashboard iteration |

---

### User Inputs Required — Dashboards

In addition to the existing user inputs needed:

#### Public Dashboard
1. **Name/Brand**: What is the public dashboard called? ("Le Pouls de la France"? Something else?)
2. **Domain**: Preferred domain name
3. **Design references**: Any dashboards, data viz projects, or websites whose aesthetic you admire
4. **Hero visualization preference**: Breathing orb, weather map, pulse line, or something else?
5. **Launch strategy**: Soft launch or PR push? Target journalists/commentators for initial traction?

---

*This document is the complete system specification for the Meme Machine and its associated dashboards. Fill in all user input sections, then begin Phase 1 build.*
