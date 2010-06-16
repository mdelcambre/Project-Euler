#!/usr/bin/perl

for ($i=3;$i<1000;$i++){
    if ($i%5==0 || $i%3==0){
        $sum += $i;
    }
}
print "$sum \n";
