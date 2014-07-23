#!/usr/bin/perl
$number = 600851475143;
$num_temp = $number;
$check = 0;
while ($check < $number) {
    for ($i=2;$i<=$num_temp;$i++){
        if ( $num_temp% $i ==0 ){
            $num_temp /= $i;
            push(@array,$i);;
        }
    }
    $check =1;
    foreach (@array) {
        $check *= $_;
    }
}

foreach (@array){
    if ($_>$max){$max = $_};
}
print "$max\n";
