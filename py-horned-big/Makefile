all: clean out test

clean:
	- rm -r out

out:
	- mkdir out

CMD=python3 py-horned-big.py

test: out
	$(CMD) 5
	mv temp.owx out/test.owl

o10.owx:
	$(CMD) 10 
	mv temp.owx out/o10.owx

o100.owx:
	$(CMD) 100 
	mv temp.owx out/o100.owx

o1000.owx:
	$(CMD) 1000 
	mv temp.owx out/o1000.owx

o10000.owx:
	$(CMD) 10000 
	mv temp.owx out/o10000.owx

o100000.owx:
	$(CMD) 100000 
	mv temp.owx out/o100000.owx

o1000000.owx:
	$(CMD) 1000000 
	mv temp.owx out/o100000.owx

o2500000.owx:
	$(CMD) 2500000 
	mv temp.owx out/o250000.owx

o5000000.owx:
	$(CMD) 5000000 
	mv temp.owx out/o500000.owx

o10000000.owx:
	$(CMD) 10000000 
	mv temp.owx out/o1000000.owx

## This file comes in at over 1Gb which seems a nice round number to
## stop at.
o20000000.owx:
	$(CMD) 20000000 
	mv temp.owx out/o2000000.owx
