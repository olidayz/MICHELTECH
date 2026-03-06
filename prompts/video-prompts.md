# Video Prompt Craft

## Purpose
Generate video clips for: final production, animatics, social content, and tests.

## What Video Prompts Add Over Image Prompts

Three things images don't have: **motion**, **duration**, and **temporal change**.

### Motion Description
Be explicit about:
1. **Subject motion:** What does the character/object do? Direction, speed, gesture.
   - "walks slowly from left to right"
   - "turns head toward camera"
   - "hand reaches out and touches the glass"

2. **Camera motion:** What does the camera do?
   - "camera slowly dollies in"
   - "static, locked tripod"
   - "handheld, slight drift"
   - "crane up, revealing the cityscape"

3. **Environmental motion:** What moves in the world?
   - "wind blows through her hair"
   - "rain falls steadily"
   - "neon signs flicker"
   - "waves crash in background"

### Duration Planning
Most AI video tools generate 4-15 second clips. Plan accordingly:
- **One action per clip.** Don't try to fit a whole scene in one generation.
- **Simpler = better.** "A woman turns to look out the window" > "A woman stands up, walks across the room, picks up a book, sits back down, and opens it"
- **Match duration to action:** Quick gesture = 4s. Slow dolly across a landscape = 10-15s.

### Temporal Change
Things that change over the duration:
- Lighting shift (clouds passing, sun moving)
- Expression change (neutral → smile)
- Focus shift (rack focus from foreground to background)
- Color/mood evolution within the shot

## Video Prompt Structure

```
[Subject + appearance] + [subject action] + [camera type + movement] + [environment + atmosphere] + [lighting] + [style] + [duration] + [technical]
```

**Example:**
"A middle-aged man in a worn leather jacket sits at a rain-streaked window in a diner, slowly turns his head to look directly at camera, static medium close-up shot, warm interior light contrasting with cold blue rain outside, neo-noir, 6 seconds, cinematic, 24fps"

## Text-to-Video (Workflow 2)

Pure text prompt → video. Best for:
- Atmospheric/establishing shots
- Simple single-action clips
- Abstract/stylized content
- When you want the model to interpret freely

**Tips:**
- Front-load subject and action
- Camera direction is crucial — without it, the model decides
- Keep it to one clear action
- Specify duration

## Image-to-Video (Workflow 3)

Reference image → video. Best for:
- Character consistency (the image locks the look)
- Specific starting composition
- Style control (nail it in the image, video inherits it)

**Tips:**
- The image prompt and video prompt should be consistent in description
- Describe what CHANGES from the image (the motion)
- Don't describe what's already in the image — the model can see it
- Focus the video prompt on: action, camera movement, duration

**Example:**
[Start image: woman at window, as described above]
Video prompt: "She slowly turns her head toward camera, expression shifts from contemplative to surprised, camera holds static, 5 seconds"

## Bookend Workflow (Workflow 4)

Start image + end image → video interpolates between them. Best for:
- Maximum control over start and end composition
- Transformation shots
- Precise camera movement simulation

**Tips:**
- Both images must be stylistically consistent
- The transition between them must be physically plausible
- Simpler transitions = better results (don't expect magic)
- Works great for: slow dolly, slow pan, subtle expression change, lighting shift

## Common Mistakes

1. **Too much action for the duration.** 5 seconds = one action. Not three.
2. **Vague camera direction.** "Cinematic camera" means nothing. "Slow dolly in from medium to close-up" means everything.
3. **Ignoring physics.** AI struggles when asked to do physically impossible motion (for now).
4. **No temporal thinking.** Describe the start state AND the change, not just a static description with "video" appended.
5. **Style inconsistency between shots.** Same project = same style language in every prompt.
