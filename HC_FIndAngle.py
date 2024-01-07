# pythagorean theorem: a^2 + b^2 = c^2   -->   SOH CAH TOA
# get AB (line 1)
# get BC (line 2)
import math

buffer = input()
AB = int(buffer.strip())
buffer = input()
BC = int(buffer.strip())
AC = ( (AB*2) + (BC*2) ) ** .5
abc = round(math.degrees(math.asin( (AC/2) / BC )))

print(abc)
