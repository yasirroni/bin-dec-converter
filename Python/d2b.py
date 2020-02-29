import math
# def d2b(inputDecimal,outputLength=1):
# 	print(math.floor(inputDecimal/2))
# 	pass
# 	"""This function returns binary value of the entered number."""
# 	outputBinary=[]
# 	for inputDecimalTemp in inputDecimal:
# 		if inputDecimalTemp==0:
# 			outputBinaryTemp=[0]
# 		outpunLen=
# 		outputBinary.append(outputBinaryTemp)
# 	return(outputBinary)
	
# 	import math

def d2b(input, length = 0):
    nbin = int(math.floor(math.log(input, 2) + 1))
    result = [0] * abs(length - nbin)
    for i in range(0, nbin):
        result.append(input >> i & 0b1)
    result.reverse()
    result


# print(d2b(90));

# 	# get input
# 	inDec=arg[0]

# 	# get minimum output length
# 	if inDec==0:
# 		outLenMin=1
# 	else:
# 		logFloor=math.floor(math.log(inDec,2))
# 		outLenMin=max(0,logFloor)+1

# 	# get output length
# 	inputNumber=len(arg)
# 	if inputNumber==1:
# 		outLen=outLenMin
# 	elif inputNumber==2:
# 		outLenDet=arg[1]
# 		outLen=max(outLenMin,outLenDet)
# 		if outLenDet<outLenMin:
# 			print('Determined Binnary Size Is Smaller Than Output Binnary Size')
	
# 	# initialize 
# 	shift=outLen-outLenMin
# 	outBin=[None]*outLen

# 	# compute outBin
# 	for i in range(0,outLen):
# 		r=math.floor(inDec/2)
# 		outBin[shift+outLenMin-1-i]=inDec-2*r
# 		inDec=r

# 	return(outbin,outbin2)