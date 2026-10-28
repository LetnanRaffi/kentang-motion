# KentangMotion Engine 🥔

Ultra-lightweight storytelling 9:16 motion graphics engine for low-spec machines (tested on AMD A4 2-Core / 4GB RAM).

Combines:
- **GSAP + SVG Stage (`simpenhtml/`)**: Pure vectorized 2D scene animation with manual joint transformations.
- **Chrome Headless Shell (`tools/render.js`)**: Sequential deterministic frame-by-frame renderer (memory-safe, ~250MB RAM flat).
- **FFmpeg (`tools/encode.sh`, `tools/mix-audio.sh`)**: SFX synthesis, procedural backsound ducking, and MP4 assembly.

## Quick Start on Any Machine

```bash
git clone https://github.com/LetnanRaffi/kentang-motion.git
cd kentang-motion

# 1. Setup environment (Node + Remotion renderer + check FFmpeg/Python)
./engine setup

# 2. Render and export video
./engine export konten-2-2026-10-28 39.2
```

Output will be in `aikerjadisiniyatoolsudhlengkap/hasil/<konten>/<konten>.mp4`.

## CLI Usage

```bash
./engine new    <konten-id>             # Scaffold content folders
./engine audio  <konten-id> [dur]       # Synthesize SFX + backsound + mix VO
./engine render <konten-id> [dur]       # Frame-by-frame capture
./engine encode <konten-id>             # Stitch frames to MP4
./engine export <konten-id> [dur]       # Render + encode in one command
./engine status                         # Inspect local server & active jobs
```

## System Requirements
- Node.js >= 18
- Python >= 3.8
- FFmpeg >= 4.4
