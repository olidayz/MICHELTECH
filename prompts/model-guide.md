# Model Guide

> **NOTE:** This file references a living document for current model capabilities, pricing, and syntax. See: `/skills/shared/ai-tools-current.md`

Model capabilities change fast. This file provides the framework; the living document has current details.

---

## Image Generation Models

### Midjourney
- **Best for:** Aesthetic quality, style control, character references
- **Key features:** `--cref` for character consistency, `--style` parameters, `--ar` for aspect ratios, Vary (region)
- **Workflow:** Discord bot, `/imagine` prompts
- **Strengths:** Highest aesthetic quality out of box, excellent style control
- **Weaknesses:** Less photorealistic than Flux, learning curve for prompt engineering

### Flux (Black Forest Labs)
- **Best for:** Photorealism, text rendering, prompt adherence
- **Key features:** Text-in-image, multiple model versions (Schnell/Pro/Dev)
- **Workflow:** API, local, or through various UIs
- **Strengths:** Best text rendering, excellent photorealism, open-source options
- **Weaknesses:** Less stylized range than Midjourney

### DALL-E 3/4 (OpenAI)
- **Best for:** Quick concepts, integrated with ChatGPT
- **Key features:** Natural language understanding, inpainting
- **Workflow:** ChatGPT interface or API
- **Strengths:** Easiest prompt writing (natural language), good for iteration
- **Weaknesses:** Less aesthetic control than Midjourney, fewer style options

### Stable Diffusion (Stability AI)
- **Best for:** Customization, fine-tuning, local privacy
- **Key features:** LoRA fine-tuning, ControlNet, inpainting, img2img
- **Workflow:** Local (ComfyUI/A1111), online UIs, or API
- **Strengths:** Maximum control, runs locally, highly customizable
- **Weaknesses:** Requires technical setup, base models less polished

### Nano Banana / Nano Banana Pro
- **Best for:** In-chat quick previews, exploration, editing
- **Key features:** Image editing, text rendering, Gemini integration
- **Workflow:** Gemini chat interface, API
- **Strengths:** Fast in-conversation exploration, editing capabilities
- **Best use in pipeline:** Style exploration, quick previews, iteration before final generation in other tools

---

## Video Generation Models

### Sora (OpenAI)
- **Best for:** Cinematic quality, complex scenes, camera movement
- **Key features:** Long duration (up to 60s), strong physics understanding
- **Workflow:** API or chat interface
- **Strengths:** Highest cinematic quality, best physics/physics understanding
- **Weaknesses:** Character consistency across shots, hands, text

### Kling
- **Best for:** Character animation, motion quality, coherent longer clips
- **Key features:** Up to 2 minutes, good character animation
- **Workflow:** API or web interface
- **Strengths:** Strong character animation, longer duration
- **Weaknesses:** Less cinematic than Sora, occasional uncanny faces

### Runway (Gen-3/4)
- **Best for:** Stylized content, image-to-video, motion brush
- **Key features:** Image-to-video, style controls, motion brush
- **Workflow:** Web interface, API
- **Strengths:** Style control, fast iteration, good for stylized/creative content
- **Weaknesses:** Shorter clips than Kling, less cinematic than Sora

### Pika
- **Best for:** Quick generation, style experiments, social content
- **Key features:** Fast, lip sync, style transfer
- **Workflow:** Web interface
- **Strengths:** Speed, experimentation, easy to use
- **Weaknesses:** Less cinematic, shorter duration, less coherent

### Veo (Google)
- **Best for:** Long-form coherence, realistic scenes
- **Key features:** Up to 2 minutes, good scene understanding
- **Workflow:** API
- **Strengths:** Long-form coherence, realistic rendering
- **Weaknesses:** Less publicly available, evolving capabilities

### Hailuo (MiniMax)
- **Best for:** Fast generation, character consistency
- **Key features:** Quick iteration, improving character consistency
- **Workflow:** API
- **Strengths:** Speed, getting better at consistency
- **Weaknesses:** Still emerging capabilities

---

## Prompt Syntax by Model

For current syntax details, see: `/skills/shared/ai-tools-current.md`

### General Prompt Stack (Universal)

**Subject + Action + Environment + Lighting + Camera + Style + Mood + Technical**

### Model-Specific Notes

| Model | Syntax Notes |
|-------|-------------|
| Midjourney | `--ar` for aspect ratio, `--style` for variation, `--cref` for character ref |
| Flux | Standard natural language, less syntax needed |
| SD | Negative prompts important, wildcards work, LoRA triggers |
| Sora | Describe motion explicitly, camera direction matters |
| Kling | Describe movement clearly, less sensitive to negative prompts |
| Runway | `--style` parameters, `--motion` value |

---

## Model Selection Guide

| Need | Best Model(s) | Why |
|------|--------------|-----|
| Highest aesthetic quality | Midjourney | Best out-of-box look |
| Text in image | Flux | Best text rendering |
| Character consistency | Midjourney + `--cref` or Sora | Control features |
| Complex camera movement | Sora | Best camera control |
| Long clips (30s+) | Kling, Sora | Duration support |
| Quick iteration | Pika, Runway | Speed |
| Stylized/content | Runway | Style control |
| Photorealistic | Flux | Best realism |
| Local/private | Stable Diffusion | Runs anywhere |
| Fast preview in chat | Nano Banana Pro | Integrated with chat |
| Cinematic quality | Sora | Best overall |
| Animation style | Runway, Midjourney | Style range |

---

## See Also

- `/skills/shared/ai-tools-current.md` — Current model capabilities, pricing, API details
- `image-prompts.md` — Image generation craft
- `video-prompts.md` — Video generation craft
