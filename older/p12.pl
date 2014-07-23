#!/usr/bin/perl
#
for($i=1;$i<1000000000000;$i++){
    $number += $i;
    for ($j=1;$j<sqrt($number);$j++){
        if ($number % $j == 0) {$divisors +=2;}
        if ($j == sqrt($number)) {$divisors--;}
    }
    print "$number: $divisors\n";
    if ($divisors >= 500){ print $number; exit;}
    $divisors = 0;
}
