#!/bin/bash
#Write a shell sript that promts the user for a name of a file or directory and reports if it is a regular file, a directory, or another type of file.
#Also perform a ls command against the file or directory with the long listing oprtion

echo "Please enter via keyboard a name of a File or Directory"
read FILE

if [ -f $FILE ]
	then
	echo "$FILE is a file"
elif [ -d $FILE ]
	then
	echo "$FILE is a dir"
else
echo "$FILE is of a different file type"
fi

ls -l $FILE
