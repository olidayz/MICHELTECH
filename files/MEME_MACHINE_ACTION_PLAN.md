# MEME MACHINE — BUILD ACTION PLAN

## Architecture Overview

```
4 PARALLEL TRACKS
━━━━━━━━━━━━━━━━

TRACK A ─ DATA INFRASTRUCTURE      Supabase, scrapers, data pipelines
TRACK B ─ INTELLIGENCE & CREATIVE  Engines, concept generation, production
TRACK C ─ LEARNING & OPTIMIZATION  Feedback loops, virality engine, predictive model
TRACK D ─ DASHBOARDS               CMS, private command center, public dashboard

YOUR TRACK ─ CONTENT & CONFIG      Populate CMS, start posting, feed the system
```

---

## VISUAL TIMELINE

```
         WEEK 1    WEEK 2    WEEK 3    WEEK 4    WEEK 5    WEEK 6    WEEK 7    WEEK 8    WEEK 9-10    WEEK 11-12    WEEK 13-16
         ──────    ──────    ──────    ──────    ──────    ──────    ──────    ──────    ─────────    ──────────    ──────────

TRACK A  ████████  ████████  ████████  ████████
         Schema    Trend     Apify     Sentiment
         Setup     Scanning  Scrapers  Pipeline

TRACK B                      ████████  ████████  ████████  ████████
                             Creative  Audience  Prod Pkg  Newsjack
                             Engine    + Scoring Messaging Reactive

TRACK C                                                    ████████  ████████  ████████████████████
                                                           Feedback  Post-Pub  Predictive Model
                                                           Loop      Engine    Audience Graph
                                                           Hook A/B  Templates Cascade Manager
                                                                               Semantic Matching

TRACK D  ████████                                                              ████████████████████  ████████████████████████
         CMS                                                                   Private Dashboard     Public Dashboard
         (Module                                                               Command Center        Le Pouls de la France
         20)

YOU      ████████  ████████  ████████  ████████  ████████  ████████  ████████  ████████  ████████████████████████████████████
         Populate  Populate  START     Continue  Use daily Use prod  A/B test  Review    Use dashboard  System semi-auto
         CMS       CMS       POSTING   posting   briefs    packages  hooks     learning  Full workflow   You: greenlight + produce
```

---

## WEEK 1 — Foundation

### TRACK A: Supabase Schema
| Task | Output |
|------|--------|
| Create ALL Supabase tables (core + dashboard + virality engine) | ~30 tables live |
| Configure Row Level Security | Secure access |
| Set up Supabase Realtime on key tables | Real-time data flow |

### TRACK D: CMS (Module 20)
| Task | Output |
|------|--------|
| Build React admin panel | Deployed app |
| Characters CRUD (quick add + full edit + bulk CSV import) | Character management |
| Worlds CRUD | World management |
| Editorial Pillars CRUD | Pillar management |
| Accounts to Monitor CRUD | Account management |
| System Settings page | Configuration |
| Pre-populate 10 starter characters + 8 worlds + 7 pillar templates | Not starting from zero |

### YOUR TRACK
| Task | Why |
|------|-----|
| **Start populating CMS immediately** | Everything else depends on this |
| Add/refine Tier 1 characters (5-10 politicians) | Creative engine needs characters |
| Review and customize starter worlds | Add your own, adjust aesthetics |
| Define your editorial pillars | Core positions, off-limits topics |
| Add accounts to monitor (format intel + cultural + competitor) | Scrapers need targets |

**WEEK 1 MILESTONE**: ☐ Supabase live ☐ CMS deployed ☐ You are editing characters/worlds

---

## WEEK 2 — Trend Scanning

### TRACK A: Data Ingestion
| Task | Output | Dependency |
|------|--------|------------|
| News RSS scanner (Le Monde, Le Figaro, Libération, BFM, CNews, etc.) | `trending_topics` populated | None |
| X/Twitter FR trend scanner | French Twitter trends captured | None |
| Google Trends FR integration | Search interest data | None |
| Reddit r/france + r/rance scanner | Reddit signals captured | None |
| Topic ranking skill (Module 4) — scoring + editorial filtering | Ranked topics with heat scores | Needs editorial pillars from CMS |
| Basic creative engine prompt (Module 6 — initial version) | First concept generation working | Needs ≥1 character + ≥1 world + ≥1 pillar |

### YOUR TRACK
| Task | Why |
|------|-----|
| Continue enriching CMS (especially characters — add depth to Tier 1) | Richer character profiles = better concepts |
| Review first auto-generated topic rankings | Calibrate the editorial filter |
| Review first generated concepts | Give feedback — too edgy? Too tame? Off-brand? |

**WEEK 2 MILESTONE**: ☐ Trend scanning live ☐ First automated topic rankings ☐ First concepts generated

---

## WEEK 3 — Intelligence Layer

### TRACK A: Platform Scraping
| Task | Output | Dependency |
|------|--------|------------|
| Apify scraper for TikTok FR trending | TikTok format data | Account handles from CMS |
| Apify scraper for Instagram Reels FR | Reels format data | Account handles from CMS |
| Format Intelligence skill (Module 2) — trending formats, hooks, edit styles | `format_intelligence` populated, format trend reports | |
| Cross-Pollination scanner (Module 3) — gaming, anime, football, rap | `cultural_trends` populated | Cultural account handles from CMS |
| Cross-Pollination concept generator — political adaptations | `cross_pollination_concepts` populated | |
| Format Velocity Tracker (Module 21E) — lifecycle tracking + multipliers | Format freshness multipliers active | Depends on format data |

### TRACK B: Creative Engine Enhancement
| Task | Output |
|------|--------|
| Expand creative engine to full Module 6 (all 6 layers) | Complete Meme Intelligence Engine |
| Integrate format intelligence into concept generation | Concepts reference trending formats |
| Integrate cross-pollination into concept generation | Concepts include cultural format hijacks |
| Combination justification logic active | Weak character/world combos get killed |
| Manual injection mode (Module 7) | User can inject topics via messaging |

### YOUR TRACK
| Task | Why |
|------|-----|
| **🚨 START POSTING CONTENT** | The system needs YOUR performance data to learn |
| Use system-generated concepts as inspiration | Manual production, system-suggested ideas |
| Greenlight/pass concepts to start training the system | Every decision teaches the engine |
| Target: 2-3 posts this week | Data accumulation begins |

**WEEK 3 MILESTONE**: ☐ Format intelligence live ☐ Cross-pollination live ☐ **YOU START POSTING**

---

## WEEK 4 — Sentiment & Creative Refinement

### TRACK A: Sentiment Infrastructure
| Task | Output |
|------|--------|
| Sentiment analysis pipeline (Claude API) | Topics processed into emotion breakdowns |
| Writes to `topic_sentiment` and `national_mood` | Dashboard-ready data |
| Real-time Supabase subscriptions fully configured | All data flows in real time |

### TRACK B: Creative Refinement
| Task | Output |
|------|--------|
| Audience mapping skill (Module 5) | Per-topic audience profiles |
| Full virality scoring (all Module 6 sub-scores) | Concepts scored comprehensively |
| Complete concept output format (matches full spec template) | Concept briefs with all sections |
| Combination justification quality check | Review and refine combination logic |

### YOUR TRACK
| Task | Why |
|------|-----|
| Continue posting (target: 2-3 posts/week minimum) | Data accumulation |
| Manually log performance data for each post | Until Module 9 automates this |
| Feed back: which concepts worked, which didn't | Calibrate the engine |

**WEEK 4 MILESTONE**: ☐ Sentiment pipeline live ☐ Full creative engine ☐ ~8-10 posts published

---

## WEEK 5 — Production Pipeline

### TRACK B: Production
| Task | Output | Dependency |
|------|--------|------------|
| Production package generator (Module 8) | Image prompts, text overlays, audio direction, edit blueprints | Creative engine must be working |
| Controversy radar (Module 14) — legal + platform risk | Every concept tagged with risk level | |
| Timing Optimization Engine (Module 21C) — time-of-day + topic lifecycle | Post timing recommendations | Needs topic lifecycle data |

### TRACK B: Messaging Interface
| Task | Output |
|------|--------|
| WhatsApp/Telegram bot setup | Connected to OpenClaw |
| Daily brief at 8:00 AM CET | 5 ranked concepts + top pick |
| Greenlight via messaging | Reply "1" → production package generated |
| Manual injection via messaging | Text a topic → concepts in minutes |

### YOUR TRACK
| Task | Why |
|------|-----|
| Start using daily brief workflow | Greenlight concepts via WhatsApp |
| Use production packages to speed up creation | Should cut production time significantly |
| Target: 3-4 posts/week | System is helping now |

**WEEK 5 MILESTONE**: ☐ Production packages working ☐ Daily briefs via WhatsApp ☐ Timing engine live

---

## WEEK 6 — Newsjacking & Speed

### TRACK B: Speed Layer
| Task | Output |
|------|--------|
| Newsjacking templates (Module 18) — 8 event type skeletons | Pre-built skeletons for press conferences, protests, EU votes, scandals, etc. |
| Reactive mode — urgent concept generation | Concepts in <5 minutes from topic injection |
| Event calendar population (Module 12) | Next 3 months of predictable events |
| Pre-production queue — concept skeletons for upcoming events | Ready to fill when events happen |

### YOUR TRACK
| Task | Why |
|------|-----|
| Test reactive mode — inject a breaking news topic | See how fast concepts arrive |
| Review newsjacking templates — adjust to your style | Templates should feel like YOUR voice |
| Continue posting (system producing most of what you need) | Target: 15+ total posts by end of week 6 |

**WEEK 6 MILESTONE**: ☐ Newsjacking ready ☐ Reactive mode working ☐ 15+ posts published

---

## WEEK 7 — Learning Loop Activates

### TRACK C: Feedback & Learning
| Task | Output | Dependency |
|------|--------|------------|
| Performance feedback loop (Module 9) — automated data collection | `post_performance` auto-populated | Needs API access to TikTok/IG analytics or manual input |
| Learning weights — character, world, format effectiveness | System knows what works for YOUR audience | Needs 15+ posts |
| Virality post-mortem auto-generation | Automatic analysis for high performers | |
| Content decay tracking — format lifecycle for YOUR content | Flags when your formats are getting stale | |

### TRACK C: Hook Testing
| Task | Output |
|------|--------|
| Hook A/B testing framework (Module 21B) | 3-5 hook variants per concept |
| Hook test logging and analysis | Tracks which hooks win, builds effectiveness matrix |

### YOUR TRACK
| Task | Why |
|------|-----|
| Start A/B testing hooks — post variants, report results | Hook is highest-leverage optimization |
| Review learning outputs — does system's understanding match your intuition? | Calibrate |
| By now: 15-25 posts of data feeding the system | Enough for initial learning |

**WEEK 7 MILESTONE**: ☐ Feedback loop live ☐ Hook A/B testing active ☐ System learning from YOUR data

---

## WEEK 8 — Post-Publish Intelligence

### TRACK C: Optimization
| Task | Output |
|------|--------|
| Post-publish optimization engine (Module 21D) | Real-time monitoring + underperformance/viral alerts |
| Comment intelligence | Recommends which comments to reply to, pin, ignore |
| Meme template library (Module 17) | Extracts winning templates from your best performers |
| Narrative arc tracker (Module 13) | Running storylines, callback suggestions |
| A/B testing framework (Module 16) | Auto-generates variations for testing |

### YOUR TRACK
| Task | Why |
|------|-----|
| Respond to real-time post-publish alerts | "Kill and repost" or "going viral — cross-post NOW" |
| Review meme templates — approve/reject patterns | Build your template library |
| By now: 25-40 posts, system is noticeably smarter | Quality of concepts should be visibly improving |

**WEEK 8 MILESTONE**: ☐ Post-publish engine live ☐ Template library started ☐ 25+ posts

---

## WEEK 9-10 — Virality Intelligence + Private Dashboard

### TRACK C: Virality Engine (Full Activation)
| Task | Output | Dependency |
|------|--------|------------|
| **Predictive virality model training (Module 21A)** | Dual scoring: creative engine + predictive model | **HARD: needs 50+ posts** |
| Divergence alerts — when creative score ≠ predictive score | Pressure-tests creative judgment with data | |
| Semantic trend matching (Module 21G) — embedding pipeline | Non-obvious connection alerts | |
| Audience graph intelligence (Module 21F) — share path mapping | Super-spreader identification, cluster analysis | Needs several viral posts to map |
| Virality cascade manager (Module 21H) — detection + playbook | Automated cascade management | |
| Competitor intelligence (Module 15) — automated scanning | Competitor tracking, gap detection | Competitor handles from CMS |

### TRACK D: Private Dashboard (Start)
| Task | Output |
|------|--------|
| React app scaffold (extends CMS app) | App structure, routing, auth |
| Supabase Realtime integration | Live data subscriptions |
| Trending Topics panel | Real-time ranked topic list with heat scores |
| Emotion Radar panel | What France is feeling right now |
| Engagement Velocity panel | Fastest-accelerating topics |
| Content Gap Detector panel | High engagement + low coverage = opportunity |

### YOUR TRACK
| Task | Why |
|------|-----|
| **If <50 posts, ACCELERATE POSTING** | Predictive model needs data |
| Review predictive model vs creative engine — does divergence make sense? | Calibrate |
| Start using private dashboard | Move from messaging to dashboard workflow |

**WEEK 10 MILESTONE**: ☐ Predictive model trained ☐ Private dashboard MVP ☐ 50+ posts

---

## WEEK 11-12 — Private Dashboard Complete

### TRACK D: Private Dashboard (Complete)
| Task | Output |
|------|--------|
| Cross-Pollination Alerts panel | Live cultural trend alerts + adaptation concepts |
| Performance Tracker panel | Your content metrics, running averages |
| Concept Queue with greenlight/pass buttons | Full workflow in dashboard |
| Manual Injection interface | Drop topics into UI, concepts appear in minutes |
| Module 21 integration — timing, hook variants, post-publish alerts, predictive scores | Full optimization layer visible in dashboard |
| Competitor Activity panel | What competitors posted in last 24h |
| Mobile responsive | Dashboard works on phone |

### YOUR TRACK
| Task | Why |
|------|-----|
| Full workflow now in dashboard — use it daily | Everything in one place |
| By now: 50-80 posts, predictive model calibrated | System is noticeably smarter than week 3 |
| System running semi-autonomously | You're mostly greenlighting + producing |

**WEEK 12 MILESTONE**: ☐ Private dashboard complete ☐ Full virality engine active ☐ System semi-autonomous

---

## WEEK 13-16 — Public Dashboard (Le Pouls de la France)

### TRACK D: Public Dashboard
| Week | Task | Output |
|------|------|--------|
| 13 | Design system — dark mode, emotion colors, typography, components | Complete design system |
| 13 | Hero visualization — The Mood (Three.js) | Mesmerizing hero section |
| 14 | Topic heatmap — bubble chart with physics (D3.js) | Interactive topic visualization |
| 14 | Topic detail pages — sentiment, the debate, key quotes | Individual topic pages (SEO) |
| 14 | Emotions page — radar chart, drivers, timeline | Emotion deep dive |
| 15 | The Divide — polarization tracker | Most shareable page |
| 15 | Rising Topics — early warning | "What France talks about next" |
| 15 | Historical Timeline — scrollable, event-linked | Full emotional history |
| 16 | Shareability engine — dynamic OG images, embeds, share buttons | Every view shareable |
| 16 | SEO optimization — meta, sitemaps, topic indexing | Long-tail SEO |
| 16 | **LAUNCH** | Public dashboard live |

**WEEK 16 MILESTONE**: ☐ Public dashboard launched ☐ System fully operational

---

## DEPENDENCY MAP

```
CRITICAL PATH (must happen in order):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Supabase ──→ CMS ──→ You populate data ──→ Trend scanning works
                                        ──→ Creative engine has characters/worlds
                                        ──→ Format intel has accounts to monitor

Trend scanning ──→ Topic ranking ──→ Creative engine ──→ Concepts
                                                     ──→ Production packages
                                                     ──→ Daily briefs

You start posting ──→ Performance data ──→ Feedback loop activates
                                       ──→ Predictive model trains (50+ posts)
                                       ──→ Audience graph maps share paths


PARALLEL TRACKS:
━━━━━━━━━━━━━━━

Track A (Data)  ←→  Track B (Intelligence)  — share Supabase, otherwise independent
Track C (Learn) ←→  Track D (Dashboards)    — share data, otherwise independent
Track B → Track C                           — Learning needs intelligence output
Track A → Track D                           — Dashboards need data infrastructure


HARD DEPENDENCIES (cannot skip):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. CMS must exist before you can populate data
2. ≥1 character + ≥1 world + ≥1 pillar before creative engine works
3. You must start posting before learning engine has data
4. 50+ posts required before predictive model can train
5. Sentiment pipeline must work before dashboards show emotion data
6. Trend scanning must work before format intelligence layers on
7. Creative engine must work before production packages make sense
```

---

## YOUR PERSONAL POSTING TARGETS

| Week | Posts Published | Cumulative | System State |
|------|----------------|------------|--------------|
| 1-2 | 0 | 0 | Populating CMS, no content yet |
| 3 | 2-3 | 2-3 | First posts — manual production, system-suggested concepts |
| 4 | 2-3 | 5-6 | Still manual, concepts getting better |
| 5 | 3-4 | 8-10 | Production packages speeding you up |
| 6 | 3-4 | 12-14 | Newsjacking + reactive mode available |
| 7 | 3-4 | 15-18 | Learning loop activating, hooks A/B tested |
| 8 | 4-5 | 20-23 | Post-publish engine managing your content |
| 9 | 5-6 | 25-29 | Push to hit 50 for predictive model |
| 10 | 7-8 | 33-37 | Accelerating — system is helping significantly |
| 11 | 7-8 | 40-45 | Almost at predictive model threshold |
| 12 | 7-8 | 48-53 | **🎯 50+ posts — predictive model trains** |
| 13-16 | 5-6/wk | 70-80+ | System semi-autonomous, you produce + greenlight |

---

## ONGOING CADENCE (Post-Launch)

| Cadence | Task |
|---------|------|
| **Daily** | Review daily brief (8 AM), greenlight concepts, respond to post-publish alerts |
| **Weekly** | Review learning outputs, retrain predictive model, review competitor intel |
| **Bi-weekly** | Add new characters/worlds as needed, review meme template library |
| **Monthly** | Full system performance review, update editorial pillars, adjust scan targets |
| **Quarterly** | Major system prompt optimization, new features, public dashboard iteration |

---

## QUICK REFERENCE — WHAT GETS BUILT WHEN

| Module | Name | Track | Week |
|--------|------|-------|------|
| 20 | CMS / Admin Panel | D | 1 |
| — | Supabase Schema | A | 1 |
| 1 | Trend Ingestion | A | 2 |
| 4 | Topic Ranking | A | 2 |
| 6 | Meme Intelligence Engine (basic) | B | 2 |
| 2 | Format Intelligence | A | 3 |
| 3 | Cross-Pollination | A | 3 |
| 6 | Meme Intelligence Engine (full) | B | 3-4 |
| 7 | Manual Injection | B | 3 |
| 21E | Format Velocity Tracker | A | 3 |
| 5 | Audience Mapping | B | 4 |
| — | Sentiment Pipeline | A | 4 |
| 8 | Production Packages | B | 5 |
| 14 | Controversy Radar | B | 5 |
| 21C | Timing Optimization | B | 5 |
| — | Messaging Interface | B | 5 |
| 18 | Newsjacking Templates | B | 6 |
| 12 | Trend Prediction | B | 6 |
| 9 | Performance Feedback Loop | C | 7 |
| 21B | Hook A/B Testing | C | 7 |
| 21D | Post-Publish Engine | C | 8 |
| 17 | Meme Template Library | C | 8 |
| 13 | Narrative Arc Tracker | C | 8 |
| 16 | A/B Testing Framework | C | 8 |
| 21A | Predictive Virality Model | C | 9-10 |
| 21G | Semantic Trend Matching | C | 9-10 |
| 21F | Audience Graph Intelligence | C | 9-10 |
| 21H | Virality Cascade Manager | C | 9-10 |
| 15 | Competitor Intelligence | C | 9-10 |
| 19A | Private Dashboard | D | 9-12 |
| 19B | Public Dashboard | D | 13-16 |

---

*This action plan corresponds to the MEME_MACHINE_SYSTEM_SPEC.md. The spec is the source of truth for what each module does. This document is the source of truth for when and how it gets built.*
