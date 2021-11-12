SPTK = ../../SPTK-3.9/usr/local/bin/

WAV = $(wildcard *.wav)

MCEP = $(patsubst %.wav,%.mcep,$(WAV))

all: $(MCEP)

%.mcep: %.wav
	sox $< -r16k -c1 -ts16 - | $(SPTK)/x2x +sf | \
	$(SPTK)/frame -l 400 -p 80 | $(SPTK)/window -l 400 -L 512 \
	| $(SPTK)/mcep -l 512 -m 20 -a 0.42 > $@
