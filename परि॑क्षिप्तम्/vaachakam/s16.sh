PATH=$PATH:../SPTK-3.9/usr/local/bin/
excite -p 80 anushabdah.pitch | mlsadf -m 20 -a 0.42 -p 80 anushabdah.mcep | x2x +fs -o > anushabdah.mcep.syn.s16
sox -r16k anushabdah.mcep.syn.s16 -d
