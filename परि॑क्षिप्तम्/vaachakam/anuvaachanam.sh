PATH=$PATH:../SPTK-3.9/usr/local/bin/
M=10
x2x +sf < shabdah.s16 | frame -l 400 -p 80 | window -l 400 -L 512 |mcep -l 512 -m $M -a 0.42 > shabdah2.mcep
x2x +sf < shabdah.s16 | pitch -a 1 -s 16 -p 80 -L 80 -H 165 > shabdah.pitch
#excite -p 120 shabdah.pitch
train -p 140 -l -1 | mlsadf -m $M -a 0.42 -p 120 shabdah2.mcep | x2x +fs -o > shabdah2.mcep.syn.s16

