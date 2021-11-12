import subprocess
import struct
import os
import numpy
import random

def anuvaachanam():
	subprocess.run(['sh','pm.sh'])
	
	with open("shabdah.mcep","rb") as sanchikaa:
		kootzaankah=sanchikaa.read()
		shabdaankah=struct.unpack('f'*int(len(kootzaankah)/4),kootzaankah)
		shabdah=numpy.array([[shabdaankah[i] for i in range(j*21,(j+1)*21) ] for j in range(0,int(len(shabdaankah)/21))])
	
	aagamah=[]
	aagamanaamaani=[]
	for sanchikaanaama_ in os.listdir("cb"):
		sanchikaanaama=os.fsdecode(sanchikaanaama_)
		if sanchikaanaama.endswith(".mcep") and (not sanchikaanaama.endswith("cb.mcep")):
			aagamanaamaani+=[sanchikaanaama]
			with open('cb/'+sanchikaanaama,"rb") as sanchikaa:
				kootzaankah=sanchikaa.read()
				shabdaankah=struct.unpack('f'*int(len(kootzaankah)/4),kootzaankah)
				aagamah+=[[[shabdaankah[i] for i in range(j*21,(j+1)*21) ] for j in range(0,int(len(shabdaankah)/21))]]
	for bhaagah in shabdah:
		i=0;j=0;d=float('Inf')
		for k in range(0,len(aagamah)):
			varnzah=numpy.array(aagamah[k])
			dl=numpy.sum(numpy.abs(varnzah[:,1:21]-bhaagah[1:21])**2,axis=-1)**(1./2)
			mi=numpy.argmin(dl)
			if(dl[mi]<d):
				d=dl[mi];i=k;j=mi
		print(aagamanaamaani[i]+'  \t'+str(j)+'\t'+str(bhaagah[0]))
		bhaagah[1:21]=aagamah[i][random.randrange(0,len(aagamah[i]))][1:21]
	with open("anushabdah.mcep","wb") as sanchikaa:
		sanchikaa.write(struct.pack('f'*len(shabdah)*21,*shabdah.flatten()))
	subprocess.run(['sh','s16.sh'])
