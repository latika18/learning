def unique(string1):
	status = True
	for i,v in enumerate(string1):
		if v not in string1[:i] and v not in string1[i+1:]:
			status = True
		else:
			status = False
			break
		
	return status

print(unique("tanush"))
