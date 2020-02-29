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

def d2b(inputDecimal,outputLength=1):
	"""This function returns binary value of the entered number"""
	# get input
	inDec=arg[0]

	# get minimum output length
	if inDec==0:
		outLenMin=1
	else:
		logFloor=math.floor(math.log(inDec,2))
		outLenMin=max(0,logFloor)+1

	# get output length
	inputNumber=len(arg)
	if inputNumber==1:
		outLen=outLenMin
	elif inputNumber==2:
		outLenDet=arg[1]
		outLen=max(outLenMin,outLenDet)
		if outLenDet<outLenMin:
			print('Determined Binnary Size Is Smaller Than Output Binnary Size')
	
	# initialize 
	shift=outLen-outLenMin
	outBin=[None]*outLen

	# compute outBin
	for i in range(0,outLen):
		r=math.floor(inDec/2)
		outBin[shift+outLenMin-1-i]=inDec-2*r
		inDec=r

	return(outBin)