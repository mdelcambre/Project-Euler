#!/usr/bin/perl
$one=0;
$two=1;
while( $one <4000000 && $two <4000000){
    $three = $two;
    $two += $one;
    $one = $three;
    if ($two%2 ==0) {
        $sum += $two;
    }
}
print "$sum \n";
