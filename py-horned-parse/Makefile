all: test

CMD=python3 py-horned-parse.py
LCMD=systemd-run --user --scope -p MemorySwapMax=0M
RSC=../resources

test:
	$(CMD) $(RSC)/and.owl 
	$(CMD) $(RSC)/and.owx

bfo.owl:
	$(CMD) $(RSC)/bfo.owl

bfo.owx:
	$(CMD) $(RSC)/bfo.owx

chebi.owl:
	$(CMD) $(RSC)/chebi.owl

chebi.owx:
	$(CMD) $(RSC)/chebi.owx

go.owl:
	$(CMD) $(RSC)/go.owl

go.owx:
	$(CMD) $(RSC)/go.owx

ncbitaxon.owl:
	$(CMD) $(RSC)/ncbitaxon.owl

ncbitaxon.owx:
	$(CMD) $(RSC)/ncbitaxon.owx

limit-bfo.owl:
	$(LCMD) -p MemoryMax=$(var) $(CMD) $(RSC)/bfo.owl

limit-bfo.owx:
	$(LCMD) -p MemoryMax=$(var) $(CMD) $(RSC)/bfo.owx

limit-chebi.owl:
	$(LCMD) -p MemoryMax=$(var) $(CMD) $(RSC)/chebi.owl

limit-chebi.owx:
	$(LCMD) -p MemoryMax=$(var) $(CMD) $(RSC)/chebi.owx

limit-go.owl:
	$(LCMD) -p MemoryMax=$(var) $(CMD) $(RSC)/go.owl

limit-go.owx:
	$(LCMD) -p MemoryMax=$(var) $(CMD) $(RSC)/go.owx

limit-ncbitaxon.owl:
	$(LCMD) -p MemoryMax=$(var) $(CMD) $(RSC)/ncbitaxon.owl

limit-ncbitaxon.owx:
	$(LCMD) -p MemoryMax=$(var) $(CMD) $(RSC)/ncbitaxon.owx

