#!/bin/bash
FILEPATH=$1

#Check to see if a file was passed
if [ -z "$FILEPATH" ]
then
        echo "No argument passed. Assuming default path of /var/log/zimbra.log"
        FILEPATH='/var/log/zimbra.log'

        #Check if /var/log/zimba.log exists
        if [ ! -f $FILEPATH ]
        then
                echo "/var/log/zimbra.log does not exist on this server"
                exit
        fi
fi

#Finds the absolute path of $FILEPATH
#FILEPATH=`realpath $FILEPATH`

printf "Number of emails with a spam score higher than 5 in the current log: "
zgrep -c -P --color=always "((?<=score=)[5-9]\.\d*)|((?<=score=)1[0-9]\.\d*)|((?<=score=)2[0-9]\.\d*)" $FILEPATH

printf "Average spam score in the current log: "
zgrep -o -P "((?<=score=)[5-9]\.\d*)|((?<=score=)1[0-9]\.\d*)|((?<=score=)2[0-9]\.\d*)" $FILEPATH | awk '{ SUM += $1; n++} END { print  SUM /n }'
