from b2d import b2d
from d2b import d2b

# Example to use b2d and d2b

## Usage
# 1. Convert binary to decimal
binArr=[[1,1,0],[1,1],[1,0,1,1,0,1,0]]
print(b2d(binArr))

# 2. Convert decimal to binary
# input in int
decInt=3
print(d2b(decInt))

# input in list with defined length
lenDecArr=8
decArr=[3,2,3]
print(list(map(lambda x: d2b(x,lenDecArr), decArr)))

# input in list but defined length is too short
lenDecarr=2
decInt=10
print(d2b(decInt,lenDecarr))