#!/usr/bin/perl
$sum=0;
for ($i=2;$i<2000000000;$i++){
    $not_prime = 1;
    foreach (@primes) {
        if ($i % $_ == 0) { $not_prime = 0;}
    }
    if ($not_prime == 1) {
        push(@primes,$i);
        $sum += $i;
        print "$i \n";}
}
