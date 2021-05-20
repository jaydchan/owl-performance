# owl-performance

## Requirements

* bash
* java (8)
* python3

## Usage

To conduct timings test on tools type `make`

To plot all timings (assumes test complete), type `make plot`

To plot a subset of the timings (10^1 to 10^4), type `make subset`

## Constants

* Outfile (OUT) -> time.csv
* Infile (INA) -> all.txt (generated) - list of all jobs
* Infile (INR) -> order.txt (generated) - list of all jobs in random order
* Available TOOLS (see below)
* Available COMMANDS (see below)
* Number of iterations (MAX) -> 2 by default

## Available tools

* horned-big, part of [horned-owl](https://github.com/phillord/horned-owl)
* [owl-api-big](https://github.com/jaydchan/owl-api-big), which uses [owl-api](https://github.com/owlcs/owlapi)

## Additional make commands

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
