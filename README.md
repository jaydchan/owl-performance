# owl-performance

## Requirements

* bash
* java (21)
* python3 (3.12)
* [robot](http://robot.obolibrary.org/)

## Python library requirements

* py-horned-owl
* matplotlib

## Usage

To conduct timings test on write (big) tools, type `make time`

To generate line plot for all write timings (assumes time complete), type `make plot`

To generate box plots for all write timings (assumes time complete), type `make boxplots`

To conduct timings test on read (parse) tools, type `make time-parse`

To generate bar chart for all read (parse) timings (assumes time-parse complete), type `make barchart`

## Constants

* Outfile (OUT) -> time.csv
* Infile (INA) -> all.txt (generated) - list of all jobs
* Infile (INR) -> order.txt (generated) - list of all jobs in random order
* Available TOOLS (see below)
* Available COMMANDS (see below)
* Number of iterations (MAX) -> 3 by default

## Available tools

* horned-big, part of [horned-owl](https://github.com/phillord/horned-owl)
* horned-parse, part of [horned-owl](https://github.com/phillord/horned-owl)
* py-horned-big, which uses [py-horned-owl](https://github.com/ontology-tools/py-horned-owl)
* py-horned-parse, which uses [py-horned-owl](https://github.com/ontology-tools/py-horned-owl)
* [owl-api-big](https://github.com/jaydchan/owl-api-big), which uses [owl-api](https://github.com/owlcs/owlapi)
* [owl-api-parse](https://github.com/jaydchan/owl-api-parse), which uses [owl-api](https://github.com/owlcs/owlapi)

## Additional make commands (for big tools)

* o10.owx
* o100.owx
* o1000.owx
* o10000.owx
* o100000.owx
* o1000000.owx
* o2500000.owx
* o5000000.owx
* o10000000.owx
* o20000000.owx

## Additional make commands (for parse tools)

* bfo.owl
* bfo.owx
* chebi.owl
* chebi.owx
* go.owl
* go.owx
* ncbitaxon.owl
* ncbitaxon.owx

## Additional make commands (for resources)

Downloads the following ontologies

* bfo
* chebi
* go
* ncbitaxon

Use `make resources` to download all ontologies

## Additional author notes

### How to create horned-big or horned-parse

- git clone horned-owl
- cargo build --release --bin horned-[TOOLNAME]
- copy and paste executable into relevant directory

### How to create owl-api-big or owl-api-parse

- git clone owl-api-big or owl-api-parse
- `make`
- copy and paste jar (with dependencies) into relevant directory

### Relevant venv commands

Activate venv:
- `source venv/bin/activate`

Deactivate venv:
- `deactivate`

