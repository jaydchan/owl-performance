all: clean out

clean:
	- rm -r out

out:
	- mkdir out
	
CMD=./horned-parse
RSC=../resources

test: out
	$(CMD) $(RSC)/and.owl > out/test_owl.owx
	$(CMD) $(RSC)/and.owx > out/test_owx.owx
	
bfo.owl:
	$(CMD) $(RSC)/bfo.owl > out/bfo_owl.owx
	
bfo.owx:
	$(CMD) $(RSC)/bfo.owx > out/bfo_owx.owx
	
chebi.owl:
	$(CMD) $(RSC)/chebi.owl > out/chebi_owl.owx

chebi.owx:
	$(CMD) $(RSC)/chebi.owx > out/chebi_owx.owx

go.owl:
	$(CMD) $(RSC)/go.owl > out/go_owl.owx
	
go.owx:
	$(CMD) $(RSC)/go.owx > out/go_owx.owx
	
ncbitaxon.owl:
	$(CMD) $(RSC)/ncbitaxon.owl > out/ncbitaxon_owl.owx
	
ncbitaxon.owx:
	$(CMD) $(RSC)/ncbitaxon.owx > out/ncbitaxon_owx.owx
	
snomedct.owl:
	$(CMD) $(RSC)/snomedct.owl > out/snomedct.owx

snomedct.owx:
	$(CMD) $(RSC)/snomedct.owx > out/snomedct.owx

