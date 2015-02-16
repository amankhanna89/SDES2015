from gcd import gcd

def test_gcd():
	gcd(48,-64)
	gcd(-48,64)
	gcd(48,'a')
	assert gcd(48,64)==6
	assert gcd(48,64)==16
	assert gcd(44,19)==1

if __name__=='__main__':
	test_gcd()