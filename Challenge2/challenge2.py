mass = {'H':1.0079, 'S':32.065, 'O':15.9994, 'K':39.0983, 'Mn':54.938, 'C':12.0107, 'Ca':40.078}

def computeMass(s):
	n = len(s)
	ans = 0
	i = 0
	while i<n:
		element = s[i]
		if element == '(':
			i += 1
			element = ''
			while s[i]!=')':
				element += s[i]
				i+=1
			temp = computeMass(element)
			i+=1
			factor = ''
			while i<n and s[i].isdigit():
				factor += s[i]
				i+=1
				
			if factor:
				factor = int(factor)
				temp*=factor
			ans += temp
		else:
			factor = ''
			if i!=n-1 and s[i+1].islower():
				i+=1
				element += s[i]
			while i!=n-1 and s[i+1].isdigit():
				i+=1
				factor+=s[i]
			i+=1
			temp = mass[element]
			if factor:
				factor = int(factor)
				temp*=factor
			ans += temp
	return ans			
				
s = input()
res = computeMass(s)
print("%.4f" % res)
