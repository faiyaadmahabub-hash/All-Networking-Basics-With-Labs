from pathlib import Path
import collections,hashlib,json
root=Path(__file__).resolve().parents[1]
files=sorted([*root.glob('*.pka'),*root.glob('*.pkt')])
counts=collections.Counter(p.suffix for p in files)
assert len(files)==30 and counts['.pka']==28 and counts['.pkt']==2
assert all(p.stat().st_size>0 for p in files)
modules=collections.Counter(p.name.split('.')[0] for p in files)
print('PASS: 30 non-empty Packet Tracer files: 28 activities, 2 topologies.')
print('Activity counts by filename module:',json.dumps(dict(modules),sort_keys=True))
print('Total bytes:',sum(p.stat().st_size for p in files))
for p in files:print(hashlib.sha256(p.read_bytes()).hexdigest(),p.name)
print('NOT RUN: activity scoring, device configuration completion or live connectivity tests.')
