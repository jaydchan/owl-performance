all: clean time

clean:
	- rm performance.log

time:
	./time.sh > performance.log

plot:
	python3 plot.py
