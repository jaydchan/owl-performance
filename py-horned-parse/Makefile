all: clean out

clean:
	- rm -r out

out:
	- mkdir out

CMD=python3 py-horned-parse.py
RSC=../resources

test: out
	$(CMD) $(RSC)/and.owl 
	mv temp.owx out/test_owl.owx
	$(CMD) $(RSC)/and.owx
	mv temp.owx out/test_owx.owx
	
bfo.owl:
	$(CMD) $(RSC)/bfo.owl
	mv temp.owx out/bfo_owl.owx
	
bfo.owx:
	$(CMD) $(RSC)/bfo.owx
	mv temp.owx out/bfo_owx.owx
	
chebi.owl:
	$(CMD) $(RSC)/chebi.owl
	mv temp.owx out/chebi_owl.owx

chebi.owx:
	$(CMD) $(RSC)/chebi.owx
	mv temp.owx out/chebi_owx.owx

go.owl:
	$(CMD) $(RSC)/go.owl
	mv temp.owx out/go_owl.owx
	
go.owx:
	$(CMD) $(RSC)/go.owx
	mv temp.owx out/go_owx.owx
	
ncbitaxon.owl:
	$(CMD) $(RSC)/ncbitaxon.owl
	mv temp.owx out/ncbitaxon_owl.owx
	
ncbitaxon.owx:
	$(CMD) $(RSC)/ncbitaxon.owx
	mv temp.owx out/ncbitaxon_owx.owx
	
snomedct.owl:
	$(CMD) $(RSC)/snomedct.owl
	mv temp.owx out/snomedct.owx

snomedct.owx:
	$(CMD) $(RSC)/snomedct.owx
	mv temp.owx out/snomedct.owx

