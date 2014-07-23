#!/usr/bin/perl

for ($i=998001;$i>9999;$i--) {
    $length = length($i);
    if ($length % 2==0) {
        $length /= 2;
        $sub1 = substr($i,0,$length);
        $sub2 = substr($i,$length,$length);
        $sub2 = reverse $sub2;
        if ($sub1 == $sub2){
            for ($j=999;$j>99;$j--){
                if ($i % $j == 0 && length($i/$j) == 3){
                    print "$i \n";
                    exit;
                }
            }
        }
    }else{
        $length /= 2;
        $sub1 = substr($i,0,$length);
        $sub2 = substr($i,$length+1,$length);
        $sub2 = reverse $sub2;
        if ( $sub1 == $sub2){
            for ($j=999;$j>99;$j--) {
                if ($i % $j == 0 && length($i/$j) == 3){
                    print "$i \n";
                    exit;
                }
            }
        }
    }
}
