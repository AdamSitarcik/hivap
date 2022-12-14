reset
set terminal qt enhanced size 500,700
set multiplot layout 3,1 margins 0.11, 0.9, .085, .93 spacing 0, .025

set logscale y

ymin=1e-8
ymax=1e-3

set yrange [ymin:ymax]
set xrange [20:75]

set format y "10^{%L}"
set ytics font ',10'

set key opaque

set title '93Nb+100Ru->193At*, BF=0.61' font ',12' 

set xtics
set format x '' 
plot for [i=3:7] '93Nb_100Ru_193At.dat' index 0 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=3:6] '' index 1 using 1:i with l lw 2.5 lt i dt 3 title ''

unset title
set ylabel '{/Symbol s} [mb]' font ',12' offset -1,0
set format x '' 
plot for [i=3:7] '93Nb_100Ru_193At.dat' index 2 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=3:6] '' index 3 using 1:i with l lw 2.5 lt i dt 3 title ''

unset title
set yrange [ymin*10:ymax*10]
set xlabel 'E* [MeV]' font ',12' offset 0,0
set format x '%h' 
set xtics font ',10'
set xtics
unset ylabel
plot for [i=3:7] '93Nb_100Ru_193At.dat' index 4 using 1:i with l lw 2.5 lt i title columnhead(i), for [i=3:6] '' index 5 using 1:i with l lw 2.5 lt i dt 3 title ''

unset multiplot
