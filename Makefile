all: clean resources

clean:
	- rm performance.log
	- rm all.txt
	- rm order.txt
	- rm times.csv
	- rm *~

big:
	./time.sh > big.log

parse:
	./time_parse.sh > parse.log

plot:
	python3 plot.py

subset:
	python3 plot.py --subset

RSC=./resources

resources: go ncbitaxon

clean-resources:
	rm $(RSC)/go.ow*
	rm $(RSC)/ncbitaxon.ow*

go:
	wget -nc http://purl.obolibrary.org/obo/go.owl# -P $(RSC)/
	robot convert --input $(RSC)/go.owl --output $(RSC)/go.owx

ncbitaxon:
	wget -nc http://purl.obolibrary.org/obo/ncbitaxon.owl -P $(RSC)/
	robot convert --input $(RSC)/ncbitaxon.owl --output $(RSC)/ncbitaxon.owx
