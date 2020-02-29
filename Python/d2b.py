ASDF

"""Convert a binary list to a positive integer list. Works with more than one row input."""
def b2d(inputBinary):
	if isinstance(inputBinary[0], int): #1 dimension
		outputInteger=[0]
		inputBinary=inputBinary[::-1]
		for col in range(len(inputBinary)):
			if inputBinary[col]==1:
				outputInteger[0]=outputInteger[0]+2**col
	else: #2 dimensions
		outputInteger=[]
		for row in range(len(inputBinary)):
			inputBinaryReverse=inputBinary[row][::-1]
			outputIntegerTemp=0
			for col in range(len(inputBinaryReverse)):
				if inputBinaryReverse[col]==1:
					outputIntegerTemp=outputIntegerTemp+2**col
			outputInteger.append(outputIntegerTemp)
	return(outputInteger)

import math

def d2b(inp, length = 0):
    nbin = int(math.floor(math.log(inp, 2) + 1));
    result = [0] * 0 if (length - nbin) > 0 else (length - nbin);
    for i in range(0, nbin):
        result.append(inp >> i & 0b1);
    return result;
