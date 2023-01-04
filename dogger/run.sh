#!/bin/bash

apt-cache pkgnames | sort > bener.txt 
wc -l bener.txt

echo "Start!"
for pkgname in `cat bener.txt`
do
	apt-cache depends $pkgname > pkg_dependencies.txt
	echo $pkgname
done