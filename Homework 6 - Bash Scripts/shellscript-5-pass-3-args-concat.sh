#!/bin/bash
#Use arguments in a script. Total number of arguments should be three.

while [ $# -lt 3 ]
	do
	echo "Please enter more arguments, you have less than 3 !"
	read  args_added
	set -- "$@" $args_added
done

echo "\n$1$2$3"
 
if  [ $# -gt 3 ]
	then

	echo "You have supplied more that 3 args and those will be printed below not cat-ed together ;)"

	shift 3
	while [ $# -gt 0 ]
	do
	echo "$1"
	shift
	done

fi
