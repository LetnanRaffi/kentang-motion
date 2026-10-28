#!/usr/bin/env bash
# VO (vo-timed.wav kalau ada) + sfx + score -> mix.wav (musik di-duck di bawah VO)
# pakai: tools/mix-audio.sh konten-1
set -euo pipefail
N=${1:?nama konten}
R=$(cd "$(dirname "$0")/.." && pwd)
A="$R/audio/sfx/$N"
VO="$A/vo-timed.wav"
[ -f "$VO" ] || VO=$(ls "$R/audio/voiceover/$N"/*.mp3 2>/dev/null | head -1)
[ -n "$VO" ] && [ -f "$VO" ] || { echo "VO tidak ada di audio/voiceover/$N/"; exit 1; }
[ -f "$A/sfx.wav" ] || { echo "sfx tidak ada (jalankan: python3 tools/sfx.py $N)"; exit 1; }
if [ -f "$A/score.wav" ]; then
  ffmpeg -y -v error -i "$VO" -i "$A/sfx.wav" -i "$A/score.wav" \
    -filter_complex "[0:a]highpass=f=85,acompressor=threshold=-16dB:ratio=2.5:attack=8:release=180,asplit=2[v1][v2];\
[2:a]volume=0.30[m];\
[m][v2]sidechaincompress=threshold=0.025:ratio=6:attack=15:release=420[md];\
[v1][1:a][md]amix=inputs=3:duration=longest:normalize=0,alimiter=limit=0.9,loudnorm=I=-15:TP=-1.5:LRA=11[out]" \
    -map "[out]" -c:a pcm_s16le -ar 44100 "$A/mix.wav"
else
  ffmpeg -y -v error -i "$VO" -i "$A/sfx.wav" \
    -filter_complex "[0:a]highpass=f=85,acompressor=threshold=-16dB:ratio=2.5:attack=8:release=180[v];\
[v][1:a]amix=inputs=2:duration=longest:normalize=0,alimiter=limit=0.9,loudnorm=I=-15:TP=-1.5:LRA=11[out]" \
    -map "[out]" -c:a pcm_s16le -ar 44100 "$A/mix.wav"
fi
ffprobe -v error -show_entries format=duration -of default=nw=1 "$A/mix.wav"
echo "ok: audio/sfx/$N/mix.wav"
