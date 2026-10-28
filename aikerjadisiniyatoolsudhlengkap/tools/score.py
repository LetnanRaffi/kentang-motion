import math, os, sys, wave, struct

K = sys.argv[1] if len(sys.argv) > 1 else 'konten-1'
DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 39.2
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'audio', 'sfx', K)
os.makedirs(OUT, exist_ok=True)

SR = 44100
BPM = 76.0
BEAT = 60.0 / BPM
BAR = BEAT * 4
n = int(SR * DUR)
buf = [0.0] * n

CHORDS = [
    [130.81, 196.00, 261.63, 329.63],
    [98.00, 146.83, 196.00, 246.94],
    [110.00, 164.81, 220.00, 261.63],
    [87.31, 130.81, 174.61, 220.00],
]

def add(t0, sig):
    i0 = int(t0 * SR)
    for i, v in enumerate(sig):
        k = i0 + i
        if 0 <= k < n:
            buf[k] += v

def pad(t0, freqs, dur):
    m = int(SR * dur)
    out = []
    for i in range(m):
        t = i / SR
        att = min(1.0, t / 0.55)
        rel = min(1.0, max(0.0, (dur - t) / 0.9))
        env = att * rel
        s = 0.0
        for f in freqs:
            s += math.sin(2 * math.pi * f * t) + 0.5 * math.sin(2 * math.pi * f * 2.002 * t)
        out.append(s * env * 0.030)
    return out

def pluck(t0, f, dur=0.30, g=0.055):
    m = int(SR * dur)
    out = []
    for i in range(m):
        t = i / SR
        env = math.exp(-7.5 * t) * (1 - math.exp(-900 * t))
        v = math.sin(2 * math.pi * f * t) + 0.28 * math.sin(4 * math.pi * f * t)
        out.append(v * env * g)
    return out

def soft(freqs, idx, step):
    base = freqs[1] * 2
    seq = [base, base * 1.5, base * 2, base * 1.5]
    add(idx * step, pluck(idx * step, seq[idx % len(seq)]))

t = 0.0
bar = 0
while t < DUR:
    ch = CHORDS[bar % 4]
    add(t, pad(t, ch, BAR + 0.4)[: int(SR * BAR)])
    root = ch[1] * 2
    eighth = BAR / 8
    for k in range(0, 8, 2):
        f = [root, root * 1.5, root * 2.0, root * 1.25][(k // 2 + bar) % 4]
        add(t + k * eighth, pluck(t, f, 0.34, 0.050))
    t += BAR
    bar += 1

peak = max(abs(v) for v in buf) or 1.0
buf = [v / peak * 0.55 for v in buf]

w = wave.open(os.path.join(OUT, 'score.wav'), 'wb')
w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes(b''.join(struct.pack('<h', int(max(-1, min(1, v)) * 32767)) for v in buf))
w.close()
print('score ok', round(DUR, 2), 's ->', os.path.join(OUT, 'score.wav'))
