#%%
"""

Ping statistics for 8.8.8.8:
    Packets: Sent = 15000, Received = 14951, Lost = 49 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 13ms, Maximum = 142ms, Average = 14ms

Ping statistics for 8.8.8.8:...
{'General failure.': 8,
 'Reply from 8.8.8.8: bytes=32 time=13ms TTL=117': 464,
 'Reply from 8.8.8.8: bytes=32 time=142ms TTL=117': 1,
 'Reply from 8.8.8.8: bytes=32 time=14ms TTL=11': 1,
 'Reply from 8.8.8.8: bytes=32 time=14ms TTL=117': 8153,
 'Reply from 8.8.8.8: bytes=32 time=15ms TTL=117': 5920,
 'Reply from 8.8.8.8: bytes=32 time=16ms TTL=117': 263,
 'Reply from 8.8.8.8: bytes=32 time=17ms TTL=117': 65,
 'Reply from 8.8.8.8: bytes=32 time=18ms TTL=117': 29,
 'Reply from 8.8.8.8: bytes=32 time=19ms TTL=117': 22,
 'Reply from 8.8.8.8: bytes=32 time=20ms TTL=117': 16,
 'Reply from 8.8.8.8: bytes=32 time=21ms TTL=117': 7,
 'Reply from 8.8.8.8: bytes=32 time=22ms TTL=117': 6,
 'Reply from 8.8.8.8: bytes=32 time=23ms TTL=117': 1,
 'Reply from 8.8.8.8: bytes=32 time=24ms TTL=117': 1,
 'Reply from 8.8.8.8: bytes=32 time=26ms TTL=117': 2,
 'Request timed out.': 41}
 
"""
import numpy as np
from collections import Counter
from pprint import pprint as pp

with open("pingresults", "r") as f:
  res = [line[:-1] for line in f]

d = Counter(res)
d = dict(sorted(d.items(), key=lambda item: item[1]))

pp(d)