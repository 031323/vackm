import array
import subprocess
import struct
import time
s0g=343
class vadanam:
	def __init__(s, bh0s, m0aa, n0aa):
		s._bh0s=bh0s
		s._n0bh0s=int(bh0s*n0aa/m0aa)
		s._m0aa=m0aa
		s._n0aa=n0aa
		s._m0d=array.array('f',[0.]*bh0s)
		s._m0v=array.array('f',[0.]*bh0s)
		s._n0d=array.array('f',[0.]*s._n0bh0s)
		s._n0v=array.array('f',[0.]*s._n0bh0s)
		s._n0s=bh0s-s._n0bh0s
		if s._n0s==0:s._n0s=1
		s.m0vi=array.array('f',[1.]*bh0s)
		s.n0vi=array.array('f',[1.]*s._n0bh0s)
		s.n0vi[0]=0
		
		s._0m0d=array.array('f',[0.]*(s._bh0s+1))
		s._0m0v=array.array('f',[0.]*(s._bh0s+1))
		s._0n0d=array.array('f',[0.]*(s._n0bh0s+1))
		s._0n0v=array.array('f',[0.]*(s._n0bh0s+1))
		
		s._m0a=array.array('f',[0.]*(s._bh0s))
		s._n0a=array.array('f',[0.]*(s._n0bh0s))
		
	def yojanam(s,sth,m):
		s._m0v[int(s._bh0s*sth)]+=m/2
		s._m0d[int(s._bh0s*sth)]+=m/2
	def nirgatih(s):
		return s._m0v[s._bh0s-1]+s._m0d[s._bh0s-1]+s._n0v[s._n0bh0s-1]+s._n0d[s._n0bh0s-1]
	def mukhasamsthaanam(s):
		for bh in range(1,s._bh0s):
			s._m0a[bh]=(s.m0vi[bh-1]-s.m0vi[bh])/(s.m0vi[bh-1]+s.m0vi[bh])
		bh=1;s._n0a[bh]=(s.n0vi[bh-1]-s.n0vi[bh])/(s.n0vi[bh-1]+s.n0vi[bh])
	def naasikaasamsthaanam(s):
		for bh in range(1,s._n0bh0s):
			s._n0a[bh]=(s.n0vi[bh-1]-s.n0vi[bh])/(s.n0vi[bh-1]+s.n0vi[bh])
	def pravaahah(s):
		m0d,m0v,n0d,n0v=s._0m0d,s._0m0v,s._0n0d,s._0n0v
		
		for bh in range(1,s._bh0s):
			a=s._m0a[bh]*(s._m0d[bh-1]+s._m0v[bh])
			m0d[bh]=s._m0d[bh-1]-a
			m0v[bh]=s._m0v[bh]+a

		for bh in range(1,s._n0bh0s):
			a=s._n0a[bh]*(s._n0d[bh-1]+s._n0v[bh])
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
		
		s._m0d[0:s._bh0s]=m0d[0:s._bh0s];s._m0v[0:s._bh0s]=m0v[1:1+s._bh0s]
		s._n0d[0:s._n0bh0s]=n0d[0:s._n0bh0s];s._n0v[0:s._n0bh0s]=n0v[1:1+s._n0bh0s]
		return s._m0aa/s._bh0s/s0g

def varnzanirnzayah(shabdah):
	varnzaah=[]
	for i in range (0,len(shabdah)):
		if shabdah[i] in 'कखगघङचछजझञटठडढणतथदधनपफबभमयरलळवशषसह':
			if len(shabdah)==i+1:
				varnzaah+=[shabdah[i],'अ']
			elif shabdah[i+1] == '्':
				varnzaah+=[shabdah[i]]
			elif shabdah[i+1] in 'ा ि ी ु ू ृ ॄ ॢ ॣ े ै ो ौ'.split(' '):
				varnzaah+=[shabdah[i],'आइईउऊऋॠऌॡएऐओऔ'['ा ि ी ु ू ृ ॄ ॢ ॣ े ै ो ौ'.split(' ').index(shabdah[i+1])]]
			else: varnzaah+=[shabdah[i],'अ']
		elif shabdah[i] in 'अआइईउऊऋॠऌॡएऐओऔ'+'ं'+'ः':
			varnzaah+=[shabdah[i]]
		elif shabdah[i] == 'ँ':
			varnzaah[-1]+='ँ'
	return varnzaah

class kriyaa:
	def __init__(s,aa0k,a0k,kr):
		s.aa0k=aa0k
		s.a0k=a0k
		s.kr=kr

def vyaaharanzam(sa,m,k0s):
	m.naasikaasamsthaanam()
	m.mukhasamsthaanam()
	
	k=0
	sh=[]
	sa0s=0
	while (k<1):#True:
		#av0s=0
		#for kr in k0s:
		#	if kr.a0k>k:
		#		av0s+=1
		#		if kr.aa0k<k:kr.kr(m,k)
		#if av0s==0:break
		
		k+=m.pravaahah()
		n0sa0s=int(k*sa)
		if n0sa0s!=sa0s:
			sh+=[m.nirgatih()]
			sa0s=n0sa0s
			m.mukhasamsthaanam()
	return sh

sa=16000
def patzhanam(shabdah):
	varnzaah=[' ']+varnzanirnzayah(shabdah)+[' ']
	m=vadanam(44,0.17,0.11)
	ka=0;ta=0.3;moo=0.6;da=0.8;osz=1
	def kantzhyam(m,k,p):
		p0a=1/600
		p0k=int(k/p)*p
		if k-p0k<p0a:
			m.yojanam(0,4*(k-p0k)*(p0k+p0a-k)/p0a/p0a)
	k0s=[kriyaa(0,1,lambda m,k:kantzhyam(m,k,120))]
	aa0k=time.time()
	sh=vyaaharanzam(sa,m,k0s)
	print(time.time()-aa0k)
	return sh

def ghoshah(sh):
	subprocess.run(["aplay","-fFLOAT_LE","-r"+str(sa)],input=struct.pack('f'*len(sh),*sh))
