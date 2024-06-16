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
TOOLS=("horned-parse" "owl-api-parse" "py-horned-parse")
# list of commands
# COMMANDS=("bfo" "chebi" "go" "ncbitaxon" "snomedct")
COMMANDS=("bfo.owl" "bfo.owx" "chebi.owl" "chebi.owx" "go.owl" "go.owx")
# number of iterations
MAX=2
# start from line
START=0

# if no args are passed in
if [ $# -eq 0 ]
then
    # clean files
    rm $INA $INR $OUT
    touch $INA
    touch $OUT

    # clean tool directories
    for tool in ${TOOLS[@]}
    do
	cd $tool
	make
	cd ..
    done

    # generate in file
    for tool in ${TOOLS[@]}
    do
	for command in ${COMMANDS[@]}
	do
            for (( i=1; i<=$MAX; i++ ))
            do
		echo "$tool $command" >> $INA
            done
	done
    done

    # shuffle in file
    shuf $INA > $INR
else
    # how many todo?
    todo=$(cat $INR | wc -l)

    # how many done?
    done=$(cat $OUT | wc -l)

    # check status
    if [[ $todo -gt $done ]]
    then
	# if there are some left
	echo "Continue from $done"
	START=$done
    else
	# exit early
	echo "All done"
	exit
    fi
fi

# for each line of in file
while read line
do
    # check start
    if [ $START -gt 0 ]
    then
	# decrement line count
	(( START-- ))
	# skip this line
	continue
    fi

    # Set space as the delimiter
    IFS=' '

    # Read the split words into an array based on space delimiter
    read -a strarr <<< "$line"

    # get tool and command
    tool=${strarr[0]}
    size=${strarr[1]}

    # move into directory
    cd $tool 
    
    # get time
    start=$(date +%s.%N)

    # run make
    make $size

    # calc time
    duration=$(echo "$(date +%s.%N) - $start" | bc)
    execution_time=`printf "%.2f seconds" $duration`
    
    # output to file
    echo "$tool,$size,$execution_time" >> $OUT
    
    # go back
    cd ..

    # sleep 2 secs
    sleep 2
    
done < $INR
