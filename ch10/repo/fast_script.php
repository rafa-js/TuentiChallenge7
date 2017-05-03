#!/usr/bin/env php
<?php

ini_set( 'memory_limit', '4095M' );

# Usage:
#  generate-password.php <user_id> <old_hash>

$secret1 = $argv[ 1 ];
$secret2 = $argv[ 2 ];

if ( !isset($argv[ 4 ]) ) {
    # First password for this user
    $secret3 = crc32( $argv[ 3 ] );
} else {
    # Existing user, password reset
    $secret3 = crc32( $argv[ 4 ] );
}


$N = 10000000;
$counter = ($secret3 * $secret1) % $secret2;
$founds = array(0 => $counter);
$period = 1;
$prev = $counter;
for ( $i = 1 ; $i < $N ; $i++ ) {
    $counter = ($counter * $secret1) % $secret2;
    if ( $founds[ 0 ] == $counter ) {
        break;
    } else {
        $founds[ $i ] = $counter;
        $period++;
    }
}

$endIndex = ($N - 1) % $period;
$counter = $founds[ $endIndex ];

$password = "";
for ( $i = 0 ; $i < 10 ; $i++ ) {
    # Generate random passwords
    $counter = ($counter * $secret1) % $secret2;
    $password .= chr( $counter % 94 + 33 );
}

$hash = md5( $password );
echo "$password $hash\n";
