import numpy
import struct
import subprocess
from matplotlib import pyplot

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

mukhaakrtyah={
'अ':         [ 2.4938972 , -0.25811443,  0.75897503, -0.50855708,
       -0.47334781,  0.58060956, -0.3783119 , -0.06384721, -0.13303453,
       -0.21353258,  0.42628017, -0.27035865,  0.32324335, -0.11368971,
        0.0407615 , -0.08952652,  0.3060663 , -0.10236479, -0.09362874,
        0.08141548],
'इ':               [ 1.64354980e+00, -1.68168545e-01,  1.80663288e+00,
        3.70125681e-01, -3.78588796e-01,  3.84436965e-01, -9.01250690e-02,
       -2.60897633e-03, -2.36531913e-01, -4.38939303e-01,  1.14223823e-01,
       -1.12961240e-01, -2.42094964e-01, -2.86946129e-02, -9.20108780e-02,
        2.58584321e-01,  2.45855264e-02,  7.01531395e-02,  9.28345323e-02,
        1.91095769e-01],
'इँ':               [ 1.86273026,  0.78867781,  1.22439563,  0.39179814,
       -0.58342892,  0.13705377, -0.28654122, -0.19083506,  0.14373049,
       -0.32107666,  0.3101407 , -0.30233443, -0.22949857,  0.30842045,
        0.02608323, -0.22810996,  0.06270856, -0.04781586,  0.13913324,
       -0.14511493],

'न': 		[ 2.80067492,  0.10380825,  1.07299125,  0.42505243,
       -0.29069427,  0.36551443,  0.19595574, -0.03104033, -0.15095679,
       -0.27203244,  0.03345011, -0.81705338,  0.04503266,  0.0312927 ,
        0.27021012, -0.01799309,  0.34096679, -0.22150873,  0.12515771,
       -0.27064335],

'क':{ 'अ':         [ 1.76525009,  0.37437674, -0.61993361, -0.30854726,
        0.29453388, -0.0266886 ,  0.24192725, -0.18828785, -0.10950498,
        0.02471261, -0.14801686, -0.14229566,  0.01707278,  0.07909557,
        0.12054458,  0.02636348,  0.28060699, -0.12606168,  0.2485424 ,
       -0.21290423],
       
       'इ':       [ 8.35889935e-01, -9.51772649e-03,  7.36127794e-01,
       -2.28255853e-01, -3.58452827e-01, -2.00624801e-02, -1.39441565e-01,
       -2.87562788e-01,  2.86811832e-02,  8.33751708e-02,  5.08770812e-03,
       -2.19127357e-01,  2.43235797e-01,  1.70738734e-02, -1.07338093e-02,
        1.58899277e-03, -2.48189550e-02, -4.33556922e-02, -2.28646118e-02,
       -3.15698935e-03],
       
	'उ':      [ 1.98637509e+00,  7.14789450e-01, -8.28038843e-04,
       -6.24757886e-01,  7.07264710e-03, -5.64263046e-01, -2.10269634e-02,
       -5.39174676e-02,  1.16523109e-01,  5.19152395e-02,  2.81225611e-02,
       -3.99021178e-01,  3.47398818e-02, -3.23909342e-01,  2.33434439e-01,
       -2.71443296e-02,  1.93404853e-01, -1.05463564e-02, -7.23784119e-02,
       -2.55850870e-02]
     }
}


def vaachanam(shabdah):
	
	bhaagaavadhih=0.005
	varnzaah=[' ']+varnzanirnzayah(shabdah)+[' ']
	mcep=numpy.empty(shape=(0,20))
	preranzam=numpy.empty(0)
	v0=0
	v01=5
	v011=6
	v1=7
	pitch=numpy.empty(0)
	
	def prayaasah(kaalah,poorvaa,pashchimaa,maatraa1,maatraa2,kampanam):
		nonlocal mcep,preranzam,pitch
		mcep=numpy.concatenate((mcep,numpy.linspace(poorvaa,pashchimaa,int(kaalah/bhaagaavadhih))))
		preranzam=numpy.concatenate((preranzam,numpy.linspace(maatraa1,maatraa2,int(kaalah/bhaagaavadhih))))
		pitch=numpy.concatenate((pitch,numpy.full(int(kaalah/bhaagaavadhih),150*kampanam)))
	for i in range(0,len(varnzaah)-1):
		if varnzaah[i] ==' ':
			if varnzaah[i+1] in 'अइन':
				prayaasah(0.06,mukhaakrtyah[varnzaah[i+1]],mukhaakrtyah[varnzaah[i+1]],v0,v1,1)	
		if varnzaah[i] in 'अइ':
			if varnzaah[i-1] in 'अइ':
				prayaasah(0.08,mukhaakrtyah[varnzaah[i]],mukhaakrtyah[varnzaah[i]],v01,v1,1)
			elif varnzaah[i-1] in 'न':
				prayaasah(0.05,mukhaakrtyah[varnzaah[i]+'ँ'],mukhaakrtyah[varnzaah[i]+'ँ'],v011,v1,1)
			if varnzaah[i+1] == ' ':
				prayaasah(0.125,mukhaakrtyah[varnzaah[i]],mukhaakrtyah[varnzaah[i]],v1,v0,1)
			elif varnzaah[i+1] in 'अइ':
				prayaasah(0.08,mukhaakrtyah[varnzaah[i]],mukhaakrtyah[varnzaah[i]],v1,v01,1)
			elif varnzaah[i+1] in 'न':
				prayaasah(0.06,mukhaakrtyah[varnzaah[i]],mukhaakrtyah[varnzaah[i]],v1,v011,1)
				#prayaasah(0.08,mukhaakrtyah[varnzaah[i]],mukhaakrtyah[varnzaah[i+1]],v1,v011,1)
			elif varnzaah[i+1] =='क':
				poorvaa=mukhaakrtyah[varnzaah[i]]
				pashchimaa=mukhaakrtyah[varnzaah[i+1]][varnzaah[i]]
				
				prayaasah(0.03,poorvaa,pashchimaa,v1,v1,1)
				prayaasah(0.06,pashchimaa,pashchimaa,v0,v0,0)
				
		elif varnzaah[i] in 'न':
			if varnzaah[i+1] == ' ' or (not varnzaah[i+1] in 'अइ') or (not varnzaah[i-1] in 'अइ'):
				prayaasah(0.1,mukhaakrtyah[varnzaah[i]],mukhaakrtyah[varnzaah[i]],v011,v011,1)
			else: prayaasah(0.02,mukhaakrtyah[varnzaah[i]],mukhaakrtyah[varnzaah[i]],v011,v011,1)
		
		elif varnzaah[i] in 'क':
			if i<len(varnzaah)-1:
				if varnzaah[i+1] in 'अइ':
					poorvaa=mukhaakrtyah[varnzaah[i]][varnzaah[i+1]]
					pashchimaa=mukhaakrtyah[varnzaah[i+1]]
					
					prayaasah(0.005,poorvaa,poorvaa,v0,v1,0)
					prayaasah(0.005,poorvaa,poorvaa,v1,v0,0)
					
					prayaasah(0.03,poorvaa,pashchimaa,v0,v1,1)
			elif i>0:
				if varnzaah[i-1] in 'अइ':
					prayaasah(0.01,mukhaakrtyah[varnzaah[i]][varnzaah[i-1]],mukhaakrtyah[varnzaah[i]][varnzaah[i-1]],v1,v1,0)
				
				
		
	
	mcep=numpy.concatenate((numpy.transpose([preranzam]),mcep),axis=1)
	
	with open('anushabdah.mcep','wb') as sanchika:
		sanchika.write(struct.pack('f'*len(mcep)*21,*mcep.flatten()))
	with open('anushabdah.pitch','wb') as sanchika:
		sanchika.write(struct.pack('f'*len(pitch),*pitch.flatten()))
	subprocess.run(['sh','s16.sh'])

def shabdagrahanzam(sanchikaanaama,m=20):
	m+=1
	global shabdah
	with open(sanchikaanaama,"rb") as sanchika:
		kootzashabdah=sanchika.read()
		shabdasaarah=struct.unpack('f'*int(len(kootzashabdah)/4),kootzashabdah)
		shabdah=numpy.array([[shabdasaarah[j] for j in range(i*m,(i+1)*m) ] for i in range(0,int(len(shabdasaarah)/m)) ])
