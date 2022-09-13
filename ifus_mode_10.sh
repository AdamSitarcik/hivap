#!/bin/bash

ifus_opt=IFUS=10

test=$(sed '32q;d' hivapein.dat)

IFS=' '
read -a ifus_test <<< "$test"

if [ ${ifus_test[3]} = $ifus_opt ] 
then
	cp hivapein_IFUS10.dat hivapein.dat
	echo File hivapein.dat in $ifus_opt mode updated
else
	cp hivapein_IFUS10.dat hivapein.dat
	echo File hivapein.dat changed from ${ifus_test[3]} to $ifus_opt mode and updated
fi
