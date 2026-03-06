# Image Prompt Craft

## Purpose
Generate still images for: concept art, mood boards, storyboard frames, start/end frames for video, pitch decks, and standalone visual content.

## Image Prompt Structure

Follow the universal stack from `prompt-architecture.md`, but with image-specific emphasis:

### Composition is King
In a still image, composition does ALL the storytelling work. No motion, no sound — just the frame.

- **Specify placement:** "subject positioned in the left third of frame"
- **Specify depth:** "foreground rain drops, midground subject, background city lights blurred"
- **Specify negative space:** "large empty sky above the figure" (powerful for mood)
- **Specify what's IN and OUT of focus:** Guides the eye

### Detail Level
More detail in prompt = more control, but diminishing returns past a point.

**Minimum viable prompt (for exploration):**
Subject + environment + style + mood
"A lone astronaut on a beach at sunset, Makoto Shinkai style, melancholic"

**Production prompt (for final output):**
Full stack with specifics
"A lone astronaut in a weathered white spacesuit, sitting on wet sand at the water's edge, facing away from camera, golden hour sunset with purple and orange sky, wide shot, 35mm lens, shallow depth of field on the helmet visor reflecting the sunset, Makoto Shinkai style painted background, melancholic, warm fading light, 16:9 aspect ratio"

### Character Consistency Across Shots
The biggest challenge in AI image generation for narrative content:

1. **Describe the character identically every time.** Create a character block and copy-paste it.
```
Character block: "a young woman with short black hair, round glasses, wearing an oversized olive green jacket and white t-shirt, mid-20s, East Asian"
```
2. **Use tool-specific features:** Midjourney --cref, Stable Diffusion LoRA, reference images
3. **Distinctive silhouette helps:** Bold wardrobe choices are easier to maintain
4. **Avoid small distinguishing details:** AI struggles with tattoos, specific jewelry, etc.

### For Start/End Frames (Workflow 3 & 4)
When generating images as input for video generation:

**Start frame:**
- Compose exactly as you want the video to begin
- Include any motion cues in the composition (leaning = about to move)
- Ensure the style matches your video tool's aesthetic range

**End frame (Workflow 4):**
- Compose where you want the video to arrive
- Should be achievable from the start frame (realistic motion path)
- Maintain character and environment consistency with start frame

**Tip:** Generate start and end frames in the same session/batch to maximize style consistency.

## Common Mistakes

1. **Too vague:** "A beautiful scene" — gives the model nothing to work with
2. **Too contradictory:** "dark moody bright cheerful" — pick a direction
3. **Ignoring composition:** Describing what's in the scene but not WHERE in the frame
4. **Style soup:** Mixing too many style references. One dominant, one accent maximum.
5. **Forgetting aspect ratio:** Default varies by model. Specify for your platform.
