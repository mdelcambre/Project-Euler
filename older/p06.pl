#!/usr/bin/perl

for ($i=1;$i<101;$i++){
    $sum_sq += $i;
    $sq_sum += $i**2;
}

$diff = $sum_sq**2 -$sq_sum;
print $diff;
