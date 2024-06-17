all: clean

clean:
	- rm performance.log
	- rm all.txt
	- rm order.txt
	- rm times.csv
	- rm *~

clean-png:
	- rm *.png

time:
	./time.sh > performance.log

time-parse:
	./time_parse.sh > performance.log

continue:
	./time.sh 1 >> performance.log

plot:
	python3 plot.py

subset:
	python3 plot.py --subset

boxplots:
	python3 plot.py --boxplots

barchart:
	python3 plot_parse.py

RSC=./resources

clean-bfo:
	rm $(RSC)/bfo.ow*

clean-chebi:
	rm $(RSC)/chebi.ow*

clean-go:
	rm $(RSC)/go.ow*

clean-ncbitaxon:
	rm $(RSC)/ncbitaxon.ow*

resources: bfo chebi go ncbitaxon

bfo:
	wget -nc http://purl.obolibrary.org/obo/bfo.owl# -P $(RSC)/
	robot convert --input $(RSC)/bfo.owl --output $(RSC)/bfo.owx

chebi:
	wget -nc http://purl.obolibrary.org/obo/chebi.owl# -P $(RSC)/
	robot convert --input $(RSC)/chebi.owl --output $(RSC)/chebi.owx

go:
	wget -nc http://purl.obolibrary.org/obo/go.owl# -P $(RSC)/
	robot convert --input $(RSC)/go.owl --output $(RSC)/go.owx

ncbitaxon:
	wget -nc http://purl.obolibrary.org/obo/ncbitaxon.owl# -P $(RSC)/
	robot convert --input $(RSC)/ncbitaxon.owl --output $(RSC)/ncbitaxon.owx

create-venv:
	python3 -m venv venv

