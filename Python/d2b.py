import math

def d2b(arr, length = 1):
	"""Convert a binary list to a positive integer list. Works with more than one row input."""
	result = []
	if isinstance(arr, int):
		return _d2b(arr, length)

	for item in arr:
		result.append(_d2b(item, length))
	return result

def _d2b(inp, length = 1):
	# for inpTemp in inp:
	binData = []
	nbin = int(math.floor(math.log(inp, 2) + 1))
	# 90 = 0b0101101 & 0b0000001
	for i in range(0, nbin):
		binData.append(inp >> i & 0b1)
	binData.reverse()

	result = [0] * max(1, length - nbin)
	result.extend(binData)
	return result