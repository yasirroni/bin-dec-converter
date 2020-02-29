import math
def d2b(inp, length = 1):
    """Convert a binary list to a positive integer list. Works with more than one row input."""
    nbin = int(math.floor(math.log(inp, 2) + 1));
    result = [0] * max(1, length - nbin);
    for i in range(0, nbin):
        result.append(inp >> i & 0b1);
    return result;