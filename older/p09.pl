#!/usr/bin/perl

for ($i=1;$i<1000;$i++){
    for ($j=$i;$j<1000;$j++){
        $num = $i + $j + sqrt($i**2+$j**2);
        if ($num == 1000) {print $i*$j*(sqrt($i**2+$j**2));}
    }
}
