all: clean out test

clean:
	- rm -r out

out:
	- mkdir out

CMD=./horned-parse
RSC=../resources

test: out
	$(CMD) $(RSC)/and.owl > out/test_owl.owx 2>/dev/null
	$(CMD) $(RSC)/and.owx > out/test_owx.owx 2>/dev/null

go.owl:
	$(CMD) $(RSC)/go.owl > out/go_owl.owx 2>/dev/null

go.owx:
	$(CMD) $(RSC)/go.owx > out/go_owx.owx 2>/dev/null

ncbitaxon.owl:
	$(CMD) $(RSC)/$ncbitaxon.owl > out/ncbitaxon_owl.owx 2>/dev/null

ncbitaxon.owx:
	$(CMD) $(RSC)/ncbitaxon.owx > out/ncbitaxon_owx.owx 2>/dev/null
