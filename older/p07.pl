#!/usr/bin/perl
$j=0;
for ($i=2;$i<1000000000000;$i++){
    $not_prime = 1;
    foreach (@primes) {
        if ($i % $_ == 0) { $not_prime = 0;}
    }
    if ($not_prime == 1) { push(@primes,$i); $j++;}
    if ($j == 10001) { print $i; exit;}
    print "$j \n";
}
