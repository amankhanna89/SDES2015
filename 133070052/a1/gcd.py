def gcd(a,b):
  try:
	a=g(a)
	b=g(b)
	if b==0:
		return a
	return gcd(b,a%b)
  except ValueError as e:
	print("Negative value({})".format(e))
	
  except TypeError as e:
        print ("Type Mismatch({})".format(e))
    
def g(x):
    if x < 0: raise ValueError, "I can't cope with a negative number here({})".format(x)
    else: return x
  
  


