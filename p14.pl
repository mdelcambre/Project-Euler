#!/usr/bin/perl
$max = 0;
for ($i=999999;$i>=1;$i--){
    $seq = $i;
    while ($seq >1 ){
        if ($seq %2 ==0){
            $seq /= 2; #even
            $steps++;
        } else {
            $seq = 3*$seq +1; #odd
            $steps++;
        }
    }
    if ($steps > $max) {
        $max = $steps;
        $max_n = $i;
    }
    print "$i \n";
    $steps = 0;
}

print "$max_n";
