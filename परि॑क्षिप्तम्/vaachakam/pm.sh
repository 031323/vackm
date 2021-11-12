PATH=$PATH:../SPTK-3.9/usr/local/bin/
sox shabdah.wav -r16k -c1 shabdah.s16
x2x +sf < shabdah.s16 | pitch -a 1 -s 16 -p 80 -L 80 -H 165 > anushabdah.pitch
x2x +sf < shabdah.s16 | frame -l 400 -p 80 | window -l 400 -L 512 |mcep -l 512 -m 20 -a 0.42 > shabdah.mcep
