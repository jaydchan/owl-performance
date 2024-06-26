#!/bin/bash
# Adapted from
# https://www.golinuxcloud.com/get-script-execution-time-command-bash-script/
# https://linuxhint.com/bash_split_examples/


# CONSTANTS
# filepaths
PWD=$(pwd)
OUT=$PWD/times.csv
INA=$PWD/all.txt
INR=$PWD/order.txt
# list of tools
# TOOLS=("horned-parse" "owl-api-parse" "py-horned-parse")
TOOLS=("owl-api-parse")
# list of commands
COMMANDS=("bfo.owl" "bfo.owx" "go.owl" "go.owx" "chebi.owl" "chebi.owx" "ncbitaxon.owl" "ncbitaxon.owx")
# list of increments
INCS=(1000 100 10 1)
# number of iterations
MAX=3
# max for memory
MEM=22000
# start from line
START=0


find_memory () {
    start=$1
    increment=$2

    for (( j=$start; j<=$MEM; j=j+$increment ))
    do
	# make command
	all="limit-$command var=$j"
	all+="M"
	# echo "$all"

	# run make command
	result=$(make $all)
		
	# if worked
	if [ $? -eq 0 ]
	then
	    # stop
	    break
	fi
    done

    # sleep 2 secs
    sleep 2

    # else return j
    echo "$j"
}


# clean files
rm $OUT
touch $OUT

# clean tool directories
for tool in ${TOOLS[@]}
do
    cd $tool
    make
    cd ..
done

# generate out file
for tool in ${TOOLS[@]}
do
    # move into directory
    cd $tool

    # for each ontology
    for command in ${COMMANDS[@]}
    do
	echo "$tool, $command"
	if [ "$tool" != "owl-api-parse" -a "$command" == "bfo.owx" ]
	then
	    continue
	fi

	# find start
	start=1
	# for each increment
	for inc in ${INCS[@]}
	do
	    result=$(find_memory $start $inc)
	    start=$(( result - inc ))
	    echo "$tool, $command, $inc, $start"
	done
	
	# for each iteration
        for (( i=1; i<=$MAX; i++ ))
        do
	    # run iteration
	    result="$(find_memory $start 1)"

	    # if worked
	    if [ $result -gt 0 ]
	    then
		# output to file
		echo "$tool,$command,$result" >> $OUT
	    fi

        done
    done

    # go back
    cd ..

done
