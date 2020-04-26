s0g=343
class vadanam:
	def __init__(s, bh0s, m0aa, n0aa):
		s._bh0s=bh0s
		s._n0bh0s=int(bh0s*n0aa/m0aa)
		s._m0aa=m0aa
		s._n0aa=n0aa
		s._m0d=numpy.zeros(bh0s,dtype=numpy.float)
		s._m0v=numpy.zeros(bh0s,dtype=numpy.float)
		s._n0d=numpy.zeros(s._n0bh0s,dtype=numpy.float)
		s._n0v=numpy.zeros(s._n0bh0s,dtype=numpy.float)
		s._n0s=bh0s-s._n0bh0s
		if s._n0s==0:s._n0s=1
		s.m0vi=numpy.full(bh0s,1,dtype=numpy.float)
		s.n0vi=numpy.full(s._n0bh0s,1,dtype=numpy.float)
		s.n0vi[0]=0
		
		s._0m0d=numpy.zeros(s._bh0s+1,dtype=numpy.float)
		s._0m0v=numpy.zeros(s._bh0s+1,dtype=numpy.float)
		s._0n0d=numpy.zeros(s._n0bh0s+1,dtype=numpy.float)
		s._0n0v=numpy.zeros(s._n0bh0s+1,dtype=numpy.float)
		
		
	def yojanam(s,sth,m):
		s._m0v[int(s._bh0s*sth)]+=m/2
		s._m0d[int(s._bh0s*sth)]+=m/2
	def nirgatih(s):
		return s._m0v[s._bh0s-1]+s._m0d[s._bh0s-1]+s._n0v[s._n0bh0s-1]+s._n0d[s._n0bh0s-1]
	def pravaahah(s):
		
		m0d,m0v,n0d,n0v=s._0m0d,s._0m0v,s._0n0d,s._0n0v
		
		for bh in range(1,s._bh0s):
			a=(s.m0vi[bh-1]-s.m0vi[bh])/(s.m0vi[bh-1]+s.m0vi[bh])*(s._m0d[bh-1]+s._m0v[bh])
			m0d[bh]=s._m0d[bh-1]-a
			m0v[bh]=s._m0v[bh]+a

		for bh in range(1,s._n0bh0s):
			a=(s.n0vi[bh-1]-s.n0vi[bh])/(s.n0vi[bh-1]+s.n0vi[bh])*(s._n0d[bh-1]+s._n0v[bh])
			n0d[bh]=s._n0d[bh-1]-a
			n0v[bh]=s._n0v[bh]+a
		
		m0d[0]=s._m0v[0]*0.75
		m0v[s._bh0s]=s._m0d[s._bh0s-1]*(-0.85)
		n0v[s._n0bh0s]=s._n0d[s._n0bh0s-1]*(-0.85)
		
		y=s.m0vi[s._n0s]+s.m0vi[s._n0s-1]+s.n0vi[0]
		a=(2*s.m0vi[s._n0s-1]-y)/y
		m0v[s._n0s]=a*s._m0d[s._n0s-1]+(1+a)*(s._n0v[0]+s._m0v[s._n0s])
		a=(2*s.m0vi[s._n0s]-y)/y
		m0d[s._n0s]=a*s._m0v[s._n0s]+(1+a)*(s._n0v[0]+s._m0d[s._n0s-1])
		a=(2*s.n0vi[0]-y)/y
		n0d[0]=a*s._n0v[0]+(1+a)*(s._m0d[s._n0s-1]+s._m0v[s._n0s])
		
		s._m0d[0:s._bh0s]=m0d[0:s._bh0s]
		s._m0v[0:s._bh0s]=m0v[1:1+s._bh0s]
		
		s._n0d[0:s._n0bh0s]=n0d[0:s._n0bh0s]
		s._n0v[0:s._n0bh0s]=n0v[1:1+s._n0bh0s]
		
		return s._m0aa/s._bh0s/s0g

def vyaaharanzam():
	import subprocess
	import struct
	m=vadanam(44,0.17,0.11)
	k=0
	global sh
	sh=[]
	p=1/100
	sa=16000
	sa0s=0
	p0s=0
	
	while k<1:
	
		n0p0s=int(k/p)
		if n0p0s!=p0s:
			m.yojanam(0,1)
			p0s=n0p0s
		
		k+=m.pravaahah()
		
		n0sa0s=int(k*sa)
		if n0sa0s!=sa0s:
			sh+=[m.nirgatih()]
			sa0s=n0sa0s

	

