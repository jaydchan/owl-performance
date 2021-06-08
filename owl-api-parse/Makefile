all: test

CMD=java -jar owl-api-parse-1.0-SNAPSHOT-jar-with-dependencies.jar
RSC=../resources

test:
	$(CMD) $(RSC)/and.owl 2>/dev/null
	$(CMD) $(RSC)/and.owx 2>/dev/null

go.owl:
	$(CMD) $(RSC)/go.owl 2>/dev/null

go.owx:
	$(CMD) $(RSC)/go.owx 2>/dev/null

ncbitaxon.owl:
	$(CMD) $(RSC)/$ncbitaxon.owl 2>/dev/null

ncbitaxon.owx:
	$(CMD) $(RSC)/ncbitaxon.owx 2>/dev/null
