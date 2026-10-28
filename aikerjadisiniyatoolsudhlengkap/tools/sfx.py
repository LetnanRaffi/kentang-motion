import math, os, random, sys, wave, struct
K=sys.argv[1] if len(sys.argv)>1 else 'konten-1'
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','audio','sfx',K)
os.makedirs(OUT,exist_ok=True)
SR=44100; DUR=float(sys.argv[2]) if len(sys.argv)>2 else 43.0; random.seed(7)
n=int(SR*DUR); buf=[0.0]*n

def put(t0,sig):
    i0=int(t0*SR)
    for i,v in enumerate(sig):
        k=i0+i
        if 0<=k<n: buf[k]+=v

def whoosh(dur=0.55,g=0.30):
    m=int(SR*dur); out=[]; y=0.0; ph=0.0
    for i in range(m):
        p=i/m
        f=300+2600*math.sin(math.pi*min(1,p*1.15))**1.4
        a=2*math.pi*f/SR
        lp=1-math.exp(-a)
        y+=lp*((random.random()*2-1)-y)
        env=(p**0.6)*math.exp(-3.2*max(0,p-0.55))
        out.append(y*env*g*3.0)
    out[-1]=0.0
    return out

def thud(dur=0.42,g=0.55):
    m=int(SR*dur); out=[]; ph=0.0
    for i in range(m):
        p=i/m; t=i/SR
        f=140*math.exp(-9*t)+45
        ph+=2*math.pi*f/SR
        env=math.exp(-8.5*t)
        click=(random.random()*2-1)*math.exp(-90*t)*0.6
        out.append((math.sin(ph)*env+click)*g)
    return out

def boom(dur=1.1,g=0.5):
    m=int(SR*dur); out=[]; ph=0.0; y=0.0
    for i in range(m):
        t=i/SR
        f=78*math.exp(-4.5*t)+36
        ph+=2*math.pi*f/SR
        env=math.exp(-3.4*t)
        y+=0.06*((random.random()*2-1)-y)
        out.append((math.sin(ph)*env+y*env*3.0)*g)
    return out

def ding(dur=1.0,g=0.16):
    m=int(SR*dur); out=[]
    for i in range(m):
        t=i/SR; env=math.exp(-4.2*t)
        v=math.sin(2*math.pi*1568*t)*0.6+math.sin(2*math.pi*2093*t)*0.3+math.sin(2*math.pi*3136*t)*0.12
        out.append(v*env*g)
    return out

def pop(dur=0.14,g=0.18):
    m=int(SR*dur); out=[]; ph=0.0
    for i in range(m):
        p=i/m; t=i/SR
        f=520+900*p
        ph+=2*math.pi*f/SR
        out.append(math.sin(ph)*math.exp(-26*t)*g)
    return out

CUES=os.path.join(OUT,'cues.txt')
if os.path.exists(CUES):
    for line in open(CUES):
        line=line.strip()
        if not line or line.startswith('#'): continue
        a,b=line.split(); t=float(a); kind=b
        if kind=='whoosh': put(t-0.22,whoosh())
        elif kind=='thud': put(t,thud(0.42,0.44))
        elif kind=='thud2': put(t,thud(0.36,0.52))
        elif kind=='boom': put(t,boom())
        elif kind=='ding': put(t,ding())
        elif kind=='pop': put(t,pop(0.14,0.16))
        elif kind=='pop2': put(t,pop(0.16,0.14))
else:
    for t in (7.30,15.10,23.30,31.40): put(t-0.22,whoosh())
    put(3.55,thud(0.42,0.42))
    put(9.00,thud(0.42,0.40))
    put(16.90,thud(0.36,0.50))
    put(19.10,thud(0.36,0.50))
    put(31.42,ding())
    put(35.05,boom())
    put(36.50,pop(0.14,0.16)); put(36.90,pop(0.14,0.16)); put(37.50,pop(0.16,0.14))

peak=max(abs(v) for v in buf) or 1.0
if peak>0.99: buf=[v/peak*0.99 for v in buf]
w=wave.open(os.path.join(OUT,'sfx.wav'),'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes(b''.join(struct.pack('<h',int(max(-1,min(1,v))*32767)) for v in buf)); w.close()
print('sfx ok', round(peak,3), '->', os.path.join(OUT,'sfx.wav'))
