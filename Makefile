all: clean time

clean:
	- rm performance.log
	- rm all.txt
	- rm order.txt
	- rm times.csv
	- rm *~

time:
	./time.sh > performance.log

continue:
	./time.sh 1 >> performance.log

plot:
	python3 plot.py

subset:
	python3 plot.py --subset
