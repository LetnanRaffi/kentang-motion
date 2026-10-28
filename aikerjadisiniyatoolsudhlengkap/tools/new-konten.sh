#!/usr/bin/env bash
# bikin struktur folder konten baru
# pakai: tools/new-konten.sh konten-2-2026-10-29
set -euo pipefail
N=${1:?nama folder, cth: konten-2-2026-10-29}
R=$(cd "$(dirname "$0")/.." && pwd)
for d in simpenhtml frames hasil caption voiceovernaskahai audio/voiceover audio/sfx; do
  mkdir -p "$R/$d/$N"
done
echo "ok: $N"
for d in simpenhtml frames hasil caption voiceovernaskahai audio/voiceover audio/sfx; do
  echo "  $d/$N"
done
