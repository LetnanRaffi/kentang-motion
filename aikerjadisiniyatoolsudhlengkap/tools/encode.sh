#!/usr/bin/env bash
# frames + mix.wav -> hasil/<konten>/<konten>.mp4
# pakai: tools/encode.sh konten-1
set -euo pipefail
N=${1:?nama konten}
R=$(cd "$(dirname "$0")/.." && pwd)
F="$R/frames/$N"
A="$R/audio/sfx/$N/mix.wav"
[ -f "$F/f00000.jpg" ] || { echo "frame kosong: $F"; exit 1; }
[ -f "$A" ] || { echo "audio kosong: $A"; exit 1; }
mkdir -p "$R/hasil/$N"
ffmpeg -y -v error -framerate 30 -i "$F/f%05d.jpg" -i "$A" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 44100 -movflags +faststart -shortest \
  "$R/hasil/$N/$N.mp4"
ffprobe -v error -show_entries format=duration,size -of default=nw=1 "$R/hasil/$N/$N.mp4"
