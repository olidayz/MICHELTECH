# Prompt Architecture

## The Universal Prompt Stack

Every generation prompt — image or video — is built from layers. The order and emphasis of layers determines the output.

### The Stack (image)

```
[Subject] + [Action/Pose] + [Environment] + [Lighting] + [Camera/Lens] + [Style] + [Color] + [Mood] + [Technical]
```

**Example:**
"A woman in a red dress standing at the edge of a rooftop, looking out at a neon-lit city at night, rim lighting from behind, close-up shot with shallow depth of field, neo-noir style, teal and magenta color palette, melancholic mood, 35mm film grain, cinematic"

### The Stack (video)

```
[Subject] + [Action/Motion] + [Environment] + [Lighting] + [Camera Movement] + [Style] + [Color] + [Duration] + [Technical]
```

**Example:**
"A woman in a red dress walks slowly toward the edge of a rooftop, camera slowly dollies in from behind, neon city reveals in background, rim lighting, neo-noir, teal and magenta, 8 seconds, cinematic, 24fps"

## Layer Breakdown

### Subject
Who or what is in the frame. Be specific.
- Bad: "a person"
- Good: "a middle-aged man with graying temples, wearing a worn leather jacket"
- For consistency: describe the same details every time the character appears

### Action/Pose (image) or Motion (video)
- Image: What are they doing in this frozen moment?
- Video: What happens over the duration? Start state → end state.
- Be explicit about movement direction and speed

### Environment
Where are we? Layer it:
- Location type (interior/exterior, specific place)
- Background details (what's visible behind the subject)
- Atmosphere (fog, rain, dust, clean air)
- Time of day

### Lighting
How is the scene lit? (Reference `color-and-light.md`)
- Source: where the light comes from
- Quality: hard/soft, direct/diffused
- Color temperature: warm/cool
- Named setups: "Rembrandt lighting," "rim lit," "practical neon"

### Camera/Lens
How are we seeing this? (Reference `cinematography.md`)
- Shot type: close-up, wide, medium
- Angle: eye level, low, high
- Lens: wide-angle, telephoto, macro, anamorphic
- For video: camera movement (static, dolly, pan, handheld)

### Style
Visual style direction (reference style/ files)
- Can be a single style or a mix
- Reference directors, movements, formats
- "In the style of Wong Kar-wai" or "neo-noir meets anime"

### Color
Color palette and treatment (reference `color-and-light.md`)
- Dominant colors
- Saturation level
- Color grading reference
- Treatment: desaturated, cross-processed, etc.

### Mood
The feeling. Sometimes redundant with style/color, but can be a useful nudge.
- "Melancholic," "tense," "euphoric," "eerie calm"

### Technical
Model-specific parameters:
- Aspect ratio
- Quality settings
- Negative prompts (what to avoid)
- Style/seed references
- Duration (video)
- Frame rate (video)

## Prompt Principles

1. **Front-load the important stuff.** Most models weight the beginning of prompts more heavily.
2. **Be specific, not verbose.** "Warm golden hour light" > "the light is warm and it looks like golden hour when the sun is setting"
3. **Describe what you want, not what you don't want.** Use negative prompts separately for exclusions.
4. **Consistency = repetition.** Same character across shots? Same description every time. Copy-paste the character block.
5. **Style words are powerful shortcuts.** "Cinematic" "editorial" "documentary" each invoke a whole visual language.
6. **Test and iterate.** First generation is a starting point. Refine from there.

## Workflow Selection Per Shot

For each shot in your storyboard, determine:

| Question | If yes → |
|----------|----------|
| Need exact composition? | Image first (Workflow 3 or 4) |
| Character must match other shots? | Image first with consistent description |
| Simple atmospheric/establishing? | Text-to-video (Workflow 2) |
| Need specific start AND end? | Bookend images (Workflow 4) |
| Stills only (moodboard/deck)? | Image only (Workflow 1) |

## Batch Export Format

When generating a full prompt set, export as:

```
=== SHOT 01 | CU | Static | 4s ===
[Workflow: Text → Video]
[Model: Sora]
[Prompt]: ...

=== SHOT 02 | WS | Dolly in | 6s ===
[Workflow: Image → Video]
[Model: Midjourney → Kling]
[Start Image Prompt]: ...
[Video Prompt]: ...

=== SHOT 03 | MS | Handheld | 5s ===
[Workflow: Bookend]
[Model: Flux → Runway]
[Start Image Prompt]: ...
[End Image Prompt]: ...
[Video Prompt]: ...
```

Ordered: all images first (batch generate), then videos referencing those images.
